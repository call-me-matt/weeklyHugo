#!/usr/bin/env python3
import sys
import subprocess
import zipfile
import tempfile
import shutil
from pathlib import Path

"""
################################################################################
# Purpose: Master script to process OSMBC markdown downloads from an inbox.
# 1. Scans 'migration/inbox' for .zip files (ignoring those with 'OK_' prefix).
# 2. Extracts each ZIP to a temporary directory.
# 3. Runs transformation, title updates, and migration scripts.
# 4. Renames the ZIP file in the inbox to 'OK_<original_name>.zip' on success.
#
# Usage:
#   python3 ./migration/migrate_osmbc_md.py
################################################################################
"""


def run_step(script_name, source_path):
    script_path = Path(__file__).parent / script_name
    print(f"   -> Executing {script_name}...")

    # Ensure source_path is passed as a string for subprocess
    args = [sys.executable, str(script_path), str(source_path)]
    result = subprocess.run(args)

    if result.returncode != 0:
        print(f"   [!] ERROR: {script_name} failed.")
        return False
    return True


def process_zip(zip_path):
    print(f"\n--- Processing: {zip_path.name} ---")

    # Create a temporary directory for extraction and processing
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        try:
            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                zip_ref.extractall(temp_path)
        except zipfile.BadZipFile:
            print(f"   [!] ERROR: {zip_path.name} is not a valid ZIP file. Skipping.")
            return False

        # Step 1: Process Lead Image and Frontmatter (In-place in temp)
        if not run_step("transform_osmbc_leadimage.py", temp_path):
            return False

        # Step 2: Finalize titles using languages.toml (In-place in temp)
        if not run_step("update_hugo_titles.py", temp_path):
            return False

        # Step 3: Move finalized files to the Hugo content folder
        if not run_step("move_osmbc_md.py", temp_path):
            return False

        # Step 4: Create shadow files for missing languages
        if not run_step("create_shadow_files.py", temp_path):
            return False

    # Success: All steps completed
    print(f"--- Finished: {zip_path.name} ---")
    return True


def main():
    # Define paths relative to the Hugo root
    base_path = Path(__file__).parent
    inbox_path = base_path / "inbox"

    if not inbox_path.exists():
        print(f"Creating missing inbox directory: {inbox_path}")
        inbox_path.mkdir(parents=True, exist_ok=True)
        return

    # Find all zip files that DO NOT start with 'OK_'
    zip_files = [f for f in inbox_path.glob("*.zip") if not f.name.startswith("OK_")]

    if not zip_files:
        print("No new ZIP files found in migration/inbox/.")
        return

    print(f"Found {len(zip_files)} new ZIP file(s) to process.")

    for zip_file in zip_files:
        success = process_zip(zip_file)

        if success:
            # Prefix the file with OK_ to mark it as processed
            new_name = zip_file.with_name(f"OK_{zip_file.name}")
            zip_file.rename(new_name)
            print(
                f"   [+] {zip_file.name} marked as processed (renamed to {new_name.name})."
            )
        else:
            print(
                f"   [!] {zip_file.name} was not fully processed. It remains unchanged in the inbox."
            )

    print("\n✅ All new ZIP files have been handled.")


if __name__ == "__main__":
    main()

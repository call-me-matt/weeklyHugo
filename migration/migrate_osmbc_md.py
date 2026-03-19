#!/usr/bin/env python3
import sys
import subprocess
import zipfile
import tempfile
import shutil
from pathlib import Path

"""
################################################################################
# Purpose: Master script to process OSMBC markdown downloads from a ZIP file.
# 1. Extracts ZIP to a temporary directory.
# 2. transform_osmbc_leadimage.py: Processes image & frontmatter.
# 3. update_hugo_titles.py: Updates titles via languages.toml.
# 4. move_osmbc_md.py: Moves finalized files to Hugo content folder.
#
# Usage:
#   python3 ./migration/migrate_osmbc_md.py /path/to/downloads.zip
################################################################################
"""


def run_step(script_name, source_path=None):
    script_path = Path(__file__).parent / script_name
    print(f"--- Starting {script_name} ---")

    args = [sys.executable, str(script_path)]
    if source_path:
        args.append(str(source_path))

    result = subprocess.run(args)
    if result.returncode != 0:
        print(f"ABORTED: {script_name} failed.")
        return False
    print(f"--- {script_name} finished successfully ---\n")
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ./migration/migrate_osmbc_md.py <input_zip_file>")
        sys.exit(1)

    zip_path = Path(sys.argv[1])
    if not zip_path.suffix == ".zip":
        print("Error: Input must be a .zip file.")
        sys.exit(1)

    # Create a temporary directory to work in
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        print(f"Extracting {zip_path.name} to temporary directory...")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(temp_path)

        # Step 1: Process Lead Image and Frontmatter
        if not run_step("transform_osmbc_leadimage.py", temp_path):
            sys.exit(1)

        # Step 2: Finalize titles using the Hugo languages.toml
        if not run_step("update_hugo_titles.py", temp_path):
            sys.exit(1)

        # Step 3: Move finalized files to the Hugo content folder
        if not run_step("move_osmbc_md.py", temp_path):
            sys.exit(1)

    print("✅ Success: All files from ZIP processed and migrated to ./content/")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import sys
import subprocess
from pathlib import Path

"""
################################################################################
# Purpose: Master script to process OSMBC markdown downloads.
# 1. Extracts lead image/caption to Hugo frontmatter.
# 2. Migrates files (Moves them to ./content/<lang>/archives/0xxx.md).
#
# Usage:
#   python3 ./migration/migrate_osmbc_md.py /path/to/downloads
################################################################################
"""

def run_step(script_name, source_path):
    script_path = Path(__file__).parent / script_name
    print(f"--- Running {script_name} ---")

    # Execute the sub-scripts using the same python interpreter
    result = subprocess.run([sys.executable, str(script_path), source_path])

    if result.returncode != 0:
        print(f"CRITICAL ERROR: {script_name} failed. Aborting workflow.")
        sys.exit(1)
    print(f"--- Finished {script_name} successfully ---\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ./migration/migrate_osmbc_md.py <source_directory>")
        sys.exit(1)

    source_dir = sys.argv[1]

    # Step 1: Transform Image and Metadata
    # This script will exit(1) if a lead image is missing
    run_step("transform_osmbc_leadimage.py", source_dir)

    # Step 2: Move and Rename Files
    # This handles the language-code folders and 4-digit naming
    run_step("move_osmbc_md.py", source_dir)

    print("All tasks completed successfully.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import os
import re
import sys
import shutil
from pathlib import Path

"""
################################################################################
# Purpose: This script moves OSMBC markdown downloads into the Hugo content 
# folder. It extracts the issue number and language code, then moves the file 
# to the appropriate archives directory (e.g., ./content/br/archives/0816.md).
#
# Usage (run from Hugo base directory):
#   python3 ./migration/move_osmbc_md.py /path/to/markdown/files
################################################################################
"""

def migrate_files(source_path):
    # Path to your Hugo base content directory
    hugo_base = Path("./content")
    source_dir = Path(source_path)

    if not source_dir.exists():
        print(f"Error: Source directory '{source_path}' does not exist.")
        return

    # Iterate through all .md files starting with "WN"
    for file_path in source_dir.glob("WN*.md"):
        filename = file_path.name

        # 1. Extract the issue number (digits following "WN")
        # Example: "WN816..." -> 816
        number_match = re.search(r'WN(\d+)', filename)
        if not number_match:
            continue
            
        issue_number = number_match.group(1)
        # Format to 4-digit string (e.g., 0816.md)
        target_filename = f"{issue_number.zfill(4)}.md"

        # 2. Extract the language code
        # Logic: Get the part before '.md', then the part after the last dot
        # Example: "WN816.2026.BR.md" -> BR
        try:
            lang_upper = file_path.stem.split('.')[-1]
            lang_lower = lang_upper.lower()
        except IndexError:
            print(f"Skipping {filename}: Could not determine language code.")
            continue

        # 3. Define and create the destination directory
        target_dir = hugo_base / lang_lower / "archives"
        target_dir.mkdir(parents=True, exist_ok=True)

        # Move and rename the file
        target_path = target_dir / target_filename
        shutil.move(str(file_path), str(target_path))

        print(f"Processed: {filename} -> {target_path}")

if __name__ == "__main__":
    # Get the source directory from command line argument, default to current dir
    src = sys.argv[1] if len(sys.argv) > 1 else "."
    migrate_files(src)

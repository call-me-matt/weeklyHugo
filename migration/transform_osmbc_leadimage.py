#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path
from datetime import datetime

"""
################################################################################
# Purpose: This script transforms OSMBC markdown files into Hugo format.
# It identifies the first category (regardless of language/name), extracts 
# the lead image and the caption text beneath it, and converts them into 
# TOML frontmatter. The first category is then removed from the body.
#
# Constraint: If no lead image is found, the script exits with an error.
#
# Usage (run from Hugo base directory):
#   python3 ./migration/transform_osmbc_leadimage.py ./content/path/to/files
################################################################################
"""

def transform_file(file_path):
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    # 1. Extract Issue Number from filename (e.g., 0816.md -> 816)
    issue_match = re.search(r'(\d+)', file_path.name)
    issue_num = issue_match.group(1).lstrip('0') if issue_match else "Unknown"

    # 2. Set current date (today)
    formatted_date = datetime.now().strftime("%Y-%m-%d")

    # 3. Split content into the first section and the rest
    # Logic: Find the first and second "## " to isolate the lead image category
    parts = re.split(r'^##\s+', content, flags=re.MULTILINE)
    
    # parts[0] is the date header (e.g., 05/03/2026-11/03/2026)
    # parts[1] is the first category (Image/Caption)
    # parts[2:] is the rest of the article
    if len(parts) < 3:
        print(f"CRITICAL ERROR: Could not find enough sections in {file_path.name}. Aborting.")
        sys.exit(1)

    first_category_body = parts[1]
    remaining_body = "## " + "## ".join(parts[2:])

    # 4. Extract Image URL from the first category
    img_match = re.search(r'\!\[.*?\]\((.*?)(\s+=\d+x\d+)?\)', first_category_body)
    if not img_match:
        print(f"CRITICAL ERROR: No lead image found in first category of {file_path.name}. Aborting.")
        sys.exit(1)
        
    img_url = img_match.group(1)

    # 5. Extract Caption (everything after the image block in that section)
    # We look for the text following the markdown image link closing parenthesis
    cap_match = re.search(r'\)\s*\n\n(.*?)(?=\n\n|$)', first_category_body, re.DOTALL)
    img_cap = cap_match.group(1).replace('\n', ' ').strip() if cap_match else ""

    # 6. Create Frontmatter (TOML)
    # "Birthday Adapter" remains untranslated in this workflow [cite: 2026-01-27]
    frontmatter = f"""+++
date = {formatted_date}
draft = false
title = 'weeklyOSM {issue_num}'
featureImage = '{img_url}'
featureImageCap = '{img_cap}'
+++

"""
    # Write the new file structure
    file_path.write_text(frontmatter + remaining_body.strip(), encoding='utf-8')
    print(f"Successfully transformed: {file_path.name}")

def main(source_path):
    source_dir = Path(source_path)
    if not source_dir.exists():
        print(f"Error: Path {source_path} not found.")
        sys.exit(1)

    md_files = list(source_dir.rglob("*.md"))
    if not md_files:
        print("No markdown files found.")
        return

    for md_file in md_files:
        # Avoid double processing
        file_start = md_file.read_text(encoding='utf-8').lstrip()
        if not file_start.startswith('+++'):
            transform_file(md_file)

if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "."
    main(src)

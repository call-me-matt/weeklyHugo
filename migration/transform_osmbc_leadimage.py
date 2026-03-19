#!/usr/bin/env python3
import os
import re
import sys
from pathlib import Path
from datetime import datetime

"""
################################################################################
# Purpose: This script targets the lead image section of OSMBC markdown files.
# It extracts the image URL and the caption text to create Hugo frontmatter 
# while removing the image category from the body.
#
# Constraint: If no lead image is found, the script exits with an error.
#
# Usage:
#   python3 ./migration/transform_osmbc_leadimage.py /path/to/markdown/files
################################################################################
"""


def transform_file(file_path):
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    # 1. Extract Issue Number from filename (e.g., 0816.md -> 816)
    issue_match = re.search(r"(\d+)", file_path.name)
    issue_num = issue_match.group(1).lstrip("0") if issue_match else "Unknown"

    # 2. Set current date (today) for Hugo frontmatter
    formatted_date = datetime.now().strftime("%Y-%m-%d")

    # 3. Separate the sections
    # parts[0] is the date header (e.g., 05/03/2026-11/03/2026)
    # parts[1] is the first category (Lead Image/Caption)
    # parts[2:] is the rest of the content
    parts = re.split(r"^##\s+", content, flags=re.MULTILINE)

    if len(parts) < 3:
        print(f"CRITICAL ERROR: Insufficient sections in {file_path.name}. Aborting.")
        sys.exit(1)

    date_header = parts[0].strip()
    first_category_body = parts[1]
    remaining_body = "## " + "## ".join(parts[2:])

    # 4. Extract Lead Image URL
    img_match = re.search(r"\!\[.*?\]\((.*?)(\s+=\d+x\d+)?\)", first_category_body)
    if not img_match:
        print(f"CRITICAL ERROR: No lead image found in {file_path.name}. Aborting.")
        sys.exit(1)

    img_url = img_match.group(1)

    # 5. Extract Caption text from the lead image category
    # Captures everything after the image link until the end of that section
    cap_match = re.search(r"\)\s*\n\n(.*?)(?=\n\n|$)", first_category_body, re.DOTALL)
    img_cap = cap_match.group(1).replace("\n", " ").strip() if cap_match else ""

    # 6. Construct Frontmatter (TOML)
    # "Birthday Adapter" remains untranslated per project rules [cite: 2026-01-27]
    frontmatter = f"""+++
date = {formatted_date}
draft = false
title = 'weeklyOSM {issue_num}'
featureImage = '{img_url}'
featureImageCap = '{img_cap}'
+++

"""
    # Build final file: Frontmatter + Original Date Line + Content
    new_content = frontmatter + date_header + "\n\n" + remaining_body.strip()

    file_path.write_text(new_content, encoding="utf-8")
    print(f"Successfully processed lead image for: {file_path.name}")


def main(source_path):
    source_dir = Path(source_path)
    if not source_dir.exists():
        print(f"Error: Path {source_path} not found.")
        sys.exit(1)

    md_files = list(source_dir.rglob("*.md"))
    for md_file in md_files:
        # Check if already processed to avoid corruption
        if not md_file.read_text(encoding="utf-8").lstrip().startswith("+++"):
            transform_file(md_file)


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "."
    main(src)

#!/usr/bin/env python3
import os
import re
import sys
import tomllib  # Use 'toml' if on Python < 3.11
from pathlib import Path

"""
################################################################################
# Purpose: This script ensures every language has at least a "shadow file"
# for a specific issue. It copies the Frontmatter from the English source.
#
# Usage:
#   python3 ./migration/create_shadow_files.py /path/to/markdown/files
################################################################################
"""


def create_shadows(source_path):
    source_dir = Path(source_path)
    if not source_dir.exists():
        print(f"Error: Source directory '{source_path}' does not exist.")
        return

    hugo_root = Path(".")
    lang_config_path = hugo_root / "config" / "_default" / "languages.toml"

    # 1. Extract issue number from the source filename
    for file_path in source_dir.glob("WN*.md"):
        filename = file_path.name

        # Extract the issue number (digits following "WN")
        # Example: "WN816..." -> 816
        number_match = re.search(r"WN(\d+)", filename)
        if not number_match:
            print(f"Skipping {filename}: Could not extract issue number.")
            continue
        issue_number = number_match.group(1)
        break  # We only need the issue number from one file to create shadows

    # 2. Load language configuration
    if not lang_config_path.exists():
        print("Error: languages.toml not found in current directory.")
        return

    with open(lang_config_path, "rb") as f:
        # tomllib is standard in Python 3.11+.
        # For older versions, use: import toml; languages = toml.load(f)
        languages = tomllib.load(f)

    # 3. Locate the English source file (the "Master")
    # Adjust 'en' if your default content language folder is named differently
    en_source = (
        hugo_root / "content" / "en" / "archives" / f"{issue_number.zfill(4)}.md"
    )

    if not en_source.exists():
        print(f"Error: English source file '{en_source}' not found. Cannot sync.")
        return

    # 4. Extract Frontmatter from English file
    with open(en_source, "r", encoding="utf-8") as f:
        content = f.read()
        # Regex to grab everything between the first two +++ markers
        match = re.match(r"^\+\+\+.*?\+\+\+", content, re.DOTALL)
        if not match:
            print(f"Error: Could not find TOML Frontmatter in {en_source}")
            return
        en_header = match.group(0)

    print(f"Syncing issue {issue_number} across all languages...")

    # 5. Iterate through languages defined in languages.toml
    for lang_code, config in languages.items():
        # Get the content directory (e.g., 'content/br')
        content_dir_rel = config.get("contentDir", f"content/{lang_code}")
        target_dir = hugo_root / content_dir_rel / "archives"
        target_file = target_dir / f"{issue_number.zfill(4)}.md"

        # Check if file already exists
        if target_file.exists():
            print(f"  [Skip] {lang_code}: File already exists.")
            continue

        # Create directory if it doesn't exist
        target_dir.mkdir(parents=True, exist_ok=True)

        # Write the shadow file (Header only, no body)
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(en_header + "\n")

        print(f"  [Created] {lang_code}: {target_file}")


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "."
    create_shadows(src)

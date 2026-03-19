#!/usr/bin/env python3
import re
import sys
from pathlib import Path

"""
################################################################################
# Purpose: This script updates the 'title' in the Hugo frontmatter based on 
# the language-specific name defined in config/_default/languages.toml.
# It identifies the correct language section by matching 'contentDir'.
# The issue number is extracted from the filename and appended to the title.
#
# Usage:
#   python3 ./migration/update_hugo_titles.py /path/to/temporary/source
################################################################################
"""


def get_language_titles():
    """
    Parses languages.toml and returns a mapping of lang_code -> title_prefix.
    Example: {'br': 'SemanárioOSM', 'de': 'Wochennotiz'}
    """
    config_path = Path("config/_default/languages.toml")
    if not config_path.exists():
        print(f"Error: Configuration not found at {config_path}")
        return {}

    content = config_path.read_text(encoding="utf-8")
    lang_map = {}

    # Split the TOML into blocks based on [language_code]
    blocks = re.split(r"\[([a-zA-Z\-]+)\]", content)

    for i in range(1, len(blocks), 2):
        block_content = blocks[i + 1]

        # Reliable check: Look for contentDir = "content/xx"
        dir_match = re.search(
            r'contentDir\s*=\s*["\']?content/([a-z]+)["\']?', block_content
        )
        # Look for the title = "..."
        title_match = re.search(r'title\s*=\s*["\'](.*?)["\']', block_content)

        if dir_match and title_match:
            lang_code = dir_match.group(1)
            title_prefix = title_match.group(1)
            lang_map[lang_code] = title_prefix

    return lang_map


def update():
    # Take the source path from argument (temp dir from zip) or default to ./content
    source_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("./content")

    if not source_path.exists():
        print(f"Error: Source path {source_path} does not exist.")
        sys.exit(1)

    # 1. Load the localized title prefixes (e.g., 'SemanárioOSM')
    titles_by_lang = get_language_titles()
    if not titles_by_lang:
        print("No language titles found in config. Aborting title update.")
        return

    # 2. Walk through the directory (recursively to handle ZIP structures)
    for md_file in source_path.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception as e:
            print(f"Could not read file {md_file}: {e}")
            continue

        # Skip files that don't have frontmatter yet
        if not content.lstrip().startswith("+++"):
            continue

        # 3. Detect language code
        # Pattern A: From filename suffix (e.g., .DE.md)
        lang_match = re.search(r"\.([A-Z]{2})\.md$", md_file.name)
        if lang_match:
            lang_code = lang_match.group(1).lower()
        else:
            # Pattern B: From parent directory structure (if already migrated)
            # path/to/content/de/archives/0816.md -> 'de'
            try:
                lang_code = md_file.parents[1].name
            except IndexError:
                continue

        prefix = titles_by_lang.get(lang_code)
        if not prefix:
            print(f"No title prefix found for language code: {lang_code}")
            continue

        # 4. Extract issue number (from filename WN816... or 0816.md)
        num_match = re.search(r"(\d+)", md_file.name)
        if num_match:
            # Remove leading zeros for the display title (0816 -> 816)
            issue_num = num_match.group(1).lstrip("0")

            # The new title: Localized Name + Space + Issue Number
            new_title_value = f"{prefix} {issue_num}"

            # Replace the title line in the frontmatter (matches 'TEMP 816' or similar)
            updated_content = re.sub(
                r"title\s*=\s*'.*?'", f"title = '{new_title_value}'", content
            )

            if content != updated_content:
                md_file.write_text(updated_content, encoding="utf-8")
                print(
                    f"Title updated for {md_file.name} ({lang_code}): {new_title_value}"
                )


if __name__ == "__main__":
    update()

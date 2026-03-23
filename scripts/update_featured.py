#!/usr/bin/env python3
"""
WEEKLY FEATURED POST UPDATER
----------------------------
This script automates the 'featured' flag for weekly posts (e.g., 0815.md or WN0815.md).
Target Path: content/<lang>/archives/<number>.md
Logic:
1. Scans only the 'archives' subfolders for numeric Markdown files.
2. Identifies the highest issue number for each language.
3. Removes any existing 'featured: ...' lines from all previous posts.
4. Injects 'featured: true' only into the post with the highest number.
"""

import os
import re


def update_featured():
    content_root = "content"

    # Regex for path:
    # 1. content[\\/]           -> Start folder
    # 2. ([^\\/]+)              -> Group 1: Language (e.g., 'de')
    # 3. [\\/]archives[\\/]     -> Target subfolder
    # 4. .*?                    -> Non-greedy match for any prefix (optional)
    # 5. (\d+)                  -> Group 2: The actual number at the end
    # 6. \.md$                  -> File extension
    path_pattern = re.compile(r"content[\\/]([^\\/]+)[\\/]archives[\\/].*?(\d+)\.md$")

    # Matches 'featured = true' or 'featured: true' (including variations in spacing/quotes)
    featured_line_pattern = re.compile(
        r"^featured\s*[:=].*\n?", re.MULTILINE | re.IGNORECASE
    )

    latest_issues = {}
    all_issue_files = []

    if not os.path.exists(content_root):
        print(f"Error: {content_root} directory not found.")
        return

    # Phase 1: Scan for the highest number per language
    for root, _, files in os.walk(content_root):
        for filename in files:
            full_path = os.path.join(root, filename)
            match = path_pattern.search(full_path)

            if match:
                lang = match.group(1)
                issue_num = int(match.group(2))
                all_issue_files.append((lang, issue_num, full_path))

                if lang not in latest_issues or issue_num > latest_issues[lang]:
                    latest_issues[lang] = issue_num

    # Phase 2: Update the TOML metadata
    for lang, issue_num, file_path in all_issue_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        is_latest = issue_num == latest_issues[lang]

        # Remove any existing featured line (clean slate)
        temp_content = featured_line_pattern.sub("", content)

        if is_latest:
            # Inject 'featured = true' into the TOML block (after the first +++)
            new_content = temp_content.replace("+++\n", "+++\nfeatured = true\n", 1)
        else:
            new_content = temp_content

        # Save only if changed
        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            status = "SET (latest)" if is_latest else "CLEANED"
            print(f"[{lang.upper()}] {status}: {file_path}")


if __name__ == "__main__":
    update_featured()

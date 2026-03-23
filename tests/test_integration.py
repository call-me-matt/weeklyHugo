import os
import glob
import re
import tomllib
import pytest
from pathlib import Path


# Load languages from the Hugo configuration file to ensure tests are aligned with the actual site setup
def get_languages():
    with open("config/_default/languages.toml", "rb") as f:
        config = tomllib.load(f)
    return list(config.keys())


LANGUAGES = get_languages()


@pytest.mark.parametrize("lang", LANGUAGES)
def test_content_directory_exists(lang):
    """Checks if the public directory for the language was generated."""
    path = f"public/{lang}"
    assert os.path.isdir(path), f"Output directory '{path}' was not generated!"


def test_global_search_index():
    """Checks if the main Pagefind JS file exists."""
    assert os.path.exists(
        "public/pagefind/pagefind.js"
    ), "Global Pagefind index is missing!"


@pytest.mark.parametrize("lang", LANGUAGES)
def test_pagefind_metadata_exists(lang):
    """Checks if Pagefind generated metadata for the specific language."""
    pattern = f"public/pagefind/pagefind.{lang}_*.pf_meta"
    matches = glob.glob(pattern)
    assert len(matches) > 0, f"Pagefind search metadata missing for language: {lang}"


def get_archive_issues(lang):
    """Helper to collect all numeric issues from a language's archive."""
    archive_path = f"content/{lang}/archives"
    suffix_number_regex = re.compile(r"(\d+)$")

    if not os.path.isdir(archive_path):
        return None, []

    issues = []
    for filename in os.listdir(archive_path):
        p = Path(filename)
        # Only accept files like '0815.md' or 'WN1000.md'
        if p.suffix == ".md":

            match = suffix_number_regex.search(p.stem)
            if match:
                # match.group(1) extrahiert nur den Zahlenteil (z.B. 0815 aus WN_0815)
                issue_num = int(match.group(1))

                issues.append(
                    {
                        "num": issue_num,
                        "name": filename,
                        "path": os.path.join(archive_path, filename),
                    }
                )
    return archive_path, issues


@pytest.mark.parametrize("lang", LANGUAGES)
def test_only_one_featured_issue(lang):
    """Ensures exactly ONE 'featured = true' exists in the TOML header."""
    _, issues = get_archive_issues(lang)
    if not issues:
        pytest.skip(f"No issues found for {lang}")

    featured_found = []
    for issue in issues:
        with open(issue["path"], "r", encoding="utf-8") as f:
            content = f.read()
            # Isolate the TOML frontmatter between +++ markers
            parts = content.split("+++")
            if len(parts) >= 3:
                # Clean spaces to match 'featured=true' regardless of formatting
                header = parts[1].replace(" ", "")
                if "featured=true" in header:
                    featured_found.append(issue["name"])

    assert (
        len(featured_found) == 1
    ), f"Expected 1 featured post in {lang}, but found {len(featured_found)}: {featured_found}"


@pytest.mark.parametrize("lang", LANGUAGES)
def test_latest_issue_is_featured(lang):
    """Verifies that the highest numeric issue carries the featured flag."""
    _, issues = get_archive_issues(lang)
    if not issues:
        pytest.skip(f"No issues found for {lang}")

    latest_num = max(issue["num"] for issue in issues)

    for issue in issues:
        if issue["num"] == latest_num:
            with open(issue["path"], "r", encoding="utf-8") as f:
                content = f.read()
                parts = content.split("+++")
                has_flag = len(parts) >= 3 and "featured = true" in parts[1]
                assert (
                    has_flag
                ), f"Latest issue {issue['name']} in {lang} is missing 'featured = true'!"

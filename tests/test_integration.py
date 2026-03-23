import os
import glob
import tomllib
import pytest


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

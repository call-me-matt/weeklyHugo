"""
=============================================================================
ASSET MIGRATION SCRIPT (TESTING ONLY)
=============================================================================
Description:
This script scans all Markdown files in the './content/' directory for 
external 'weeklyosm.eu/wp-content/...' or 'www.weeklyosm.eu/wp-content/...' 
links. It downloads the referenced resources and saves them into 
'./static/wp-content/' while preserving the original folder structure.

Use Case:
This is intended for testing purposes when you do not want to copy or 
download the entire wp-content directory manually, but only the assets 
actually used in your content.
=============================================================================
"""

import os
import re
import requests
from pathlib import Path

# Configuration
SOURCE_DIR = "./content"
TARGET_BASE_DIR = "./static/wp-content"

# Updated Regex to handle optional 'www.'
# Captures everything until the next space, closing parenthesis, quote, or angle bracket
URL_PATTERN = re.compile(r'https://(?:www\.)?weeklyosm\.eu/wp-content/[^\s\)\"\'\>]+')

def download_file(session, url, local_path):
    """Downloads a file if it doesn't exist locally yet."""
    if local_path.exists():
        # Skip if file is already present to save bandwidth
        return 
    
    try:
        print(f"Downloading: {url}")
        response = session.get(url, stream=True, timeout=10)
        response.raise_for_status()
        
        # Ensure the local directory structure exists
        local_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Save the file in chunks to handle larger files safely
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def main():
    # Initialize a session for better performance (reuses the connection)
    session = requests.Session()
    
    # Find all Markdown files recursively
    md_files = list(Path(SOURCE_DIR).rglob("*.md"))
    print(f"Found {len(md_files)} Markdown files to scan.")
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Could not read file {md_file}: {e}")
            continue
            
        urls = URL_PATTERN.findall(content)
        
        # Use set() to avoid redundant downloads within the same file
        for url in set(urls):
            # Clean the URL to extract the relative path after 'wp-content/'
            # This handles both www.weeklyosm.eu and weeklyosm.eu
            relative_path = re.sub(r'http(?:s)://(?:www\.)?weeklyosm\.eu/wp-content/', '', url).lstrip("/")
            local_target = Path(TARGET_BASE_DIR) / relative_path
            
            download_file(session, url, local_target)

if __name__ == "__main__":
    main()

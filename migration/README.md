# OSMBC to Hugo Migration Toolkit

This toolkit automates the processing of **weeklyOSM** markdown exports. It transforms raw exports into Hugo-compatible blog posts, handles lead images, localizes titles based on your Hugo configuration, and organizes files into the correct directory structure.

## 🚀 Standard Workflow

1. Export: Download the "Markdown ZIP" from OSMBC for the required issue.

2. Prepare Inbox: Place the ZIP file(s) into migration/inbox/.

3. Run Migration: Execute the orchestrator from the project root:
```bash
python3 ./migration/migrate_osmbc_md.py
```

What happens during migration?

- Extraction: ZIPs are unpacked into a temporary workspace.

- Lead Image: The first category is parsed for the image URL and caption. These are moved to frontmatter (featureImage).

- Title Fix: Titles are updated (e.g., SemanárioOSM 816) using the languages.toml mapping.

- Routing: Files are renamed (e.g., 0816.md) and moved to content/<lang>/archives/.

- Archiving: Successfully processed ZIPs in the inbox are prefixed with OK_.


## 📂 Directory Structure

The scripts are designed to reside in a `migration/` folder within your Hugo project root:

```text
your-hugo-project/
├── config/
│   └── _default/
│       └── languages.toml        # Source for localized titles
├── content/                     # Target for processed archives
├── static/
│   └── wp-content/               # Target for local image assets
├── migration/
│   ├── inbox/                   # Place your downloaded ZIP files here
│   ├── migrate_osmbc_md.py      # The Master Orchestrator
│   ├── transform_osmbc_leadimage.py
│   ├── update_hugo_titles.py
│   ├── move_osmbc_md.py         # Final file routing
│   └── dev-content-loader.py    # Local asset downloader
└── README.md
```

## 🖼 Local Development & Assets

dev-content-loader.py

To avoid broken images or unnecessary external requests during local development, use this script to mirror remote images:

Purpose: It scans your markdown files for external URLs (specifically from weeklyosm.eu), downloads them, and saves them into static/wp-content/.

Usage:
```bash
python3 ./migration/dev-content-loader.py
```

Benefit: This allows your local Hugo server to serve images directly from the static/ folder, ensuring a fast and offline-capable preview of the archives.

## 🛠 Script Overview

| Script | Responsibility |
| :--- | :--- |
| **migrate_osmbc_md.py** | The **Master Orchestrator**. Manages the temp workspace and runs steps in sequence. |
| **transform_osmbc_leadimage.py** | Extracts image/caption to frontmatter. Preserves the original date line in the body. |
| **update_hugo_titles.py** | Matches `contentDir` to `languages.toml` to set localized issue titles. |
| **move_osmbc_md.py** | Final step: Moves files to their permanent language-specific archive folders. |
| **dev-content-loader.py** | Downloads remote picture uploads to the local `static/wp-content` directory. Only needed for local setup. |

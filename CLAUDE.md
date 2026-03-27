# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static HTML/CSS coaching website for Nick Hampshire (nickhampshire.com), hosted on GitHub Pages. There is no build system — all pages are hand-authored HTML files with shared CSS.

## Commands

**Sync blog from Substack RSS:**
```bash
pip install requests feedparser beautifulsoup4
python generate_blog.py
```
This fetches the latest posts from `https://nickhampshire.substack.com/feed`, regenerates `blog/index.html`, all individual `blog/*.html` post pages, and updates the "Latest from the Blog" section in `index.html`.

**Local development server:**
The `.vscode/launch.json` is configured to open Chrome at `http://localhost:8080`. Use any static file server (e.g. `python -m http.server 8080`).

## Architecture

### Pages
Each section is a directory with its own `index.html`: `about/`, `coaching/`, `speaking/`, `contact/`. Blog post files live flat in `blog/`.

### CSS
All styles are in `css/custom.css` using CSS custom properties (design tokens) defined at the top:
- Primary: `#9FEDED` (teal), Secondary: `#7A3EE3` (purple), Background: `#0F0A1A` (near-black)
- Bootstrap 5.3.0 is the grid/component foundation; `custom.css` overrides and extends it.

### Blog Generation (`generate_blog.py`)
- Fetches up to 20 entries from Substack RSS
- Entry 0 → featured card layout; entries 1–19 → standard card layout in `blog/index.html`
- Individual post HTML files are named by slugified title (e.g. `blog/my-post-title.html`)
- The homepage blog section is delimited by `<!-- BLOG_SECTION_START -->` and `<!-- BLOG_SECTION_END -->` markers; the script replaces content between them on each run
- Nav, footer, and `<head>` for generated pages are hardcoded in `POST_TEMPLATE` and `INDEX_HEADER`/`INDEX_FOOTER` strings inside the script — update those constants to change shared structure on generated pages

### External Integrations
- Calendly booking: `https://calendly.com/nickhampshire1/chat`
- Google Translate widget: `translate.js`
- Social links: Twitter/X, LinkedIn, Facebook, YouTube, Instagram, Substack

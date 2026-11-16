# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static HTML/CSS coaching website for Nick Hampshire (nickhampshire.com), hosted on GitHub Pages. Pages are hand-authored HTML with shared CSS. The only build step is a small Python script that copies the shared nav, footer and head assets into every page; its output is committed, so GitHub Pages serves the files as they are.

## Commands

**Update shared nav, footer, head assets or post footer:**
```bash
python build_partials.py
```
Edit the files in `partials/`, then run this. It replaces the content between marker pairs (for example `<!-- NAV_SECTION_START -->` / `<!-- NAV_SECTION_END -->`) on every page, including all blog posts, and marks the current nav item with `active` and `aria-current="page"`.

**Sync blog from Substack RSS:**
```bash
pip install requests feedparser beautifulsoup4
python generate_blog.py                    # latest posts from the feed
python generate_blog.py --rebuild-archive  # also re-render older posts no longer in the feed
```
This fetches the latest posts from `https://nickhampshire.substack.com/feed`, regenerates `blog/index.html`, the individual `blog/*.html` post pages, and the "Latest from the blog" section in `index.html`, then runs `build_partials.py`. The feed only carries 20 posts, so use `--rebuild-archive` after changing `POST_TEMPLATE` to reach the older posts too.

**Local development server:**
The `.vscode/launch.json` is configured to open Chrome at `http://localhost:8080`. Use any static file server (e.g. `python -m http.server 8080`).

## Architecture

### Pages
Each section is a directory with its own `index.html`: `about/`, `coaching/`, `speaking/`, `contact/`, `privacy/`. Blog post files live flat in `blog/`. `thankyou.html` (contact form redirect) and `404.html` sit at the root. Use root-relative URLs (`/about/`, `/css/custom.css`) everywhere, because GitHub Pages serves `404.html` at whatever path was missing.

### Shared blocks (`partials/`)
- `head-assets.html`: favicon, fonts, Bootstrap, Bootstrap Icons, `custom.css`
- `nav.html`: skip link and navbar
- `footer.html`: footer plus the Bootstrap and `main.js` scripts
- `post-end.html`: author block at the end of every blog post

Never edit these blocks inside a page; edit the partial and run `python build_partials.py`.

### CSS
All styles are in `css/custom.css` using CSS custom properties (design tokens) defined at the top:
- Primary: `#9FEDED` (teal), Secondary: `#7A3EE3` (purple), Background: `#0F0A1A` (near-black)
- Every font-size uses the seven-rung type scale; spacing between top-level sections comes only from `--section-gap`, so keep Bootstrap spacing utilities off `<section>`
- Transitions use `--duration` and `--ease-out` and name their properties; never `transition: all`
- Bootstrap 5.3.0 is the grid/component foundation; `custom.css` overrides and extends it.

### Blog Generation (`generate_blog.py`)
- Fetches up to 20 entries from Substack RSS
- Entry 0 → featured card layout; entries 1–19 → standard card layout in `blog/index.html`
- Individual post HTML files are named by slugified title (e.g. `blog/my-post-title.html`)
- The homepage blog section is delimited by `<!-- BLOG_SECTION_START -->` and `<!-- BLOG_SECTION_END -->` markers; the script replaces content between them on each run, so edit that markup in the script, not in `index.html`
- `POST_TEMPLATE` and `INDEX_HEADER`/`INDEX_FOOTER` hold the page skeletons; nav, footer and head assets come from `partials/`
- Posts without their own image get one from `FALLBACK_IMAGES` (3:2 crops in `images/blog-fallback/`), picked by a hash of the slug so it stays stable between runs

### External Integrations
- Calendly booking: `https://calendly.com/nickhampshire1/chat` (every booking button uses the label "Book a free call")
- Contact form: Web3Forms, redirecting to `thankyou.html`
- Google Translate widget: `translate.js`
- Social links: X, LinkedIn, Facebook, YouTube, Instagram, Substack

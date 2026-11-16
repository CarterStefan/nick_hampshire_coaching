"""Inject the shared nav, footer, head assets and post footer into every page.

Each page marks where a shared block goes with a pair of comments, for example
<!-- NAV_SECTION_START --> ... <!-- NAV_SECTION_END -->. Anything between the
markers is replaced with the matching file from partials/. Pages without a
given pair of markers are left alone for that block.

Run after editing anything in partials/:
    python build_partials.py

generate_blog.py calls this automatically after it writes the blog.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
PARTIALS_DIR = ROOT / "partials"

# page -> nav href to mark as the current page (None marks nothing)
PAGES = {
    "index.html": "/",
    "about/index.html": "/about/",
    "coaching/index.html": "/coaching/",
    "speaking/index.html": "/speaking/",
    "contact/index.html": "/contact/",
    "thankyou.html": None,
    "privacy/index.html": None,
    "404.html": None,
}

# marker name -> partial file
BLOCKS = {
    "HEAD_ASSETS": "head-assets.html",
    "NAV_SECTION": "nav.html",
    "FOOTER_SECTION": "footer.html",
    "POST_END": "post-end.html",
}


def load_partials():
    return {marker: (PARTIALS_DIR / name).read_text(encoding="utf-8").rstrip() for marker, name in BLOCKS.items()}


def with_active(nav, href):
    """Mark the nav link for href as the current page."""
    if not href:
        return nav
    return nav.replace(
        f'class="nav-link" href="{href}"',
        f'class="nav-link active" aria-current="page" href="{href}"',
    )


def inject(html, marker, block):
    pattern = rf"(<!-- {marker}_START -->).*?([ \t]*<!-- {marker}_END -->)"
    return re.sub(pattern, lambda m: f"{m.group(1)}\n{block}\n{m.group(2)}", html, flags=re.DOTALL)


def render(html, partials, active_href):
    for marker, block in partials.items():
        if marker == "NAV_SECTION":
            block = with_active(block, active_href)
        html = inject(html, marker, block)
    return html


def all_pages():
    """Every page that takes shared blocks, with the nav item it should mark."""
    pages = [(ROOT / page, href) for page, href in PAGES.items()]
    pages += [(path, "/blog/") for path in sorted((ROOT / "blog").glob("*.html"))]
    return [(path, href) for path, href in pages if path.exists()]


def main():
    partials = load_partials()
    updated = 0
    for path, href in all_pages():
        html = path.read_text(encoding="utf-8")
        new_html = render(html, partials, href)
        if new_html != html:
            path.write_text(new_html, encoding="utf-8")
            updated += 1
    print(f"Shared blocks injected: {updated} page(s) changed")


if __name__ == "__main__":
    main()

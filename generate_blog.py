"""Sync the blog from Substack.

    python generate_blog.py                    # latest posts from the feed
    python generate_blog.py --rebuild-archive  # also re-render older posts on disk

The feed only carries the latest 20 posts. Older posts stay in blog/ and are
re-rendered from their own HTML with --rebuild-archive, so a template change
reaches every post. Shared nav, footer and head assets come from partials/
via build_partials.py, which runs at the end.
"""
import argparse
import hashlib
import html
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import feedparser
import requests
from bs4 import BeautifulSoup

import build_partials

# ---------------- CONFIG ----------------
FEED_URL = "https://nickhampshire.substack.com/feed"
SITE_URL = "https://nickhampshire.com"
ROOT = Path(__file__).parent
BLOG_DIR = ROOT / "blog"
HOMEPAGE = ROOT / "index.html"
INDEX_LIMIT = 20
HOMEPAGE_LIMIT = 4

# Posts without an image of their own get one of these (paths under images/).
# The choice comes from a hash of the slug, so a post keeps the same image
# between runs. They are 3:2 crops of photos the homepage does not use, so the
# blog cards never repeat the gallery above them.
FALLBACK_IMAGES = [
    "blog-fallback/Nick_Pensive.webp",
    "blog-fallback/Nick_Podcast.webp",
    "blog-fallback/Nick_Podcast_2.webp",
    "blog-fallback/Nick_Running.webp",
    "blog-fallback/Nick_Running_2.webp",
    "blog-fallback/RunningMinds041.webp",
    "blog-fallback/1000128511.webp",
    "blog-fallback/RunningMinds034.webp",
]
# ----------------------------------------

# ---------------- HTML Templates ----------------
INDEX_HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blog | Nick Hampshire</title>
  <meta name="description" content="Insights on communication, leadership and personal performance from Nick Hampshire, coach, speaker and event host.">
  <link rel="canonical" href="https://nickhampshire.com/blog/">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://nickhampshire.com/blog/">
  <meta property="og:title" content="Blog | Nick Hampshire">
  <meta property="og:description" content="Insights on communication, leadership and personal performance from Nick Hampshire, coach, speaker and event host.">
  <meta property="og:image" content="https://nickhampshire.com/images/Nick_Hero.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="627">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Blog | Nick Hampshire">
  <meta name="twitter:description" content="Insights on communication, leadership and personal performance from Nick Hampshire, coach, speaker and event host.">
  <meta name="twitter:image" content="https://nickhampshire.com/images/Nick_Hero.jpg">
  <!-- HEAD_ASSETS_START -->
  <!-- HEAD_ASSETS_END -->
</head>
<body>
  <!-- NAV_SECTION_START -->
  <!-- NAV_SECTION_END -->
  <main id="main" class="container">
    <div class="page-intro">
      <h1>The blog</h1>
      <p class="lead">Insights on communication, leadership and performance.</p>
    </div>
    <div class="blog-list-group">
"""

INDEX_FOOTER = """    </div>
  </main>
  <!-- FOOTER_SECTION_START -->
  <!-- FOOTER_SECTION_END -->
</body>
</html>
"""

POST_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_attr} | Nick Hampshire</title>
  <meta name="description" content="{subtitle_attr}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{title_attr} | Nick Hampshire">
  <meta property="og:description" content="{subtitle_attr}">
  <meta property="og:image" content="{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title_attr} | Nick Hampshire">
  <meta name="twitter:description" content="{subtitle_attr}">
  <meta name="twitter:image" content="{og_image}">
  <!-- HEAD_ASSETS_START -->
  <!-- HEAD_ASSETS_END -->
  <script type="application/ld+json">
{ld_json}
  </script>
</head>
<body>
  <!-- NAV_SECTION_START -->
  <!-- NAV_SECTION_END -->
  <main id="main" class="container">
    <article class="post">
      <div class="post-header">
        <h1>{title_html}</h1>
        <p class="post-date">{date}</p>
      </div>
      <div class="post-body">
      {content}
      </div>
    </article>
    <!-- POST_END_START -->
    <!-- POST_END_END -->
  </main>
  <!-- FOOTER_SECTION_START -->
  <!-- FOOTER_SECTION_END -->
</body>
</html>
"""
# ------------------------------------------------


@dataclass
class Post:
    slug: str
    title: str
    subtitle: str
    content: str
    published: datetime | None
    image: str          # root-relative or absolute URL
    has_own_image: bool

    @property
    def url(self):
        return f"{SITE_URL}/blog/{self.slug}.html"

    @property
    def og_image(self):
        return self.image if self.image.startswith("http") else SITE_URL + self.image

    @property
    def date_long(self):
        return self.published.strftime("%B %d, %Y") if self.published else ""

    @property
    def date_short(self):
        return self.published.strftime("%b %d, %Y") if self.published else ""


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def fallback_image(slug):
    digest = int(hashlib.md5(slug.encode()).hexdigest(), 16)
    return FALLBACK_IMAGES[digest % len(FALLBACK_IMAGES)]


def image_for(slug, content):
    """The post's first image, or a stable fallback from the pool."""
    img_tag = BeautifulSoup(content, "html.parser").find("img")
    if img_tag and img_tag.get("src"):
        return img_tag["src"], True
    return f"/images/{fallback_image(slug)}", False


def clean_content(content):
    soup = BeautifulSoup(content, "html.parser")
    for tag in soup(["script", "iframe"]):
        tag.extract()
    return str(soup)


def post_from_entry(entry):
    content = entry.get("content", [{"value": entry.get("summary", "")}])[0]["value"]
    raw_subtitle = entry.get("summary", "")
    subtitle = BeautifulSoup(raw_subtitle, "html.parser").get_text().strip() if raw_subtitle else ""
    slug = slugify(entry.title)
    image, own = image_for(slug, content)
    return Post(
        slug=slug,
        title=entry.title,
        subtitle=subtitle,
        content=clean_content(content),
        published=datetime(*entry.published_parsed[:6]),
        image=image,
        has_own_image=own,
    )


def post_from_file(path):
    """Rebuild a Post from a page already in blog/ (old or new template)."""
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    h1 = soup.find("h1")
    body = soup.select_one(".post-body") or soup.find("article")
    date_tag = soup.select_one(".post-date") or (h1.find_next_sibling("p") if h1 else None)
    description = soup.find("meta", attrs={"name": "description"})

    published = None
    if date_tag:
        try:
            published = datetime.strptime(date_tag.get_text(strip=True), "%B %d, %Y")
        except ValueError:
            pass

    content = "".join(str(child) for child in body.contents).strip() if body else ""
    image, own = image_for(path.stem, content)
    return Post(
        slug=path.stem,
        title=h1.get_text(strip=True) if h1 else path.stem,
        subtitle=description["content"] if description else "",
        content=content,
        published=published,
        image=image,
        has_own_image=own,
    )


def render_post(post):
    ld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": post.title,
        "description": post.subtitle,
        "image": post.og_image,
        "author": {"@type": "Person", "name": "Nick Hampshire", "url": SITE_URL},
        "publisher": {"@type": "Person", "name": "Nick Hampshire", "url": SITE_URL},
        "url": post.url,
    }
    if post.published:
        ld["datePublished"] = post.published.date().isoformat()
    ld_json = json.dumps(ld, indent=2, ensure_ascii=False).replace("</", "<\\/")

    subtitle = post.subtitle or "Insights on communication, leadership and personal performance from Nick Hampshire."
    return POST_TEMPLATE.format(
        title_attr=html.escape(post.title),
        title_html=html.escape(post.title, quote=False),
        subtitle_attr=html.escape(subtitle),
        url=post.url,
        og_image=html.escape(post.og_image),
        ld_json=ld_json,
        date=post.date_long,
        content=post.content,
    )


def display_images(posts, window):
    """Images for a run of cards, stepping a fallback forward through the pool
    when it would repeat one of the previous `window` cards."""
    recent, images = [], []
    for post in posts:
        image = post.image
        if not post.has_own_image:
            name = image.removeprefix("/images/")
            start = FALLBACK_IMAGES.index(name)
            for step in range(len(FALLBACK_IMAGES)):
                name = FALLBACK_IMAGES[(start + step) % len(FALLBACK_IMAGES)]
                if f"/images/{name}" not in recent[-window:]:
                    break
            image = f"/images/{name}"
        recent.append(image)
        images.append(image)
    return images


def blog_tile(post, image, featured):
    classes = "blog-tile blog-tile--featured" if featured else "blog-tile"
    loading = "" if featured else ' loading="lazy"'
    subtitle = f'\n          <p class="blog-tile-subtitle">{html.escape(post.subtitle, quote=False)}</p>' if post.subtitle else ""
    return f"""      <a href="{post.slug}.html" class="{classes}">
        <img src="{html.escape(image)}" alt=""{loading}>
        <div class="blog-tile-body">
          <h2 class="blog-tile-title">{html.escape(post.title, quote=False)}</h2>{subtitle}
          <p class="blog-tile-date">{post.date_short}</p>
        </div>
      </a>
"""


def build_index(posts):
    posts = posts[:INDEX_LIMIT]
    images = display_images(posts, window=2)
    tiles = [blog_tile(post, image, featured=(i == 0)) for i, (post, image) in enumerate(zip(posts, images))]
    (BLOG_DIR / "index.html").write_text(INDEX_HEADER + "".join(tiles) + INDEX_FOOTER, encoding="utf-8")


def build_homepage_section(posts):
    posts = posts[:HOMEPAGE_LIMIT]
    images = display_images(posts, window=HOMEPAGE_LIMIT)
    featured, recent = posts[0], posts[1:]

    cards = f"""<section id="latest-blog" class="container">
      <div class="section-head">
        <h2>Latest from the blog</h2>
      </div>
      <div class="blog-grid">

        <div class="blog-featured">
          <a href="/blog/{featured.slug}.html" class="text-decoration-none text-reset">
            <div class="card h-100 text-bg-dark">
              <img src="{html.escape(images[0])}" class="card-img-top" alt="" loading="lazy">
              <div class="card-body">
                <h3 class="card-title">{html.escape(featured.title, quote=False)}</h3>
                <p class="card-subtitle">{html.escape(featured.subtitle, quote=False)}</p>
                <p class="card-text">{featured.date_short}</p>
              </div>
            </div>
          </a>
        </div>

        <div class="blog-recent">
"""
    for post, image in zip(recent, images[1:]):
        cards += f"""
          <div class="blog-mini">
            <a href="/blog/{post.slug}.html" class="text-decoration-none text-reset">
              <div class="card text-bg-dark">
                <div class="blog-mini-row">
                  <img src="{html.escape(image)}" class="blog-mini-img" alt="" loading="lazy">
                  <div class="blog-mini-body">
                    <h3 class="card-title">{html.escape(post.title, quote=False)}</h3>
                    <p class="card-text">{post.date_short}</p>
                  </div>
                </div>
              </div>
            </a>
          </div>
"""
    cards += """        </div>
      </div>
    </section>"""

    wrapped = f"<!-- BLOG_SECTION_START -->\n    {cards}\n    <!-- BLOG_SECTION_END -->"
    homepage = HOMEPAGE.read_text(encoding="utf-8")
    pattern = r"<!-- BLOG_SECTION_START -->.*?<!-- BLOG_SECTION_END -->"
    if re.search(pattern, homepage, flags=re.DOTALL):
        homepage = re.sub(pattern, lambda _: wrapped, homepage, flags=re.DOTALL)
        print("✅ Homepage blog section replaced with the latest posts")
    else:
        homepage += "\n" + wrapped
        print("✅ Homepage blog section added at end (first time)")
    HOMEPAGE.write_text(homepage, encoding="utf-8")


def rebuild_archive(feed_slugs):
    """Re-render posts that are on disk but no longer in the feed."""
    count = 0
    for path in sorted(BLOG_DIR.glob("*.html")):
        if path.name == "index.html" or path.stem in feed_slugs:
            continue
        path.write_text(render_post(post_from_file(path)), encoding="utf-8")
        count += 1
    print(f"✅ Re-rendered {count} archived post(s)")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--rebuild-archive", action="store_true",
                        help="also re-render older posts in blog/ that are no longer in the feed")
    args = parser.parse_args()

    BLOG_DIR.mkdir(exist_ok=True)
    feed = feedparser.parse(requests.get(FEED_URL, timeout=30).content)
    posts = [post_from_entry(entry) for entry in feed.entries]

    build_index(posts)
    for i, post in enumerate(posts, start=1):
        (BLOG_DIR / f"{post.slug}.html").write_text(render_post(post), encoding="utf-8")
        print(f"✅ Generated post {i}: {post.title} → {post.slug}.html")

    build_homepage_section(posts)

    if args.rebuild_archive:
        rebuild_archive({post.slug for post in posts})

    build_partials.main()


if __name__ == "__main__":
    main()

import os
import requests
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime
import re

# ---------------- CONFIG ----------------
FEED_URL = "https://nickhampshire.substack.com/feed"
BLOG_DIR = "blog"
HOMEPAGE = "index.html"
PLACEHOLDER = "<!-- BLOG_SECTION -->"
# ----------------------------------------

os.makedirs(BLOG_DIR, exist_ok=True)

feed = feedparser.parse(requests.get(FEED_URL).content)

# ---------------- HTML Templates ----------------
INDEX_HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nick Hampshire Coaching - Blog</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link
    href="https://fonts.googleapis.com/css2?family=Archivo+Narrow:ital,wght@0,400..700;1,400..700&family=Bebas+Neue&display=swap"
    rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">  
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
  <link href="../css/custom.css" rel="stylesheet">
</head>
<body>
  <nav class="navbar navbar-expand-lg">
    <div class="container">
      <a class="navbar-brand" href="../index.html">N</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
          <li class="nav-item"><a class="nav-link" href="../services.html">Services</a></li>
          <li class="nav-item"><a class="nav-link active" href="/index.html">Blog</a></li>
          <li class="nav-item"><a class="nav-link" href="../contact.html">Contact</a></li>
          <li class="nav-item"><a class="nav-link" onclick="translatePage('en')">English</a></li>
          <li class="nav-item"><a class="nav-link" onclick="translatePage('es')">Español</a></li>
          <!-- Hidden Google Translate element -->
          <div id="google_translate_element" style="display:none;"></div>
        </ul>
      </div>
    </div>
  </nav>
  <main class="container mt-5">
    <h1 class="text-center mb-4">My Blog</h1>
    <div class="blog-list-group">
"""

INDEX_FOOTER = """
    </div>
  </main>
  <footer id="footer" class="bg-black text-white text-center">
    <div class="">
      <a href="https://x.com/nickhamps04" class="social-icon" aria-label="Twitter"><i class="bi bi-twitter"
          style="font-size: 1.5rem;"></i></a>
      <a href="https://www.linkedin.com/in/nickhampshire1/" class="social-icon" aria-label="LinkedIn"><i
          class="bi bi-linkedin" style="font-size: 1.5rem;"></i></a>
      <a href="https://www.facebook.com/nickhampshirefitness/" class="social-icon" aria-label="Facebook"><i
          class="bi bi-facebook" style="font-size: 1.5rem;"></i></a>
      <a href="https://www.youtube.com/@nickhampshire" class="social-icon" aria-label="YouTube"><i class="bi bi-youtube"
          style="font-size: 1.5rem;"></i></a>
      <a href="https://www.instagram.com/nickhampshire_/?hl=en" class="social-icon" aria-label="Instagram"><i
          class="bi bi-instagram" style="font-size: 1.5rem;"></i></a>
      <a href="https://nickhampshire.substack.com/" class="social-icon" aria-label="Substack"><i class="bi bi-substack"
          style="font-size: 1.5rem;"></i></a>
    </div>
    <div>
      <p>&copy; 2025 Nick Hampshire Coaching. All rights reserved.</p>
    </div>
  </footer>

  <!-- FOOTER_SECTION_END -->

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  <script src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
  <!-- Load your custom translation JS -->
  <script src="../translate.js"></script>
</body>
</html>
"""

POST_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Blog</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Narrow:...&family=Bebas+Neue&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/all.min.css">
  <link href="../css/custom.css" rel="stylesheet">
</head>
<body>
  <nav class="navbar navbar-expand-lg">
    <div class="container">
      <a class="navbar-brand" href="../index.html">N</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item"><a class="nav-link" href="../index.html">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="../about.html">About</a></li>
          <li class="nav-item"><a class="nav-link" href="../services.html">Services</a></li>
          <li class="nav-item"><a class="nav-link active" href="blog/index.html">Blog</a></li>
          <li class="nav-item"><a class="nav-link" href="../contact.html">Contact</a></li>
          <li class="nav-item"><a class="nav-link" onclick="translatePage('en')">English</a></li>
          <li class="nav-item"><a class="nav-link" onclick="translatePage('es')">Español</a></li>
          <!-- Hidden Google Translate element -->
          <div id="google_translate_element" style="display:none;"></div>
        </ul>
      </div>
    </div>
  </nav>
  <main class="container mt-5">
    <h1>{title}</h1>
    <p class="text-muted">{date}</p>
    <article class="mt-4">
      {content}
    </article>
    <a href="index.html" class="btn btn-primary mt-4">← Back to Blog</a>
  </main>
  <footer id="footer" class="bg-black text-white text-center">
    <div class="">
      <a href="https://x.com/nickhamps04" class="social-icon" aria-label="Twitter"><i class="bi bi-twitter"
          style="font-size: 1.5rem;"></i></a>
      <a href="https://www.linkedin.com/in/nickhampshire1/" class="social-icon" aria-label="LinkedIn"><i
          class="bi bi-linkedin" style="font-size: 1.5rem;"></i></a>
      <a href="https://www.facebook.com/nickhampshirefitness/" class="social-icon" aria-label="Facebook"><i
          class="bi bi-facebook" style="font-size: 1.5rem;"></i></a>
      <a href="https://www.youtube.com/@nickhampshire" class="social-icon" aria-label="YouTube"><i class="bi bi-youtube"
          style="font-size: 1.5rem;"></i></a>
      <a href="https://www.instagram.com/nickhampshire_/?hl=en" class="social-icon" aria-label="Instagram"><i
          class="bi bi-instagram" style="font-size: 1.5rem;"></i></a>
      <a href="https://nickhampshire.substack.com/" class="social-icon" aria-label="Substack"><i class="bi bi-substack"
          style="font-size: 1.5rem;"></i></a>
    </div>
    <div>
      <p>&copy; 2025 Nick Hampshire Coaching. All rights reserved.</p>
    </div>
  </footer>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  <script src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
  <!-- Load your custom translation JS -->
  <script src="../translate.js"></script>
</body>
</html>
"""
# ------------------------------------------------

def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

# --- Build blog index ---
index_html = INDEX_HEADER

for i, entry in enumerate(feed.entries[:20]):  # only latest 20
    slug = slugify(entry.title)
    date = datetime(*entry.published_parsed[:6]).strftime("%b %d, %Y")

    # Try to get first image from post, else default
    content = entry.get("content", [{"value": entry.get("summary", "")}])[0]["value"]
    soup = BeautifulSoup(content, "html.parser")
    img_tag = soup.find("img")
    if img_tag and img_tag.get("src"):
        img_src = img_tag["src"]
    else:
        img_src = "../images/blog_default.jpg"

    # Subtitle (cleaned summary, or blank if none)
    raw_subtitle = entry.get("summary", "")
    subtitle = BeautifulSoup(raw_subtitle, "html.parser").get_text().strip() if raw_subtitle else ""

    if i == 0:
        # --- Featured (latest) blog post ---
        index_html += f"""
        <div class="card mb-4 text-bg-dark featured-blog-card">
          <div class="row g-0 h-100">
            <div class="col-md-6">
              <img src="{img_src}" class="img-fluid h-100 w-100 object-fit-cover rounded-start" alt="{entry.title}">
            </div>
            <div class="col-md-6 d-flex flex-column justify-content-center p-4">
              <h2 class="card-title">{entry.title}</h2>
              <p class="card-subtitle mb-2">{subtitle}</p>
              <p class="card-text"><small class="">{date}</small></p>
              <a href="{slug}.html" class="btn btn-primary mt-3">Read More</a>
            </div>
          </div>
        </div>
        """
    else:
        # --- Regular blog posts ---
        index_html += f"""
        <div class="card mb-3 text-bg-dark blog-card">
          <div class="row g-0">
            <div class="col-md-4">
              <img src="{img_src}" class="img-fluid h-100 w-100 object-fit-cover rounded-start" alt="{entry.title}">
            </div>
            <div class="col-md-8 d-flex flex-column justify-content-center p-3">
              <h5 class="card-title">{entry.title}</h5>
              <p class="card-subtitle mb-2">{subtitle}</p>
              <p class="card-text"><small class="">{date}</small></p>
              <a href="{slug}.html" class="btn btn-sm btn-secondary mt-2">Read More</a>
            </div>
          </div>
        </div>
        """

index_html += INDEX_FOOTER

with open(os.path.join(BLOG_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

# --- Build individual posts ---
for i, entry in enumerate(feed.entries, start=1):
    slug = slugify(entry.title)
    date = datetime(*entry.published_parsed[:6]).strftime("%B %d, %Y")

    # use content if available, else summary
    content = entry.get("content", [{"value": entry.get("summary", "")}])[0]["value"]

    soup = BeautifulSoup(content, "html.parser")
    [s.extract() for s in soup(["script", "iframe"])]  # remove scripts
    clean_content = str(soup)

    html = POST_TEMPLATE.format(title=entry.title, date=date, content=clean_content)
    with open(os.path.join(BLOG_DIR, f"{slug}.html"), "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Generated post {i}: {entry.title} → {slug}.html")

# --- Update homepage with latest 3 ---
latest_posts = feed.entries[:3]
cards_html = '<section id="latest-blog" class="container my-5">\n'
cards_html += '  <h2 class="text-center mb-4">Latest from the Blog</h2>\n'
cards_html += '  <div class="row g-4">\n'

for entry in latest_posts:
    slug = slugify(entry.title)
    date = datetime(*entry.published_parsed[:6]).strftime("%b %d, %Y")

    # find first image in content
    content = entry.get("content", [{"value": entry.get("summary", "")}])[0]["value"]
    soup = BeautifulSoup(content, "html.parser")
    img_tag = soup.find("img")

    # choose thumbnail: prefer post image, else use default
    if img_tag and img_tag.get("src"):
        img_src = img_tag["src"]
    else:
        img_src = "images/blog_default.jpg"  # relative to index.html

    img_html = f'<img src="{img_src}" class="card-img-top" alt="{entry.title}">'

    # Subtitle (cleaned summary, or blank if none)
    raw_subtitle = entry.get("summary", "")
    subtitle = BeautifulSoup(raw_subtitle, "html.parser").get_text().strip() if raw_subtitle else ""

    cards_html += f"""
    <div class="col-md-4">
      <div class="card h-100 text-bg-dark">
        {img_html}
        <div class="card-body">
          <h5 class="card-title">{entry.title}</h5>
          <p class="card-subtitle">{subtitle}</p>
          <p class="card-text">{date}</p>
          <a href="blog/{slug}.html" class="btn btn-primary">Read More</a>
        </div>
      </div>
    </div>
    """

cards_html += "  </div>\n</section>\n"


# Wrap with markers so future runs can replace
wrapped_cards = f"<!-- BLOG_SECTION_START -->\n{cards_html}\n<!-- BLOG_SECTION_END -->"

with open(HOMEPAGE, "r", encoding="utf-8") as f:
    homepage_html = f.read()

if "<!-- BLOG_SECTION_START -->" in homepage_html and "<!-- BLOG_SECTION_END -->" in homepage_html:
    # Replace existing section
    import re
    homepage_html = re.sub(
        r"<!-- BLOG_SECTION_START -->(.*?)<!-- BLOG_SECTION_END -->",
        wrapped_cards,
        homepage_html,
        flags=re.DOTALL
    )
    print("✅ Homepage blog section replaced with latest 3 posts")
else:
    # If markers not found, append at end
    homepage_html += "\n" + wrapped_cards
    print("✅ Homepage blog section added at end (first time)")

with open(HOMEPAGE, "w", encoding="utf-8") as f:
    f.write(homepage_html)



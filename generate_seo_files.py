import glob
import os
from datetime import datetime

base_url = "https://belubeari-exim-solutions.vercel.app"
today = datetime.now().strftime("%Y-%m-%d")

# 1. Create robots.txt
robots_content = f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""

with open("robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)

# 2. Create sitemap.xml with all 54 pages
html_files = sorted(glob.glob("*.html"))

sitemap_entries = []
for f in html_files:
    if f == "index.html":
        priority = "1.0"
        changefreq = "daily"
        loc = f"{base_url}/"
    elif f in ["products.html", "brands.html", "contact-us.html", "about-us.html", "industries.html"]:
        priority = "0.9"
        changefreq = "weekly"
        loc = f"{base_url}/{f}"
    else:
        priority = "0.8"
        changefreq = "monthly"
        loc = f"{base_url}/{f}"
        
    entry = f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""
    sitemap_entries.append(entry)

sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(sitemap_entries)}
</urlset>
"""

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"Generated robots.txt and sitemap.xml with {len(html_files)} URLs!")

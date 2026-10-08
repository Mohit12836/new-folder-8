import os
import glob
import re
import json
from bs4 import BeautifulSoup
from datetime import date

BASE_URL = "https://belubeari-exim-solutions.vercel.app"
TODAY = date.today().isoformat()

# Verified business info
ORG_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "M/s Belubeari Exim",
    "image": f"{BASE_URL}/assets/images/logo.png",
    "@id": f"{BASE_URL}/#organization",
    "url": f"{BASE_URL}/",
    "telephone": "+919967384878",
    "email": "belubeariexim@gmail.com",
    "priceRange": "$$",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "135/137, Narayan Dhuru Street, Masjid Bunder",
        "addressLocality": "Mumbai",
        "addressRegion": "Maharashtra",
        "postalCode": "400003",
        "addressCountry": "IN"
    },
    "geo": {
        "@type": "GeoCoordinates",
        "latitude": 18.9510344,
        "longitude": 72.8335803
    },
    "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "opens": "10:00",
        "closes": "19:30"
    },
    "sameAs": [
        "https://in.linkedin.com/in/belubeari-exim-1b6760166",
        "https://www.instagram.com/belubeariexim"
    ]
}

def clean_name(filename):
    name = filename.replace('.html', '').replace('-', ' ').title()
    name_map = {
        'Index': 'Home',
        'About Us': 'About Us',
        'Contact Us': 'Contact Us',
        'Products': 'Industrial Products',
        'Industries': 'Industries Served',
        'Brands': 'Authorized Brands',
        'Ball Bearing': 'Ball Bearings',
        'Timing Belts': 'Timing Belts',
        'Conveyor Belts': 'Conveyor Belts',
        'V Belts': 'V-Belts & Wedge Belts',
        'Flat Belts': 'Flat Transmission Belts',
        'Linear Motion Bearing': 'Linear Motion Bearings & LM Guides',
        'Pillow Block Bearing': 'Pillow Block & Plummer Blocks',
        'Oil Grease': 'Lubrication Oil & Greases',
        'Lubrications Oil Grease': 'Lubrication Oil & Greases',
        'Seals O Ring': 'Industrial Oil Seals & O-Rings',
        'Cots Apron': 'Textile Cots & Aprons',
        'Rubber Emery Roller Covering': 'Rubber Emery & Roller Covering',
        'Special Coated Belts': 'Special Coated Belts',
        'Skf': 'SKF Bearings',
        'Fag': 'FAG Bearings',
        'Timken': 'Timken Bearings',
        'Nachi': 'Nachi Bearings',
        'Ijk': 'IJK Bearings',
        'Nmb': 'NMB Minebea Bearings',
        'Gates': 'Gates Power Transmission Belts',
        'Mitsuboshi': 'Mitsuboshi Industrial Belts',
        'Continental': 'Continental Contitech Belts',
        'Fenner': 'JK Fenner Industrial Belts',
        'Megadyne': 'Megadyne Belts',
        'Bearings': 'Industrial Bearings Catalog',
        'Belts': 'Industrial Belts Catalog'
    }
    return name_map.get(name, name)

def get_page_meta(filename):
    name = clean_name(filename)
    
    if filename == 'index.html':
        title = "Belubeari Exim | Industrial Belts, Bearings & Conveyor Solutions Mumbai"
        desc = "Leading supplier of genuine industrial timing belts, ball bearings, conveyor belts, and power transmission solutions in Masjid Bunder, Mumbai. Fast dispatch across India."
        priority = "1.0"
        changefreq = "daily"
    elif filename == 'about-us.html':
        title = "About Us | M/s Belubeari Exim Mumbai - Industrial Power Transmission"
        desc = "Learn about M/s Belubeari Exim, Mumbai's trusted distributor of high-performance industrial belts, precision bearings, and engineering transmission spares."
        priority = "0.9"
        changefreq = "monthly"
    elif filename == 'contact-us.html':
        title = "Contact Us | M/s Belubeari Exim Trade Desk Masjid Bunder Mumbai"
        desc = "Get in touch with Belubeari Exim technical sales team in Masjid Bunder, Mumbai. Call +91 99673 84878 or send WhatsApp for instant RFQ and quotes."
        priority = "0.9"
        changefreq = "monthly"
    elif filename == 'products.html':
        title = "Industrial Products Catalog | Belts, Bearings & Conveyors | Belubeari Exim"
        desc = "Explore our complete range of precision ball bearings, timing belts, conveyor systems, V-belts, and lubrication supplies in Mumbai."
        priority = "0.9"
        changefreq = "weekly"
    elif filename == 'brands.html':
        title = "Authorized Global Brands | SKF, FAG, Timken, Gates, Fenner | Belubeari Exim"
        desc = "100% genuine industrial bearings and belts from SKF, FAG, Timken, Gates, Mitsuboshi, Continental, and JK Fenner with manufacturer test certificates."
        priority = "0.9"
        changefreq = "weekly"
    elif filename == 'industries.html':
        title = "Industries Served | Cement, Steel, Pharma, Food, Textile | Belubeari Exim"
        desc = "Customized heavy-duty power transmission and bearing solutions for 20+ industries including cement, steel, automotive, packaging, and textiles across India."
        priority = "0.9"
        changefreq = "weekly"
    elif filename == 'oil-grease.html':
        title = "Industrial Lubrication Oil & High-Performance Greases | Belubeari Exim Mumbai"
        desc = "High-performance synthetic industrial machinery oils, bearing greases, and gear lubricants in Masjid Bunder, Mumbai. Wholesale rates & technical specs."
        priority = "0.8"
        changefreq = "monthly"
    elif filename == 'lubrications-oil-grease.html':
        title = "Industrial Machinery Lubrication & Heavy-Duty Greases | Belubeari Exim"
        desc = "Heavy-duty industrial lubricants, high-temp bearing greases, and maintenance oils from top manufacturers in Mumbai. Fast dispatch by Belubeari Exim."
        priority = "0.8"
        changefreq = "monthly"
    elif 'industry' in filename:
        title = f"{name} Transmission & Bearing Solutions | Belubeari Exim Mumbai"
        desc = f"Heavy-duty conveyor belts, precision bearings, and high-temp power transmission solutions engineered specifically for the {name} by Belubeari Exim Mumbai."
        priority = "0.8"
        changefreq = "monthly"
    elif filename in ['skf.html', 'fag.html', 'timken.html', 'nachi.html', 'ijk.html', 'nmb.html', 'gates.html', 'mitsuboshi.html', 'continental.html', 'fenner.html', 'megadyne.html']:
        title = f"Genuine {name} Stockist & Distributor in Mumbai | Belubeari Exim"
        desc = f"Official supplier and dealer of genuine {name} products in Masjid Bunder, Mumbai. 100% original packaging, test certificates & fast pan-India dispatch."
        priority = "0.8"
        changefreq = "monthly"
    else:
        title = f"{name} Supplier & Stockist in Mumbai | Belubeari Exim"
        desc = f"High quality {name.lower()} available with immediate dispatch from Masjid Bunder, Mumbai. Technical consultation, CAD specs & wholesale quotes from Belubeari Exim."
        priority = "0.8"
        changefreq = "monthly"
        
    return title, desc, priority, changefreq

def process_files():
    html_files = sorted(glob.glob('*.html'))
    print(f"Processing {len(html_files)} HTML files...")
    
    sitemap_entries = []
    
    for file in html_files:
        is_demo = (file == 'test.html')
        canon_path = "" if file == 'index.html' else file
        canonical_url = f"{BASE_URL}/{canon_path}".rstrip('/')
        if file == 'index.html':
            canonical_url = f"{BASE_URL}/"
            
        title, desc, priority, changefreq = get_page_meta(file)
        
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        
        # 1. Update Title
        if not is_demo:
            if soup.title:
                soup.title.string = title
            else:
                new_title = soup.new_tag('title')
                new_title.string = title
                if soup.head:
                    soup.head.insert(0, new_title)
                    
        # 2. Update Meta Description
        meta_desc = soup.find('meta', attrs={'name': re.compile(r'^description$', re.I)})
        if not is_demo:
            if meta_desc:
                meta_desc['content'] = desc
            else:
                new_desc = soup.new_tag('meta', attrs={'name': 'description', 'content': desc})
                if soup.head:
                    soup.head.append(new_desc)
                    
        # 3. Handle Robots meta for Demo vs Production
        robots_meta = soup.find('meta', attrs={'name': re.compile(r'^robots$', re.I)})
        if is_demo:
            if robots_meta:
                robots_meta['content'] = 'noindex, nofollow'
            else:
                new_rob = soup.new_tag('meta', attrs={'name': 'robots', 'content': 'noindex, nofollow'})
                if soup.head:
                    soup.head.append(new_rob)
        else:
            if robots_meta:
                robots_meta['content'] = 'index, follow'
            else:
                new_rob = soup.new_tag('meta', attrs={'name': 'robots', 'content': 'index, follow'})
                if soup.head:
                    soup.head.append(new_rob)
                    
        # 4. Canonical Link
        if not is_demo:
            canon_link = soup.find('link', attrs={'rel': re.compile(r'^canonical$', re.I)})
            if canon_link:
                canon_link['href'] = canonical_url
            else:
                new_canon = soup.new_tag('link', attrs={'rel': 'canonical', 'href': canonical_url})
                if soup.head:
                    soup.head.append(new_canon)
                    
        # 5. Open Graph Tags
        if not is_demo:
            og_tags = [
                ('og:type', 'website'),
                ('og:site_name', 'M/s Belubeari Exim'),
                ('og:locale', 'en_IN'),
                ('og:title', title),
                ('og:description', desc),
                ('og:url', canonical_url),
                ('og:image', f"{BASE_URL}/assets/images/logo.png")
            ]
            for prop, val in og_tags:
                og_tag = soup.find('meta', attrs={'property': prop})
                if og_tag:
                    og_tag['content'] = val
                else:
                    new_og = soup.new_tag('meta', attrs={'property': prop, 'content': val})
                    if soup.head:
                        soup.head.append(new_og)
                        
            # 6. Twitter Card Tags
            tw_tags = [
                ('twitter:card', 'summary_large_image'),
                ('twitter:title', title),
                ('twitter:description', desc),
                ('twitter:image', f"{BASE_URL}/assets/images/logo.png")
            ]
            for name_attr, val in tw_tags:
                tw_tag = soup.find('meta', attrs={'name': name_attr})
                if tw_tag:
                    tw_tag['content'] = val
                else:
                    new_tw = soup.new_tag('meta', attrs={'name': name_attr, 'content': val})
                    if soup.head:
                        soup.head.append(new_tw)
                        
        # 7. Add Organization / LocalBusiness JSON-LD Schema
        if not is_demo:
            existing_schemas = soup.find_all('script', attrs={'type': 'application/ld+json'})
            has_org = False
            for s in existing_schemas:
                try:
                    data = json.loads(s.string) if s.string else {}
                    if data.get('@type') in ['LocalBusiness', 'Organization']:
                        s.string = json.dumps(ORG_SCHEMA, indent=2)
                        has_org = True
                except:
                    pass
            if not has_org:
                new_schema = soup.new_tag('script', attrs={'type': 'application/ld+json'})
                new_schema.string = json.dumps(ORG_SCHEMA, indent=2)
                if soup.head:
                    soup.head.append(new_schema)
                    
            # 8. Check visible breadcrumbs and add BreadcrumbList schema if present
            # Look for nav containing breadcrumbs
            breadcrumb_nav = soup.find('nav', attrs={'aria-label': re.compile(r'breadcrumb', re.I)})
            if not breadcrumb_nav:
                # Check for breadcrumb comment or structure
                for nav in soup.find_all('nav'):
                    if 'Home' in nav.get_text() and '/' in nav.get_text():
                        breadcrumb_nav = nav
                        breadcrumb_nav['aria-label'] = 'Breadcrumb'
                        break
                        
            if breadcrumb_nav:
                # Extract links
                b_links = breadcrumb_nav.find_all('a')
                current_span = breadcrumb_nav.find_all('span')
                items = []
                pos = 1
                for a in b_links:
                    href = a.get('href', '')
                    if href == 'index.html':
                        full_href = f"{BASE_URL}/"
                    elif href:
                        full_href = f"{BASE_URL}/{href}"
                    else:
                        full_href = canonical_url
                    name_text = a.get_text(strip=True).replace('Home', 'Home').replace('/', '').strip()
                    if name_text:
                        items.append({
                            "@type": "ListItem",
                            "position": pos,
                            "name": name_text,
                            "item": full_href
                        })
                        pos += 1
                # Add current page
                page_crumb_name = clean_name(file)
                items.append({
                    "@type": "ListItem",
                    "position": pos,
                    "name": page_crumb_name,
                    "item": canonical_url
                })
                
                breadcrumb_schema = {
                    "@context": "https://schema.org",
                    "@type": "BreadcrumbList",
                    "itemListElement": items
                }
                
                # Check if breadcrumb script already exists
                has_b_schema = False
                for s in existing_schemas:
                    try:
                        data = json.loads(s.string) if s.string else {}
                        if data.get('@type') == 'BreadcrumbList':
                            s.string = json.dumps(breadcrumb_schema, indent=2)
                            has_b_schema = True
                    except:
                        pass
                if not has_b_schema:
                    new_b_schema = soup.new_tag('script', attrs={'type': 'application/ld+json'})
                    new_b_schema.string = json.dumps(breadcrumb_schema, indent=2)
                    if soup.head:
                        soup.head.append(new_b_schema)

        # 9. Audit and fix missing image alt attributes
        imgs = soup.find_all('img')
        for img in imgs:
            alt = img.get('alt')
            src = img.get('src', '')
            if not alt or alt.strip() == '' or alt.strip().lower() == 'image':
                # Generate clean alt based on src or page context
                base_img_name = os.path.splitext(os.path.basename(src))[0].replace('-', ' ').replace('_', ' ').title()
                img['alt'] = f"{base_img_name} - Belubeari Exim Mumbai"

        # Write modified content back
        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        # Collect sitemap entries
        if not is_demo:
            sitemap_entries.append({
                'loc': canonical_url,
                'lastmod': TODAY,
                'changefreq': changefreq,
                'priority': priority
            })

    # 10. Generate sitemap.xml
    print("Generating sitemap.xml...")
    sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for entry in sitemap_entries:
        sitemap_xml.append('  <url>')
        sitemap_xml.append(f"    <loc>{entry['loc']}</loc>")
        sitemap_xml.append(f"    <lastmod>{entry['lastmod']}</lastmod>")
        sitemap_xml.append(f"    <changefreq>{entry['changefreq']}</changefreq>")
        sitemap_xml.append(f"    <priority>{entry['priority']}</priority>")
        sitemap_xml.append('  </url>')
    sitemap_xml.append('</urlset>')
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(sitemap_xml) + '\n')
    print(f"sitemap.xml written with {len(sitemap_entries)} valid production URLs (excluding demo test.html).")

    # 11. Generate robots.txt
    print("Updating robots.txt...")
    robots_txt = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /test.html",
        "",
        f"Sitemap: {BASE_URL}/sitemap.xml"
    ]
    with open('robots.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(robots_txt) + '\n')
    print("robots.txt updated.")

    # 12. Generate vercel.json for Clean URLs and Performance Headers
    print("Creating vercel.json...")
    vercel_config = {
        "cleanUrls": True,
        "trailingSlash": False,
        "headers": [
            {
                "source": "/(.*)",
                "headers": [
                    {
                        "key": "X-Content-Type-Options",
                        "value": "nosniff"
                    },
                    {
                        "key": "X-Frame-Options",
                        "value": "DENY"
                    },
                    {
                        "key": "X-XSS-Protection",
                        "value": "1; mode=block"
                    },
                    {
                        "key": "Referrer-Policy",
                        "value": "strict-origin-when-cross-origin"
                    }
                ]
            },
            {
                "source": "/assets/(.*)",
                "headers": [
                    {
                        "key": "Cache-Control",
                        "value": "public, max-age=31536000, immutable"
                    }
                ]
            }
        ]
    }
    with open('vercel.json', 'w', encoding='utf-8') as f:
        json.dump(vercel_config, f, indent=2)
    print("vercel.json configured.")

if __name__ == '__main__':
    process_files()

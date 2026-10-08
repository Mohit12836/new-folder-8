import os
import glob
import re
import json
from bs4 import BeautifulSoup

def audit():
    html_files = sorted(glob.glob('*.html'))
    print(f"Total HTML files: {len(html_files)}")
    
    results = []
    total_imgs = 0
    missing_alt_total = 0
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        soup = BeautifulSoup(content, 'html.parser')
        
        title = soup.title.string.strip() if soup.title and soup.title.string else None
        
        meta_desc = soup.find('meta', attrs={'name': re.compile(r'^description$', re.I)})
        desc_content = meta_desc['content'].strip() if meta_desc and meta_desc.get('content') else None
        
        canonical = soup.find('link', attrs={'rel': re.compile(r'^canonical$', re.I)})
        canon_url = canonical['href'].strip() if canonical and canonical.get('href') else None
        
        og_title = soup.find('meta', attrs={'property': 'og:title'})
        og_desc = soup.find('meta', attrs={'property': 'og:description'})
        og_url = soup.find('meta', attrs={'property': 'og:url'})
        og_image = soup.find('meta', attrs={'property': 'og:image'})
        
        tw_card = soup.find('meta', attrs={'name': 'twitter:card'})
        
        h1s = [h1.get_text(strip=True) for h1 in soup.find_all('h1')]
        
        schemas = soup.find_all('script', attrs={'type': 'application/ld+json'})
        
        imgs = soup.find_all('img')
        total_imgs += len(imgs)
        imgs_missing_alt = [img.get('src') for img in imgs if not img.get('alt') or img.get('alt').strip() == '']
        missing_alt_total += len(imgs_missing_alt)
        
        robots_meta = soup.find('meta', attrs={'name': re.compile(r'^robots$', re.I)})
        robots_content = robots_meta['content'].strip() if robots_meta and robots_meta.get('content') else None
        
        results.append({
            'file': file,
            'title': title,
            'desc': desc_content,
            'canonical': canon_url,
            'og_title': og_title['content'].strip() if og_title and og_title.get('content') else None,
            'og_desc': og_desc['content'].strip() if og_desc and og_desc.get('content') else None,
            'og_url': og_url['content'].strip() if og_url and og_url.get('content') else None,
            'og_image': og_image['content'].strip() if og_image and og_image.get('content') else None,
            'twitter_card': tw_card['content'].strip() if tw_card and tw_card.get('content') else None,
            'h1_count': len(h1s),
            'h1s': h1s,
            'schema_count': len(schemas),
            'missing_alts': imgs_missing_alt,
            'robots': robots_content
        })
        
    print("\n================ DETAILED AUDIT RESULTS ================")
    missing_titles = [r for r in results if not r['title']]
    duplicate_titles = {}
    for r in results:
        if r['title']:
            duplicate_titles.setdefault(r['title'], []).append(r['file'])
    dupe_titles = {k: v for k, v in duplicate_titles.items() if len(v) > 1}
    
    missing_desc = [r for r in results if not r['desc']]
    missing_canon = [r for r in results if not r['canonical']]
    missing_og = [r for r in results if not r['og_title'] or not r['og_desc'] or not r['og_url'] or not r['og_image']]
    missing_tw = [r for r in results if not r['twitter_card']]
    h1_none = [r for r in results if r['h1_count'] == 0]
    h1_multiple = [r for r in results if r['h1_count'] > 1]
    missing_schema = [r for r in results if r['schema_count'] == 0]
    files_with_missing_alts = [r for r in results if len(r['missing_alts']) > 0]
    
    print(f"Total Pages: {len(results)}")
    print(f"Pages Missing <title>: {len(missing_titles)}")
    print(f"Duplicate Titles Across Pages: {len(dupe_titles)}")
    if dupe_titles:
        for t, pages in list(dupe_titles.items())[:5]:
            print(f"  - '{t}': {pages}")
            
    print(f"Pages Missing Meta Description: {len(missing_desc)}")
    print(f"Pages Missing Canonical URL: {len(missing_canon)}")
    print(f"Pages Incomplete OpenGraph Tags: {len(missing_og)}")
    print(f"Pages Missing Twitter Card: {len(missing_tw)}")
    print(f"Pages with 0 <h1> Tags: {len(h1_none)}")
    print(f"Pages with >1 <h1> Tags: {len(h1_multiple)}")
    print(f"Pages with 0 Schema.org JSON-LD: {len(missing_schema)}")
    print(f"Pages with Missing Image Alt Tags: {len(files_with_missing_alts)} (Total missing alt tags: {missing_alt_total} / {total_imgs})")
    
    # Check robots.txt and sitemap.xml
    print("\n--- Site Files ---")
    print(f"robots.txt exists: {os.path.exists('robots.txt')}")
    print(f"sitemap.xml exists: {os.path.exists('sitemap.xml')}")
    print(f"vercel.json exists: {os.path.exists('vercel.json')}")

    # Output detailed JSON for before/after comparison
    with open('seo_audit_before.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    print("Full audit report saved to seo_audit_before.json")

if __name__ == '__main__':
    audit()

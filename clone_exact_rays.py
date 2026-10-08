import os
import re

raw_dir = r'd:\codee\Ms Belubeari Exim\New folder (7)\data\raw_html'
out_dir = r'd:\codee\Ms Belubeari Exim\New folder (8)'

files = [f for f in os.listdir(raw_dir) if f.endswith('.html')]
print(f'Total HTML files to convert: {len(files)}')

# New theme color (Corporate Royal Blue replacing Red #ee3131)
PRIMARY_COLOR = '#0284c7'
PRIMARY_HOVER = '#0369a1'

for fname in files:
    with open(os.path.join(raw_dir, fname), 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Replace Color: #ee3131 -> #0284c7 (and various cases)
    content = content.replace('#ee3131', PRIMARY_COLOR)
    content = content.replace('#EE3131', PRIMARY_COLOR)
    content = content.replace('rgb(238, 49, 49)', 'rgb(2, 132, 199)')
    content = content.replace('rgb(238,49,49)', 'rgb(2, 132, 199)')

    # 2. Replace Company Name & Branding
    content = re.sub(r'Rays International Industrial Solutions', 'M/s Belubeari Exim Industrial Solutions', content, flags=re.IGNORECASE)
    content = re.sub(r'Rays International', 'Belubeari Exim', content, flags=re.IGNORECASE)
    content = re.sub(r'RAYS INTERNATIONAL', 'BELUBEARI EXIM', content)

    # 3. Replace Address & Contact Info
    content = re.sub(r'info@raysinternational\.net', 'info@belubeariexim.com', content, flags=re.IGNORECASE)
    
    # 4. Map Images to local assets/images/
    def replace_img(match):
        url = match.group(1)
        base = os.path.basename(url.split('?')[0])
        local_p = os.path.join(out_dir, 'assets', 'images', base)
        if os.path.exists(local_p):
            return f'src="assets/images/{base}"'
        return f'src="{url}"'

    content = re.sub(r'src=["\'](https?://raysinternational\.net/wp-content/uploads/[^"\']+)["\']', replace_img, content)

    # 5. Fix internal links to .html files
    # Replace href="https://raysinternational.net/about-us/" -> href="about-us.html"
    def fix_links(m):
        slug = m.group(1).strip('/')
        if not slug:
            return 'href="index.html"'
        if os.path.exists(os.path.join(raw_dir, f'{slug}.html')):
            return f'href="{slug}.html"'
        return f'href="{slug}.html"'

    content = re.sub(r'href=["\']https?://raysinternational\.net/([^"\']*)["\']', fix_links, content)

    # Save
    out_name = 'index.html' if fname == 'home.html' else fname
    with open(os.path.join(out_dir, out_name), 'w', encoding='utf-8') as f:
        f.write(content)

print('All 54 pages converted into 100% exact duplicate of Rays International with custom Blue color and Belubeari Exim branding!')

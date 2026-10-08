import urllib.request
import re
from bs4 import BeautifulSoup

url = 'https://raysinternational.net/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

print("All main containers on Rays homepage:")
containers = soup.find_all('div', class_=re.compile(r'e-con-parent|elementor-top-section|e-con'))
for c in containers:
    h = [heading.get_text(strip=True) for heading in c.find_all(['h1', 'h2', 'h3', 'h4', 'h5'])]
    p = [para.get_text(strip=True) for para in c.find_all('p')]
    imgs = [img.get('src') for img in c.find_all('img')]
    if h or p:
        print("Classes:", c.get('class'))
        print("Headings:", h)
        print("Paragraphs:", p[:3])
        print("Images:", [i.split('/')[-1] for i in imgs if i])
        print("-" * 50)

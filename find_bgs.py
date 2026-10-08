import urllib.request
import re

url = 'https://raysinternational.net/'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')

css_files = re.findall(r'href=[\"\'](https://raysinternational\.net/[^\"\']+\.css[^\"\']*)[\"\']', html)
for c in css_files:
    try:
        req_c = urllib.request.Request(c, headers={'User-Agent': 'Mozilla/5.0'})
        css = urllib.request.urlopen(req_c).read().decode('utf-8')
        bg_imgs = re.findall(r'url\([\"\']?([^\"\'\)]+)[\"\']?\)', css)
        if bg_imgs:
            print("CSS:", c)
            for bg in set(bg_imgs):
                print("  BG:", bg)
    except Exception as e:
        print("Error:", e)

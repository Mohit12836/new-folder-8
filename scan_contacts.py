import glob
import re

files = glob.glob('*.html')
all_phones = set()
all_emails = set()
all_wame = set()
all_tel = set()

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # Find all emails
        emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', content)
        for e in emails:
            all_emails.add(e)
            
        # Find wa.me links
        wame = re.findall(r'wa\.me/([0-9]+)', content)
        for w in wame:
            all_wame.add(w)
            
        # Find tel: links
        tels = re.findall(r'tel:([^\s"\'<>]+)', content)
        for t in tels:
            all_tel.add(t)

print("Found Emails:", all_emails)
print("Found WhatsApp numbers (wa.me/):", all_wame)
print("Found Tel links (tel:):", all_tel)

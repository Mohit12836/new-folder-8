import glob
import re

files = glob.glob('*.html')
print(f"Normalizing contact info across {len(files)} HTML files...")

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Clean Emails
    content = content.replace('raysinternational16@gmail.com', 'belubeariexim@gmail.com')
    content = content.replace('raysinternational@gmail.com', 'belubeariexim@gmail.com')
    content = content.replace('info@belubeariexim.com', 'belubeariexim@gmail.com')
    
    # 2. Clean Phone Numbers
    content = content.replace('9321469698', '9967384878')
    content = content.replace('9820000000', '9967384878')
    content = re.sub(r'tel:\+?91[0-9]{10}', 'tel:+919967384878', content)
    content = re.sub(r'wa\.me/91[0-9]{10}', 'wa.me/919967384878', content)
    
    # 3. Ensure topbar and footer address & email consistency
    # Replace any remnant Rays name in footer/header if present
    content = content.replace('Rays International', 'Belubeari Exim')
    content = content.replace('RAYS INTERNATIONAL', 'BELUBEARI EXIM')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Contact normalization complete across all files!")

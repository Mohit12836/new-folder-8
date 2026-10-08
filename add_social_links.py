import glob
import re

files = glob.glob('*.html')
print(f"Adding LinkedIn, Instagram, and WhatsApp social links across {len(files)} files...")

topbar_social_html = '''        <div class="hidden sm:flex items-center gap-2.5 text-neutral-400 border-l border-neutral-700 pl-3">
          <a href="https://wa.me/919967384878?text=Hi%20Belubeari%20Exim,%20I%20need%20a%20quotation" target="_blank" class="hover:text-emerald-400 transition" title="WhatsApp"><i class="fa-brands fa-whatsapp text-sm"></i></a>
          <a href="https://in.linkedin.com/in/belubeari-exim-1b6760166" target="_blank" class="hover:text-sky-400 transition" title="LinkedIn"><i class="fa-brands fa-linkedin text-sm"></i></a>
          <a href="https://www.instagram.com/belubeariexim?utm_source=qr&stkn=czg0aGc2eGxrejA5" target="_blank" class="hover:text-pink-400 transition" title="Instagram"><i class="fa-brands fa-instagram text-sm"></i></a>
        </div>'''

footer_social_html = '''          <div class="flex items-center gap-3 mt-4">
            <a href="https://wa.me/919967384878?text=Hi%20Belubeari%20Exim,%20I%20need%20a%20quotation" target="_blank" class="w-8 h-8 rounded-full bg-emerald-600 hover:bg-emerald-500 text-white flex items-center justify-center transition shadow hover:scale-110" title="WhatsApp Trade Desk">
              <i class="fa-brands fa-whatsapp text-sm"></i>
            </a>
            <a href="https://in.linkedin.com/in/belubeari-exim-1b6760166" target="_blank" class="w-8 h-8 rounded-full bg-sky-700 hover:bg-sky-600 text-white flex items-center justify-center transition shadow hover:scale-110" title="LinkedIn Profile">
              <i class="fa-brands fa-linkedin-in text-sm"></i>
            </a>
            <a href="https://www.instagram.com/belubeariexim?utm_source=qr&stkn=czg0aGc2eGxrejA5" target="_blank" class="w-8 h-8 rounded-full bg-gradient-to-tr from-amber-600 via-rose-600 to-purple-600 hover:opacity-90 text-white flex items-center justify-center transition shadow hover:scale-110" title="Instagram Profile">
              <i class="fa-brands fa-instagram text-sm"></i>
            </a>
          </div>'''

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Add topbar social icons if not present
    if 'belubeariexim-1b6760166' not in content:
        content = content.replace(
            '<span class="hidden sm:inline text-neutral-300">Mon - Sat : 10:00 AM - 7:30 PM</span>',
            '<span class="hidden sm:inline text-neutral-300">Mon - Sat : 10:00 AM - 7:30 PM</span>\n' + topbar_social_html
        )
        
    # 2. Add footer social icons if not present
    if 'instagram.com/belubeariexim' not in content:
        # insert after col 1 paragraph
        content = re.sub(
            r'(<!-- Col 1: Belubeari Exim -->\s*<div>.*?<p[^>]*>.*?</p>)',
            r'\1\n' + footer_social_html,
            content,
            flags=re.DOTALL
        )
        
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Successfully injected LinkedIn, Instagram, and WhatsApp across all 54 files!")

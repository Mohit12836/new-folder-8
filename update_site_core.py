import glob
import re

files = glob.glob('*.html')
print(f"Processing {len(files)} files...")

preloader_html = """  <!-- 3-SECOND CINEMATIC SITE PRELOADER -->
  <div id="site-preloader">
    <div class="preloader-glow-orb"></div>
    <div class="preloader-logo-box">
      <img src="assets/images/logo.png" alt="Belubeari Exim" class="preloader-logo-img">
      <div class="text-xs uppercase font-bold tracking-[0.25em] text-sky-400 mt-4">
        BEARINGS • BELTS • INDUSTRIAL SOLUTIONS
      </div>
      <div class="text-[11px] text-slate-400 mt-1">Masjid Bunder, Mumbai • Global Supply</div>
      <div class="preloader-progress-track">
        <div class="preloader-progress-bar"></div>
      </div>
      <div class="preloader-percent-text text-[11px] font-mono text-slate-400 mt-2 font-bold">0%</div>
    </div>
  </div>"""

logo_header_replacement = """      <!-- BRAND LOGO -->
      <a href="index.html" class="flex items-center gap-3 py-1">
        <img src="assets/images/logo.png" alt="Belubeari Exim Logo" class="h-12 sm:h-14 w-auto object-contain drop-shadow-sm">
      </a>"""

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Update phone numbers
    content = content.replace('9321469698', '9967384878')
    
    # 2. Update/Add belubeariexim@gmail.com
    content = content.replace('info@belubeariexim.com', 'belubeariexim@gmail.com')
    
    # 3. Add Preloader if not already present
    if 'id="site-preloader"' not in content:
        content = re.sub(r'(<body[^>]*>)', r'\1\n' + preloader_html, content, count=1)
        
    # 4. Update Header Logo to official image
    content = re.sub(
        r'<!-- BRAND LOGO -->\s*<a href="index\.html"[^>]*>.*?</a>',
        logo_header_replacement,
        content,
        flags=re.DOTALL
    )
    
    # 5. Add belubeariexim@gmail.com in footer if sales@belubeariexim.com is there
    if 'belubeariexim@gmail.com' not in content and 'sales@belubeariexim.com' in content:
        content = content.replace(
            '<a href="mailto:sales@belubeariexim.com" class="hover:text-white">sales@belubeariexim.com</a>',
            '<a href="mailto:belubeariexim@gmail.com" class="hover:text-white font-medium">belubeariexim@gmail.com</a><br><a href="mailto:sales@belubeariexim.com" class="hover:text-white text-slate-400">sales@belubeariexim.com</a>'
        )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Successfully processed and updated {len(files)} files!")

import os
import re

out_dir = r'd:\codee\Ms Belubeari Exim\New folder (8)'

# 1. UPDATE INDEX.HTML
index_path = os.path.join(out_dir, 'index.html')
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add animations.css link if not present
    if 'animations.css' not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="assets/css/animations.css">\n</head>')

    # Add canvas in hero section
    if 'id="hero-particle-canvas"' not in content:
        content = re.sub(r'(<!-- 1\. HERO BANNER -->\s*<section[^>]*>)', r'\1\n      <canvas id="hero-particle-canvas"></canvas>', content)

    # Convert Stats numbers to animated odometers
    content = content.replace('<div class="text-3xl sm:text-5xl font-extrabold font-heading text-white tracking-tight">500</div>',
                              '<div class="text-3xl sm:text-5xl font-extrabold font-heading text-white tracking-tight" data-counter-target="500" data-counter-suffix="+">500+</div>')
    content = content.replace('<div class="text-3xl sm:text-5xl font-extrabold font-heading text-white tracking-tight">1,500</div>',
                              '<div class="text-3xl sm:text-5xl font-extrabold font-heading text-white tracking-tight" data-counter-target="1500" data-counter-suffix="+">1,500+</div>')
    content = content.replace('<div class="text-3xl sm:text-5xl font-extrabold font-heading text-white tracking-tight">96%</div>',
                              '<div class="text-3xl sm:text-5xl font-extrabold font-heading text-white tracking-tight" data-counter-target="96" data-counter-suffix="%">96%</div>')

    # Add tilt-card and spotlight-card to industry cards in index.html
    content = content.replace('class="animated-border-card group block glow-hover"',
                              'class="animated-border-card tilt-card spotlight-card reveal-init group block glow-hover"')

    # Add stagger reveals to industry grid
    # Replace the section tags with reveal-init
    content = content.replace('<!-- 2. MEET & ASK SECTION -->\n    <section class="py-14 bg-slate-50 border-b border-slate-200">',
                              '<!-- 2. MEET & ASK SECTION -->\n    <section class="reveal-init py-14 bg-slate-50 border-b border-slate-200">')
    content = content.replace('<!-- 3. OUR EXPERTISE / 20+ INDUSTRIES -->\n    <section class="py-16 bg-white border-b border-slate-200">',
                              '<!-- 3. OUR EXPERTISE / 20+ INDUSTRIES -->\n    <section class="reveal-init py-16 bg-white border-b border-slate-200">')
    content = content.replace('<!-- 4. LATEST PRODUCTS SHOWCASE (Exact Split Layout Match From Screenshot 1) -->\n    <section class="py-16 bg-[#111111] relative overflow-hidden border-b border-neutral-800">',
                              '<!-- 4. LATEST PRODUCTS SHOWCASE (Exact Split Layout Match From Screenshot 1) -->\n    <section class="reveal-init py-16 bg-[#111111] relative overflow-hidden border-b border-neutral-800">')

    # Upgrade the Brand Logos section into an Infinite Smooth Continuous Marquee
    marquee_html = """<!-- 6. OUR BRANDS (Infinite 60fps Smooth Continuous Marquee) -->
    <section class="py-16 bg-white border-b border-slate-200 space-y-10 overflow-hidden reveal-init">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-2xl sm:text-3xl font-bold uppercase tracking-wider text-[#0284c7] font-heading">
          AUTHORIZED & STOCKED GLOBAL BRANDS
        </h2>
        <div class="section-divider-bar justify-center">
          <div class="bar-left"></div>
          <div class="bar-mid"></div>
          <div class="bar-right"></div>
        </div>
        <p class="text-xs sm:text-sm text-slate-500 font-sans">100% Genuine, Original Factory Packaging With Test Certificates</p>
      </div>

      <!-- Marquee Carousel Track -->
      <div class="marquee-container py-4">
        <div class="marquee-track">
          <!-- First Set -->
          <div class="marquee-item"><img src="assets/images/FAG.jpg" alt="FAG Bearings" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/TIMKEN.jpg" alt="Timken Bearings" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/NACHI.jpg" alt="Nachi Bearings" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/IJK.jpg" alt="IJK Bearings" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/NMB.jpg" alt="NMB Minebea Bearings" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/GATES.jpg" alt="Gates Belts" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/MITSUBOSHI.jpg" alt="Mitsuboshi Belts" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/CONTINENTAL.jpg" alt="Continental Belts" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/FENNER.jpg" alt="JK Fenner Belts" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/nitta.png" alt="Nitta Belts" class="h-10 w-auto object-contain"></div>
          
          <!-- Duplicated for seamless loop -->
          <div class="marquee-item"><img src="assets/images/FAG.jpg" alt="FAG Bearings" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/TIMKEN.jpg" alt="Timken Bearings" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/NACHI.jpg" alt="Nachi Bearings" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/IJK.jpg" alt="IJK Bearings" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/NMB.jpg" alt="NMB Minebea Bearings" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/GATES.jpg" alt="Gates Belts" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/MITSUBOSHI.jpg" alt="Mitsuboshi Belts" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/CONTINENTAL.jpg" alt="Continental Belts" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/FENNER.jpg" alt="JK Fenner Belts" class="h-10 w-auto object-contain"></div>
          <div class="marquee-item"><img src="assets/images/nitta.png" alt="Nitta Belts" class="h-10 w-auto object-contain"></div>
        </div>
      </div>
    </section>"""

    # Replace old brands section with the infinite marquee
    content = re.sub(r'<!-- 6\. OUR BRANDS OF BEARINGS & BELTS.*?<!-- 7\. QUOTATION CALLOUT STRIP -->', marquee_html + '\n\n    <!-- 7. QUOTATION CALLOUT STRIP -->', content, flags=re.DOTALL)

    # Add scripts and floating radar WhatsApp before </body>
    if 'animations.js' not in content:
        replacement_footer = """
  <!-- FLOATING WHATSAPP WITH RADAR PULSE -->
  <div class="fixed bottom-6 right-6 z-50">
    <a href="https://wa.me/919321469698?text=Hello%20Belubeari%20Exim" target="_blank" class="pulse-ring-container w-14 h-14 bg-emerald-600 hover:bg-emerald-700 text-white rounded-full flex items-center justify-center text-2xl shadow-2xl transition transform hover:scale-110" title="Chat on WhatsApp">
      <i class="fa-brands fa-whatsapp"></i>
    </a>
  </div>

  <script src="assets/js/animations.js"></script>
</body>
</html>"""
        content = re.sub(r'<!-- FLOATING WHATSAPP -->.*', replacement_footer, content, flags=re.DOTALL)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html with animations!")

# 2. UPDATE OTHER MAIN PAGES (products.html, brands.html, about-us.html, contact-us.html)
other_pages = ['products.html', 'brands.html', 'about-us.html', 'contact-us.html', 'industries.html']
for page_name in other_pages:
    p_path = os.path.join(out_dir, page_name)
    if os.path.exists(p_path):
        with open(p_path, 'r', encoding='utf-8') as f:
            c = f.read()

        if 'animations.css' not in c:
            c = c.replace('</head>', '  <link rel="stylesheet" href="assets/css/animations.css">\n</head>')

        c = c.replace('class="animated-border-card', 'class="animated-border-card tilt-card spotlight-card reveal-init')

        if 'animations.js' not in c:
            if '</body>' in c:
                c = c.replace('</body>', """
  <!-- FLOATING WHATSAPP WITH RADAR PULSE -->
  <div class="fixed bottom-6 right-6 z-50">
    <a href="https://wa.me/919321469698?text=Hello%20Belubeari%20Exim" target="_blank" class="pulse-ring-container w-14 h-14 bg-emerald-600 hover:bg-emerald-700 text-white rounded-full flex items-center justify-center text-2xl shadow-2xl transition transform hover:scale-110" title="Chat on WhatsApp">
      <i class="fa-brands fa-whatsapp"></i>
    </a>
  </div>
  <script src="assets/js/animations.js"></script>
</body>""")

        with open(p_path, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"Updated {page_name} with animations!")

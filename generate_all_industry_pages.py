import json
import os
import re

img_dir = r'd:\codee\Ms Belubeari Exim\New folder (8)\assets\images'
disk_files = {f.lower(): f for f in os.listdir(img_dir)}

def get_disk_img(fname):
    if not fname:
        return 'Belt.jpg'
    fname_clean = fname.split('/')[-1].split('?')[0]
    if fname_clean.lower() in disk_files:
        return disk_files[fname_clean.lower()]
    base = os.path.splitext(fname_clean)[0].lower()
    for df in disk_files:
        if os.path.splitext(df)[0].lower() == base:
            return disk_files[df]
    return fname_clean

with open('scraped_industries.json', 'r', encoding='utf-8') as f:
    scraped_data = json.load(f)

# Industry list metadata
INDUSTRIES_LIST = [
    ('cement-industry', 'Cement Industry', 'cement-industry.html', 'Cement-Industry-1.jpg'),
    ('steel-industry', 'Steel Industry', 'steel-industry.html', 'Steel-Industry.webp'),
    ('textile-industry', 'Textile Industry', 'textile-industry.html', 'Textile-Industry.jpg'),
    ('paper-industry', 'Paper Industry', 'paper-industry.html', 'Paper-Industry.jpg'),
    ('pharmaceutical-industry', 'Pharmaceutical Industry', 'pharmaceutical-industry.html', 'Pharmaceutical-Industry.webp'),
    ('food-industry', 'Food Industry', 'food-industry.html', 'Food-Industry.jpeg'),
    ('oil-gas-industry', 'Oil & Gas Industry', 'oil-gas-industry.html', 'Oil-Gas-Industry.jpg'),
    ('mining-industry', 'Mining Industry', 'mining-industry.html', 'Mining-Industry.jpg'),
    ('wood-industry', 'Wood Industry', 'wood-industry.html', 'Wood-Industry.webp'),
    ('glass-industry', 'Glass Industry', 'glass-industry.html', 'Glass-Industry.jpg'),
    ('wire-drawing-industry', 'Wire Drawing Industry', 'wire-drawing-industry.html', 'Wire-Drawing-Industry.jpg'),
    ('metalworking', 'Metalworking Industry', 'metalworking.html', 'Metalworking.jpg'),
    ('marine-industry', 'Marine Industry', 'marine-industry.html', 'Marine-Industry.jpg'),
    ('railway-industry', 'Railway Industry', 'railway-industry.html', 'Railway-Industry.jpg'),
    ('wind-power-industry', 'Wind Power Industry', 'wind-power-industry.html', 'Wind-Power-Industry.jpeg'),
    ('hydropower-industry', 'Hydropower Industry', 'hydropower-industry.html', 'Hydropower-Industry.jpg'),
    ('rubber-and-plastics-industry', 'Rubber & Plastics Industry', 'rubber-and-plastics-industry.html', 'Rubber-And-Plastics-Industry.jpeg'),
    ('automation-industry', 'Automation Industry', 'automation-industry.html', 'Bearings-and-Belts-for-the-Automation-Industry.jpg'),
    ('overhead-cranes', 'Overhead Cranes', 'overhead-cranes.html', 'Overhead-Cranes.jpg'),
    ('chemical-industry', 'Chemical Industry', 'chemical-industry.html', 'Chemical-Industry.jpg'),
]

# Shared Header & Footer
HEADER_HTML = """<!-- Top Bar -->
<div class="bg-[#111111] text-slate-300 text-xs py-2 px-4 border-b border-slate-800 tracking-wide font-sans">
  <div class="max-w-7xl mx-auto flex flex-wrap justify-between items-center gap-3">
    <div class="flex flex-wrap items-center gap-4 sm:gap-6">
      <span class="flex items-center gap-1.5"><i class="fa-solid fa-location-dot text-[#0284c7]"></i> Flat No. 8, 261/63 Yusuf Meherali Road, Masjid Bunder, Mumbai – 400003</span>
      <a href="mailto:sales@belubeariexim.com" class="hover:text-white transition flex items-center gap-1.5"><i class="fa-solid fa-envelope text-[#0284c7]"></i> sales@belubeariexim.com</a>
    </div>
    <div class="flex items-center gap-4">
      <a href="tel:+919321469698" class="hover:text-white transition flex items-center gap-1.5 font-bold text-sky-400"><i class="fa-solid fa-phone text-[#0284c7]"></i> +91 9321469698</a>
      <span class="hidden md:inline-block text-slate-600">|</span>
      <span class="hidden md:inline-block text-slate-400"><i class="fa-solid fa-clock text-[#0284c7] mr-1"></i> Mon - Sat: 9:30 AM - 7:00 PM</span>
    </div>
  </div>
</div>

<!-- Main Sticky Header -->
<header class="bg-white/95 backdrop-blur shadow-md sticky top-0 z-50 transition-all duration-200 border-b border-slate-100">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between items-center h-20">
      <!-- Logo -->
      <a href="index.html" class="flex items-center gap-3 group">
        <div class="w-12 h-12 bg-gradient-to-br from-sky-600 to-blue-800 text-white flex items-center justify-center font-heading font-black text-2xl rounded-lg shadow-md group-hover:scale-105 transition">
          BE
        </div>
        <div>
          <span class="block font-heading font-bold text-2xl tracking-tight text-slate-900 leading-none">BELUBEARI <span class="text-[#0284c7]">EXIM</span></span>
          <span class="block text-[10px] font-bold text-slate-500 tracking-widest uppercase mt-0.5">Industrial Solutions • Mumbai</span>
        </div>
      </a>

      <!-- Desktop Nav Menu -->
      <nav class="hidden lg:flex items-center space-x-1 xl:space-x-2 font-heading text-sm font-semibold tracking-wide uppercase text-slate-700">
        <a href="index.html" class="px-3 py-2 hover:text-[#0284c7] transition">Home</a>
        <a href="about-us.html" class="px-3 py-2 hover:text-[#0284c7] transition">About Us</a>
        
        <!-- Products Dropdown -->
        <div class="relative group">
          <a href="products.html" class="px-3 py-2 hover:text-[#0284c7] transition flex items-center gap-1 group-hover:text-[#0284c7]">
            Products <i class="fa-solid fa-chevron-down text-[10px] transition group-hover:rotate-180"></i>
          </a>
          <div class="absolute left-0 top-full hidden group-hover:block w-72 bg-white shadow-2xl rounded-lg border border-slate-100 py-2 z-50">
            <a href="ball-bearing.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] transition border-b border-slate-50">Ball Bearings & Roller Units</a>
            <a href="timing-belts.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] transition border-b border-slate-50">Timing Belts & Synchronous Drives</a>
            <a href="conveyor-belts.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] transition border-b border-slate-50">Conveyor Belts (PVC/PU/Rubber)</a>
            <a href="v-belts.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] transition border-b border-slate-50">V-Belts & Wedge Belts</a>
            <a href="flat-belts.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] transition border-b border-slate-50">Flat Belts & High Speed Transmission</a>
            <a href="linear-motion-bearing.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] transition border-b border-slate-50">Linear Motion Bearings & LM Guides</a>
            <a href="pillow-block-bearing.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] transition border-b border-slate-50">Pillow Block & Plummer Blocks</a>
            <a href="oil-grease.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] transition border-b border-slate-50">Lubrication Oil & Industrial Greases</a>
            <a href="seals-o-ring.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] transition border-b border-slate-50">Oil Seals & O-Rings</a>
            <a href="cots-apron.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] transition border-b border-slate-50">Textile Cots & Aprons</a>
            <a href="rubber-emery-roller-covering.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] transition border-b border-slate-50">Rubber Emery / Roller Covering</a>
            <a href="special-coated-belts.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] transition">Special Coated Belts</a>
          </div>
        </div>

        <!-- Industries Dropdown -->
        <div class="relative group">
          <a href="industries.html" class="px-3 py-2 text-[#0284c7] hover:text-[#0284c7] transition flex items-center gap-1 group-hover:text-[#0284c7]">
            Industries <i class="fa-solid fa-chevron-down text-[10px] transition group-hover:rotate-180"></i>
          </a>
          <div class="absolute left-0 top-full hidden group-hover:grid grid-cols-2 w-[520px] bg-white shadow-2xl rounded-lg border border-slate-100 p-3 gap-1 z-50 max-h-[80vh] overflow-y-auto">
            <a href="cement-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-industry text-[10px] text-sky-500"></i> Cement Industry</a>
            <a href="steel-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-cubes-stacked text-[10px] text-sky-500"></i> Steel Industry</a>
            <a href="textile-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-scroll text-[10px] text-sky-500"></i> Textile Industry</a>
            <a href="paper-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-newspaper text-[10px] text-sky-500"></i> Paper Industry</a>
            <a href="pharmaceutical-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-capsules text-[10px] text-sky-500"></i> Pharma Industry</a>
            <a href="food-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-utensils text-[10px] text-sky-500"></i> Food & Beverage</a>
            <a href="oil-gas-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-oil-well text-[10px] text-sky-500"></i> Oil & Gas</a>
            <a href="mining-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-mountain text-[10px] text-sky-500"></i> Mining Industry</a>
            <a href="automation-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-robot text-[10px] text-sky-500"></i> Automation</a>
            <a href="chemical-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-flask text-[10px] text-sky-500"></i> Chemical Industry</a>
            <a href="wood-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-tree text-[10px] text-sky-500"></i> Wood & Timber</a>
            <a href="glass-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-wine-glass text-[10px] text-sky-500"></i> Glass Industry</a>
            <a href="metalworking.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-gears text-[10px] text-sky-500"></i> Metalworking</a>
            <a href="railway-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-train text-[10px] text-sky-500"></i> Railway Industry</a>
            <a href="marine-industry.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-ship text-[10px] text-sky-500"></i> Marine Industry</a>
            <a href="overhead-cranes.html" class="px-3 py-2 text-xs text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] rounded transition flex items-center gap-1.5"><i class="fa-solid fa-anchor text-[10px] text-sky-500"></i> Overhead Cranes</a>
          </div>
        </div>

        <a href="brands.html" class="px-3 py-2 hover:text-[#0284c7] transition">Brands</a>
        <a href="contact-us.html" class="px-3 py-2 hover:text-[#0284c7] transition">Contact</a>
      </nav>

      <!-- Action Button -->
      <div class="hidden sm:flex items-center gap-3">
        <a href="https://wa.me/919321469698?text=Hello%20Belubeari%20Exim,%20I%20need%20a%20quote%20for%20industrial%20bearings%20and%20belts." target="_blank" class="bg-emerald-600 hover:bg-emerald-700 text-white text-xs font-heading font-bold px-3 py-2.5 rounded shadow flex items-center gap-1.5 transition">
          <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp
        </a>
        <a href="contact-us.html" class="bg-[#0284c7] hover:bg-sky-700 text-white text-xs font-heading font-bold uppercase tracking-wider px-4 py-2.5 rounded shadow-md transition transform hover:-translate-y-0.5">
          Get Instant Quote
        </a>
      </div>

      <!-- Mobile Menu Button -->
      <div class="lg:hidden flex items-center">
        <button id="mobileMenuToggle" class="text-slate-800 p-2 focus:outline-none">
          <i class="fa-solid fa-bars text-2xl"></i>
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile Dropdown Navigation -->
  <div id="mobileMenu" class="hidden lg:hidden bg-white border-b border-slate-200 px-4 pt-2 pb-6 space-y-2 font-heading uppercase text-sm font-semibold">
    <a href="index.html" class="block py-2 text-slate-800 hover:text-[#0284c7]">Home</a>
    <a href="about-us.html" class="block py-2 text-slate-800 hover:text-[#0284c7]">About Us</a>
    <a href="products.html" class="block py-2 text-slate-800 hover:text-[#0284c7]">All Products</a>
    <a href="industries.html" class="block py-2 text-[#0284c7]">All Industries</a>
    <a href="brands.html" class="block py-2 text-slate-800 hover:text-[#0284c7]">Brands</a>
    <a href="contact-us.html" class="block py-2 text-slate-800 hover:text-[#0284c7]">Contact Us</a>
    <div class="pt-3 flex gap-2">
      <a href="https://wa.me/919321469698" class="flex-1 bg-emerald-600 text-white text-center py-2.5 rounded text-xs font-bold font-heading">WhatsApp</a>
      <a href="contact-us.html" class="flex-1 bg-[#0284c7] text-white text-center py-2.5 rounded text-xs font-bold font-heading">Get Quote</a>
    </div>
  </div>
</header>
"""

FOOTER_HTML = """<!-- Site Footer -->
<footer class="bg-[#111111] text-slate-300 font-sans border-t-4 border-[#0284c7] pt-14 pb-8">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 pb-12 border-b border-slate-800">
      
      <!-- Col 1: About Belubeari Exim -->
      <div>
        <div class="flex items-center gap-3 mb-4">
          <div class="w-10 h-10 bg-[#0284c7] text-white flex items-center justify-center font-heading font-black text-xl rounded">
            BE
          </div>
          <div>
            <span class="block font-heading font-bold text-xl text-white tracking-wide">BELUBEARI <span class="text-[#0284c7]">EXIM</span></span>
            <span class="block text-[9px] font-bold text-slate-400 tracking-widest uppercase">Industrial Solutions</span>
          </div>
        </div>
        <p class="text-xs text-slate-400 leading-relaxed mb-4">
          M/s Belubeari Exim is Mumbai's leading stockist, trader, and distributor of industrial bearings, power transmission belts, conveyor solutions, fasteners, seals, and specialized lubrication products.
        </p>
        <div class="flex gap-2">
          <a href="#" class="w-8 h-8 rounded bg-slate-800 hover:bg-[#0284c7] text-white flex items-center justify-center text-xs transition"><i class="fa-brands fa-facebook-f"></i></a>
          <a href="#" class="w-8 h-8 rounded bg-slate-800 hover:bg-[#0284c7] text-white flex items-center justify-center text-xs transition"><i class="fa-brands fa-linkedin-in"></i></a>
          <a href="#" class="w-8 h-8 rounded bg-slate-800 hover:bg-[#0284c7] text-white flex items-center justify-center text-xs transition"><i class="fa-brands fa-whatsapp"></i></a>
        </div>
      </div>

      <!-- Col 2: Quick Links -->
      <div>
        <h4 class="font-heading text-lg font-bold text-white uppercase tracking-wider mb-4 border-l-2 border-[#0284c7] pl-2.5">Quick Links</h4>
        <ul class="space-y-2 text-xs text-slate-400 font-sans">
          <li><a href="index.html" class="hover:text-white hover:translate-x-1 inline-block transition"><i class="fa-solid fa-angle-right text-[#0284c7] mr-1.5"></i> Home Page</a></li>
          <li><a href="about-us.html" class="hover:text-white hover:translate-x-1 inline-block transition"><i class="fa-solid fa-angle-right text-[#0284c7] mr-1.5"></i> About Belubeari Exim</a></li>
          <li><a href="products.html" class="hover:text-white hover:translate-x-1 inline-block transition"><i class="fa-solid fa-angle-right text-[#0284c7] mr-1.5"></i> Product Range</a></li>
          <li><a href="industries.html" class="hover:text-white hover:translate-x-1 inline-block transition"><i class="fa-solid fa-angle-right text-[#0284c7] mr-1.5"></i> Industries Served</a></li>
          <li><a href="brands.html" class="hover:text-white hover:translate-x-1 inline-block transition"><i class="fa-solid fa-angle-right text-[#0284c7] mr-1.5"></i> Authorized Brands</a></li>
          <li><a href="contact-us.html" class="hover:text-white hover:translate-x-1 inline-block transition"><i class="fa-solid fa-angle-right text-[#0284c7] mr-1.5"></i> Request a Quote</a></li>
        </ul>
      </div>

      <!-- Col 3: Key Products -->
      <div>
        <h4 class="font-heading text-lg font-bold text-white uppercase tracking-wider mb-4 border-l-2 border-[#0284c7] pl-2.5">Key Solutions</h4>
        <ul class="space-y-2 text-xs text-slate-400 font-sans">
          <li><a href="ball-bearing.html" class="hover:text-white transition"><i class="fa-solid fa-angle-right text-[#0284c7] mr-1.5"></i> Ball & Roller Bearings</a></li>
          <li><a href="timing-belts.html" class="hover:text-white transition"><i class="fa-solid fa-angle-right text-[#0284c7] mr-1.5"></i> Timing & Synchronous Belts</a></li>
          <li><a href="conveyor-belts.html" class="hover:text-white transition"><i class="fa-solid fa-angle-right text-[#0284c7] mr-1.5"></i> Industrial Conveyor Belts</a></li>
          <li><a href="linear-motion-bearing.html" class="hover:text-white transition"><i class="fa-solid fa-angle-right text-[#0284c7] mr-1.5"></i> Linear Motion Guides</a></li>
          <li><a href="pillow-block-bearing.html" class="hover:text-white transition"><i class="fa-solid fa-angle-right text-[#0284c7] mr-1.5"></i> Pillow Block Housings</a></li>
          <li><a href="oil-grease.html" class="hover:text-white transition"><i class="fa-solid fa-angle-right text-[#0284c7] mr-1.5"></i> Kluber / THK Lubrication</a></li>
        </ul>
      </div>

      <!-- Col 4: Trade Desk Address -->
      <div>
        <h4 class="font-heading text-lg font-bold text-white uppercase tracking-wider mb-4 border-l-2 border-[#0284c7] pl-2.5">Trade Desk</h4>
        <div class="space-y-3 text-xs text-slate-400">
          <p class="flex items-start gap-2">
            <i class="fa-solid fa-location-dot text-[#0284c7] mt-0.5"></i>
            <span>Flat No. 8, 261/63 Yusuf Meherali Road, Masjid Bunder, Mumbai – 400003, Maharashtra, India</span>
          </p>
          <p class="flex items-center gap-2">
            <i class="fa-solid fa-phone text-[#0284c7]"></i>
            <a href="tel:+919321469698" class="hover:text-white font-bold text-sky-400">+91 9321469698</a>
          </p>
          <p class="flex items-center gap-2">
            <i class="fa-solid fa-envelope text-[#0284c7]"></i>
            <a href="mailto:sales@belubeariexim.com" class="hover:text-white">sales@belubeariexim.com</a>
          </p>
          <div class="pt-2">
            <a href="contact-us.html" class="inline-block bg-[#0284c7] hover:bg-sky-600 text-white text-[11px] font-heading font-bold uppercase tracking-wider px-3.5 py-2 rounded shadow transition">
              Dispatch Inquiry
            </a>
          </div>
        </div>
      </div>

    </div>

    <!-- Copyright -->
    <div class="pt-6 text-center text-xs text-slate-500 font-sans flex flex-wrap justify-between items-center gap-2">
      <p>© 2026 M/s Belubeari Exim. All Rights Reserved. Engineered for Heavy Industry.</p>
      <div class="flex gap-4">
        <a href="about-us.html" class="hover:text-slate-400 transition">Privacy Policy</a>
        <a href="contact-us.html" class="hover:text-slate-400 transition">Terms of Supply</a>
      </div>
    </div>
  </div>
</footer>

<!-- Floating WhatsApp Action with Animated Radar Rings -->
<div class="fixed bottom-6 right-6 z-50 flex flex-col gap-3">
  <a href="https://wa.me/919321469698?text=Hello%20Belubeari%20Exim,%20I%20would%20like%20to%20inquire%20about%20industrial%20products." target="_blank" class="pulse-ring-container w-14 h-14 bg-emerald-600 hover:bg-emerald-700 text-white rounded-full flex items-center justify-center text-2xl shadow-2xl transition transform hover:scale-110" title="Chat on WhatsApp">
    <i class="fa-brands fa-whatsapp"></i>
  </a>
</div>

<script src="assets/js/animations.js"></script>
<script>
  // Mobile menu toggle
  document.getElementById('mobileMenuToggle')?.addEventListener('click', function() {
    const menu = document.getElementById('mobileMenu');
    menu.classList.toggle('hidden');
  });
</script>
"""

HEAD_CONTENT = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{PAGE_TITLE} - M/s Belubeari Exim Mumbai</title>
  <meta name="description" content="{META_DESC}">
  <meta name="keywords" content="{PAGE_TITLE}, Bearings, Timing Belts, Conveyor Belts, Industrial Solutions, Belubeari Exim, Mumbai">
  
  <!-- Animation Stylesheet -->
  <link rel="stylesheet" href="assets/css/animations.css">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#f0f9ff',
              100: '#e0f2fe',
              500: '#0ea5e9',
              600: '#0284c7',
              700: '#0369a1',
              800: '#075985',
              900: '#0c4a6e',
            },
            accent: '#0284c7',
            charcoal: '#111111',
            heading: '#0f172a'
          },
          fontFamily: {
            heading: ['Arial', 'Helvetica Neue', 'Helvetica', 'sans-serif'],
            sans: ['Arial', 'Helvetica Neue', 'Helvetica', 'sans-serif'],
          }
        }
      }
    }
  </script>

  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

  <style>
    body, button, input, select, textarea {
      font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
      font-weight: 400;
      color: #475569;
    }
    h1, h2, h3, h4, h5, h6 {
      font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
      font-weight: 700;
      color: #0f172a;
      letter-spacing: -0.01em;
    }
    p, span, li, a {
      font-family: Arial, 'Helvetica Neue', Helvetica, sans-serif;
    }

    /* Section Divider Accent Line with Shimmer */
    .section-divider-bar {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin-top: 8px;
      margin-bottom: 16px;
    }
    .section-divider-bar .bar-left {
      width: 14px;
      height: 3px;
      background-color: #0284c7;
      border-radius: 2px;
      transition: width 0.3s ease;
    }
    .section-divider-bar .bar-mid {
      width: 42px;
      height: 4px;
      background: linear-gradient(90deg, #0284c7, #38bdf8, #0284c7);
      background-size: 200% 100%;
      border-radius: 2px;
      animation: bar-gradient 3s infinite linear;
    }
    .section-divider-bar .bar-right {
      width: 14px;
      height: 3px;
      background-color: #0284c7;
      border-radius: 2px;
      transition: width 0.3s ease;
    }
    @keyframes bar-gradient {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    /* Button Light Sweep Shine Animation */
    .btn-shine {
      position: relative;
      overflow: hidden;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .btn-shine::after {
      content: '';
      position: absolute;
      top: -50%;
      left: -60%;
      width: 40%;
      height: 200%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.35), transparent);
      transform: rotate(25deg);
      animation: shine-sweep 3.5s infinite ease-in-out;
    }
    @keyframes shine-sweep {
      0% { left: -60%; }
      35% { left: 130%; }
      100% { left: 130%; }
    }

    /* Floating subtle animation */
    .float-slow {
      animation: floatSlow 4s ease-in-out infinite;
    }
    @keyframes floatSlow {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-6px); }
    }

    /* Badge Pulse Animation */
    .badge-pulse {
      animation: badgeGlow 2.5s infinite;
    }
    @keyframes badgeGlow {
      0%, 100% { box-shadow: 0 0 0 0 rgba(2, 132, 199, 0.4); }
      50% { box-shadow: 0 0 0 8px rgba(2, 132, 199, 0); }
    }

    /* Auto-fit Stage Containers */
    .hero-stage {
      width: 100%;
      height: 320px;
      background-color: #f8fafc;
      border-radius: 0.75rem;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }
    .hero-stage img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }
    .hero-stage:hover img {
      transform: scale(1.03);
    }

    .card-stage {
      width: 100%;
      height: 200px;
      background-color: #f8fafc;
      border-radius: 0.5rem;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }
    .card-stage img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.35s ease;
    }
    .card-stage:hover img {
      transform: scale(1.05);
    }

    /* Running Border Beam Animation */
    .border-beam-card {
      position: relative;
      background: #ffffff;
      border-radius: 0.75rem;
      z-index: 1;
      overflow: hidden;
    }
    .border-beam-card::before {
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: conic-gradient(transparent, rgba(2, 132, 199, 0.4), transparent 30%);
      animation: border-beam-rotate 7s linear infinite;
      z-index: -2;
    }
    .border-beam-card::after {
      content: '';
      position: absolute;
      inset: 1px;
      background: #ffffff;
      border-radius: inherit;
      z-index: -1;
    }
    @keyframes border-beam-rotate {
      100% {
        transform: rotate(360deg);
      }
    }

    /* Ambient Glow on hover */
    .glow-hover {
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .glow-hover:hover {
      box-shadow: 0 10px 25px -5px rgba(2, 132, 199, 0.2), 0 8px 10px -6px rgba(2, 132, 199, 0.15);
      transform: translateY(-4px);
    }
  </style>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased overflow-x-hidden">
"""

# Let's write generator for all 20 industry pages
for slug, industry_name, html_file, default_hero_img in INDUSTRIES_LIST:
    data = scraped_data.get(slug, {})
    
    # Process text content
    paras = data.get('paragraphs', [])
    headings = data.get('headings', [])
    raw_images = data.get('images', [])
    
    # Filter valid images
    clean_images = []
    for img_url in raw_images:
        fn = img_url.split('/')[-1]
        if not ('whatsapp' in fn.lower() or 'logo' in fn.lower() or not fn):
            clean_images.append(get_disk_img(fn))
            
    # Hero image
    hero_img = clean_images[0] if clean_images else get_disk_img(default_hero_img)
    
    # Intro paragraph
    intro_p = ""
    for p in paras:
        if 'dedicated' in p or 'specifically designed' in p or 'unique demands' in p or 'high-quality products' in p or 'understand the critical' in p or 'specialize in' in p:
            intro_p = p.replace('Rays International', 'Belubeari Exim')
            break
    if not intro_p and paras:
        intro_p = paras[0].replace('Rays International', 'Belubeari Exim')
    if not intro_p:
        intro_p = f"At Belubeari Exim Industrial Solutions, we are dedicated to providing high-performance bearings, timing belts, conveyor systems, seals, and specialized lubrication tailored to the rigorous demands of the {industry_name}."

    # Specific products for industry (4 cards)
    # Default generic product names and descriptions if scraping differs
    product_items = []
    
    # Automation has special layout
    if slug == 'automation-industry':
        product_items = [
            ("High Precision Bearings", "Automation systems require components that can withstand high-speed operations and varying loads. Our range of high-quality bearings from NSK, SKF, and FAG ensures reduced friction, minimal maintenance, and prolonged machine life.", get_disk_img("Types-of-bearings-1.jpg")),
            ("Synchronous & Timing Belts", "Our selection of belts for the Automation Industry ensures smooth and efficient power transmission, crucial for the seamless functioning of automated assembly lines and robotic workcells.", get_disk_img("belts-1.jpg")),
            ("Linear Motion Guides", "Precision LM guide rails and ball screw assemblies designed for repeatable micrometer-accurate positioning in modern CNC, Cartesian robots, and packaging machinery.", get_disk_img("linear-motion-bearing.jpeg")),
            ("Specialized High-Speed Greases", "Ultra-pure synthetic greases engineered for high cycle rates, cleanroom automation, and continuous duty without thermal breakdown.", get_disk_img("Kluber-Lubrication.jpg"))
        ]
        
        app_items = [
            ("Robotics & Cartesian Arms", "Ensuring smooth multi-axis positioning and backlash-free drive transmission for factory robotics.", get_disk_img("Material-Handling.jpg")),
            ("Automated Conveying & Sorters", "Heavy-duty modular belts and high-reliability bearing assemblies for high-speed logistics and warehouse sorting.", get_disk_img("Conveying-Systems.jpg")),
            ("Pick & Place Machinery", "High-acceleration linear guides and synchronous timing belts for ultra-precise electronics and assembly units.", get_disk_img("Mixing-and-Grinding.jpg")),
            ("Packaging & Boxing Lines", "Long-life sealed bearings and wear-resistant coatings ensuring 24/7 continuous duty without line stoppage.", get_disk_img("Packaging-Equipment.jpg"))
        ]
    else:
        # Standard 4 products
        p1_desc = "Our fasteners, nut & bolt products, and heavy-duty bearings are engineered to withstand extreme loads, shock vibrations, and harsh environments, ensuring complete structural integrity and continuous machine uptime."
        p2_desc = "We offer a variety of precision seals, gaskets, and O-rings designed to prevent contamination and fluid leaks, maintaining peak operational reliability under severe temperature and pressure differentials."
        p3_desc = "Formulated to minimize friction and thermal wear across rotating assemblies. Using high-performance Kluber, Shell, and THK lubricants extends equipment lifespan and cuts maintenance cycles."
        p4_desc = "Engineered to deliver superior friction grip, abrasion resistance, and tensile durability. These coverings and industrial belts reduce slippage, prevent downtime, and maximize throughput."
        
        # Scan scraped paragraphs for exact product descriptions
        for p in paras:
            p_clean = p.replace('Rays International', 'Belubeari Exim')
            if 'nut and bolt' in p.lower() or 'fasteners' in p.lower():
                p1_desc = p_clean
            elif 'seals' in p.lower() or 'o-rings' in p.lower() or 'o-ring' in p.lower():
                p2_desc = p_clean
            elif 'lubrication' in p.lower() or 'greases' in p.lower() or 'lubricant' in p.lower():
                p3_desc = p_clean
            elif 'rubber emery' in p.lower() or 'roller covering' in p.lower():
                p4_desc = p_clean
        
        # Match product images
        prod_img1 = clean_images[1] if len(clean_images) > 1 else 'Petrochemical-Studbolts.jpg'
        prod_img2 = clean_images[2] if len(clean_images) > 2 else 'O-Ring-Feature.jpg'
        prod_img3 = clean_images[3] if len(clean_images) > 3 else 'Kluber-Lubrication.jpg'
        prod_img4 = clean_images[4] if len(clean_images) > 4 else '6.jpg'
        
        product_items = [
            ("Fasteners & Bearing Units", p1_desc, get_disk_img(prod_img1)),
            ("Seals & O-Ring Products", p2_desc, get_disk_img(prod_img2)),
            ("Lubrication Oil & Grease", p3_desc, get_disk_img(prod_img3)),
            ("Rubber Emery & Belting Solutions", p4_desc, get_disk_img(prod_img4))
        ]
        
        # 4 Applications
        app_img1 = clean_images[5] if len(clean_images) > 5 else 'Material-Handling.jpg'
        app_img2 = clean_images[6] if len(clean_images) > 6 else 'Mixing-and-Grinding.jpg'
        app_img3 = clean_images[7] if len(clean_images) > 7 else 'Kiln-Operation.jpeg'
        app_img4 = clean_images[8] if len(clean_images) > 8 else 'Packaging-and-Shipping.jpg'
        
        # Extract application titles from image basenames or text
        def clean_app_title(img_name):
            base = os.path.splitext(img_name)[0]
            base = re.sub(r'-\d+$', '', base)
            base = base.replace('-', ' ').replace('_', ' ')
            return base.title()
            
        app1_title = clean_app_title(app_img1)
        app2_title = clean_app_title(app_img2)
        app3_title = clean_app_title(app_img3)
        app4_title = clean_app_title(app_img4)
        
        # Match application descriptions
        app_paras = [p.replace('Rays International', 'Belubeari Exim') for p in paras if any(kw in p.lower() for kw in ['contribute', 'optimal performance', 'conveyors', 'crushers', 'smooth and efficient', 'durable seals', 'crucial role', 'processing', 'machinery', 'equipment'])]
        
        app1_desc = app_paras[0] if len(app_paras) > 0 else f"Our high-load bearings and belting components are deployed across {app1_title.lower()} equipment to ensure uninterrupted operations."
        app2_desc = app_paras[1] if len(app_paras) > 1 else f"High-strength fasteners, reliable seals, and effective lubricants contribute to the optimal performance of {app2_title.lower()} systems."
        app3_desc = app_paras[2] if len(app_paras) > 2 else f"Durable heat-resistant seals and synthetic lubrication solutions ensure safe and efficient operation in {app3_title.lower()}."
        app4_desc = app_paras[3] if len(app_paras) > 3 else f"From high-grip conveyor belts to zero-friction bearings, our products play a crucial role in {app4_title.lower()}."
        
        app_items = [
            (app1_title, app1_desc, get_disk_img(app_img1)),
            (app2_title, app2_desc, get_disk_img(app_img2)),
            (app3_title, app3_desc, get_disk_img(app_img3)),
            (app4_title, app4_desc, get_disk_img(app_img4))
        ]

    # Build Sidebar links with active state
    sidebar_links_html = ""
    for ind_slug, ind_name, ind_file, _ in INDUSTRIES_LIST:
        is_active = (ind_slug == slug)
        if is_active:
            sidebar_links_html += f"""
            <li class="bg-sky-50 border-l-4 border-[#0284c7] font-bold text-[#0284c7] rounded-r py-2.5 px-3.5 flex justify-between items-center text-xs shadow-sm">
              <span><i class="fa-solid fa-angle-right mr-2 text-[#0284c7]"></i> {ind_name}</span>
              <span class="text-[10px] bg-[#0284c7] text-white px-2 py-0.5 rounded font-sans uppercase">Active</span>
            </li>
            """
        else:
            sidebar_links_html += f"""
            <li class="border-b border-slate-100 last:border-0">
              <a href="{ind_file}" class="py-2.5 px-3.5 block text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] hover:pl-5 transition duration-150 text-xs flex justify-between items-center">
                <span><i class="fa-solid fa-angle-right mr-2 text-slate-400"></i> {ind_name}</span>
                <i class="fa-solid fa-chevron-right text-[9px] text-slate-300"></i>
              </a>
            </li>
            """

    # Generate the Page HTML
    page_html = HEAD_CONTENT.replace("{PAGE_TITLE}", f"{industry_name} Solutions").replace(
        "{META_DESC}", f"Industrial bearings, power transmission belts, conveyor solutions, fasteners, and seals engineered for the {industry_name}. Stocked and distributed by M/s Belubeari Exim Mumbai."
    )
    
    page_html += HEADER_HTML

    # Hero / Breadcrumb Section
    page_html += f"""
    <!-- Page Hero Banner -->
    <section class="bg-gradient-to-r from-slate-950 via-slate-900 to-sky-950 text-white py-12 lg:py-16 relative border-b border-sky-900/40">
      <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#38bdf8_1px,transparent_1px)] [background-size:16px_16px]"></div>
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div>
            <span class="inline-flex items-center gap-1.5 text-sky-400 text-xs font-bold uppercase tracking-widest bg-sky-950/80 border border-sky-800/60 px-3 py-1 rounded-full mb-3">
              <i class="fa-solid fa-industry"></i> Industry Vertical Solutions
            </span>
            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-heading font-black tracking-tight text-white uppercase">
              {industry_name}
            </h1>
          </div>
          <!-- Breadcrumb -->
          <nav class="flex items-center text-xs font-sans text-slate-300 bg-slate-900/80 px-4 py-2 rounded-lg border border-slate-800">
            <a href="index.html" class="hover:text-sky-400 transition"><i class="fa-solid fa-house mr-1"></i> Home</a>
            <span class="mx-2 text-slate-600">/</span>
            <a href="industries.html" class="hover:text-sky-400 transition">Industries</a>
            <span class="mx-2 text-slate-600">/</span>
            <span class="text-sky-400 font-semibold">{industry_name}</span>
          </nav>
        </div>
      </div>
    </section>

    <!-- Main Content Layout (70% Left / 30% Sticky Sidebar) -->
    <section class="py-12 lg:py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12">
          
          <!-- LEFT / MAIN CONTENT (8 Cols) -->
          <div class="lg:col-span-8 space-y-12">
            
            <!-- Featured Hero Stage Image -->
            <div class="border-beam-card glow-hover shadow-xl p-2 bg-white">
              <div class="hero-stage">
                <img src="assets/images/{hero_img}" alt="{industry_name} Machinery and Bearing Solutions" loading="eager">
              </div>
            </div>

            <!-- Section 1: Industry Solutions Overview -->
            <div class="bg-white rounded-xl p-6 sm:p-8 shadow-sm border border-slate-200/80">
              <h2 class="text-2xl sm:text-3xl font-heading font-bold text-slate-900 uppercase tracking-tight">
                Industry Solutions for {industry_name}
              </h2>
              <div class="section-divider-bar">
                <div class="bar-left"></div>
                <div class="bar-mid"></div>
                <div class="bar-right"></div>
              </div>
              <p class="text-slate-600 text-sm sm:text-base leading-relaxed mt-4 font-sans">
                {intro_p}
              </p>
              
              <div class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-3 pt-6 border-t border-slate-100">
                <div class="bg-slate-50 p-3 rounded-lg text-center border border-slate-100">
                  <span class="block text-sky-600 font-heading font-bold text-xl">100%</span>
                  <span class="text-[11px] text-slate-500 font-medium">Genuine Brands</span>
                </div>
                <div class="bg-slate-50 p-3 rounded-lg text-center border border-slate-100">
                  <span class="block text-sky-600 font-heading font-bold text-xl">24/7</span>
                  <span class="text-[11px] text-slate-500 font-medium">Dispatch Desk</span>
                </div>
                <div class="bg-slate-50 p-3 rounded-lg text-center border border-slate-100">
                  <span class="block text-sky-600 font-heading font-bold text-xl">Custom</span>
                  <span class="text-[11px] text-slate-500 font-medium">Sizing Available</span>
                </div>
                <div class="bg-slate-50 p-3 rounded-lg text-center border border-slate-100">
                  <span class="block text-sky-600 font-heading font-bold text-xl">OEM</span>
                  <span class="text-[11px] text-slate-500 font-medium">Standard Fit</span>
                </div>
              </div>
            </div>

            <!-- Section 2: Our Products for this Industry (4-Card Grid) -->
            <div>
              <div class="mb-6">
                <h3 class="text-2xl sm:text-3xl font-heading font-bold text-slate-900 uppercase tracking-tight">
                  Our Products for the {industry_name}
                </h3>
                <div class="section-divider-bar">
                  <div class="bar-left"></div>
                  <div class="bar-mid"></div>
                  <div class="bar-right"></div>
                </div>
                <p class="text-slate-500 text-xs sm:text-sm">Engineered components designed for extreme duty cycles, high mechanical stress, and minimal downtime.</p>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
    """

    for p_title, p_desc, p_img in product_items:
        page_html += f"""
                <div class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden flex flex-col glow-hover group">
                  <div class="card-stage p-2 bg-slate-50 border-b border-slate-100">
                    <img src="assets/images/{p_img}" alt="{p_title}" loading="lazy">
                  </div>
                  <div class="p-5 flex-1 flex flex-col justify-between">
                    <div>
                      <h4 class="font-heading font-bold text-lg text-slate-900 group-hover:text-[#0284c7] transition uppercase mb-2">
                        {p_title}
                      </h4>
                      <p class="text-xs text-slate-600 leading-relaxed">
                        {p_desc}
                      </p>
                    </div>
                    <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between">
                      <a href="contact-us.html" class="text-xs font-heading font-bold text-[#0284c7] hover:text-sky-700 flex items-center gap-1">
                        Inquire Specifications <i class="fa-solid fa-arrow-right text-[10px]"></i>
                      </a>
                      <span class="text-[10px] font-semibold text-slate-400 uppercase bg-slate-100 px-2 py-0.5 rounded">In Stock</span>
                    </div>
                  </div>
                </div>
        """

    page_html += f"""
              </div>
            </div>

            <!-- Section 3: Applications in the Industry (4-Card Grid) -->
            <div>
              <div class="mb-6">
                <h3 class="text-2xl sm:text-3xl font-heading font-bold text-slate-900 uppercase tracking-tight">
                  Applications in the {industry_name}
                </h3>
                <div class="section-divider-bar">
                  <div class="bar-left"></div>
                  <div class="bar-mid"></div>
                  <div class="bar-right"></div>
                </div>
                <p class="text-slate-500 text-xs sm:text-sm">Where our bearings, drive belts, and sealing solutions power critical production stages.</p>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
    """

    for a_title, a_desc, a_img in app_items:
        page_html += f"""
                <div class="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden flex flex-col glow-hover group">
                  <div class="card-stage p-2 bg-slate-50 border-b border-slate-100">
                    <img src="assets/images/{a_img}" alt="{a_title}" loading="lazy">
                  </div>
                  <div class="p-5 flex-1 flex flex-col justify-between">
                    <div>
                      <h4 class="font-heading font-bold text-lg text-slate-900 group-hover:text-[#0284c7] transition uppercase mb-2">
                        {a_title}
                      </h4>
                      <p class="text-xs text-slate-600 leading-relaxed">
                        {a_desc}
                      </p>
                    </div>
                    <div class="mt-4 pt-3 border-t border-slate-100">
                      <span class="text-[11px] font-medium text-emerald-600 flex items-center gap-1.5">
                        <i class="fa-solid fa-circle-check"></i> High Load Tested
                      </span>
                    </div>
                  </div>
                </div>
        """

    page_html += f"""
              </div>
            </div>

            <!-- Section 4: Why Choose Belubeari Exim -->
            <div class="bg-gradient-to-br from-slate-900 to-sky-950 rounded-2xl p-8 text-white relative overflow-hidden shadow-xl border border-sky-800/40">
              <div class="relative z-10">
                <h3 class="text-2xl sm:text-3xl font-heading font-bold text-white uppercase tracking-tight mb-2">
                  Why Choose M/s Belubeari Exim?
                </h3>
                <div class="section-divider-bar">
                  <div class="bar-left bg-sky-400"></div>
                  <div class="bar-mid bg-sky-400"></div>
                  <div class="bar-right bg-sky-400"></div>
                </div>
                <p class="text-slate-300 text-sm leading-relaxed mb-6 font-sans">
                  Trust M/s Belubeari Exim Industrial Solutions to provide reliable, certified high-grade products that enhance the efficiency, mechanical uptime, and operational longevity of your {industry_name.lower()} facilities.
                </p>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div class="flex items-start gap-3 bg-white/5 backdrop-blur p-3.5 rounded-lg border border-white/10">
                    <i class="fa-solid fa-medal text-sky-400 text-lg mt-0.5"></i>
                    <div>
                      <h5 class="font-heading font-bold text-sm uppercase">100% Genuine Inventory</h5>
                      <p class="text-xs text-slate-300">Direct sourcing from SKF, NSK, Continental, Fenner, Megadyne, and Gates.</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-3 bg-white/5 backdrop-blur p-3.5 rounded-lg border border-white/10">
                    <i class="fa-solid fa-truck-fast text-sky-400 text-lg mt-0.5"></i>
                    <div>
                      <h5 class="font-heading font-bold text-sm uppercase">Ready Mumbai Stock</h5>
                      <p class="text-xs text-slate-300">Massive warehouse in Masjid Bunder with immediate dispatch capability.</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-3 bg-white/5 backdrop-blur p-3.5 rounded-lg border border-white/10">
                    <i class="fa-solid fa-ruler-combined text-sky-400 text-lg mt-0.5"></i>
                    <div>
                      <h5 class="font-heading font-bold text-sm uppercase">Custom Fabrication</h5>
                      <p class="text-xs text-slate-300">Cleated belts, food-grade coatings, custom O-rings, and special sizes.</p>
                    </div>
                  </div>
                  <div class="flex items-start gap-3 bg-white/5 backdrop-blur p-3.5 rounded-lg border border-white/10">
                    <i class="fa-solid fa-headset text-sky-400 text-lg mt-0.5"></i>
                    <div>
                      <h5 class="font-heading font-bold text-sm uppercase">Engineering Support</h5>
                      <p class="text-xs text-slate-300">Technical sizing and maintenance consulting from seasoned experts.</p>
                    </div>
                  </div>
                </div>

                <div class="mt-8 pt-6 border-t border-white/10 flex flex-wrap items-center justify-between gap-4">
                  <div>
                    <span class="text-xs text-slate-400 block uppercase font-heading font-bold">Need Fast Pricing for Your Plant?</span>
                    <span class="text-base font-bold text-white font-sans">Contact Our Technical Sales Team in Mumbai</span>
                  </div>
                  <div class="flex gap-3">
                    <a href="tel:+919321469698" class="btn-shine bg-[#0284c7] hover:bg-sky-500 text-white text-xs font-heading font-bold uppercase tracking-wider px-5 py-3 rounded-lg shadow-md transition transform hover:-translate-y-0.5">
                      <i class="fa-solid fa-phone mr-1.5"></i> Call +91 9321469698
                    </a>
                    <a href="https://wa.me/919321469698?text=Hello%20Belubeari%20Exim,%20I%20need%20a%20quote%20for%20{industry_name.replace(' ', '%20')}." class="btn-shine bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-heading font-bold uppercase tracking-wider px-5 py-3 rounded-lg shadow-md transition flex items-center gap-1.5 transform hover:-translate-y-0.5">
                      <i class="fa-brands fa-whatsapp"></i> WhatsApp Quote
                    </a>
                  </div>
                </div>
              </div>
            </div>

          </div>

          <!-- RIGHT / STICKY SIDEBAR (4 Cols) -->
          <div class="lg:col-span-4 space-y-8">
            
            <!-- Widget 1: Our Industry Solutions List -->
            <div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden sticky top-24">
              <div class="bg-[#111111] text-white p-4 border-b border-slate-800 flex justify-between items-center">
                <div>
                  <h4 class="font-heading font-bold text-base uppercase tracking-wider text-white">Our Industry Solutions</h4>
                  <span class="text-[10px] text-sky-400 uppercase tracking-widest font-bold block mt-0.5">20 Specialized Sectors</span>
                </div>
                <i class="fa-solid fa-layer-group text-sky-400"></i>
              </div>
              <ul class="divide-y divide-slate-100 max-h-[460px] overflow-y-auto">
                {sidebar_links_html}
              </ul>

              <!-- Widget 2: Enquiry Now Box inside sidebar -->
              <div class="p-6 bg-slate-50 border-t border-slate-200">
                <div class="flex items-center gap-2 mb-3">
                  <i class="fa-solid fa-paper-plane text-[#0284c7]"></i>
                  <h4 class="font-heading font-bold text-base text-slate-900 uppercase">Enquiry Now</h4>
                </div>
                <p class="text-xs text-slate-500 mb-4 font-sans">Request technical catalog & wholesale price list for {industry_name}.</p>
                <form onsubmit="alert('Thank you! Your inquiry has been sent to Belubeari Exim Mumbai trade desk.'); return false;" class="space-y-3 font-sans">
                  <div>
                    <input type="text" placeholder="Your Name" required class="w-full text-xs p-2.5 bg-white border border-slate-300 rounded focus:ring-1 focus:ring-sky-500 focus:outline-none">
                  </div>
                  <div>
                    <input type="tel" placeholder="Mobile Number" required class="w-full text-xs p-2.5 bg-white border border-slate-300 rounded focus:ring-1 focus:ring-sky-500 focus:outline-none">
                  </div>
                  <div>
                    <input type="email" placeholder="Business Email" required class="w-full text-xs p-2.5 bg-white border border-slate-300 rounded focus:ring-1 focus:ring-sky-500 focus:outline-none">
                  </div>
                  <div>
                    <textarea placeholder="Your Requirement / Part Numbers" rows="3" class="w-full text-xs p-2.5 bg-white border border-slate-300 rounded focus:ring-1 focus:ring-sky-500 focus:outline-none"></textarea>
                  </div>
                  <button type="submit" class="btn-shine w-full bg-[#0284c7] hover:bg-sky-700 text-white text-xs font-heading font-bold uppercase tracking-wider py-2.5 rounded shadow transition transform hover:-translate-y-0.5">
                    Send Instant Inquiry
                  </button>
                </form>
              </div>

              <!-- Widget 3: Call Us CTA Box -->
              <div class="p-6 bg-gradient-to-br from-[#111111] to-slate-900 text-white border-t border-slate-800 text-center">
                <div class="w-12 h-12 rounded-full bg-sky-600/30 text-sky-400 flex items-center justify-center mx-auto mb-3 text-xl border border-sky-500/30">
                  <i class="fa-solid fa-phone-volume"></i>
                </div>
                <h5 class="font-heading font-bold text-sm uppercase tracking-wide text-white">Direct Engineering Desk</h5>
                <p class="text-xs text-slate-400 mt-1 mb-3">Speak directly with our senior bearing & belt specialist:</p>
                <a href="tel:+919321469698" class="text-lg font-heading font-black text-sky-400 hover:text-white block transition tracking-wide">
                  +91 9321469698
                </a>
                <span class="text-[10px] text-slate-500 uppercase mt-1 block">Yusuf Meherali Rd, Masjid Bunder, Mumbai</span>
              </div>

            </div>

          </div>

        </div>
      </div>
    </section>
    """

    page_html += FOOTER_HTML
    page_html += "</body></html>"

    with open(html_file, 'w', encoding='utf-8') as f_out:
        f_out.write(page_html)

print("Successfully generated all 20 individual industry pages with exact copy, images, and sidebar!")

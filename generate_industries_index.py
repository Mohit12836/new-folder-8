import os
import re

img_dir = r'd:\codee\Ms Belubeari Exim\New folder (8)\assets\images'
disk_files = {f.lower(): f for f in os.listdir(img_dir)}

def get_disk_img(fname):
    if not fname:
        return 'Belt.jpg'
    fname_clean = fname.split('/')[-1].split('?')[0]
    return disk_files.get(fname_clean.lower(), fname_clean)

INDUSTRIES_LIST = [
    ('cement-industry', 'Cement Industry', 'cement-industry.html', 'Cement-Industry-1.jpg', 'High-load bearings, heavy duty crusher fasteners, and heat-resistant seals for cement production.'),
    ('steel-industry', 'Steel Industry', 'steel-industry.html', 'Steel-Industry.webp', 'Severe-temperature roller bearings, slab mill timing drives, and synthetic grease for continuous casting.'),
    ('textile-industry', 'Textile Industry', 'textile-industry.html', 'Textile-Industry.jpg', 'High-speed spinning bearings, synthetic aprons, cots, tangential flat belts, and roller coverings.'),
    ('paper-industry', 'Paper Industry', 'paper-industry.html', 'Paper-Industry.jpg', 'Corrosion-proof stainless bearings, felt conveyor belts, and steam joint seals for paper mills.'),
    ('pharmaceutical-industry', 'Pharmaceutical Industry', 'pharmaceutical-industry.html', 'Pharmaceutical-Industry.webp', 'Cleanroom-certified bearings, FDA food-grade conveyor belts, and sanitary O-rings.'),
    ('food-industry', 'Food Industry', 'food-industry.html', 'Food-Industry.jpeg', 'Non-toxic FDA lubricants, PU hygienic conveyor belts, and stainless steel mounted units.'),
    ('oil-gas-industry', 'Oil & Gas Industry', 'oil-gas-industry.html', 'Oil-Gas-Industry.jpg', 'High-pressure seals, drilling rig bearings, and explosion-resistant power transmission drives.'),
    ('mining-industry', 'Mining Industry', 'mining-industry.html', 'Mining-Industry.jpg', 'Extra heavy-duty spherical roller bearings, high-tensile quarry belts, and crusher parts.'),
    ('wood-industry', 'Wood Industry', 'wood-industry.html', 'Wood-Industry.webp', 'Sawmill cutterhead bearings, high-speed planers, wide sanding belts, and roller coverings.'),
    ('glass-industry', 'Glass Industry', 'glass-industry.html', 'Glass-Industry.jpg', 'Ultra-high temperature conveyor belting, precision beveling bearings, and heat-resistant seals.'),
    ('wire-drawing-industry', 'Wire Drawing Industry', 'wire-drawing-industry.html', 'Wire-Drawing-Industry.jpg', 'Capstan drawing roller bearings, ceramic guide pulleys, and tensioning timing belts.'),
    ('metalworking', 'Metalworking Industry', 'metalworking.html', 'Metalworking.jpg', 'CNC linear guide rails, spindle high-precision bearings, and cutting fluid resistant seals.'),
    ('marine-industry', 'Marine Industry', 'marine-industry.html', 'Marine-Industry.jpg', 'Saltwater-resistant bronze bearings, propulsion seals, deck crane winches, and marine lubricants.'),
    ('railway-industry', 'Railway Industry', 'railway-industry.html', 'Railway-Industry.jpg', 'Traction motor axle bearings, bogie suspension seals, and high-load transmission drives.'),
    ('wind-power-industry', 'Wind Power Industry', 'wind-power-industry.html', 'Wind-Power-Industry.jpeg', 'Main shaft multi-megawatt bearings, yaw and pitch gear drives, and synthetic turbine greases.'),
    ('hydropower-industry', 'Hydropower Industry', 'hydropower-industry.html', 'Hydropower-Industry.jpg', 'Hydro turbine thrust bearings, high-pressure penstock seals, and eco-friendly lubricants.'),
    ('rubber-and-plastics-industry', 'Rubber & Plastics Industry', 'rubber-and-plastics-industry.html', 'Rubber-And-Plastics-Industry.jpeg', 'Extruder thrust bearings, injection moulding seals, and heat-resistant haul-off belts.'),
    ('automation-industry', 'Automation Industry', 'automation-industry.html', 'Bearings-and-Belts-for-the-Automation-Industry.jpg', 'Robotics LM guides, miniature ball bearings, and zero-backlash timing belts for smart factories.'),
    ('overhead-cranes', 'Overhead Cranes', 'overhead-cranes.html', 'Overhead-Cranes.jpg', 'Hoist wire rope sheaves, bridge crane wheel bearings, and heavy-duty braking belts.'),
    ('chemical-industry', 'Chemical Industry', 'chemical-industry.html', 'Chemical-Industry.jpg', 'Acid-resistant PTFE seals, corrosion-resistant ceramic bearings, and chemical plant belting.'),
]

from generate_all_industry_pages import HEAD_CONTENT, HEADER_HTML, FOOTER_HTML

page_html = HEAD_CONTENT.replace('{PAGE_TITLE}', 'Industries Served').replace(
    '{META_DESC}', 'Explore the 20 specialized industrial sectors powered by Belubeari Exim Mumbai with certified bearings, power transmission belts, conveyor solutions, fasteners, and seals.'
)
page_html += HEADER_HTML

page_html += """
<!-- Page Hero Banner -->
<section class="bg-gradient-to-r from-slate-950 via-slate-900 to-sky-950 text-white py-14 lg:py-20 relative border-b border-sky-900/40">
  <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#38bdf8_1px,transparent_1px)] [background-size:16px_16px]"></div>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 text-center">
    <span class="inline-flex items-center gap-1.5 text-sky-400 text-xs font-bold uppercase tracking-widest bg-sky-950/80 border border-sky-800/60 px-4 py-1.5 rounded-full mb-4">
      <i class="fa-solid fa-industry"></i> Comprehensive Sector Capabilities
    </span>
    <h1 class="text-3xl sm:text-5xl lg:text-6xl font-heading font-black tracking-tight text-white uppercase mb-4">
      Industries We Serve
    </h1>
    <p class="text-slate-300 text-sm sm:text-base max-w-2xl mx-auto font-sans">
      Supplying high-reliability bearings, drive belts, conveyor solutions, fasteners, and lubricants engineered to withstand extreme mechanical loads across 20 core heavy industries.
    </p>
    <!-- Breadcrumb -->
    <nav class="flex justify-center items-center text-xs font-sans text-slate-300 mt-6">
      <a href="index.html" class="hover:text-sky-400 transition"><i class="fa-solid fa-house mr-1"></i> Home</a>
      <span class="mx-2 text-slate-600">/</span>
      <span class="text-sky-400 font-semibold">Industries</span>
    </nav>
  </div>
</section>

<!-- Industries 20-Card Grid Section -->
<section class="py-14 lg:py-20 bg-slate-50">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    
    <div class="text-center max-w-3xl mx-auto mb-12">
      <h2 class="text-2xl sm:text-4xl font-heading font-bold text-slate-900 uppercase tracking-tight">
        Explore Industry Solutions
      </h2>
      <div class="section-divider-bar justify-center">
        <div class="bar-left"></div>
        <div class="bar-mid"></div>
        <div class="bar-right"></div>
      </div>
      <p class="text-slate-600 text-sm font-sans">
        Select your vertical to view customized component specifications, machinery applications, and immediate wholesale supply options.
      </p>
    </div>

    <!-- 20 Cards Grid -->
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
"""

for slug, name, link_file, img_name, desc in INDUSTRIES_LIST:
    real_img = get_disk_img(img_name)
    page_html += f"""
      <div class="bg-white rounded-xl border border-slate-200/80 shadow-sm overflow-hidden flex flex-col glow-hover group">
        <div class="card-stage p-2 bg-slate-100 border-b border-slate-100">
          <img src="assets/images/{real_img}" alt="{name}" loading="lazy">
        </div>
        <div class="p-5 flex-1 flex flex-col justify-between">
          <div>
            <h3 class="font-heading font-bold text-lg text-slate-900 group-hover:text-[#0284c7] transition uppercase mb-2">
              {name}
            </h3>
            <p class="text-xs text-slate-600 leading-relaxed font-sans line-clamp-3">
              {desc}
            </p>
          </div>
          <div class="mt-4 pt-3 border-t border-slate-100 flex items-center justify-between">
            <a href="{link_file}" class="text-xs font-heading font-bold text-[#0284c7] hover:text-sky-700 flex items-center gap-1.5 uppercase tracking-wide">
              View Solutions <i class="fa-solid fa-arrow-right text-[10px]"></i>
            </a>
            <span class="w-7 h-7 rounded-full bg-sky-50 text-sky-600 flex items-center justify-center text-xs group-hover:bg-[#0284c7] group-hover:text-white transition">
              <i class="fa-solid fa-chevron-right text-[10px]"></i>
            </span>
          </div>
        </div>
      </div>
    """

page_html += """
    </div>

    <!-- Bottom Engineering Consultation Banner -->
    <div class="mt-16 bg-gradient-to-r from-slate-900 via-sky-950 to-slate-900 rounded-2xl p-8 lg:p-12 text-white shadow-xl border border-sky-800/40">
      <div class="flex flex-col lg:flex-row items-center justify-between gap-8">
        <div class="max-w-2xl text-center lg:text-left">
          <span class="text-sky-400 text-xs font-bold uppercase tracking-widest font-heading mb-2 block">Custom Industrial Engineering Desk</span>
          <h3 class="text-2xl sm:text-3xl font-heading font-bold text-white uppercase tracking-tight mb-2">
            Have a specialized plant or custom machinery requirement?
          </h3>
          <p class="text-xs sm:text-sm text-slate-300 font-sans">
            Our engineering desk in Yusuf Meherali Road, Masjid Bunder, Mumbai stocks over 15,000+ ready SKUs of industrial bearings, timing belts, conveyor belts, and custom fabricated assemblies.
          </p>
        </div>
        <div class="flex flex-wrap items-center gap-4">
          <a href="tel:+919321469698" class="bg-[#0284c7] hover:bg-sky-500 text-white font-heading font-bold text-xs uppercase tracking-wider px-6 py-3.5 rounded-lg shadow-lg transition">
            <i class="fa-solid fa-phone mr-1.5"></i> Call +91 9321469698
          </a>
          <a href="contact-us.html" class="bg-white hover:bg-slate-100 text-slate-900 font-heading font-bold text-xs uppercase tracking-wider px-6 py-3.5 rounded-lg shadow-lg transition">
            Request Engineering Quote
          </a>
        </div>
      </div>
    </div>

  </div>
</section>
"""

page_html += FOOTER_HTML
page_html += "</body></html>"

with open('industries.html', 'w', encoding='utf-8') as f:
    f.write(page_html)

print("Successfully generated master industries.html overview hub!")

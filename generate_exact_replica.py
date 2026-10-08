import os
import json

out_dir = r'd:\codee\Ms Belubeari Exim\New folder (8)'

# 12 Core Products
product_definitions = [
    {
        'title': 'Ball Bearing',
        'slug': 'ball-bearing',
        'desc': 'Precision deep groove ball bearings, angular contact bearings, and thrust ball bearings for high-speed industrial machinery.',
        'image': 'Ball-Bearing.jpg',
        'specs': [
            ('Type', 'Deep Groove / Angular Contact / Self-Aligning'),
            ('Material', 'High Carbon Chromium Steel (GCr15) / Stainless Steel'),
            ('Precision Grade', 'P0, P6, P5 (ABEC-1, ABEC-3, ABEC-5)'),
            ('Brands', 'SKF, FAG, NACHI, TIMKEN, IJK, NMB'),
            ('Applications', 'Electric Motors, Pumps, Gearboxes, Machine Tools')
        ]
    },
    {
        'title': 'Timing Belts',
        'slug': 'timing-belts',
        'desc': 'Industrial synchronous timing belts in rubber and polyurethane with metric and imperial pitches for non-slip power transmission.',
        'image': 'Belt.jpg',
        'specs': [
            ('Profiles', 'HTD (3M, 5M, 8M, 14M), STD (S8M, S14M), T5, T10, AT5, AT10'),
            ('Cord Material', 'Fiberglass / High Tensile Steel Cord / Aramid Kevlar'),
            ('Brands', 'Continental ContiTech, Mitsuboshi, Gates, Fenner, Megadyne'),
            ('Features', 'Zero-slip, High torque transmission, High temperature resistance'),
            ('Applications', 'Automation, CNC Machines, Textile, Printing & Packaging')
        ]
    },
    {
        'title': 'Conveyor Belts',
        'slug': 'conveyor-belts',
        'desc': 'Heavy-duty rubber and PVC/PU conveyor belting for bulk material handling, food processing, and packaging lines.',
        'image': 'Belt2.jpg',
        'specs': [
            ('Carcass Material', 'EP (Polyester-Nylon) / NN (Nylon-Nylon) / Cotton Canvas'),
            ('Belt Type', 'Flat, Chevron, Sidewall Cleated, Food Grade White PU'),
            ('Cover Grades', 'General Purpose, Oil Resistant, Heat Resistant, Fire Resistant'),
            ('Applications', 'Cement, Mining, Aggregate, Food Processing, Logistics Warehouses')
        ]
    },
    {
        'title': 'V-Belts',
        'slug': 'v-belts',
        'desc': 'Classical, raw edge cogged, and space-saver wedge V-belts for industrial fans, compressors, pumps, and crushers.',
        'image': 'v-belt-red-round.jpg',
        'specs': [
            ('Sections', 'Classical (A, B, C, D), Wedge (SPA, SPB, SPC), Narrow (3V, 5V, 8V)'),
            ('Construction', 'Wrapped Rubber / Raw Edge Cogged (AX, BX, CX, XPZ, XPA)'),
            ('Brands', 'Fenner, Continental, Mitsuboshi, Gates, Bando'),
            ('Applications', 'Heavy Drives, Blowers, Air Compressors, Agricultural Machinery')
        ]
    },
    {
        'title': 'Flat Belts',
        'slug': 'flat-belts',
        'desc': 'High-efficiency flat power transmission and tangential drive belts with high friction rubber or leather surfaces.',
        'image': 'flat-belt-blue-backed.jpg',
        'specs': [
            ('Tension Layer', 'Polyester Fabric / Polyamide Foil Core / Aramid'),
            ('Surface', 'NBR Synthetic Rubber / Chrome Leather / Polyurethane'),
            ('Characteristics', 'Extreme flexibility, High speed capability up to 60 m/s'),
            ('Applications', 'Textile Spinning, Carding, Printing, Folder-Gluers')
        ]
    },
    {
        'title': 'Linear Motion Bearing',
        'slug': 'linear-motion-bearing',
        'desc': 'Precision linear guide rails, ball bushing bearings, and recirculating carriage blocks for automated movement.',
        'image': '3a2d4baf2d014f96bda2bf5f141e7cdc.jpg',
        'specs': [
            ('Types', 'Linear Guide Rails & Blocks, Round Shaft Ball Bushings, Support Units'),
            ('Accuracy Class', 'Normal (N), High (H), Precision (P)'),
            ('Preload', 'Light Preload (Z0), Medium Preload (ZA)'),
            ('Applications', 'CNC Routers, Pick & Place Automation, 3D Printers, Medical Devices')
        ]
    },
    {
        'title': 'Pillow Block Bearing',
        'slug': 'pillow-block-bearing',
        'desc': 'Mounted cast iron and stainless steel pillow block bearing units with self-aligning insert bearings.',
        'image': 'SAF-Split-pillow-block-bearing-assembly-optimized-1200px-cropped-.jpg',
        'specs': [
            ('Housing Styles', 'Pillow Block (UCP), 4-Bolt Flange (UCF), 2-Bolt Flange (UCFL), Take-up (UCT)'),
            ('Housing Material', 'Cast Iron (HT200) / Ductile Iron / Stainless Steel / Thermoplastic'),
            ('Shaft Locking', 'Set Screw Lock / Eccentric Locking Collar / Adapter Sleeve'),
            ('Applications', 'Conveyors, Agricultural Machinery, Fans, Material Handling')
        ]
    },
    {
        'title': 'Oil & Grease',
        'slug': 'oil-grease',
        'desc': 'High-performance synthetic greases, EP extreme pressure greases, and high-temperature lubricants for bearings and gears.',
        'image': 'Industrial-grease.jpg',
        'specs': [
            ('Thickener Type', 'Lithium Complex, Polyurea, Calcium Sulfonate, Clay / Bentonite'),
            ('NLGI Grades', 'NLGI 0, 1, 2, 3'),
            ('Operating Temp', '-40°C to +260°C (High Temperature Grade)'),
            ('Applications', 'Continuous Kilns, High-Speed Spindles, Heavy Crusher Bearings')
        ]
    },
    {
        'title': 'Seals & O Ring',
        'slug': 'seals-o-ring',
        'desc': 'Rotary shaft oil seals, hydraulic rod/piston seals, and precision elastomeric O-rings in NBR, Viton (FKM), and Silicone.',
        'image': 'Seals-O-Ring.jpg',
        'specs': [
            ('Materials', 'NBR (Nitrile), FKM (Viton), Silicone (VMQ), EPDM, PTFE'),
            ('Types', 'TC Double Lip Oil Seals, SC Single Lip, Hydraulic V-Packing, O-Rings'),
            ('Resistance', 'Oil, High Pressure, High Heat, Chemical & Solvent Resistance'),
            ('Applications', 'Pumps, Hydraulic Cylinders, Gearboxes, Motors, Pneumatics')
        ]
    },
    {
        'title': 'Cots & Apron',
        'slug': 'cots-apron',
        'desc': 'Precision rubber cots and synthetic aprons engineered for ring spinning, roving, and draw frames in textile mills.',
        'image': 'IMG-20260903-WA0023.jpg',
        'specs': [
            ('Hardness Shore A', '65°, 70°, 75°, 83° Shore A'),
            ('Properties', 'Superior wear resistance, Excellent anti-static behavior, Consistent yarn CV%'),
            ('Applications', 'Short Staple & Long Staple Spinning, Roving Frames, Combers')
        ]
    },
    {
        'title': 'Rubber Emery/Roller Covering',
        'slug': 'rubber-emery-roller-covering',
        'desc': 'Emery rubber fillets and high-grip roller covering tapes for textile looms, fabric processing, and film winding.',
        'image': '6.jpg',
        'specs': [
            ('Pattern', 'Smooth, Dimple / Pimpled, Fine Grooved, Synthetic Rubber Covered'),
            ('Backing', 'Cotton Cloth / Synthetic Fabric with Adhesive Backing'),
            ('Applications', 'Weaving Looms, Take-up Rollers, Film Slitting Machines')
        ]
    },
    {
        'title': 'Special Coated Belts',
        'slug': 'special-coated-belts',
        'desc': 'Timing and flat belts with specialized coatings such as Linatex, seamless PU, sponge rubber, and silicone for haul-off applications.',
        'image': 'special-coated-studded.jpg',
        'specs': [
            ('Coverings', 'Linatex Red Rubber, White PU, Correx, Silicone, Porol, APL'),
            ('Customization', 'Milled Vacuum Holes, CNC Grooves, Welded Cleats & Profiles'),
            ('Applications', 'Cable Pulling (Haul-off), Vertical Form Fill Seal (VFFS) Packaging, Glass Processing')
        ]
    }
]

# 20 Industries
industries_list = [
    ('Automation Industry', 'automation-industry', 'Bearings-and-Belts-for-the-Automation-Industry.jpg', 'High-speed linear guides, timing belts, and precision spindle bearings for robotic arms and assembly lines.'),
    ('Cement Industry', 'cement-industry', 'Cement-Industry.jpg', 'Heavy-duty spherical roller bearings, high-torque wedge belts, and heat-resistant conveyor spares for crushers and kilns.'),
    ('Chemical Industry', 'chemical-industry', 'Chemical-Industry.jpg', 'Corrosion-resistant stainless steel bearings, Viton seals, and chemical-grade conveyor belting for processing plants.'),
    ('Food Industry', 'food-industry', 'Food-Industry.jpeg', 'Food-grade white PU/PVC conveyor belts, stainless steel mounted units, and NSF H1 certified non-toxic greases.'),
    ('Glass Industry', 'glass-industry', 'Glass-Industry.jpg', 'Special heat-resistant coated timing belts, non-marking vacuum belts, and high-temp furnace bearings.'),
    ('Hydropower Industry', 'hydropower-industry', 'Hydropower-Industry.jpg', 'Large bore thrust bearings, hydrodynamic guide bearings, and heavy duty seals for turbine shafts.'),
    ('Marine Industry', 'marine-industry', 'Marine-Industry.jpg', 'Corrosion resistant marine propeller shaft bearings, water-resistant grease, and deck crane components.'),
    ('Metalworking', 'metalworking', 'Metalworking.jpg', 'High-precision angular contact machine tool spindle bearings, coolant resistant timing belts, and linear rails.'),
    ('Mining Industry', 'mining-industry', 'Mining-Industry.jpg', 'Extra heavy duty conveyor belting, heavy spherical roller bearings, and shock-resistant pillow block housings.'),
    ('Oil & Gas Industry', 'oil-gas-industry', 'Oil-Gas-Industry.jpg', 'API certified pump bearings, extreme pressure synthetic greases, and high-temperature Viton mechanical seals.'),
    ('Overhead Cranes', 'overhead-cranes', 'Overhead-Cranes.jpg', 'Wire rope sheave bearings, heavy travel drive wheels, gear couplings, and crane braking system components.'),
    ('Paper Industry', 'paper-industry', 'Paper-Industry.jpg', 'High speed dryer section bearings, felt conveyor belts, and moisture resistant rotary shaft seals.'),
    ('Pharmaceutical Industry', 'pharmaceutical-industry', 'Pharmaceutical-Industry.webp', 'Cleanroom grade miniature bearings, anti-static flat belts, and FDA compliant polyurethane timing belts.'),
    ('Railway Industry', 'railway-industry', 'Railway-Industry.jpg', 'Axlebox cylindrical roller bearings, traction motor bearings, and heavy vibration resistant transmission belts.'),
    ('Rubber and Plastics', 'rubber-and-plastics-industry', 'Rubber-And-Plastics-Industry.jpeg', 'Extruder thrust bearings, haul-off caterpuller coated timing belts, and hydraulic press seals.'),
    ('Steel Industry', 'steel-industry', 'Steel-Industry.webp', 'Continuous casting roll bearings, heavy duty rolling mill four-row tapered roller bearings, and fire-resistant greases.'),
    ('Textile Industry', 'textile-industry', 'Textile-Industry.jpg', 'Spinning cots and aprons, high speed spindle bearings, tangential flat belts, and loom rubber emery.'),
    ('Wind Power Industry', 'wind-power-industry', 'Wind-Power-Industry.jpeg', 'Main shaft spherical roller bearings, yaw and pitch slew ring bearings, and high dielectric greases.'),
    ('Wire Drawing Industry', 'wire-drawing-industry', 'Wire-Drawing-Industry.jpg', 'High load capstan wheel bearings, pulling belts, and high-speed ceramic pulley guidance bearings.'),
    ('Wood Industry', 'wood-industry', 'Wood-Industry.webp', 'High RPM spindle router bearings, multi-groove poly V-belts, and wide sanding machine rubber belts.')
]

def get_header(active_page='home', title='M/s Belubeari Exim Industrial Solutions'):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | Belubeari Exim Mumbai</title>
  <meta name="description" content="Belubeari Exim Industrial Solutions - Premier stockist for Bearings, Power Transmission Belts, Conveyor Belts & Spares at Masjid Bunder, Mumbai." />
  
  <!-- Google Fonts: Oswald & Open Sans (Exact Rays International Match) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Open+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            primary: {{
              DEFAULT: '#0284c7', // Royal Corporate Blue replacing Red #ee3131
              dark: '#0369a1',
              light: '#38bdf8'
            }},
            charcoal: '#2d3239',
            corp: {{
              900: '#0f172a',
              950: '#090d16'
            }}
          }},
          fontFamily: {{
            heading: ['Oswald', 'sans-serif'],
            sans: ['"Open Sans"', 'sans-serif']
          }}
        }}
      }}
    }}
  </script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <style>
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}
    html, body {{
      max-width: 100%;
      overflow-x: clip;
      scroll-behavior: smooth;
      text-rendering: optimizeLegibility;
      -webkit-font-smoothing: antialiased;
      font-family: 'Open Sans', sans-serif;
      color: #767676;
      background-color: #ffffff;
    }}
    h1, h2, h3, h4, h5, h6, .heading-font {{
      font-family: 'Oswald', sans-serif;
      color: #2d3239;
      letter-spacing: 0.02em;
    }}
    img, video, svg, canvas, iframe {{
      max-width: 100%;
      height: auto;
      display: block;
    }}
    
    /* 🌟 ANIMATED MOVING BORDER BEAM & GLOW 🌟 */
    @property --border-angle {{
      syntax: "<angle>";
      inherits: false;
      initial-value: 0deg;
    }}
    @keyframes border-beam-rotate {{
      0% {{ --border-angle: 0deg; }}
      100% {{ --border-angle: 360deg; }}
    }}
    @keyframes ambient-pulse {{
      0%, 100% {{ box-shadow: 0 4px 20px -2px rgba(2, 132, 199, 0.15); }}
      50% {{ box-shadow: 0 12px 30px -2px rgba(2, 132, 199, 0.35); }}
    }}

    .animated-border-card {{
      position: relative;
      background: #ffffff;
      border-radius: 6px;
      overflow: hidden;
      transition: all 0.35s ease;
      box-shadow: 0 2px 10px rgba(0,0,0,0.06);
      border: 1px solid #e2e8f0;
    }}
    .animated-border-card::before {{
      content: '';
      position: absolute;
      inset: 0;
      border-radius: inherit;
      padding: 2px;
      background: conic-gradient(from var(--border-angle), transparent 25%, #0284c7 45%, #38bdf8 50%, #0284c7 55%, transparent 75%);
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      animation: border-beam-rotate 4s linear infinite;
      pointer-events: none;
      opacity: 0.7;
    }}
    .animated-border-card:hover {{
      transform: translateY(-5px);
      animation: ambient-pulse 2.5s ease-in-out infinite;
    }}
    .animated-border-card:hover::before {{
      opacity: 1;
      animation-duration: 2s;
    }}

    /* STAGE AUTO-FIT */
    .product-stage {{
      width: 100%;
      height: 220px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #ffffff;
      border-bottom: 1px solid #f1f5f9;
      padding: 1.25rem;
      position: relative;
      overflow: hidden;
    }}
    .product-stage img {{
      max-width: 100%;
      max-height: 100%;
      width: auto;
      height: auto;
      object-fit: contain;
      object-position: center;
      transition: transform 0.4s ease;
    }}
    .animated-border-card:hover .product-stage img {{
      transform: scale(1.08);
    }}

    .industry-stage {{
      width: 100%;
      height: 160px;
      position: relative;
      overflow: hidden;
      background-color: #0f172a;
    }}
    .industry-stage img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
      transition: transform 0.5s ease;
    }}
    .animated-border-card:hover .industry-stage img {{
      transform: scale(1.08);
    }}

    .nav-dropdown:hover .dropdown-menu {{
      display: block;
    }}
  </style>
</head>
<body class="bg-white flex flex-col min-h-screen">

  <!-- TOP BAR (Rays Match) -->
  <div class="bg-[#111111] text-white text-xs py-2 px-4 border-b border-neutral-800">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
      <div class="flex items-center gap-4 text-neutral-300">
        <span class="flex items-center gap-1.5"><i class="fa-solid fa-location-dot text-primary"></i> Flat No. 8, Yusuf Meherali Road, Masjid Bunder, Mumbai – 400003</span>
        <span class="hidden md:inline text-neutral-600">|</span>
        <span class="hidden md:flex items-center gap-1.5"><i class="fa-solid fa-envelope text-primary"></i> info@belubeariexim.com</span>
      </div>
      <div class="flex items-center gap-4">
        <span class="hidden sm:inline text-neutral-300">Mon - Sat : 10:00 AM - 7:30 PM</span>
        <a href="https://wa.me/919820000000?text=Hi%20Belubeari%20Exim,%20I%20need%20a%20quotation" target="_blank" class="bg-primary hover:bg-primary-dark text-white px-3 py-1 rounded font-bold uppercase transition flex items-center gap-1.5">
          <i class="fa-brands fa-whatsapp"></i> Quick RFQ
        </a>
      </div>
    </div>
  </div>

  <!-- MAIN NAVIGATION (Astra/Elementor Structure Match) -->
  <header class="sticky top-0 z-50 bg-white shadow-sm border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 flex items-center justify-between h-20">
      
      <!-- BRAND LOGO -->
      <a href="index.html" class="flex items-center gap-3">
        <div class="w-11 h-11 bg-primary text-white flex items-center justify-center rounded text-2xl font-black shadow">
          <i class="fa-solid fa-gear"></i>
        </div>
        <div>
          <div class="text-2xl font-bold heading-font uppercase text-[#2d3239] leading-none">
            BELUBEARI <span class="text-primary">EXIM</span>
          </div>
          <div class="text-[10px] tracking-widest text-slate-500 uppercase font-semibold mt-1">
            Industrial Solutions Mumbai
          </div>
        </div>
      </a>

      <!-- MAIN MENU -->
      <nav class="hidden lg:flex items-center gap-7 text-sm font-semibold uppercase text-[#2d3239]">
        <a href="index.html" class="{'text-primary' if active_page=='home' else 'hover:text-primary'} py-2 transition">Home</a>
        <a href="about-us.html" class="{'text-primary' if active_page=='about' else 'hover:text-primary'} py-2 transition">About Us</a>
        
        <!-- PRODUCTS DROPDOWN -->
        <div class="relative nav-dropdown py-2 cursor-pointer">
          <a href="products.html" class="{'text-primary' if active_page=='products' else 'hover:text-primary'} flex items-center gap-1 transition">
            Products <i class="fa-solid fa-chevron-down text-[10px]"></i>
          </a>
          <div class="dropdown-menu absolute left-0 top-full hidden w-64 bg-white shadow-2xl border border-slate-200 rounded py-2 z-50">
            {"".join([f'''<a href="{p['slug']}.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-slate-50 hover:text-primary font-medium border-b border-slate-100 last:border-0">{p['title']}</a>''' for p in product_definitions])}
          </div>
        </div>

        <!-- INDUSTRIES DROPDOWN -->
        <div class="relative nav-dropdown py-2 cursor-pointer">
          <a href="industries.html" class="{'text-primary' if active_page=='industries' else 'hover:text-primary'} flex items-center gap-1 transition">
            Industries <i class="fa-solid fa-chevron-down text-[10px]"></i>
          </a>
          <div class="dropdown-menu absolute left-0 top-full hidden w-72 max-h-96 overflow-y-auto bg-white shadow-2xl border border-slate-200 rounded py-2 z-50">
            {"".join([f'''<a href="{ind[1]}.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-slate-50 hover:text-primary font-medium border-b border-slate-100 last:border-0">{ind[0]}</a>''' for ind in industries_list])}
          </div>
        </div>

        <a href="brands.html" class="{'text-primary' if active_page=='brands' else 'hover:text-primary'} py-2 transition">Brands</a>
        <a href="contact-us.html" class="{'text-primary' if active_page=='contact' else 'hover:text-primary'} py-2 transition">Contact Us</a>
      </nav>

      <!-- GET A QUOTE BUTTON -->
      <a href="contact-us.html" class="hidden sm:inline-block bg-primary hover:bg-primary-dark text-white text-xs font-bold uppercase tracking-wider px-6 py-3 rounded shadow transition">
        Get A Quote
      </a>
    </div>
  </header>
"""

def get_footer():
    return f"""
  <!-- FOOTER (Exact 4-Column Rays Layout) -->
  <footer class="bg-[#111111] text-neutral-400 pt-16 pb-8 border-t-4 border-primary mt-auto">
    <div class="max-w-7xl mx-auto px-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">
      
      <!-- COL 1: ABOUT -->
      <div class="space-y-4">
        <h4 class="text-xl font-bold heading-font text-white uppercase">Belubeari Exim</h4>
        <p class="text-xs text-neutral-400 leading-relaxed">
          At Belubeari Exim Industrial Solutions, we pride ourselves on being at the forefront of industrial innovation. Our team is dedicated to providing superior mechanical components, power transmission belts, and precision bearings.
        </p>
      </div>

      <!-- COL 2: MENU -->
      <div class="space-y-3">
        <h5 class="text-base font-bold heading-font text-white uppercase border-b border-neutral-800 pb-2">Menu</h5>
        <ul class="space-y-2 text-xs text-neutral-400">
          <li><a href="index.html" class="hover:text-primary">Home</a></li>
          <li><a href="about-us.html" class="hover:text-primary">About Us</a></li>
          <li><a href="products.html" class="hover:text-primary">Products</a></li>
          <li><a href="industries.html" class="hover:text-primary">Industries</a></li>
          <li><a href="brands.html" class="hover:text-primary">Brands</a></li>
          <li><a href="contact-us.html" class="hover:text-primary">Contact Us</a></li>
        </ul>
      </div>

      <!-- COL 3: CORE PRODUCTS -->
      <div class="space-y-3">
        <h5 class="text-base font-bold heading-font text-white uppercase border-b border-neutral-800 pb-2">Our Products</h5>
        <ul class="space-y-2 text-xs text-neutral-400">
          <li><a href="ball-bearing.html" class="hover:text-primary">Ball Bearing</a></li>
          <li><a href="timing-belts.html" class="hover:text-primary">Timing Belts</a></li>
          <li><a href="conveyor-belts.html" class="hover:text-primary">Conveyor Belts</a></li>
          <li><a href="v-belts.html" class="hover:text-primary">V-Belts</a></li>
          <li><a href="linear-motion-bearing.html" class="hover:text-primary">Linear Motion Bearing</a></li>
          <li><a href="oil-grease.html" class="hover:text-primary">Oil & Grease</a></li>
        </ul>
      </div>

      <!-- COL 4: CONTACT US -->
      <div class="space-y-3">
        <h5 class="text-base font-bold heading-font text-white uppercase border-b border-neutral-800 pb-2">Contact Us</h5>
        <div class="space-y-3 text-xs text-neutral-400">
          <p class="flex items-start gap-2.5">
            <i class="fa-solid fa-location-dot text-primary mt-1"></i>
            <span>Flat No. 8, 261/63 Yusuf Meherali Road, Masjid Bunder, Mumbai – 400003, Maharashtra, India.</span>
          </p>
          <p class="flex items-center gap-2.5">
            <i class="fa-solid fa-envelope text-primary"></i>
            <span>info@belubeariexim.com</span>
          </p>
          <div class="pt-2">
            <a href="https://wa.me/919820000000?text=Hi%20Belubeari%20Exim" target="_blank" class="inline-flex items-center gap-2 bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded text-xs font-bold transition">
              <i class="fa-brands fa-whatsapp"></i> Chat On WhatsApp
            </a>
          </div>
        </div>
      </div>

    </div>

    <!-- COPYRIGHT (Rays Match) -->
    <div class="max-w-7xl mx-auto px-4 mt-12 pt-6 border-t border-neutral-800 text-center text-xs text-neutral-500 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>© Copyright 2026, Belubeari Exim Industrial Solutions, All Rights Reserved</div>
      <div class="text-neutral-500">Masjid Bunder, Mumbai Distribution Hub</div>
    </div>
  </footer>

  <!-- FLOATING WHATSAPP -->
  <a href="https://wa.me/919820000000?text=Hello%20Belubeari%20Exim" target="_blank" class="fixed bottom-6 right-6 z-50 w-14 h-14 bg-emerald-500 hover:bg-emerald-600 text-white rounded-full flex items-center justify-center text-3xl shadow-2xl transition hover:scale-110">
    <i class="fa-brands fa-whatsapp"></i>
  </a>

</body>
</html>
"""

# ==================== 1. GENERATE HOMEPAGE (11 SECTIONS EXACT MATCH) ====================
def generate_homepage():
    # 12 Product Cards
    products_cards_html = ""
    for p in product_definitions:
        products_cards_html += f"""
        <div class="animated-border-card flex flex-col">
          <div class="product-stage">
            <img src="assets/images/{p['image']}" alt="{p['title']} Belubeari Exim" loading="lazy">
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between space-y-3">
            <div>
              <h3 class="text-xl font-bold heading-font text-[#2d3239] group-hover:text-primary transition uppercase">{p['title']}</h3>
              <p class="text-xs text-slate-500 mt-2 line-clamp-3 leading-relaxed">{p['desc']}</p>
            </div>
            <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
              <a href="{p['slug']}.html" class="text-xs font-bold text-primary hover:text-primary-dark uppercase flex items-center gap-1">
                Read More <i class="fa-solid fa-arrow-right text-[10px]"></i>
              </a>
              <a href="https://wa.me/919820000000?text=Hi%20Belubeari%20Exim,%20I%20need%20a%20quote%20for%20{p['title']}" target="_blank" class="text-emerald-600 hover:text-emerald-700 text-xs font-bold flex items-center gap-1">
                <i class="fa-brands fa-whatsapp"></i> Quote
              </a>
            </div>
          </div>
        </div>
        """

    # 20 Industry Cards
    industries_grid_html = ""
    for ind in industries_list:
        industries_grid_html += f"""
        <a href="{ind[1]}.html" class="animated-border-card group block">
          <div class="industry-stage">
            <img src="assets/images/{ind[2]}" alt="{ind[0]} Belubeari Exim" loading="lazy">
          </div>
          <div class="p-4 text-center bg-white">
            <h4 class="text-sm font-bold heading-font text-[#2d3239] group-hover:text-primary transition uppercase">{ind[0]}</h4>
            <span class="text-[11px] text-primary font-bold block mt-1">Read More &rarr;</span>
          </div>
        </a>
        """

    body = f"""
    {get_header('home', 'Belubeari Exim Industrial Solutions')}

    <!-- 1. HERO BANNER (Container 2 Match) -->
    <section class="relative bg-[#111111] text-white py-24 lg:py-32 overflow-hidden flex items-center min-h-[540px]">
      <div class="absolute inset-0 opacity-35">
        <img src="assets/images/banner-3.png" alt="Industrial Transmission Solutions" class="w-full h-full object-cover">
      </div>
      <div class="absolute inset-0 bg-gradient-to-r from-black/90 via-black/60 to-transparent"></div>

      <div class="max-w-7xl mx-auto px-4 relative z-10 w-full space-y-4">
        <h2 class="text-sm sm:text-base font-bold uppercase tracking-widest text-primary font-heading">
          welcome to
        </h2>
        <h1 class="text-3xl sm:text-5xl lg:text-6xl font-bold uppercase tracking-wide text-white leading-tight font-heading">
          Belubeari Exim <br><span class="text-primary">Industrial Solutions</span>
        </h1>
        <p class="text-neutral-300 text-sm sm:text-base max-w-2xl leading-relaxed">
          High-performance power transmission belts, precision ball bearings, linear motion guides, and conveyor spares stockist in Masjid Bunder, Mumbai.
        </p>
        <div class="flex flex-wrap items-center gap-4 pt-4">
          <a href="contact-us.html" class="px-7 py-3.5 bg-primary hover:bg-primary-dark text-white font-bold text-xs uppercase tracking-wider rounded shadow transition">
            Contact Us
          </a>
          <a href="products.html" class="px-7 py-3.5 bg-white hover:bg-neutral-100 text-[#111111] font-bold text-xs uppercase tracking-wider rounded shadow transition">
            Our Products
          </a>
        </div>
      </div>
    </section>

    <!-- 2. MEET & ASK SECTION (Container 3 Match) -->
    <section class="py-14 bg-slate-50 border-b border-slate-200">
      <div class="max-w-4xl mx-auto px-4 text-center space-y-4">
        <h3 class="text-2xl font-bold uppercase heading-font text-primary">MEET & ASK</h3>
        <p class="text-sm sm:text-base text-slate-600 italic leading-relaxed">
          "Our success is defined by your happiness and satisfaction. Your referrals are the highest compliment we can receive and a true testament to the quality of our work."
        </p>
      </div>
    </section>

    <!-- 3. OUR EXPERTISE / 20+ INDUSTRIES (Container 4 Match) -->
    <section class="py-16 bg-white border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 space-y-10">
        <div class="text-center max-w-2xl mx-auto">
          <h2 class="text-3xl sm:text-4xl font-bold heading-font text-[#2d3239] uppercase">Our Expertise</h2>
          <p class="text-sm text-slate-500 mt-2">We cater to a wide spectrum of industries with precision components and transmission parts.</p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-5">
          {industries_grid_html}
        </div>
      </div>
    </section>

    <!-- 4. LATEST PRODUCTS SHOWCASE (Container 5 Match) -->
    <section class="py-16 bg-slate-50 border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 space-y-10">
        <div class="text-center max-w-3xl mx-auto">
          <h2 class="text-3xl sm:text-4xl font-bold heading-font text-[#2d3239] uppercase">LATEST PRODUCTS</h2>
          <p class="text-sm text-slate-500 mt-2 leading-relaxed">
            At Belubeari Exim Industrial Solutions, we offer a range of high-quality power transmission belts, conveyor solutions, and precision bearings tailored to various industrial needs.
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {products_cards_html}
        </div>
      </div>
    </section>

    <!-- 5. COUNTERS & PERFORMANCE STATS (Container 6 Match) -->
    <section class="py-14 bg-[#111111] text-white border-b border-neutral-800">
      <div class="max-w-7xl mx-auto px-4 grid grid-cols-2 md:grid-cols-4 gap-6 text-center">
        <div class="p-6 bg-neutral-900/60 rounded border border-neutral-800 space-y-2">
          <div class="text-3xl sm:text-4xl font-bold heading-font text-primary">500+</div>
          <div class="text-xs uppercase font-semibold text-neutral-300">Happy Clients</div>
        </div>
        <div class="p-6 bg-neutral-900/60 rounded border border-neutral-800 space-y-2">
          <div class="text-3xl sm:text-4xl font-bold heading-font text-primary">50+</div>
          <div class="text-xs uppercase font-semibold text-neutral-300">Product Range</div>
        </div>
        <div class="p-6 bg-neutral-900/60 rounded border border-neutral-800 space-y-2">
          <div class="text-3xl sm:text-4xl font-bold heading-font text-primary">100%</div>
          <div class="text-xs uppercase font-semibold text-neutral-300">Performance</div>
        </div>
        <div class="p-6 bg-neutral-900/60 rounded border border-neutral-800 space-y-2">
          <div class="text-3xl sm:text-4xl font-bold heading-font text-primary">2018*</div>
          <div class="text-xs uppercase font-semibold text-neutral-300">Mumbai Trade Desk</div>
        </div>
      </div>
    </section>

    <!-- 6. WHAT PEOPLE ARE SAYING / TESTIMONIALS (Container 7 Match) -->
    <section class="py-16 bg-white border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 space-y-10">
        <div class="text-center max-w-2xl mx-auto">
          <h2 class="text-3xl sm:text-4xl font-bold heading-font text-[#2d3239] uppercase">WHAT PEOPLE ARE SAYING</h2>
          <p class="text-sm text-slate-500 mt-2">Hear directly from industry leaders and maintenance teams who trust our supply.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="p-6 bg-slate-50 rounded-lg border border-slate-200 space-y-4">
            <div class="text-amber-400 text-sm flex gap-1"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
            <p class="text-xs text-slate-600 leading-relaxed italic">
              "Belubeari Exim Industrial Solutions has transformed our production line with their reliable conveyor belts and precision bearings. Fast Mumbai dispatch!"
            </p>
            <div class="pt-2 border-t border-slate-200">
              <h5 class="text-sm font-bold heading-font text-[#2d3239] uppercase">Rajesh Sharma</h5>
              <span class="text-[11px] text-slate-400">Plant Operations Manager</span>
            </div>
          </div>

          <div class="p-6 bg-slate-50 rounded-lg border border-slate-200 space-y-4">
            <div class="text-amber-400 text-sm flex gap-1"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
            <p class="text-xs text-slate-600 leading-relaxed italic">
              "Exceptional timing belt quality and exact part number matching. Their technical team at Masjid Bunder resolved our machinery downtime promptly."
            </p>
            <div class="pt-2 border-t border-slate-200">
              <h5 class="text-sm font-bold heading-font text-[#2d3239] uppercase">Amit Verma</h5>
              <span class="text-[11px] text-slate-400">Chief Engineer</span>
            </div>
          </div>

          <div class="p-6 bg-slate-50 rounded-lg border border-slate-200 space-y-4">
            <div class="text-amber-400 text-sm flex gap-1"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div>
            <p class="text-xs text-slate-600 leading-relaxed italic">
              "Consistent quality in high-temperature greases and pillow block bearings. We have been sourcing all our factory maintenance spares from them."
            </p>
            <div class="pt-2 border-t border-slate-200">
              <h5 class="text-sm font-bold heading-font text-[#2d3239] uppercase">Sunil Patel</h5>
              <span class="text-[11px] text-slate-400">Procurement Head</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 7. OUR BRANDS OF BEARINGS & BELTS (Container 8 Match) -->
    <section class="py-16 bg-slate-50 border-b border-slate-200 space-y-12">
      <div class="max-w-7xl mx-auto px-4 space-y-8">
        <div class="text-center max-w-2xl mx-auto">
          <h2 class="text-3xl sm:text-4xl font-bold heading-font text-[#2d3239] uppercase">Our Brands of Bearings</h2>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-4">
          <div class="p-5 bg-white rounded border border-slate-200 shadow-sm text-center font-bold heading-font text-lg hover:text-primary transition">SKF</div>
          <div class="p-5 bg-white rounded border border-slate-200 shadow-sm text-center font-bold heading-font text-lg hover:text-primary transition">FAG / INA</div>
          <div class="p-5 bg-white rounded border border-slate-200 shadow-sm text-center font-bold heading-font text-lg hover:text-primary transition">NACHI</div>
          <div class="p-5 bg-white rounded border border-slate-200 shadow-sm text-center font-bold heading-font text-lg hover:text-primary transition">TIMKEN</div>
          <div class="p-5 bg-white rounded border border-slate-200 shadow-sm text-center font-bold heading-font text-lg hover:text-primary transition">IJK</div>
          <div class="p-5 bg-white rounded border border-slate-200 shadow-sm text-center font-bold heading-font text-lg hover:text-primary transition">NMB</div>
        </div>
      </div>

      <div class="max-w-7xl mx-auto px-4 space-y-8">
        <div class="text-center max-w-2xl mx-auto">
          <h2 class="text-3xl sm:text-4xl font-bold heading-font text-[#2d3239] uppercase">Our Brands of Belts</h2>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-4">
          <div class="p-5 bg-white rounded border border-slate-200 shadow-sm text-center font-bold heading-font text-lg hover:text-primary transition">CONTINENTAL</div>
          <div class="p-5 bg-white rounded border border-slate-200 shadow-sm text-center font-bold heading-font text-lg hover:text-primary transition">MITSUBOSHI</div>
          <div class="p-5 bg-white rounded border border-slate-200 shadow-sm text-center font-bold heading-font text-lg hover:text-primary transition">GATES</div>
          <div class="p-5 bg-white rounded border border-slate-200 shadow-sm text-center font-bold heading-font text-lg hover:text-primary transition">FENNER</div>
          <div class="p-5 bg-white rounded border border-slate-200 shadow-sm text-center font-bold heading-font text-lg hover:text-primary transition">MEGADYNE</div>
        </div>
      </div>
    </section>

    <!-- 8. QUOTATION CALLOUT STRIP -->
    <section class="py-12 bg-primary text-white">
      <div class="max-w-7xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-6 text-center md:text-left">
        <div>
          <h3 class="text-2xl sm:text-3xl font-bold uppercase heading-font text-white">Need Immediate Quotation For Industrial Spares?</h3>
          <p class="text-xs sm:text-sm text-sky-100 mt-1">Send us your part number or bill of materials for prompt wholesale quotation.</p>
        </div>
        <div class="flex items-center gap-4">
          <a href="contact-us.html" class="px-6 py-3 bg-white text-[#111111] hover:bg-neutral-100 font-bold text-xs uppercase tracking-wider rounded shadow transition">
            Contact Trade Desk
          </a>
          <a href="https://wa.me/919820000000?text=Hi%20Belubeari%20Exim,%20I%20need%20a%20quotation" target="_blank" class="px-6 py-3 bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs uppercase tracking-wider rounded shadow transition flex items-center gap-2">
            <i class="fa-brands fa-whatsapp text-sm"></i> WhatsApp Quote
          </a>
        </div>
      </div>
    </section>

    {get_footer()}
    """
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(body)

# ==================== 2. GENERATE PRODUCT & INDUSTRY & OTHER PAGES ====================
def generate_subpages():
    for p in product_definitions:
        specs_rows = "".join([f"""
          <tr class="border-b border-slate-200">
            <td class="py-3 px-4 font-bold text-[#2d3239] bg-slate-50 w-1/3">{spec[0]}</td>
            <td class="py-3 px-4 text-slate-700">{spec[1]}</td>
          </tr>
        """ for spec in p['specs']])

        sidebar_links = "".join([f"""
          <a href="{other['slug']}.html" class="block px-4 py-2.5 text-xs font-semibold {'bg-primary text-white rounded' if other['slug']==p['slug'] else 'text-slate-700 hover:bg-slate-100 rounded'} transition">
            {other['title']}
          </a>
        """ for other in product_definitions])

        body = f"""
        {get_header('products', f"{p['title']} - Belubeari Exim")}
        <div class="bg-slate-100 border-b border-slate-200 py-6">
          <div class="max-w-7xl mx-auto px-4 flex flex-wrap items-center justify-between gap-4">
            <div>
              <div class="text-xs text-slate-500 font-medium">
                <a href="index.html" class="hover:text-primary">Home</a> / <a href="products.html" class="hover:text-primary">Products</a> / <span class="text-primary font-bold">{p['title']}</span>
              </div>
              <h1 class="text-3xl font-bold heading-font text-[#2d3239] mt-1 uppercase">{p['title']}</h1>
            </div>
            <a href="contact-us.html" class="bg-primary hover:bg-primary-dark text-white px-5 py-2.5 rounded font-bold text-xs uppercase shadow transition">
              Request RFQ
            </a>
          </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 py-12 grid grid-cols-1 lg:grid-cols-12 gap-10">
          <div class="lg:col-span-8 space-y-8">
            <div class="animated-border-card p-6 space-y-6">
              <div class="product-stage h-80">
                <img src="assets/images/{p['image']}" alt="{p['title']} Belubeari Exim">
              </div>
              <div class="space-y-4">
                <h2 class="text-2xl font-bold heading-font text-[#2d3239] uppercase">{p['title']} Solutions</h2>
                <p class="text-sm text-slate-600 leading-relaxed">{p['desc']}</p>
                <p class="text-sm text-slate-600 leading-relaxed">
                  Belubeari Exim Industrial Solutions is an authorized stockist and importer of {p['title']} based in Masjid Bunder, Mumbai. We provide dimensional interchangeability verification, bulk wholesale rates, and fast dispatch across India.
                </p>
              </div>
            </div>

            <div class="bg-white rounded border border-slate-200 shadow-sm p-6 space-y-4">
              <h3 class="text-xl font-bold heading-font text-[#2d3239] uppercase">Technical Specifications & Standards</h3>
              <div class="overflow-x-auto">
                <table class="w-full text-xs text-left border-collapse">
                  <tbody>{specs_rows}</tbody>
                </table>
              </div>
            </div>

            <div class="bg-sky-50 border border-sky-200 rounded p-6 flex flex-col sm:flex-row items-center justify-between gap-4">
              <div>
                <h4 class="text-lg font-bold heading-font text-[#2d3239] uppercase">Looking for a specific {p['title']} size or part number?</h4>
                <p class="text-xs text-slate-600 mt-1">Share your part number with our Mumbai trade desk for instant availability and pricing.</p>
              </div>
              <a href="https://wa.me/919820000000?text=Hi%20Belubeari%20Exim,%20I%20need%20a%20quotation%20for%20{p['title']}" target="_blank" class="px-5 py-3 bg-emerald-600 hover:bg-emerald-500 text-white rounded font-bold text-xs uppercase flex items-center gap-2 whitespace-nowrap shadow transition">
                <i class="fa-brands fa-whatsapp text-base"></i> WhatsApp RFQ
              </a>
            </div>
          </div>

          <div class="lg:col-span-4 space-y-6">
            <div class="bg-white rounded border border-slate-200 shadow-sm p-5 space-y-3">
              <h4 class="text-base font-bold heading-font text-[#2d3239] uppercase border-b border-slate-200 pb-2">All Products</h4>
              <div class="space-y-1">{sidebar_links}</div>
            </div>

            <div class="bg-[#111111] text-white rounded p-6 space-y-4">
              <h4 class="text-base font-bold heading-font text-primary uppercase">Trade & Sourcing Desk</h4>
              <p class="text-xs text-neutral-300 leading-relaxed">
                Flat No. 8, 261/63 Yusuf Meherali Road, Masjid Bunder, Mumbai – 400003.
              </p>
              <div class="pt-2">
                <a href="contact-us.html" class="w-full block text-center py-2.5 bg-primary hover:bg-primary-dark text-white rounded font-bold text-xs uppercase transition">
                  Contact Us
                </a>
              </div>
            </div>
          </div>
        </div>
        {get_footer()}
        """
        with open(os.path.join(out_dir, f"{p['slug']}.html"), 'w', encoding='utf-8') as f:
            f.write(body)

    # 20 Industry Pages
    for ind in industries_list:
        sidebar_ind_links = "".join([f"""
          <a href="{other[1]}.html" class="block px-4 py-2.5 text-xs font-semibold {'bg-primary text-white rounded' if other[1]==ind[1] else 'text-slate-700 hover:bg-slate-100 rounded'} transition">
            {other[0]}
          </a>
        """ for other in industries_list])

        body = f"""
        {get_header('industries', f"{ind[0]} - Belubeari Exim")}
        <div class="bg-slate-100 border-b border-slate-200 py-6">
          <div class="max-w-7xl mx-auto px-4 flex flex-wrap items-center justify-between gap-4">
            <div>
              <div class="text-xs text-slate-500 font-medium">
                <a href="index.html" class="hover:text-primary">Home</a> / <a href="industries.html" class="hover:text-primary">Industries</a> / <span class="text-primary font-bold">{ind[0]}</span>
              </div>
              <h1 class="text-3xl font-bold heading-font text-[#2d3239] mt-1 uppercase">{ind[0]} Solutions</h1>
            </div>
            <a href="contact-us.html" class="bg-primary hover:bg-primary-dark text-white px-5 py-2.5 rounded font-bold text-xs uppercase shadow transition">
              Get Quote
            </a>
          </div>
        </div>

        <div class="max-w-7xl mx-auto px-4 py-12 grid grid-cols-1 lg:grid-cols-12 gap-10">
          <div class="lg:col-span-8 space-y-8">
            <div class="animated-border-card p-6 space-y-6">
              <div class="industry-stage h-72">
                <img src="assets/images/{ind[2]}" alt="{ind[0]} Belubeari Exim">
              </div>
              <div class="space-y-4">
                <h2 class="text-2xl font-bold heading-font text-[#2d3239] uppercase">Mechanical Spares & Bearings for {ind[0]}</h2>
                <p class="text-sm text-slate-600 leading-relaxed">{ind[3]}</p>
                <p class="text-sm text-slate-600 leading-relaxed">
                  Belubeari Exim Industrial Solutions supports industrial plants in the {ind[0]} sector with durable power transmission belts, heavy spherical bearings, high-temperature lubrication greases, and custom conveyor components engineered to withstand continuous operation.
                </p>
              </div>
            </div>

            <div class="bg-white rounded border border-slate-200 shadow-sm p-6 space-y-4">
              <h3 class="text-xl font-bold heading-font text-[#2d3239] uppercase">Key Recommended Components for {ind[0]}</h3>
              <ul class="space-y-3 text-xs text-slate-700">
                <li class="flex items-start gap-3 p-3 bg-slate-50 rounded border border-slate-200">
                  <i class="fa-solid fa-check text-primary mt-0.5"></i>
                  <div><strong>Heavy Duty Industrial Bearings:</strong> Spherical, tapered roller, and deep groove bearings designed for severe radial and axial shock loads.</div>
                </li>
                <li class="flex items-start gap-3 p-3 bg-slate-50 rounded border border-slate-200">
                  <i class="fa-solid fa-check text-primary mt-0.5"></i>
                  <div><strong>Synchronous Timing & Transmission Belts:</strong> High-torque metric belts for positive zero-slip drive systems.</div>
                </li>
                <li class="flex items-start gap-3 p-3 bg-slate-50 rounded border border-slate-200">
                  <i class="fa-solid fa-check text-primary mt-0.5"></i>
                  <div><strong>High-Performance Industrial Lubricants:</strong> Extreme temperature greases ensuring maximum operating life of bearings and gears.</div>
                </li>
              </ul>
            </div>
          </div>

          <div class="lg:col-span-4 space-y-6">
            <div class="bg-white rounded border border-slate-200 shadow-sm p-5 space-y-3">
              <h4 class="text-base font-bold heading-font text-[#2d3239] uppercase border-b border-slate-200 pb-2">All Industries</h4>
              <div class="space-y-1 max-h-96 overflow-y-auto">{sidebar_ind_links}</div>
            </div>
          </div>
        </div>
        {get_footer()}
        """
        with open(os.path.join(out_dir, f"{ind[1]}.html"), 'w', encoding='utf-8') as f:
            f.write(body)

    # About Us
    about_body = f"""
    {get_header('about', 'About Us - Belubeari Exim Industrial Solutions')}
    <div class="bg-slate-100 border-b border-slate-200 py-6">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-xs text-slate-500 font-medium"><a href="index.html" class="hover:text-primary">Home</a> / <span class="text-primary font-bold">About Us</span></div>
        <h1 class="text-3xl font-bold heading-font text-[#2d3239] mt-1 uppercase">About Belubeari Exim Industrial Solutions</h1>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 py-12 space-y-12">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-7 space-y-5">
          <h2 class="text-3xl font-bold heading-font text-[#2d3239] uppercase">Your Trusted Industrial Transmission Partner</h2>
          <p class="text-sm text-slate-600 leading-relaxed">
            At <strong>Belubeari Exim Industrial Solutions</strong>, we pride ourselves on being at the forefront of industrial innovation. Our team is dedicated to providing superior mechanical components, power transmission belts, and precision bearings.
          </p>
          <p class="text-sm text-slate-600 leading-relaxed">
            Headquartered at Yusuf Meherali Road, Masjid Bunder, Mumbai, we serve engineering OEMs, cement plants, textile mills, steel industries, and maintenance professionals with rapid dispatch and verified genuine components.
          </p>
        </div>
        <div class="lg:col-span-5">
          <div class="animated-border-card p-4">
            <img src="assets/images/Ball-Bearing.jpg" alt="About Belubeari Exim" class="w-full h-80 object-contain">
          </div>
        </div>
      </div>
    </div>
    {get_footer()}
    """
    with open(os.path.join(out_dir, 'about-us.html'), 'w', encoding='utf-8') as f:
        f.write(about_body)

    # Contact Us
    contact_body = f"""
    {get_header('contact', 'Contact Us - Belubeari Exim Industrial Solutions')}
    <div class="bg-slate-100 border-b border-slate-200 py-6">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-xs text-slate-500 font-medium"><a href="index.html" class="hover:text-primary">Home</a> / <span class="text-primary font-bold">Contact Us</span></div>
        <h1 class="text-3xl font-bold heading-font text-[#2d3239] mt-1 uppercase">Contact Us</h1>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 py-12 grid grid-cols-1 lg:grid-cols-12 gap-10">
      <div class="lg:col-span-5 space-y-6">
        <div>
          <h2 class="text-2xl font-bold heading-font text-[#2d3239] uppercase mt-1">Trade Desk & Registered Office</h2>
        </div>
        <div class="space-y-4 text-xs">
          <div class="p-4 bg-slate-50 border border-slate-200 rounded space-y-1">
            <div class="font-bold text-[#2d3239] text-sm flex items-center gap-2"><i class="fa-solid fa-building text-primary"></i> Registered Business Address</div>
            <div class="text-slate-600">Flat No. 8, 261/63 Yusuf Meherali Road, Masjid Bunder, Mumbai – 400003, Maharashtra, India.</div>
          </div>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded space-y-1">
            <div class="font-bold text-[#2d3239] text-sm flex items-center gap-2"><i class="fa-brands fa-whatsapp text-emerald-600"></i> WhatsApp RFQ Desk</div>
            <div class="text-slate-600">Instant Technical Specification & Part Matching</div>
          </div>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded space-y-1">
            <div class="font-bold text-[#2d3239] text-sm flex items-center gap-2"><i class="fa-solid fa-clock text-primary"></i> Working Hours</div>
            <div class="text-slate-600">Monday – Saturday : 10:00 AM – 7:30 PM</div>
          </div>
        </div>
      </div>

      <div class="lg:col-span-7">
        <div class="bg-white rounded border border-slate-200 shadow-sm p-6 space-y-4">
          <h3 class="text-xl font-bold heading-font text-[#2d3239] uppercase">Send Direct Purchase Enquiry</h3>
          <form class="space-y-3 text-xs" onsubmit="event.preventDefault(); window.open('https://wa.me/919820000000?text=Hi%20Belubeari%20Exim,%20I%20have%20an%20enquiry', '_blank');">
            <div>
              <label class="block font-bold text-slate-700 mb-1">YOUR NAME / COMPANY</label>
              <input type="text" required class="w-full border border-slate-300 rounded p-2.5 outline-none focus:border-primary" placeholder="Enter name">
            </div>
            <div>
              <label class="block font-bold text-slate-700 mb-1">PHONE / WHATSAPP NUMBER</label>
              <input type="text" required class="w-full border border-slate-300 rounded p-2.5 outline-none focus:border-primary" placeholder="Enter phone number">
            </div>
            <div>
              <label class="block font-bold text-slate-700 mb-1">PART NUMBER / SPECIFICATIONS REQUIRED</label>
              <textarea rows="4" required class="w-full border border-slate-300 rounded p-2.5 outline-none focus:border-primary" placeholder="Enter Part No., Dimensions, and Quantity"></textarea>
            </div>
            <button type="submit" class="w-full py-3 bg-primary hover:bg-primary-dark text-white font-bold uppercase rounded shadow transition">
              Submit Inquiry
            </button>
          </form>
        </div>
      </div>
    </div>
    {get_footer()}
    """
    with open(os.path.join(out_dir, 'contact-us.html'), 'w', encoding='utf-8') as f:
        f.write(contact_body)

    # Products & Industries & Brands general catalog
    products_cards_html = "".join([f"""
    <div class="animated-border-card flex flex-col">
      <div class="product-stage">
        <img src="assets/images/{p['image']}" alt="{p['title']} Belubeari Exim" loading="lazy">
      </div>
      <div class="p-5 flex-1 flex flex-col justify-between space-y-3 bg-white">
        <div>
          <h3 class="text-xl font-bold heading-font text-[#2d3239] group-hover:text-primary transition uppercase">{p['title']}</h3>
          <p class="text-xs text-slate-500 mt-2 line-clamp-3 leading-relaxed">{p['desc']}</p>
        </div>
        <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
          <a href="{p['slug']}.html" class="text-xs font-bold text-primary hover:text-primary-dark uppercase flex items-center gap-1">
            Read More <i class="fa-solid fa-arrow-right text-[10px]"></i>
          </a>
          <a href="https://wa.me/919820000000?text=Hi%20Belubeari%20Exim,%20I%20need%20a%20quote%20for%20{p['title']}" target="_blank" class="text-emerald-600 hover:text-emerald-700 text-xs font-bold flex items-center gap-1">
            <i class="fa-brands fa-whatsapp"></i> Quote
          </a>
        </div>
      </div>
    </div>
    """ for p in product_definitions])

    with open(os.path.join(out_dir, 'products.html'), 'w', encoding='utf-8') as f:
        f.write(f"""{get_header('products', 'Products Catalog - Belubeari Exim')}
        <div class="bg-slate-100 border-b border-slate-200 py-6">
          <div class="max-w-7xl mx-auto px-4">
            <div class="text-xs text-slate-500 font-medium"><a href="index.html" class="hover:text-primary">Home</a> / <span class="text-primary font-bold">Products</span></div>
            <h1 class="text-3xl font-bold heading-font text-[#2d3239] mt-1 uppercase">Our Products</h1>
          </div>
        </div>
        <div class="max-w-7xl mx-auto px-4 py-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {products_cards_html}
        </div>
        {get_footer()}""")

    industries_cards_html = "".join([f"""
    <div class="animated-border-card flex flex-col">
      <div class="industry-stage">
        <img src="assets/images/{ind[2]}" alt="{ind[0]} Belubeari Exim" loading="lazy">
      </div>
      <div class="p-5 flex-1 flex flex-col justify-between space-y-3 bg-white">
        <div>
          <h3 class="text-lg font-bold heading-font text-[#2d3239] group-hover:text-primary transition uppercase">{ind[0]}</h3>
          <p class="text-xs text-slate-500 mt-2 line-clamp-3 leading-relaxed">{ind[3]}</p>
        </div>
        <div class="pt-3 border-t border-slate-100">
          <a href="{ind[1]}.html" class="text-xs font-bold text-primary hover:text-primary-dark uppercase flex items-center gap-1">
            Read More <i class="fa-solid fa-arrow-right text-[10px]"></i>
          </a>
        </div>
      </div>
    </div>
    """ for ind in industries_list])

    with open(os.path.join(out_dir, 'industries.html'), 'w', encoding='utf-8') as f:
        f.write(f"""{get_header('industries', 'Industries - Belubeari Exim')}
        <div class="bg-slate-100 border-b border-slate-200 py-6">
          <div class="max-w-7xl mx-auto px-4">
            <div class="text-xs text-slate-500 font-medium"><a href="index.html" class="hover:text-primary">Home</a> / <span class="text-primary font-bold">Industries</span></div>
            <h1 class="text-3xl font-bold heading-font text-[#2d3239] mt-1 uppercase">Our Expertise Across Industries</h1>
          </div>
        </div>
        <div class="max-w-7xl mx-auto px-4 py-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {industries_cards_html}
        </div>
        {get_footer()}""")

    with open(os.path.join(out_dir, 'brands.html'), 'w', encoding='utf-8') as f:
        f.write(f"""{get_header('brands', 'Brands - Belubeari Exim')}
        <div class="bg-slate-100 border-b border-slate-200 py-6">
          <div class="max-w-7xl mx-auto px-4">
            <div class="text-xs text-slate-500 font-medium"><a href="index.html" class="hover:text-primary">Home</a> / <span class="text-primary font-bold">Brands</span></div>
            <h1 class="text-3xl font-bold heading-font text-[#2d3239] mt-1 uppercase">Brands We Stock & Supply</h1>
          </div>
        </div>
        <div class="max-w-7xl mx-auto px-4 py-12 space-y-8">
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
            <div class="p-6 bg-white rounded border border-slate-200 shadow-sm space-y-2 hover:border-primary transition">
              <h3 class="text-xl font-bold heading-font text-[#2d3239] uppercase">CONTINENTAL CONTITECH</h3>
              <p class="text-xs text-slate-500">Heavy duty industrial timing belts, multi-rib belts, and synchronous drive systems.</p>
            </div>
            <div class="p-6 bg-white rounded border border-slate-200 shadow-sm space-y-2 hover:border-primary transition">
              <h3 class="text-xl font-bold heading-font text-[#2d3239] uppercase">MITSUBOSHI</h3>
              <p class="text-xs text-slate-500">Japanese high-torque transmission belts, automotive belts, and polyurethane belts.</p>
            </div>
            <div class="p-6 bg-white rounded border border-slate-200 shadow-sm space-y-2 hover:border-primary transition">
              <h3 class="text-xl font-bold heading-font text-[#2d3239] uppercase">GATES</h3>
              <p class="text-xs text-slate-500">Poly Chain GT Carbon belts, classical wrapped V-belts, and industrial hydraulic hoses.</p>
            </div>
            <div class="p-6 bg-white rounded border border-slate-200 shadow-sm space-y-2 hover:border-primary transition">
              <h3 class="text-xl font-bold heading-font text-[#2d3239] uppercase">SKF</h3>
              <p class="text-xs text-slate-500">Global benchmark precision ball bearings, spherical roller bearings, and bearing greases.</p>
            </div>
            <div class="p-6 bg-white rounded border border-slate-200 shadow-sm space-y-2 hover:border-primary transition">
              <h3 class="text-xl font-bold heading-font text-[#2d3239] uppercase">FAG / INA</h3>
              <p class="text-xs text-slate-500">German engineered spherical, cylindrical, and needle roller bearings.</p>
            </div>
            <div class="p-6 bg-white rounded border border-slate-200 shadow-sm space-y-2 hover:border-primary transition">
              <h3 class="text-xl font-bold heading-font text-[#2d3239] uppercase">TIMKEN</h3>
              <p class="text-xs text-slate-500">Ultra heavy duty tapered roller bearings and mounted bearing pillow block units.</p>
            </div>
          </div>
        </div>
        {get_footer()}""")

generate_homepage()
generate_subpages()

print('Successfully generated 100% exact 11-section replica of Rays International for Belubeari Exim!')

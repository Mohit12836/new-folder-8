import os
import json

out_dir = r'd:\codee\Ms Belubeari Exim\New folder (8)'

# Exact verified product definitions
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

# Exact verified industries list
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

def get_header(active_page='home', title='Industrial Bearings & Transmission Belts Stockist Mumbai'):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | M/s Belubeari Exim Mumbai</title>
  <meta name="description" content="M/s Belubeari Exim - Premier Mumbai stockist and wholesale distributor for industrial bearings, timing belts, conveyor spares and lubrication solutions located at Masjid Bunder, Mumbai." />
  
  <!-- Google Fonts -->
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
              DEFAULT: '#0284c7',
              dark: '#0369a1',
              light: '#38bdf8'
            }},
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
      color: #475569;
    }}
    
    /* 100% AUTO-FIT IMAGES SYSTEM */
    img, video, svg, canvas, iframe {{
      max-width: 100%;
      height: auto;
      display: block;
    }}
    
    /* ======================================================== */
    /* 🌟 ANIMATED MOVING BORDER BEAM & GLOWING SHADOW ENGINE 🌟 */
    /* ======================================================== */
    
    @property --border-angle {{
      syntax: "<angle>";
      inherits: false;
      initial-value: 0deg;
    }}

    @keyframes border-beam-rotate {{
      0% {{
        --border-angle: 0deg;
      }}
      100% {{
        --border-angle: 360deg;
      }}
    }}

    @keyframes ambient-glow-pulse {{
      0%, 100% {{
        box-shadow: 0 8px 24px -4px rgba(2, 132, 199, 0.15), 0 0 12px rgba(56, 189, 248, 0.2);
      }}
      50% {{
        box-shadow: 0 16px 36px -4px rgba(2, 132, 199, 0.35), 0 0 25px rgba(56, 189, 248, 0.45);
      }}
    }}

    /* Card with Moving Animated Border */
    .animated-border-card {{
      position: relative;
      background: #ffffff;
      border-radius: 1rem;
      overflow: hidden;
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 0 6px 20px -2px rgba(2, 132, 199, 0.12);
      border: 1px solid rgba(226, 232, 240, 0.8);
      z-index: 1;
    }}

    .animated-border-card::before {{
      content: '';
      position: absolute;
      inset: 0;
      border-radius: inherit;
      padding: 2.5px;
      background: conic-gradient(from var(--border-angle), transparent 25%, #0284c7 45%, #38bdf8 50%, #0284c7 55%, transparent 75%);
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      animation: border-beam-rotate 4s linear infinite;
      pointer-events: none;
      opacity: 0.75;
      transition: opacity 0.3s ease;
      z-index: 2;
    }}

    .animated-border-card:hover::before {{
      opacity: 1;
      animation-duration: 2s;
    }}

    .animated-border-card:hover {{
      transform: translateY(-6px);
      animation: ambient-glow-pulse 2.5s ease-in-out infinite;
    }}

    /* PRODUCT STAGE: CONTAINED & UNIFORM FIT */
    .product-stage {{
      width: 100%;
      height: 230px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at center, #ffffff 0%, #f1f5f9 100%);
      border-bottom: 1px solid #e2e8f0;
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
      transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      filter: drop-shadow(0 6px 12px rgba(0, 0, 0, 0.12));
    }}
    
    .animated-border-card:hover .product-stage img {{
      transform: scale(1.1);
      filter: drop-shadow(0 10px 20px rgba(2, 132, 199, 0.3));
    }}
    
    /* INDUSTRY STAGE */
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

    /* DETAIL PAGE HERO STAGE WITH MOVING BORDER */
    .detail-stage {{
      width: 100%;
      height: 380px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at center, #ffffff 0%, #f8fafc 100%);
      border-radius: 1rem;
      padding: 1.5rem;
      overflow: hidden;
      position: relative;
      animation: ambient-glow-pulse 4s ease-in-out infinite;
    }}
    
    .detail-stage img {{
      max-width: 100%;
      max-height: 100%;
      width: auto;
      height: auto;
      object-fit: contain;
      object-position: center;
      filter: drop-shadow(0 12px 24px rgba(2, 132, 199, 0.2));
    }}

    .industry-detail-stage {{
      width: 100%;
      height: 340px;
      position: relative;
      overflow: hidden;
      border-radius: 1rem;
      background-color: #0f172a;
      animation: ambient-glow-pulse 4s ease-in-out infinite;
    }}
    
    .industry-detail-stage img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
    }}

    h1, h2, h3, h4, h5, h6, .heading-font {{
      font-family: 'Oswald', sans-serif;
      text-transform: uppercase;
      letter-spacing: 0.02em;
    }}
    
    .nav-dropdown:hover .dropdown-menu {{
      display: block;
    }}
  </style>
</head>
<body class="bg-white text-slate-700 flex flex-col min-h-screen">

  <!-- TOP BAR -->
  <div class="bg-corp-900 text-white text-xs py-2.5 px-4 border-b border-slate-800">
    <div class="max-w-7xl mx-auto flex flex-wrap items-center justify-between gap-3">
      <div class="flex items-center gap-4 text-slate-300">
        <span class="flex items-center gap-1.5"><i class="fa-solid fa-location-dot text-primary-light"></i> Flat No. 8, Yusuf Meherali Road, Masjid Bunder, Mumbai – 400003</span>
        <span class="hidden md:inline text-slate-600">|</span>
        <span class="hidden md:flex items-center gap-1.5"><i class="fa-solid fa-envelope text-primary-light"></i> info@belubeariexim.com</span>
      </div>
      <div class="flex items-center gap-4">
        <span class="hidden sm:inline text-emerald-400 font-semibold"><i class="fa-solid fa-check-circle"></i> ISO Standard & Genuine Brands Sourcing</span>
        <a href="https://wa.me/919820000000?text=Hi%20Belubeari%20Exim,%20I%20need%20an%20industrial%20quote" target="_blank" class="bg-primary hover:bg-primary-dark text-white px-3 py-1 rounded font-bold transition flex items-center gap-1.5">
          <i class="fa-brands fa-whatsapp"></i> Quick RFQ
        </a>
      </div>
    </div>
  </div>

  <!-- MAIN NAVIGATION -->
  <header class="sticky top-0 z-50 bg-white/95 backdrop-blur shadow-md border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 flex items-center justify-between h-20">
      
      <!-- LOGO -->
      <a href="index.html" class="flex items-center gap-3">
        <div class="w-12 h-12 bg-primary text-white flex items-center justify-center rounded-lg text-2xl font-black shadow-md">
          <i class="fa-solid fa-gear"></i>
        </div>
        <div>
          <div class="text-2xl font-bold heading-font text-slate-900 leading-none">
            BELUBEARI <span class="text-primary">EXIM</span>
          </div>
          <div class="text-[10px] tracking-widest text-slate-500 uppercase font-semibold mt-1">
            Industrial Components & B2B Supply
          </div>
        </div>
      </a>

      <!-- DESKTOP NAV -->
      <nav class="hidden lg:flex items-center gap-7 text-sm font-bold text-slate-800 uppercase">
        <a href="index.html" class="{'text-primary border-b-2 border-primary' if active_page=='home' else 'hover:text-primary'} py-2 transition">Home</a>
        <a href="about-us.html" class="{'text-primary border-b-2 border-primary' if active_page=='about' else 'hover:text-primary'} py-2 transition">About Us</a>
        
        <!-- PRODUCTS DROPDOWN -->
        <div class="relative nav-dropdown py-2 cursor-pointer">
          <a href="products.html" class="{'text-primary border-b-2 border-primary' if active_page=='products' else 'hover:text-primary'} flex items-center gap-1 transition">
            Products <i class="fa-solid fa-chevron-down text-[10px]"></i>
          </a>
          <div class="dropdown-menu absolute left-0 top-full hidden w-64 bg-white shadow-2xl border border-slate-200 rounded-lg py-2 z-50">
            {"".join([f'''<a href="{p['slug']}.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-slate-50 hover:text-primary font-semibold border-b border-slate-100 last:border-0">{p['title']}</a>''' for p in product_definitions])}
          </div>
        </div>

        <!-- INDUSTRIES DROPDOWN -->
        <div class="relative nav-dropdown py-2 cursor-pointer">
          <a href="industries.html" class="{'text-primary border-b-2 border-primary' if active_page=='industries' else 'hover:text-primary'} flex items-center gap-1 transition">
            Industries <i class="fa-solid fa-chevron-down text-[10px]"></i>
          </a>
          <div class="dropdown-menu absolute left-0 top-full hidden w-72 max-h-96 overflow-y-auto bg-white shadow-2xl border border-slate-200 rounded-lg py-2 z-50">
            {"".join([f'''<a href="{ind[1]}.html" class="block px-4 py-2 text-xs text-slate-700 hover:bg-slate-50 hover:text-primary font-semibold border-b border-slate-100 last:border-0">{ind[0]}</a>''' for ind in industries_list])}
          </div>
        </div>

        <a href="brands.html" class="{'text-primary border-b-2 border-primary' if active_page=='brands' else 'hover:text-primary'} py-2 transition">Brands</a>
        <a href="contact-us.html" class="{'text-primary border-b-2 border-primary' if active_page=='contact' else 'hover:text-primary'} py-2 transition">Contact Us</a>
      </nav>

      <!-- GET A QUOTE CTA -->
      <div class="flex items-center gap-3">
        <a href="contact-us.html" class="hidden sm:inline-flex items-center gap-2 bg-primary hover:bg-primary-dark text-white text-xs font-bold uppercase tracking-wider px-5 py-3 rounded shadow transition">
          <i class="fa-solid fa-paper-plane"></i> Get A Quote
        </a>
      </div>
    </div>
  </header>
"""

def get_footer():
    return f"""
  <!-- FOOTER -->
  <footer class="bg-corp-900 text-slate-300 pt-16 pb-8 border-t-4 border-primary mt-auto">
    <div class="max-w-7xl mx-auto px-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">
      
      <!-- ABOUT COL -->
      <div class="space-y-4">
        <div class="flex items-center gap-3">
          <div class="w-10 h-10 bg-primary text-white flex items-center justify-center rounded text-xl font-black">
            <i class="fa-solid fa-gear"></i>
          </div>
          <div class="text-xl font-bold heading-font text-white">
            BELUBEARI <span class="text-primary-light">EXIM</span>
          </div>
        </div>
        <p class="text-xs text-slate-400 leading-relaxed">
          M/s Belubeari Exim is a trusted Mumbai-based stockist, wholesaler, and distributor specializing in high-precision bearings, power transmission belts, linear motion guides, and industrial lubrication products.
        </p>
        <div class="text-xs text-slate-400">
          <p><strong class="text-white">Trade Desk:</strong> Masjid Bunder, Mumbai – 400003</p>
        </div>
      </div>

      <!-- QUICK LINKS -->
      <div class="space-y-3">
        <h4 class="text-base font-bold text-white uppercase tracking-wider border-b border-slate-700 pb-2">Quick Links</h4>
        <ul class="space-y-2 text-xs text-slate-400">
          <li><a href="index.html" class="hover:text-primary-light flex items-center gap-2"><i class="fa-solid fa-angle-right text-primary text-[10px]"></i> Home</a></li>
          <li><a href="about-us.html" class="hover:text-primary-light flex items-center gap-2"><i class="fa-solid fa-angle-right text-primary text-[10px]"></i> About Company</a></li>
          <li><a href="products.html" class="hover:text-primary-light flex items-center gap-2"><i class="fa-solid fa-angle-right text-primary text-[10px]"></i> Products Catalog</a></li>
          <li><a href="industries.html" class="hover:text-primary-light flex items-center gap-2"><i class="fa-solid fa-angle-right text-primary text-[10px]"></i> Industries Served</a></li>
          <li><a href="brands.html" class="hover:text-primary-light flex items-center gap-2"><i class="fa-solid fa-angle-right text-primary text-[10px]"></i> Brands We Stock</a></li>
          <li><a href="contact-us.html" class="hover:text-primary-light flex items-center gap-2"><i class="fa-solid fa-angle-right text-primary text-[10px]"></i> Contact Us</a></li>
        </ul>
      </div>

      <!-- CORE PRODUCTS -->
      <div class="space-y-3">
        <h4 class="text-base font-bold text-white uppercase tracking-wider border-b border-slate-700 pb-2">Core Products</h4>
        <ul class="space-y-2 text-xs text-slate-400">
          <li><a href="ball-bearing.html" class="hover:text-primary-light flex items-center gap-2"><i class="fa-solid fa-angle-right text-primary text-[10px]"></i> Ball & Roller Bearings</a></li>
          <li><a href="timing-belts.html" class="hover:text-primary-light flex items-center gap-2"><i class="fa-solid fa-angle-right text-primary text-[10px]"></i> Timing Belts (Mitsuboshi / Conti)</a></li>
          <li><a href="conveyor-belts.html" class="hover:text-primary-light flex items-center gap-2"><i class="fa-solid fa-angle-right text-primary text-[10px]"></i> Heavy Conveyor Belting</a></li>
          <li><a href="linear-motion-bearing.html" class="hover:text-primary-light flex items-center gap-2"><i class="fa-solid fa-angle-right text-primary text-[10px]"></i> Linear Motion Guides</a></li>
          <li><a href="oil-grease.html" class="hover:text-primary-light flex items-center gap-2"><i class="fa-solid fa-angle-right text-primary text-[10px]"></i> Industrial Grease & Lubricants</a></li>
          <li><a href="seals-o-ring.html" class="hover:text-primary-light flex items-center gap-2"><i class="fa-solid fa-angle-right text-primary text-[10px]"></i> Oil Seals & O-Rings</a></li>
        </ul>
      </div>

      <!-- CONTACT INFO -->
      <div class="space-y-3">
        <h4 class="text-base font-bold text-white uppercase tracking-wider border-b border-slate-700 pb-2">Contact Trade Desk</h4>
        <div class="space-y-3 text-xs text-slate-400">
          <p class="flex items-start gap-2.5">
            <i class="fa-solid fa-location-dot text-primary mt-1"></i>
            <span>Flat No. 8, 261/63 Yusuf Meherali Road, Masjid Bunder, Mumbai – 400003, Maharashtra, India.</span>
          </p>
          <p class="flex items-center gap-2.5">
            <i class="fa-solid fa-envelope text-primary"></i>
            <span>info@belubeariexim.com</span>
          </p>
          <p class="flex items-center gap-2.5">
            <i class="fa-brands fa-whatsapp text-emerald-400 text-sm"></i>
            <span>WhatsApp RFQ Support Available</span>
          </p>
          <div class="pt-2">
            <a href="https://wa.me/919820000000?text=Hi%20Belubeari%20Exim" target="_blank" class="inline-flex items-center gap-2 bg-emerald-600 hover:bg-emerald-500 text-white px-4 py-2 rounded text-xs font-bold transition">
              <i class="fa-brands fa-whatsapp"></i> Chat On WhatsApp
            </a>
          </div>
        </div>
      </div>

    </div>

    <!-- COPYRIGHT -->
    <div class="max-w-7xl mx-auto px-4 mt-12 pt-6 border-t border-slate-800 text-center text-xs text-slate-500 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>© 2026 M/s Belubeari Exim. All rights reserved. Mumbai, India.</div>
      <div class="flex items-center gap-4">
        <span>Masjid Bunder Distribution Hub</span>
        <span>•</span>
        <a href="contact-us.html" class="hover:text-primary">Inquiry Support</a>
      </div>
    </div>
  </footer>

  <!-- FLOATING WHATSAPP -->
  <a href="https://wa.me/919820000000?text=Hello%20Belubeari%20Exim,%20I%20am%20enquiring%20about%20industrial%20parts" target="_blank" class="fixed bottom-6 right-6 z-50 w-14 h-14 bg-emerald-500 hover:bg-emerald-600 text-white rounded-full flex items-center justify-center text-3xl shadow-2xl transition hover:scale-110">
    <i class="fa-brands fa-whatsapp"></i>
  </a>

</body>
</html>
"""

# ==================== 1. GENERATE HOMEPAGE (index.html) ====================
def generate_homepage():
    products_cards_html = ""
    for p in product_definitions:
        products_cards_html += f"""
        <div class="animated-border-card flex flex-col">
          <div class="product-stage">
            <img src="assets/images/{p['image']}" alt="{p['title']} Belubeari Exim" loading="lazy">
            <span class="absolute top-3 left-3 bg-primary text-white text-[11px] font-bold px-2.5 py-0.5 rounded uppercase shadow-sm">Stockist</span>
          </div>
          <div class="p-5 flex-1 flex flex-col justify-between space-y-3 bg-white">
            <div>
              <h3 class="text-xl font-bold text-slate-900 group-hover:text-primary transition">{p['title']}</h3>
              <p class="text-xs text-slate-500 mt-2 line-clamp-3 leading-relaxed">{p['desc']}</p>
            </div>
            <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
              <a href="{p['slug']}.html" class="text-xs font-bold text-primary hover:text-primary-dark uppercase flex items-center gap-1">
                Read Details <i class="fa-solid fa-arrow-right text-[10px]"></i>
              </a>
              <a href="https://wa.me/919820000000?text=Hi%20Belubeari%20Exim,%20I%20need%20a%20quote%20for%20{p['title']}" target="_blank" class="text-emerald-600 hover:text-emerald-700 text-sm font-bold flex items-center gap-1">
                <i class="fa-brands fa-whatsapp"></i> Quote
              </a>
            </div>
          </div>
        </div>
        """

    industries_grid_html = ""
    for ind in industries_list:
        industries_grid_html += f"""
        <a href="{ind[1]}.html" class="animated-border-card group overflow-hidden block">
          <div class="industry-stage">
            <img src="assets/images/{ind[2]}" alt="{ind[0]} Belubeari Exim" loading="lazy">
          </div>
          <div class="p-4 text-center bg-white">
            <h4 class="text-sm font-bold text-slate-800 group-hover:text-primary transition">{ind[0]}</h4>
            <span class="text-[11px] text-slate-400 block mt-1">View Spares &rarr;</span>
          </div>
        </a>
        """

    brands_grid_html = """
    <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-5 gap-4">
      <div class="p-5 bg-white rounded-xl border border-slate-200 shadow-sm text-center font-bold text-slate-800 text-lg hover:border-primary transition">CONTINENTAL</div>
      <div class="p-5 bg-white rounded-xl border border-slate-200 shadow-sm text-center font-bold text-slate-800 text-lg hover:border-primary transition">MITSUBOSHI</div>
      <div class="p-5 bg-white rounded-xl border border-slate-200 shadow-sm text-center font-bold text-slate-800 text-lg hover:border-primary transition">GATES</div>
      <div class="p-5 bg-white rounded-xl border border-slate-200 shadow-sm text-center font-bold text-slate-800 text-lg hover:border-primary transition">SKF</div>
      <div class="p-5 bg-white rounded-xl border border-slate-200 shadow-sm text-center font-bold text-slate-800 text-lg hover:border-primary transition">FAG / INA</div>
      <div class="p-5 bg-white rounded-xl border border-slate-200 shadow-sm text-center font-bold text-slate-800 text-lg hover:border-primary transition">TIMKEN</div>
      <div class="p-5 bg-white rounded-xl border border-slate-200 shadow-sm text-center font-bold text-slate-800 text-lg hover:border-primary transition">FENNER</div>
      <div class="p-5 bg-white rounded-xl border border-slate-200 shadow-sm text-center font-bold text-slate-800 text-lg hover:border-primary transition">MEGADYNE</div>
      <div class="p-5 bg-white rounded-xl border border-slate-200 shadow-sm text-center font-bold text-slate-800 text-lg hover:border-primary transition">NACHI</div>
      <div class="p-5 bg-white rounded-xl border border-slate-200 shadow-sm text-center font-bold text-slate-800 text-lg hover:border-primary transition">IJK / NMB</div>
    </div>
    """

    body = f"""
    {get_header('home', 'Leading Importer & Stockist of Industrial Bearings & Belts')}

    <!-- HERO BANNER SECTION WITH AUTO-FIT BACKGROUND -->
    <section class="relative bg-slate-900 text-white py-20 lg:py-28 overflow-hidden min-h-[500px] flex items-center">
      <div class="absolute inset-0 opacity-30">
        <img src="assets/images/banner-3.png" alt="Industrial Transmission Warehouse" class="w-full h-full object-cover">
      </div>
      <div class="absolute inset-0 bg-gradient-to-r from-slate-950 via-slate-900/90 to-transparent"></div>

      <div class="max-w-7xl mx-auto px-4 relative z-10 grid grid-cols-1 lg:grid-cols-12 gap-10 items-center w-full">
        <div class="lg:col-span-8 space-y-6">
          <span class="inline-block px-3 py-1 bg-primary text-white text-xs font-bold uppercase tracking-widest rounded shadow">
            Masjid Bunder, Mumbai · B2B Sourcing Hub
          </span>
          <h1 class="text-3xl sm:text-5xl lg:text-6xl font-bold leading-tight uppercase">
            Industrial Bearings & <br><span class="text-primary-light">Power Transmission</span> Solutions
          </h1>
          <p class="text-slate-300 text-base sm:text-lg max-w-2xl leading-relaxed">
            M/s Belubeari Exim supplies world-class deep groove ball bearings, synchronous timing belts, heavy-duty conveyor belts, and precision linear guides with prompt dispatch across India.
          </p>
          <div class="flex flex-wrap items-center gap-4 pt-4">
            <a href="products.html" class="px-7 py-3.5 bg-primary hover:bg-primary-dark text-white font-bold text-sm uppercase rounded shadow-lg transition flex items-center gap-2">
              <i class="fa-solid fa-list-check"></i> Explore Products
            </a>
            <a href="contact-us.html" class="px-7 py-3.5 bg-white hover:bg-slate-100 text-slate-900 font-bold text-sm uppercase rounded shadow transition flex items-center gap-2">
              <i class="fa-solid fa-envelope"></i> Request Quotation
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- WELCOME / ABOUT SECTION -->
    <section class="py-16 bg-slate-50 border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-6 space-y-5">
          <span class="text-xs font-bold text-primary uppercase tracking-widest">ABOUT BELUBEARI EXIM</span>
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900">
            Welcome To M/s Belubeari Exim
          </h2>
          <p class="text-sm text-slate-600 leading-relaxed">
            Established in Mumbai, <strong>M/s Belubeari Exim</strong> is a recognized stockist and wholesale distributor specializing in premium industrial components. We supply top-tier manufacturing units, processing plants, textile mills, and engineering workshops with genuine specification-grade parts.
          </p>
          <p class="text-sm text-slate-600 leading-relaxed">
            Operating from Yusuf Meherali Road, Masjid Bunder, we maintain extensive inventory of timing belts, conveyor spares, precision bearings, and industrial lubricants to minimize machinery downtime for our clients.
          </p>
          <div class="grid grid-cols-2 gap-4 pt-2">
            <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-sm">
              <div class="text-2xl font-bold text-primary heading-font">100% GENUINE</div>
              <p class="text-xs text-slate-500 mt-1">Authorized Brand Profiles & Exact Part No. Matching</p>
            </div>
            <div class="p-4 bg-white rounded-xl border border-slate-200 shadow-sm">
              <div class="text-2xl font-bold text-primary heading-font">FAST DISPATCH</div>
              <p class="text-xs text-slate-500 mt-1">Ex-Stock Delivery from Mumbai Logistics Hub</p>
            </div>
          </div>
        </div>

        <div class="lg:col-span-6">
          <div class="animated-border-card detail-stage shadow-2xl">
            <img src="assets/images/Ball-Bearing.jpg" alt="Industrial Bearings Belubeari Exim">
          </div>
        </div>
      </div>
    </section>

    <!-- FEATURED PRODUCTS SHOWCASE -->
    <section class="py-16 bg-white border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 space-y-10">
        <div class="text-center max-w-2xl mx-auto">
          <span class="text-xs font-bold text-primary uppercase tracking-widest">OUR CATALOG</span>
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 mt-1">Featured Industrial Products</h2>
          <p class="text-sm text-slate-500 mt-2">Comprehensive range of power transmission belts, bearings, and machinery spares with high-precision animated stages.</p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          {products_cards_html}
        </div>
      </div>
    </section>

    <!-- WHY CHOOSE US -->
    <section class="py-16 bg-corp-900 text-white border-b border-slate-800">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-center max-w-2xl mx-auto mb-12">
          <span class="text-xs font-bold text-primary-light uppercase tracking-widest">WHY BELUBEARI EXIM</span>
          <h2 class="text-3xl sm:text-4xl font-bold text-white mt-1">The Preferred Sourcing Partner</h2>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="p-6 bg-slate-800/80 rounded-xl border border-slate-700 space-y-3">
            <i class="fa-solid fa-boxes-stacked text-primary-light text-3xl"></i>
            <h4 class="text-lg font-bold text-white">Extensive Stock</h4>
            <p class="text-xs text-slate-400 leading-relaxed">Large ex-stock availability of standard and hard-to-find bearing and belt sizes.</p>
          </div>
          <div class="p-6 bg-slate-800/80 rounded-xl border border-slate-700 space-y-3">
            <i class="fa-solid fa-award text-primary-light text-3xl"></i>
            <h4 class="text-lg font-bold text-white">Quality Assurance</h4>
            <p class="text-xs text-slate-400 leading-relaxed">ISO 9001 and international standards compliant components for maximum operational life.</p>
          </div>
          <div class="p-6 bg-slate-800/80 rounded-xl border border-slate-700 space-y-3">
            <i class="fa-solid fa-tags text-primary-light text-3xl"></i>
            <h4 class="text-lg font-bold text-white">Wholesale Pricing</h4>
            <p class="text-xs text-slate-400 leading-relaxed">Direct trade discounts for bulk B2B purchases, engineering OEMs, and maintenance teams.</p>
          </div>
          <div class="p-6 bg-slate-800/80 rounded-xl border border-slate-700 space-y-3">
            <i class="fa-solid fa-truck-fast text-primary-light text-3xl"></i>
            <h4 class="text-lg font-bold text-white">Pan-India Supply</h4>
            <p class="text-xs text-slate-400 leading-relaxed">Fast logistics dispatch from Mumbai commercial trade center to every state in India.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 21+ INDUSTRIES SERVED -->
    <section class="py-16 bg-slate-50 border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 space-y-10">
        <div class="text-center max-w-2xl mx-auto">
          <span class="text-xs font-bold text-primary uppercase tracking-widest">SECTOR EXPERTISE</span>
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 mt-1">Industries We Serve</h2>
          <p class="text-sm text-slate-500 mt-2">Delivering specialized mechanical components across 20+ major industrial verticals.</p>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4">
          {industries_grid_html}
        </div>
      </div>
    </section>

    <!-- BRANDS SECTION -->
    <section class="py-16 bg-white border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 space-y-8">
        <div class="text-center max-w-2xl mx-auto">
          <span class="text-xs font-bold text-primary uppercase tracking-widest">AUTHORIZED BRANDS</span>
          <h2 class="text-3xl sm:text-4xl font-bold text-slate-900 mt-1">Major Brands We Stock & Supply</h2>
        </div>
        {brands_grid_html}
      </div>
    </section>

    <!-- DIRECT RFQ CALLOUT -->
    <section class="py-12 bg-primary text-white">
      <div class="max-w-7xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-6 text-center md:text-left">
        <div>
          <h3 class="text-2xl sm:text-3xl font-bold uppercase">Need Immediate Quotation For Bearings Or Belts?</h3>
          <p class="text-sm text-sky-100 mt-1">Send us your part number or bill of materials for prompt wholesale quotation.</p>
        </div>
        <div class="flex items-center gap-4">
          <a href="contact-us.html" class="px-6 py-3 bg-white text-slate-900 hover:bg-slate-100 font-bold text-sm uppercase rounded shadow transition">
            Contact Trade Desk
          </a>
          <a href="https://wa.me/919820000000?text=Hi%20Belubeari%20Exim,%20I%20need%20a%20quotation" target="_blank" class="px-6 py-3 bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-sm uppercase rounded shadow transition flex items-center gap-2">
            <i class="fa-brands fa-whatsapp"></i> WhatsApp Quote
          </a>
        </div>
      </div>
    </section>

    {get_footer()}
    """
    with open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(body)

# ==================== 2. GENERATE DEDICATED PRODUCT PAGES ====================
def generate_product_pages():
    for p in product_definitions:
        specs_rows = "".join([f"""
          <tr class="border-b border-slate-200">
            <td class="py-3 px-4 font-bold text-slate-900 bg-slate-50 w-1/3">{spec[0]}</td>
            <td class="py-3 px-4 text-slate-700">{spec[1]}</td>
          </tr>
        """ for spec in p['specs']])

        sidebar_links = "".join([f"""
          <a href="{other['slug']}.html" class="block px-4 py-2.5 text-xs font-semibold {'bg-primary text-white rounded' if other['slug']==p['slug'] else 'text-slate-700 hover:bg-slate-100 rounded'} transition">
            {other['title']}
          </a>
        """ for other in product_definitions])

        body = f"""
        {get_header('products', f"{p['title']} Suppliers & Stockist")}

        <!-- BREADCRUMB HEADER -->
        <div class="bg-slate-100 border-b border-slate-200 py-6">
          <div class="max-w-7xl mx-auto px-4 flex flex-wrap items-center justify-between gap-4">
            <div>
              <div class="text-xs text-slate-500 font-medium">
                <a href="index.html" class="hover:text-primary">Home</a> / <a href="products.html" class="hover:text-primary">Products</a> / <span class="text-primary font-bold">{p['title']}</span>
              </div>
              <h1 class="text-3xl font-bold text-slate-900 mt-1">{p['title']}</h1>
            </div>
            <a href="contact-us.html" class="bg-primary hover:bg-primary-dark text-white px-5 py-2.5 rounded font-bold text-xs uppercase shadow transition">
              Request RFQ
            </a>
          </div>
        </div>

        <!-- MAIN PRODUCT DETAIL -->
        <div class="max-w-7xl mx-auto px-4 py-12 grid grid-cols-1 lg:grid-cols-12 gap-10">
          
          <!-- LEFT CONTENT -->
          <div class="lg:col-span-8 space-y-8">
            
            <!-- IMAGE & MAIN SUMMARY WITH MOVING BORDER BEAM -->
            <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
              <div class="animated-border-card detail-stage">
                <img src="assets/images/{p['image']}" alt="{p['title']} M/s Belubeari Exim">
              </div>
              <div class="p-6 space-y-4">
                <h2 class="text-2xl font-bold text-slate-900">{p['title']} Solutions</h2>
                <p class="text-sm text-slate-600 leading-relaxed">{p['desc']}</p>
                <p class="text-sm text-slate-600 leading-relaxed">
                  M/s Belubeari Exim is an authorized stockist and importer of {p['title']} based in Masjid Bunder, Mumbai. We provide dimensional interchangeability verification, bulk wholesale rates, and fast dispatch across India.
                </p>
              </div>
            </div>

            <!-- TECHNICAL SPECIFICATIONS TABLE -->
            <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-4">
              <h3 class="text-xl font-bold text-slate-900">Technical Specifications & Standards</h3>
              <div class="overflow-x-auto">
                <table class="w-full text-xs text-left border-collapse">
                  <tbody>
                    {specs_rows}
                  </tbody>
                </table>
              </div>
            </div>

            <!-- SOURCING CTA -->
            <div class="bg-sky-50 border border-sky-200 rounded-2xl p-6 flex flex-col sm:flex-row items-center justify-between gap-4">
              <div>
                <h4 class="text-lg font-bold text-slate-900">Looking for a specific {p['title']} size or part number?</h4>
                <p class="text-xs text-slate-600 mt-1">Share your part number with our Mumbai trade desk for instant availability and pricing.</p>
              </div>
              <a href="https://wa.me/919820000000?text=Hi%20Belubeari%20Exim,%20I%20need%20a%20quotation%20for%20{p['title']}" target="_blank" class="px-5 py-3 bg-emerald-600 hover:bg-emerald-500 text-white rounded font-bold text-xs uppercase flex items-center gap-2 whitespace-nowrap shadow transition">
                <i class="fa-brands fa-whatsapp text-base"></i> WhatsApp RFQ
              </a>
            </div>

          </div>

          <!-- RIGHT SIDEBAR -->
          <div class="lg:col-span-4 space-y-6">
            
            <!-- CATEGORIES MENU -->
            <div class="bg-white rounded-xl border border-slate-200 shadow-sm p-5 space-y-3">
              <h4 class="text-base font-bold text-slate-900 border-b border-slate-200 pb-2">All Products</h4>
              <div class="space-y-1">
                {sidebar_links}
              </div>
            </div>

            <!-- TRADE DESK CARD -->
            <div class="bg-corp-900 text-white rounded-xl p-6 space-y-4">
              <h4 class="text-base font-bold text-primary-light">Trade & Sourcing Desk</h4>
              <p class="text-xs text-slate-300 leading-relaxed">
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

# ==================== 3. GENERATE DEDICATED INDUSTRY PAGES ====================
def generate_industry_pages():
    for ind in industries_list:
        sidebar_ind_links = "".join([f"""
          <a href="{other[1]}.html" class="block px-4 py-2.5 text-xs font-semibold {'bg-primary text-white rounded' if other[1]==ind[1] else 'text-slate-700 hover:bg-slate-100 rounded'} transition">
            {other[0]}
          </a>
        """ for other in industries_list])

        body = f"""
        {get_header('industries', f"{ind[0]} Components & Spares")}

        <!-- BREADCRUMB HEADER -->
        <div class="bg-slate-100 border-b border-slate-200 py-6">
          <div class="max-w-7xl mx-auto px-4 flex flex-wrap items-center justify-between gap-4">
            <div>
              <div class="text-xs text-slate-500 font-medium">
                <a href="index.html" class="hover:text-primary">Home</a> / <a href="industries.html" class="hover:text-primary">Industries</a> / <span class="text-primary font-bold">{ind[0]}</span>
              </div>
              <h1 class="text-3xl font-bold text-slate-900 mt-1">{ind[0]} Solutions</h1>
            </div>
            <a href="contact-us.html" class="bg-primary hover:bg-primary-dark text-white px-5 py-2.5 rounded font-bold text-xs uppercase shadow transition">
              Get Industrial Quote
            </a>
          </div>
        </div>

        <!-- MAIN INDUSTRY CONTENT -->
        <div class="max-w-7xl mx-auto px-4 py-12 grid grid-cols-1 lg:grid-cols-12 gap-10">
          
          <div class="lg:col-span-8 space-y-8">
            <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
              <div class="animated-border-card industry-detail-stage">
                <img src="assets/images/{ind[2]}" alt="{ind[0]} Belubeari Exim">
              </div>
              <div class="p-6 space-y-4">
                <h2 class="text-2xl font-bold text-slate-900">Mechanical Spares & Bearings for {ind[0]}</h2>
                <p class="text-sm text-slate-600 leading-relaxed">{ind[3]}</p>
                <p class="text-sm text-slate-600 leading-relaxed">
                  M/s Belubeari Exim supports industrial plants in the {ind[0]} sector with durable power transmission belts, heavy spherical bearings, high-temperature lubrication greases, and custom conveyor components engineered to withstand continuous operation.
                </p>
              </div>
            </div>

            <!-- RECOMMENDED PARTS SECTION -->
            <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-6 space-y-4">
              <h3 class="text-xl font-bold text-slate-900">Key Recommended Components for {ind[0]}</h3>
              <ul class="space-y-3 text-xs text-slate-700">
                <li class="flex items-start gap-3 p-3 bg-slate-50 rounded-lg border border-slate-200">
                  <i class="fa-solid fa-check text-primary mt-0.5"></i>
                  <div><strong>Heavy Duty Industrial Bearings:</strong> Spherical, tapered roller, and deep groove bearings designed for severe radial and axial shock loads.</div>
                </li>
                <li class="flex items-start gap-3 p-3 bg-slate-50 rounded-lg border border-slate-200">
                  <i class="fa-solid fa-check text-primary mt-0.5"></i>
                  <div><strong>Synchronous Timing & Transmission Belts:</strong> High-torque metric belts for positive zero-slip drive systems.</div>
                </li>
                <li class="flex items-start gap-3 p-3 bg-slate-50 rounded-lg border border-slate-200">
                  <i class="fa-solid fa-check text-primary mt-0.5"></i>
                  <div><strong>High-Performance Industrial Lubricants:</strong> Extreme temperature greases ensuring maximum operating life of bearings and gears.</div>
                </li>
              </ul>
            </div>

            <!-- RFQ BANNER -->
            <div class="bg-sky-50 border border-sky-200 rounded-2xl p-6 flex flex-col sm:flex-row items-center justify-between gap-4">
              <div>
                <h4 class="text-lg font-bold text-slate-900">Need Spares for your {ind[0]} Facility?</h4>
                <p class="text-xs text-slate-600 mt-1">Get fast technical specification matching and wholesale quotation directly on WhatsApp.</p>
              </div>
              <a href="https://wa.me/919820000000?text=Hi%20Belubeari%20Exim,%20I%20am%20enquiring%20about%20spares%20for%20{ind[0]}" target="_blank" class="px-5 py-3 bg-emerald-600 hover:bg-emerald-500 text-white rounded font-bold text-xs uppercase flex items-center gap-2 whitespace-nowrap shadow transition">
                <i class="fa-brands fa-whatsapp text-base"></i> WhatsApp RFQ
              </a>
            </div>

          </div>

          <!-- RIGHT SIDEBAR -->
          <div class="lg:col-span-4 space-y-6">
            <div class="bg-white rounded-xl border border-slate-200 shadow-sm p-5 space-y-3">
              <h4 class="text-base font-bold text-slate-900 border-b border-slate-200 pb-2">All Industries</h4>
              <div class="space-y-1 max-h-96 overflow-y-auto">
                {sidebar_ind_links}
              </div>
            </div>

            <div class="bg-corp-900 text-white rounded-xl p-6 space-y-4">
              <h4 class="text-base font-bold text-primary-light">Mumbai Trade Location</h4>
              <p class="text-xs text-slate-300 leading-relaxed">
                Flat No. 8, Yusuf Meherali Road, Masjid Bunder, Mumbai – 400003.
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
        with open(os.path.join(out_dir, f"{ind[1]}.html"), 'w', encoding='utf-8') as f:
            f.write(body)

# ==================== 4. GENERATE ABOUT-US, CONTACT-US, PRODUCTS & BRANDS ====================
def generate_standard_pages():
    # ABOUT US
    about_body = f"""
    {get_header('about', 'About Us - M/s Belubeari Exim')}
    <div class="bg-slate-100 border-b border-slate-200 py-6">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-xs text-slate-500 font-medium"><a href="index.html" class="hover:text-primary">Home</a> / <span class="text-primary font-bold">About Us</span></div>
        <h1 class="text-3xl font-bold text-slate-900 mt-1">About M/s Belubeari Exim</h1>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 py-12 space-y-12">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-10 items-center">
        <div class="lg:col-span-7 space-y-5">
          <span class="text-xs font-bold text-primary uppercase tracking-widest">COMPANY PROFILE</span>
          <h2 class="text-3xl font-bold text-slate-900">Your Trusted Industrial Transmission Partner</h2>
          <p class="text-sm text-slate-600 leading-relaxed">
            <strong>M/s Belubeari Exim</strong> is a leading stockist, trader, and distributor of high-precision industrial components located in Mumbai, India. We specialize in bearings, power transmission belts, linear motion technology, and lubrication systems for major industrial plants.
          </p>
          <p class="text-sm text-slate-600 leading-relaxed">
            Headquartered at Yusuf Meherali Road, Masjid Bunder, Mumbai, we serve engineering OEMs, cement plants, textile mills, steel industries, and maintenance professionals with rapid dispatch and verified genuine components.
          </p>
          <div class="grid grid-cols-2 gap-4 pt-4">
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-lg">
              <h4 class="font-bold text-slate-900 text-sm">Specification-Led</h4>
              <p class="text-xs text-slate-500 mt-1">Exact part number, pitch, and dimensional fitment.</p>
            </div>
            <div class="p-4 bg-slate-50 border border-slate-200 rounded-lg">
              <h4 class="font-bold text-slate-900 text-sm">Masjid Bunder Hub</h4>
              <p class="text-xs text-slate-500 mt-1">Core logistics and trade distribution network.</p>
            </div>
          </div>
        </div>
        <div class="lg:col-span-5">
          <div class="animated-border-card detail-stage shadow-xl">
            <img src="assets/images/Ball-Bearing.jpg" alt="About Belubeari Exim">
          </div>
        </div>
      </div>
    </div>
    {get_footer()}
    """
    with open(os.path.join(out_dir, 'about-us.html'), 'w', encoding='utf-8') as f:
        f.write(about_body)

    # CONTACT US
    contact_body = f"""
    {get_header('contact', 'Contact Us - M/s Belubeari Exim Mumbai')}
    <div class="bg-slate-100 border-b border-slate-200 py-6">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-xs text-slate-500 font-medium"><a href="index.html" class="hover:text-primary">Home</a> / <span class="text-primary font-bold">Contact Us</span></div>
        <h1 class="text-3xl font-bold text-slate-900 mt-1">Contact M/s Belubeari Exim</h1>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 py-12 grid grid-cols-1 lg:grid-cols-12 gap-10">
      <div class="lg:col-span-5 space-y-6">
        <div>
          <span class="text-xs font-bold text-primary uppercase tracking-widest">GET IN TOUCH</span>
          <h2 class="text-2xl font-bold text-slate-900 mt-1">Trade Desk & Registered Office</h2>
        </div>
        <div class="space-y-4 text-xs">
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
            <div class="font-bold text-slate-900 text-sm flex items-center gap-2"><i class="fa-solid fa-building text-primary"></i> Registered Business Address</div>
            <div class="text-slate-600">Flat No. 8, 261/63 Yusuf Meherali Road, Masjid Bunder, Mumbai – 400003, Maharashtra, India.</div>
          </div>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
            <div class="font-bold text-slate-900 text-sm flex items-center gap-2"><i class="fa-brands fa-whatsapp text-emerald-600"></i> WhatsApp RFQ Desk</div>
            <div class="text-slate-600">Fast Technical Specification & Part Matching</div>
          </div>
          <div class="p-4 bg-slate-50 border border-slate-200 rounded-xl space-y-1">
            <div class="font-bold text-slate-900 text-sm flex items-center gap-2"><i class="fa-solid fa-clock text-primary"></i> Working Hours</div>
            <div class="text-slate-600">Monday – Saturday : 10:00 AM – 7:30 PM</div>
          </div>
        </div>
      </div>

      <div class="lg:col-span-7">
        <div class="bg-white rounded-2xl border border-slate-200 shadow-md p-6 space-y-4">
          <h3 class="text-xl font-bold text-slate-900">Send Direct Purchase Enquiry</h3>
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

    # PRODUCTS INDEX PAGE
    products_cards_html = "".join([f"""
    <div class="animated-border-card flex flex-col">
      <div class="product-stage">
        <img src="assets/images/{p['image']}" alt="{p['title']} Belubeari Exim" loading="lazy">
      </div>
      <div class="p-5 flex-1 flex flex-col justify-between space-y-3 bg-white">
        <div>
          <h3 class="text-xl font-bold text-slate-900 group-hover:text-primary transition">{p['title']}</h3>
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

    products_body = f"""
    {get_header('products', 'All Industrial Products Catalog')}
    <div class="bg-slate-100 border-b border-slate-200 py-6">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-xs text-slate-500 font-medium"><a href="index.html" class="hover:text-primary">Home</a> / <span class="text-primary font-bold">Products</span></div>
        <h1 class="text-3xl font-bold text-slate-900 mt-1">Industrial Products Catalog</h1>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 py-12">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {products_cards_html}
      </div>
    </div>
    {get_footer()}
    """
    with open(os.path.join(out_dir, 'products.html'), 'w', encoding='utf-8') as f:
        f.write(products_body)

    # INDUSTRIES INDEX PAGE
    industries_cards_html = "".join([f"""
    <div class="animated-border-card flex flex-col">
      <div class="industry-stage">
        <img src="assets/images/{ind[2]}" alt="{ind[0]} Belubeari Exim" loading="lazy">
      </div>
      <div class="p-5 flex-1 flex flex-col justify-between space-y-3 bg-white">
        <div>
          <h3 class="text-lg font-bold text-slate-900 group-hover:text-primary transition">{ind[0]}</h3>
          <p class="text-xs text-slate-500 mt-2 line-clamp-3 leading-relaxed">{ind[3]}</p>
        </div>
        <div class="pt-3 border-t border-slate-100">
          <a href="{ind[1]}.html" class="text-xs font-bold text-primary hover:text-primary-dark uppercase flex items-center gap-1">
            Explore Application Spares <i class="fa-solid fa-arrow-right text-[10px]"></i>
          </a>
        </div>
      </div>
    </div>
    """ for ind in industries_list])

    industries_body = f"""
    {get_header('industries', 'Industries We Serve - 20+ Sectors')}
    <div class="bg-slate-100 border-b border-slate-200 py-6">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-xs text-slate-500 font-medium"><a href="index.html" class="hover:text-primary">Home</a> / <span class="text-primary font-bold">Industries</span></div>
        <h1 class="text-3xl font-bold text-slate-900 mt-1">Industries We Serve</h1>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 py-12">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
        {industries_cards_html}
      </div>
    </div>
    {get_footer()}
    """
    with open(os.path.join(out_dir, 'industries.html'), 'w', encoding='utf-8') as f:
        f.write(industries_body)

    # BRANDS PAGE
    brands_body = f"""
    {get_header('brands', 'Authorized Sourced Brands')}
    <div class="bg-slate-100 border-b border-slate-200 py-6">
      <div class="max-w-7xl mx-auto px-4">
        <div class="text-xs text-slate-500 font-medium"><a href="index.html" class="hover:text-primary">Home</a> / <span class="text-primary font-bold">Brands</span></div>
        <h1 class="text-3xl font-bold text-slate-900 mt-1">Brands We Stock & Supply</h1>
      </div>
    </div>
    <div class="max-w-7xl mx-auto px-4 py-12 space-y-8">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div class="p-6 bg-white rounded-xl border border-slate-200 shadow-sm space-y-2 hover:border-primary transition">
          <h3 class="text-xl font-bold text-slate-900">CONTINENTAL CONTITECH</h3>
          <p class="text-xs text-slate-500">Heavy duty industrial timing belts, multi-rib belts, and synchronous drive systems.</p>
        </div>
        <div class="p-6 bg-white rounded-xl border border-slate-200 shadow-sm space-y-2 hover:border-primary transition">
          <h3 class="text-xl font-bold text-slate-900">MITSUBOSHI</h3>
          <p class="text-xs text-slate-500">Japanese high-torque transmission belts, automotive belts, and polyurethane belts.</p>
        </div>
        <div class="p-6 bg-white rounded-xl border border-slate-200 shadow-sm space-y-2 hover:border-primary transition">
          <h3 class="text-xl font-bold text-slate-900">GATES</h3>
          <p class="text-xs text-slate-500">Poly Chain GT Carbon belts, classical wrapped V-belts, and industrial hydraulic hoses.</p>
        </div>
        <div class="p-6 bg-white rounded-xl border border-slate-200 shadow-sm space-y-2 hover:border-primary transition">
          <h3 class="text-xl font-bold text-slate-900">SKF</h3>
          <p class="text-xs text-slate-500">Global benchmark precision ball bearings, spherical roller bearings, and bearing greases.</p>
        </div>
        <div class="p-6 bg-white rounded-xl border border-slate-200 shadow-sm space-y-2 hover:border-primary transition">
          <h3 class="text-xl font-bold text-slate-900">FAG / INA</h3>
          <p class="text-xs text-slate-500">German engineered spherical, cylindrical, and needle roller bearings.</p>
        </div>
        <div class="p-6 bg-white rounded-xl border border-slate-200 shadow-sm space-y-2 hover:border-primary transition">
          <h3 class="text-xl font-bold text-slate-900">TIMKEN</h3>
          <p class="text-xs text-slate-500">Ultra heavy duty tapered roller bearings and mounted bearing pillow block units.</p>
        </div>
      </div>
    </div>
    {get_footer()}
    """
    with open(os.path.join(out_dir, 'brands.html'), 'w', encoding='utf-8') as f:
        f.write(brands_body)

# Run all generators
generate_homepage()
generate_product_pages()
generate_industry_pages()
generate_standard_pages()

print('Successfully regenerated all 54 pages with animated moving border beams and glowing shadows!')

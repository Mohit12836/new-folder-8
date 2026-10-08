import json
import os
import re

out_dir = r'd:\codee\Ms Belubeari Exim\New folder (8)'
img_dir = os.path.join(out_dir, 'assets', 'images')
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

with open('scraped_products.json', 'r', encoding='utf-8') as f:
    scraped_products = json.load(f)

# Complete 12 Product Definitions
PRODUCTS_LIST = [
    {
        'slug': 'ball-bearing',
        'title': 'Ball Bearing',
        'subtitle': 'High Precision Industrial Bearings',
        'primary_img': 'Ball-Bearing.jpg',
        'gallery': ['Ball-Bearing.jpg', 'ball-bearings.jpg', 'various-ball-bearings-scaled-1.jpeg', 'ball-bearing-blog.jpg', 'roller-bearing-shaft.jpg'],
        'desc': 'At Belubeari Exim Industrial Solutions, we offer a comprehensive selection of high-precision ball bearings and roller assemblies engineered for demanding rotational speeds, heavy radial and thrust loads, and prolonged operational life in industrial machinery.',
        'features': [
            ('Durability', 'Manufactured from high-grade chromium steel (GCr15) to withstand heavy loads, high speeds, and continuous industrial operation.'),
            ('Versatility', 'Available in deep groove, angular contact, spherical, and thrust configurations for diverse machinery applications.'),
            ('Precision', 'Produced to tight international tolerances (P0, P6, P5 / ABEC-1 to ABEC-5) for smooth, low-vibration running.'),
            ('Customization', 'Supplied in standard and custom bore sizes with rubber contact seals (2RS), metal shields (ZZ), or high-temp clearance (C3/C4).')
        ],
        'specs': [
            ('Type', 'Deep Groove Ball Bearings, Angular Contact, Thrust, Self-Aligning'),
            ('Material', 'High Carbon Chromium Steel (GCr15) / AISI 440C Stainless Steel'),
            ('Precision Grade', 'ISO Normal (P0), P6 (ABEC-3), P5 (ABEC-5)'),
            ('Internal Clearance', 'C2, CN (Normal), C3, C4, C5'),
            ('Operating Temp', '-30°C to +150°C (Special high-temp up to +300°C)'),
            ('Authorized Brands', 'SKF, FAG, NACHI, TIMKEN, IJK, NMB (Minebea)')
        ]
    },
    {
        'slug': 'timing-belts',
        'title': 'Timing Belts',
        'subtitle': 'Synchronous Power Transmission Drives',
        'primary_img': 'Belt.jpg',
        'gallery': ['Belt.jpg', 'timing-belt-blue-pu.jpg', 'timing-belt-h-pitch.jpg', 'timing-belt-5m-paz.jpg', 'timing-belt-pu-double.jpg'],
        'desc': 'At Belubeari Exim Industrial Solutions, we supply industrial synchronous timing belts engineered for positive, slip-free power transmission. Available in rubber and polyurethane with high-tensile steel, fiberglass, or aramid cords, our timing belts deliver exact synchronization and high torque capacity.',
        'features': [
            ('Durability', 'High-tensile cords prevent stretching and withstand high cyclic stresses, heavy shock loads, and continuous high-speed rotation.'),
            ('Versatility', 'Covering metric (HTD 3M, 5M, 8M, 14M, STD S8M, T5, T10, AT5, AT10) and imperial pitches (MXL, XL, L, H, XH).'),
            ('Precision', 'Curvilinear and trapezoidal tooth profiles molded to exact pitch tolerances for quiet, backlash-free meshing.'),
            ('Customization', 'Available in endless spliced, truly endless, open-ended rolls, and specialized backing coatings (PU, Linatex, APL).')
        ],
        'specs': [
            ('Pitch Profiles', 'HTD (3M, 5M, 8M, 14M), STD (S8M, S14M), T2.5, T5, T10, AT5, AT10'),
            ('Imperial Pitches', 'MXL (0.080"), XL (0.200"), L (0.375"), H (0.500"), XH (0.875")'),
            ('Tension Member', 'Helically wound Fiberglass Cords / High Tensile Steel Wire / Kevlar Aramid'),
            ('Body Material', 'Neoprene / HNBR Synthetic Rubber / Cast Thermoplastic Polyurethane (PU)'),
            ('Tooth Facing', 'High-wear Polyamide (PAZ/PAR) Low-Friction Fabric'),
            ('Authorized Brands', 'Continental ContiTech, Gates, Mitsuboshi, Fenner, Megadyne')
        ]
    },
    {
        'slug': 'conveyor-belts',
        'title': 'Conveyor Belts',
        'subtitle': 'Heavy-Duty & Food-Grade Conveyor Solutions',
        'primary_img': 'Belt2.jpg',
        'gallery': ['Belt2.jpg', 'conveyor-belt-types.jpg', 'Flat-Belt-Conveyor.jpg', 'Inclined-Belt-Conveyor.jpg', 'Curved-Belt-Conveyor.jpg', 'Cleated-Belt-Conveyor.webp', 'Portable-Belt-Conveyor.webp'],
        'desc': 'At Belubeari Exim Industrial Solutions, we provide high-performance conveyor belting solutions for bulk material handling, automated manufacturing, food processing, packaging, and parcel logistics across India.',
        'features': [
            ('Durability', 'High-strength multi-ply polyester-nylon (EP) carcass designed for extreme impact resistance and high tensile strength.'),
            ('Versatility', 'Suitable for flat horizontal transport, steep inclined conveying (chevron / cleats), curved runs, and bucket elevators.'),
            ('Precision', 'Calibrated uniform thickness and straight-running tracking properties to prevent edge fraying and conveyor drift.'),
            ('Customization', 'Customized longitudinal cleats, sidewalls, guide tracking ropes (V-guides), perforations, and vulcanized endless splicing.')
        ],
        'specs': [
            ('Carcass Plies', 'EP 100, EP 150, EP 200, EP 250, EP 300, EP 400 (2-ply to 6-ply)'),
            ('Belt Types', 'Smooth Flat, Chevron / Rough Top, Cleated Sidewall, White Food Grade PU/PVC'),
            ('Cover Grades', 'General Purpose (M-24, N-17), Heat Resistant (HR/SHR), Oil Resistant (OR), Fire Resistant (FR)'),
            ('Operating Temp', '-20°C to +80°C (Heat Resistant up to +180°C)'),
            ('Thickness Range', '1.0 mm to 25 mm custom specifications'),
            ('Standards', 'DIN 22102, IS 1891, ISO 14890, FDA / USDA Food Grade Approved')
        ]
    },
    {
        'slug': 'v-belts',
        'title': 'V-Belts',
        'subtitle': 'Industrial Friction Power Transmission Belts',
        'primary_img': 'v-belt-red-round.jpg',
        'gallery': ['v-belt-red-round.jpg', 'IMG-20260903-WA0014.jpg', 'IMG-20260903-WA0015.jpg', 'belts.jpg'],
        'desc': 'At Belubeari Exim Industrial Solutions, we stock a vast inventory of classical, space-saver narrow wedge, and raw edge cogged V-belts engineered for optimal power transmission across industrial fans, blowers, crushers, and pumps.',
        'features': [
            ('Durability', 'Specially compounded synthetic rubber core with high-modulus polyester tension cords providing maximum resistance to fatigue and elongation.'),
            ('Versatility', 'Broad portfolio including Classical Wrapped, Wedge Narrow, Cogged Raw Edge, Multi-Ribbed Poly-V, and Banded Belts.'),
            ('Precision', 'Precision match-set tolerances ensure equal load sharing on multi-groove pulley systems without vibration.'),
            ('Customization', 'Supplied in matched length sets, oil and heat resistant grades (ISO 1813 anti-static certified).')
        ],
        'specs': [
            ('Classical Sections', 'A, B, C, D, E (Standard Industrial Wrapped)'),
            ('Narrow Wedge Sections', 'SPZ, SPA, SPB, SPC / 3V, 5V, 8V (High Power Density)'),
            ('Raw Edge Cogged', 'AX, BX, CX, XPZ, XPA, XPB, XPC (High Flexibility & Speed)'),
            ('Multi-Rib Poly-V', 'PH, PJ, PK, PL, PM (Multiple Rib Profiles)'),
            ('Construction', 'Polyester Tension Cord, Polybutadiene / EPDM Rubber Core, Fabric Wrapped Cover'),
            ('Authorized Brands', 'Fenner, Continental, Mitsuboshi, Gates, Bando')
        ]
    },
    {
        'slug': 'flat-belts',
        'title': 'Flat Belts',
        'subtitle': 'High-Speed Transmission & Processing Belts',
        'primary_img': 'flat-belt-blue-backed.jpg',
        'gallery': ['flat-belt-blue-backed.jpg', 'flat-belt-green-pvc.jpg', 'Belt2.jpg'],
        'desc': 'At Belubeari Exim Industrial Solutions, we provide premium flat power transmission and processing belts designed for high-speed drives, textile spinning, carding, printing presses, and folder-gluer machinery.',
        'features': [
            ('Durability', 'Extremely high tensile strength polyamide foil or polyester fabric core capable of handling high peripheral speeds up to 60 m/s.'),
            ('Versatility', 'Equipped with elastomer, synthetic rubber, or chrome leather friction layers on single or both driving sides.'),
            ('Precision', 'Uniform thickness and smooth endless splice guarantee vibration-free, silent machine operation.'),
            ('Customization', 'Custom cut to exact width, length, and spliced endless or open with specialized mechanical fasteners.')
        ],
        'specs': [
            ('Tension Layer', 'High Elastic Modulus Polyamide (PA) Sheet / Polyester Fabric / Aramid'),
            ('Friction Surfaces', 'NBR Synthetic Nitrile Rubber / Chrome Split Leather / Polyurethane'),
            ('Operating Speeds', 'Up to 60 m/s with minimal centrifugal belt stretch'),
            ('Thickness Range', '0.8 mm to 6.0 mm depending on pulley diameter'),
            ('Belt Types', 'Tangential Drive, Spindle Tape, Double-Sided Rubber, Folder Gluer Belts'),
            ('Authorized Brands', 'Nitta, Habasit, Forbo Siegling, Chiorino, Megadyne')
        ]
    },
    {
        'slug': 'linear-motion-bearing',
        'title': 'Linear Motion Bearing',
        'subtitle': 'Precision Linear Guides & Ball Bushing Systems',
        'primary_img': '3a2d4baf2d014f96bda2bf5f141e7cdc.jpg',
        'gallery': ['3a2d4baf2d014f96bda2bf5f141e7cdc.jpg', 'linear-motion-bearing.jpeg', 'images-1.jpg', 'images-2.jpg', 'images-3.jpg', 'images.jpg'],
        'desc': 'At Belubeari Exim Industrial Solutions, we offer a complete range of linear motion guide rails, ball screw carriages, and linear bushing bearings that deliver smooth, micrometer-precise positioning for automation, CNC machine tools, and robotics.',
        'features': [
            ('Durability', 'High-grade alloy steel guide tracks and induction-hardened raceways guarantee long service life under high shock loads.'),
            ('Versatility', 'Available in caged ball, caged roller, miniature LM guides, round shaft ball bushings, and flanged carriage blocks.'),
            ('Precision', 'Available in Normal (N), High (H), and Precision (P) accuracy classes with preloaded clearances for backlash-free travel.'),
            ('Customization', 'Custom cut rail lengths, end-seal wipers, double scraper plates, and corrosion-resistant Raydent coatings.')
        ],
        'specs': [
            ('Rail Sizes', '15, 20, 25, 30, 35, 45, 55, 65 (Standard & Wide Rail Types)'),
            ('Block Configurations', 'Flanged (HGW/MSA), Square (HGH/MSB), Low Profile (EGH/MSB-S)'),
            ('Accuracy Grades', 'Normal (C/N), High (H), Precision (P), Super Precision (SP)'),
            ('Preload Classes', 'Normal Clearance (Z0), Light Preload (Z1), Medium Preload (ZA)'),
            ('Max Travel Speed', 'Up to 5 m/s with acceleration up to 50 m/s²'),
            ('Authorized Brands', 'THK, HIWIN, NSK, IKO, PMI, Bosch Rexroth')
        ]
    },
    {
        'slug': 'pillow-block-bearing',
        'title': 'Pillow Block Bearing',
        'subtitle': 'Mounted Cast Iron & Stainless Steel Bearing Units',
        'primary_img': 'SAF-Split-pillow-block-bearing-assembly-optimized-1200px-cropped-.jpg',
        'gallery': ['SAF-Split-pillow-block-bearing-assembly-optimized-1200px-cropped-.jpg', 'Pillow-Block-Bearing.jpg', 'images-4.jpg'],
        'desc': 'At Belubeari Exim Industrial Solutions, we stock a vast line of mounted pillow block units and plummer block housings designed for easy shaft mounting, self-alignment, and dependable operation in bulk conveying, agricultural, and industrial processing machinery.',
        'features': [
            ('Durability', 'Rigid one-piece cast iron (HT200), ductile iron, or stainless steel housing with spherical insert bearing absorbs shaft misalignments.'),
            ('Versatility', 'Housing formats include Pillow Block (UCP), 4-Bolt Square Flange (UCF), 2-Bolt Oval Flange (UCFL), Take-up Units (UCT), and Cartridge (UCC).'),
            ('Precision', 'Spherical outer ring insert bearing ground to precision tolerances with re-lubrication grease nipple fitting.'),
            ('Customization', 'Available with Set Screw lock, Eccentric Locking Collar, or Tapered Adapter Sleeve (UKP/SAF series).')
        ],
        'specs': [
            ('Shaft Bore Sizes', '12 mm to 140 mm (Metric) / 1/2" to 4" (Imperial)'),
            ('Housing Series', 'UCP (High Base Pillow), UCF (4-Bolt Flange), UCFL (2-Bolt Flange), UCT (Take-Up), SN/SAF/SNG Plummer Blocks'),
            ('Housing Materials', 'Cast Iron (FC200), Ductile Iron (FCD450), Cast Stainless Steel (SUS304/316), Thermoplastic PBT'),
            ('Sealing Options', 'Standard Rubber Contact Seal with Metal Slinger / Triple Lip L3 Seal for Heavy Dust'),
            ('Insert Bearings', 'UC200, UC300, UK200, UK300, SA200, SB200, HC200 Series'),
            ('Authorized Brands', 'FYH, ASAHI, SKF, FAG, NTN, NSK, FK')
        ]
    },
    {
        'slug': 'oil-grease',
        'title': 'Oil & Grease',
        'subtitle': 'Reliable Lubrication Solutions',
        'primary_img': 'Industrial-grease.jpg',
        'gallery': ['Industrial-grease.jpg', 'Hydraulic-oil.jpg', 'Industrial-oils-and-greases.jpg', 'Industrial-gear-oil.jpg', 'Cutting-oil.jpg', 'Lubricant-drums.jpg'],
        'desc': 'At Belubeari Exim Industrial Solutions, we understand that proper lubrication is essential to keep your machinery running smoothly and efficiently. That’s why we offer a comprehensive selection of high-quality industrial oils and greases to meet the diverse needs of your equipment and operations.',
        'features': [
            ('Durability', 'Formulated to withstand extreme temperatures, heavy loads and harsh industrial conditions.'),
            ('Versatility', 'Suitable for a wide range of applications across various heavy manufacturing and processing industries.'),
            ('Precision', 'Manufactured to strict quality standards and kinematic viscosity tolerances for consistent, reliable performance.'),
            ('Customization', 'Ability to supply the exact NLGI grade, base oil chemistry, and packaging size tailored to your requirements.')
        ],
        'specs': [
            ('Grease Thickeners', 'Lithium Complex, Polyurea, Calcium Sulfonate, Clay / Bentonite, Aluminum Complex, PTFE'),
            ('NLGI Consistency', 'NLGI 000, 00, 0, 1, 2, 3 (Semi-fluid to Heavy Grease)'),
            ('Industrial Oils', 'Hydraulic Oils (ISO VG 32, 46, 68), Industrial Gear Oils (ISO VG 150, 220, 320, 460), Compressor Oils, Cutting Fluids'),
            ('Operating Temp', '-50°C to +280°C (Extreme Temperature Specialty Formulations)'),
            ('Special Properties', 'EP Extreme Pressure, Anti-Wear (AW), High Water Washout Resistance, Rust & Oxidation Inhibited'),
            ('Authorized Brands', 'Kluber Lubrication, Shell, THK Grease, Mobil, Castrol, Fuchs, OKS')
        ]
    },
    {
        'slug': 'seals-o-ring',
        'title': 'Seals & O Ring',
        'subtitle': 'High-Performance Sealing Solutions',
        'primary_img': 'Seals-O-Ring.jpg',
        'gallery': ['Seals-O-Ring.jpg', 'orings.jpg', 'rubber-gaskets.jpg', 'static-seal_0011.jpg', 'O-Ring-Feature.jpg', 'O-ringen.jpg'],
        'desc': 'At Belubeari Exim Industrial Solutions, we understand the critical importance of reliable sealing solutions in your machinery and equipment. That’s why we offer a comprehensive selection of high-quality rotary shaft seals, hydraulic packing, and precision O-rings to meet the diverse needs of your industrial applications.',
        'features': [
            ('Durability', 'Manufactured using high-grade polymers and fluorocarbon elastomers to withstand aggressive fluids, extreme pressures, and thermal stresses.'),
            ('Versatility', 'Suitable for static sealing (O-rings, gaskets, flat washers) and dynamic applications (rotary oil seals, reciprocating hydraulic rods).'),
            ('Precision', 'Molded to strict international dimensional standards (AS568, ISO 3601, DIN 3760) with zero flash lines and exact tolerances.'),
            ('Customization', 'Available in standard metric/imperial sizes, custom molded profiles, and food-grade / chemical-resistant compounds.')
        ],
        'specs': [
            ('Elastomer Materials', 'NBR (Nitrile 70/90 Shore A), FKM/FPM (Viton®), EPDM, VMQ Silicone, HNBR, PTFE Teflon®'),
            ('Oil Seal Profiles', 'TC (Double Lip Spring Loaded), SC (Single Lip), TB, SB, VC, VB, Cassette Heavy Duty Hub Seals'),
            ('Hydraulic Packing', 'Piston U-Cups, Rod Seals, Wiper Scrapers, Guide Wear Rings, Chevron V-Packing Sets'),
            ('Operating Pressures', 'Static up to 400 bar / Dynamic up to 250 bar (with anti-extrusion back-up rings)'),
            ('Temperature Range', '-50°C (Silicone) up to +220°C (Viton® FKM)'),
            ('Authorized Brands', 'Parker, NOK, Corteco, SKF Seals, Busak+Shamban, Trelleborg')
        ]
    },
    {
        'slug': 'cots-apron',
        'title': 'Cots & Apron',
        'subtitle': 'Precision Textile Drafting Components',
        'primary_img': 'IMG-20260903-WA0023.jpg',
        'gallery': ['IMG-20260903-WA0023.jpg', '6.jpg', '5.jpg', '4.jpg'],
        'desc': 'At Belubeari Exim Industrial Solutions, we supply high-precision rubber cots and synthetic aprons engineered for ring spinning, roving, and draw frame textile machinery, ensuring uniform yarn tension, minimal end-breaks, and superior yarn quality.',
        'features': [
            ('Durability', 'Formulated from high-resilience synthetic rubber compounds to resist abrasion, chemical finishes, and fiber lap-ups.'),
            ('Versatility', 'Engineered for cotton, synthetic, wool, and blended yarn processing across compact and conventional drafting systems.'),
            ('Precision', 'Uniform inner grip and seamless vulcanization deliver consistent drafting control and optimal yarn CV% and IPI values.'),
            ('Customization', 'Available in shore hardness ratings from 65° to 85° Shore A in standard and custom inner/outer diameters.')
        ],
        'specs': [
            ('Hardness Range', '65° Shore A (Soft), 70° Shore A, 75° Shore A, 83° Shore A (Hard)'),
            ('Component Types', 'Bottom & Top Aprons (Dimpled / Smooth Knurled), Ring Spinning Cots, Texturizing Cots'),
            ('Layer Construction', 'Seamless Knurled Inner Layer with Anti-Static Conductive Intermediate Layer and High-Grip Outer Cover'),
            ('Textile Machinery', 'Rieter, Lakshmi Machine Works (LMW), Zinser, Toyoda, Marzoli, KTTM'),
            ('Operating Life', 'Over 12,000 to 18,000 running hours without surface grooving'),
            ('Authorized Brands', 'Inarco, Armstrong, Accotex, Yamauchi, Daytex')
        ]
    },
    {
        'slug': 'rubber-emery-roller-covering',
        'title': 'Rubber Emery/Roller Covering',
        'subtitle': 'Rubber Emery/Roller Covering for Textile Industry',
        'primary_img': '6.jpg',
        'gallery': ['6.jpg', '5.jpg', '4.jpg', '3.jpg', '5-1.jpg', '6-1.jpg'],
        'desc': 'At Belubeari Exim Industrial Solutions, we offer high-quality Rubber Emery and Roller Covering products specifically designed for the textile, paper, and film processing industries. Our products provide superior friction grip, abrasion resistance, and smooth web guidance without damaging delicate fabric.',
        'features': [
            ('High Durability', 'Our rubber emery and roller coverings are crafted from premium elastomer compounds to withstand heavy continuous tension and chemical exposure.'),
            ('Enhanced Performance', 'Engineered to provide positive non-slip grip, prevent fabric distortion, and maintain smooth tension across loom take-up rollers.'),
            ('Custom Solutions', 'Available in various surface textures (Dimpled, Grooved, Sanded Emery, Smooth Silicone, Cork-Rubber blends) in custom strip widths.'),
            ('Compliance', 'Manufactured to strict industrial standards with uniform thickness and strong self-adhesive or vulcanized backing.')
        ],
        'specs': [
            ('Surface Finishes', 'Fine Emery Sanded, Coarse Emery, Dimpled / Pimpled Rubber, Synthetic Rubber Cork, Silicone Heat-Resistant'),
            ('Roll Widths', '50 mm, 75 mm, 100 mm (Standard rolls 50 meters or 100 meters)'),
            ('Backing Types', 'Heavy Cotton Duck Fabric Backing / Self-Adhesive Backed / Plain Vulcanized Rubber'),
            ('Applications', 'Loom Take-Up Rollers, Fabric Inspection Machines, Sizing Machines, Film Slitting, Paper Guidance'),
            ('Friction Coefficient', 'High-friction non-marking surface engineered for synthetic and cotton fabrics'),
            ('Authorized Brands', 'Scapa, Bobotex, Nitta, Belubeari Exim Custom Covered')
        ]
    },
    {
        'slug': 'special-coated-belts',
        'title': 'Special Coated Belts',
        'subtitle': 'Application-Specific Coated Belts',
        'primary_img': 'special-coated-studded.jpg',
        'gallery': ['special-coated-studded.jpg', 'special-coated-red-pmu.jpg', 'special-coated-sponge.jpg'],
        'desc': 'At Belubeari Exim Industrial Solutions, we supply specialized coated timing and flat belts engineered for specific handling needs. With coatings such as red PMU, sponge foam, silicone, polyurethane, and studded profiles, these belts provide enhanced cushioning, high friction, and product protection for automated packaging, cable pulling, and glass transport lines.',
        'features': [
            ('Durability', 'Directly vulcanized or thermally bonded coatings resist delamination, tearing, and high cyclic flexure under heavy loads.'),
            ('Versatility', 'Customizable for vacuum pulling (with CNC milled slots and holes), glass processing, carton hauling, and sensitive product feeding.'),
            ('Precision', 'Ground to uniform coating thickness across the entire belt length to prevent unequal product clamping pressure.'),
            ('Customization', 'Choice of over 20+ coating materials in thicknesses from 1 mm to 15 mm with specialized CNC milled profiles.')
        ],
        'specs': [
            ('Base Belt Types', 'Timing Belts (HTD 8M, T10, AT10, H), Flat Belts, Poly-V Belts'),
            ('Coating Materials', 'Red Linatex® Natural Rubber, Supergrip Rubber, White Food Grade PU, Sylomer Foam, Porol Sponge, Heat Resistant Silicone'),
            ('Coating Thickness', '2.0 mm, 3.0 mm, 4.0 mm, 6.0 mm, 8.0 mm, 10.0 mm (Custom Ground)'),
            ('Secondary Machining', 'Longitudinal Grooves, Transverse Slots, Vacuum Holes, Profile Cleats'),
            ('Applications', 'Vertical Form-Fill-Seal (VFFS) Packaging, Cable Extrusion Pullers, Glass Edge Grinding, Tile Conveying'),
            ('Authorized Brands', 'Megadyne, Continental, Gates, Esband, Belubeari Exim Custom Fabricated')
        ]
    }
]

# 5 Core Application Industries with images
APPLICATIONS_DATA = [
    ('Automotive & Heavy Equipment', 'Lubricating and powering engines, gears, suspension, and high-load transmission systems for smooth, continuous operation.', 'Automotive-Industry.jpg'),
    ('Chemical & Process Plants', 'Providing reliable components engineered to withstand severe corrosion, high pressures, and chemical solvents.', 'Chemical-Industry.jpeg'),
    ('Food & Beverage Processing', 'FDA-approved, non-toxic, clean components meeting the most stringent sanitary and hygiene standards.', 'Food-Industry.jpg'),
    ('Hydropower & Energy Sector', 'Powering and protecting hydro turbines, heavy generators, bearing assemblies, and high-pressure hydraulic loops.', 'Hydropower-Industry.jpg'),
    ('Pharmaceutical Manufacturing', 'Delivering ultra-clean, contamination-free, ISO-certified precision components for cleanroom operations.', 'Pharmaceutical-Industry.jpg')
]

# Shared Header & Footer
from generate_all_industry_pages import HEAD_CONTENT, HEADER_HTML, FOOTER_HTML

# Generate all 12 individual product pages
for prod in PRODUCTS_LIST:
    slug = prod['slug']
    title = prod['title']
    subtitle = prod['subtitle']
    primary_img = get_disk_img(prod['primary_img'])
    desc = prod['desc']
    
    # Gallery HTML
    gallery_html = ""
    for g_img in prod['gallery']:
        real_g = get_disk_img(g_img)
        gallery_html += f"""
        <div class="gallery-thumb-item bg-white p-2 rounded-lg border border-slate-200 shadow-sm hover:border-[#0284c7] transition glow-hover group cursor-pointer">
          <div class="w-full h-24 bg-slate-50 rounded overflow-hidden flex items-center justify-center">
            <img src="assets/images/{real_g}" alt="{title} Variant" class="max-h-full max-w-full object-contain group-hover:scale-110 transition duration-300">
          </div>
        </div>
        """

    # Features HTML (4 cards)
    features_html = ""
    for idx, (f_title, f_desc) in enumerate(prod['features']):
        stagger_cls = f"stagger-{idx + 1}"
        features_html += f"""
        <div class="tilt-card spotlight-card reveal-init {stagger_cls} bg-white p-5 rounded-xl border border-slate-200 shadow-sm glow-hover flex flex-col justify-between">
          <div>
            <div class="w-10 h-10 rounded-lg bg-sky-50 text-[#0284c7] flex items-center justify-center text-lg mb-3 border border-sky-100 shadow-sm">
              <i class="fa-solid fa-circle-check"></i>
            </div>
            <h4 class="font-heading font-bold text-base text-slate-900 uppercase mb-1.5">{f_title}</h4>
            <p class="text-xs text-slate-600 leading-relaxed font-sans">{f_desc}</p>
          </div>
        </div>
        """

    # Applications HTML (5 cards)
    apps_html = ""
    for idx, (app_name, app_desc, app_img) in enumerate(APPLICATIONS_DATA):
        real_app_img = get_disk_img(app_img)
        stagger_cls = f"stagger-{idx + 1}"
        apps_html += f"""
        <div class="tilt-card spotlight-card reveal-init {stagger_cls} bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden glow-hover flex flex-col group">
          <div class="h-36 w-full bg-slate-100 overflow-hidden relative">
            <img src="assets/images/{real_app_img}" alt="{app_name}" class="w-full h-full object-cover group-hover:scale-110 transition duration-400">
            <div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent"></div>
            <span class="absolute bottom-2 left-3 text-white font-heading font-bold text-xs uppercase drop-shadow">{app_name}</span>
          </div>
          <div class="p-4 flex-1 flex flex-col justify-between">
            <p class="text-xs text-slate-600 leading-relaxed font-sans">{app_desc}</p>
            <div class="mt-3 pt-2 border-t border-slate-100 flex items-center justify-between text-[10px] font-bold text-[#0284c7] uppercase">
              <span>Standard Fit</span>
              <i class="fa-solid fa-arrow-right"></i>
            </div>
          </div>
        </div>
        """

    # Specs Table Rows HTML
    specs_rows_html = ""
    for k, v in prod['specs']:
        specs_rows_html += f"""
        <tr class="border-b border-slate-100 last:border-0 hover:bg-sky-50/50 transition">
          <td class="py-3 px-4 font-bold text-slate-900 bg-slate-50/80 w-1/3 font-heading uppercase text-xs">{k}</td>
          <td class="py-3 px-4 text-slate-700 font-sans text-xs">{v}</td>
        </tr>
        """

    # Sidebar products list with active indicator
    sidebar_prod_links = ""
    for other in PRODUCTS_LIST:
        is_active = (other['slug'] == slug)
        if is_active:
            sidebar_prod_links += f"""
            <li class="bg-sky-50 border-l-4 border-[#0284c7] font-bold text-[#0284c7] rounded-r py-2.5 px-3.5 flex justify-between items-center text-xs shadow-sm">
              <span><i class="fa-solid fa-angle-right mr-2 text-[#0284c7]"></i> {other['title']}</span>
              <span class="text-[10px] bg-[#0284c7] text-white px-2 py-0.5 rounded font-sans uppercase">Active</span>
            </li>
            """
        else:
            sidebar_prod_links += f"""
            <li class="border-b border-slate-100 last:border-0">
              <a href="{other['slug']}.html" class="py-2.5 px-3.5 block text-slate-700 hover:bg-sky-50 hover:text-[#0284c7] hover:pl-5 transition duration-150 text-xs flex justify-between items-center font-medium">
                <span><i class="fa-solid fa-angle-right mr-2 text-slate-400"></i> {other['title']}</span>
                <i class="fa-solid fa-chevron-right text-[9px] text-slate-300"></i>
              </a>
            </li>
            """

    page_html = HEAD_CONTENT.replace('{PAGE_TITLE}', f"{title} - Industrial Solutions").replace(
        '{META_DESC}', f"{title} - {subtitle}. Authorized stockist and distributor in Masjid Bunder, Mumbai. Certified genuine products with fast dispatch."
    )
    page_html += HEADER_HTML

    # Page Content
    page_html += f"""
    <!-- Page Hero Banner -->
    <section class="bg-gradient-to-r from-slate-950 via-slate-900 to-sky-950 text-white py-12 lg:py-16 relative border-b border-sky-900/40">
      <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#38bdf8_1px,transparent_1px)] [background-size:16px_16px]"></div>
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div>
            <span class="inline-flex items-center gap-1.5 text-sky-400 text-xs font-bold uppercase tracking-widest bg-sky-950/80 border border-sky-800/60 px-3 py-1 rounded-full mb-3">
              <i class="fa-solid fa-cube"></i> Certified Industrial Line
            </span>
            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-heading font-black tracking-tight text-white uppercase">
              {title}
            </h1>
          </div>
          <!-- Breadcrumb -->
          <nav class="flex items-center text-xs font-sans text-slate-300 bg-slate-900/80 px-4 py-2 rounded-lg border border-slate-800">
            <a href="index.html" class="hover:text-sky-400 transition"><i class="fa-solid fa-house mr-1"></i> Home</a>
            <span class="mx-2 text-slate-600">/</span>
            <a href="products.html" class="hover:text-sky-400 transition">Products</a>
            <span class="mx-2 text-slate-600">/</span>
            <span class="text-sky-400 font-semibold">{title}</span>
          </nav>
        </div>
      </div>
    </section>

    <!-- Main Content Layout (70% Left / 30% Sticky Sidebar) -->
    <section class="py-12 lg:py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 lg:gap-12">
          
          <!-- LEFT / MAIN CONTENT (8 Cols) -->
          <div class="lg:col-span-8 space-y-10">
            
            <!-- Featured Stage Image & Variant Showcase -->
            <div class="border-beam-card glow-hover shadow-xl p-4 bg-white space-y-4">
              <div class="hero-stage !h-[340px] bg-gradient-to-b from-white to-slate-50 border border-slate-100 rounded-lg p-4">
                <img src="assets/images/{primary_img}" alt="{title} Belubeari Exim Mumbai" class="!object-contain drop-shadow-md" loading="eager">
              </div>
              
              <!-- Gallery Grid -->
              <div>
                <span class="text-[11px] font-bold uppercase tracking-wider text-slate-500 block mb-2 font-heading">Available Variants & Profiles:</span>
                <div class="grid grid-cols-3 sm:grid-cols-6 gap-2.5">
                  {gallery_html}
                </div>
              </div>
            </div>

            <!-- Section 1: Overview & Reliable Solutions -->
            <div class="reveal-init bg-white rounded-xl p-6 sm:p-8 shadow-sm border border-slate-200/80">
              <h2 class="text-2xl sm:text-3xl font-heading font-bold text-slate-900 uppercase tracking-tight">
                {subtitle}
              </h2>
              <div class="section-divider-bar">
                <div class="bar-left"></div>
                <div class="bar-mid"></div>
                <div class="bar-right"></div>
              </div>
              <p class="text-slate-600 text-sm sm:text-base leading-relaxed mt-4 font-sans">
                {desc}
              </p>
              
              <div class="mt-6 grid grid-cols-2 sm:grid-cols-4 gap-3 pt-6 border-t border-slate-100">
                <div class="bg-slate-50 p-3 rounded-lg text-center border border-slate-100">
                  <span class="block text-sky-600 font-heading font-bold text-xl">100%</span>
                  <span class="text-[11px] text-slate-500 font-medium">Genuine Stock</span>
                </div>
                <div class="bg-slate-50 p-3 rounded-lg text-center border border-slate-100">
                  <span class="block text-sky-600 font-heading font-bold text-xl">24/7</span>
                  <span class="text-[11px] text-slate-500 font-medium">Dispatch Desk</span>
                </div>
                <div class="bg-slate-50 p-3 rounded-lg text-center border border-slate-100">
                  <span class="block text-sky-600 font-heading font-bold text-xl">Custom</span>
                  <span class="text-[11px] text-slate-500 font-medium">Sizes Available</span>
                </div>
                <div class="bg-slate-50 p-3 rounded-lg text-center border border-slate-100">
                  <span class="block text-sky-600 font-heading font-bold text-xl">ISO</span>
                  <span class="text-[11px] text-slate-500 font-medium">Quality Certified</span>
                </div>
              </div>
            </div>

            <!-- Section 2: Key Features (4-Grid) -->
            <div class="reveal-init">
              <div class="mb-5">
                <h3 class="text-2xl sm:text-3xl font-heading font-bold text-slate-900 uppercase tracking-tight">
                  Key Features
                </h3>
                <div class="section-divider-bar">
                  <div class="bar-left"></div>
                  <div class="bar-mid"></div>
                  <div class="bar-right"></div>
                </div>
                <p class="text-slate-500 text-xs sm:text-sm font-sans">Engineered for extreme reliability, maximum torque capacity, and reduced maintenance overhead.</p>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                {features_html}
              </div>
            </div>

            <!-- Section 3: Applications Across Industries (5-Grid) -->
            <div class="reveal-init">
              <div class="mb-5">
                <h3 class="text-2xl sm:text-3xl font-heading font-bold text-slate-900 uppercase tracking-tight">
                  Applications
                </h3>
                <div class="section-divider-bar">
                  <div class="bar-left"></div>
                  <div class="bar-mid"></div>
                  <div class="bar-right"></div>
                </div>
                <p class="text-slate-500 text-xs sm:text-sm font-sans">Our {title} components are deployed across core industrial plants nationwide.</p>
              </div>

              <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {apps_html}
              </div>
            </div>

            <!-- Section 4: Technical Specifications Table -->
            <div class="reveal-init bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
              <div class="bg-[#111111] text-white p-4 border-b border-slate-800 flex justify-between items-center">
                <div>
                  <h4 class="font-heading font-bold text-base uppercase tracking-wider text-white">Technical Specifications & Standards</h4>
                  <span class="text-[10px] text-sky-400 uppercase tracking-widest font-semibold block mt-0.5">Engineering Data Sheet</span>
                </div>
                <i class="fa-solid fa-list-check text-sky-400"></i>
              </div>
              <div class="overflow-x-auto">
                <table class="w-full text-left border-collapse">
                  <tbody>
                    {specs_rows_html}
                  </tbody>
                </table>
              </div>
            </div>

            <!-- Section 5: Direct Action Callout -->
            <div class="reveal-init bg-gradient-to-br from-slate-900 to-sky-950 rounded-2xl p-8 text-white relative overflow-hidden shadow-xl border border-sky-800/40">
              <div class="relative z-10 flex flex-col md:flex-row items-center justify-between gap-6">
                <div>
                  <span class="text-sky-400 text-xs font-bold uppercase tracking-widest font-heading mb-1 block">Have a specific part number or drawing?</span>
                  <h3 class="text-xl sm:text-2xl font-heading font-bold text-white uppercase">
                    Connect with our technical trade desk in Masjid Bunder, Mumbai
                  </h3>
                  <p class="text-xs text-slate-300 mt-2 font-sans">We stock over 15,000+ SKUs with same-day Mumbai warehouse dispatch and pan-India shipping.</p>
                </div>
                <div class="flex flex-wrap gap-3 whitespace-nowrap">
                  <a href="tel:+919321469698" class="btn-shimmer btn-magnetic bg-[#0284c7] hover:bg-sky-500 text-white text-xs font-heading font-bold uppercase tracking-wider px-5 py-3 rounded-lg shadow transition">
                    <i class="fa-solid fa-phone mr-1.5"></i> Call Now
                  </a>
                  <a href="https://wa.me/919321469698?text=Hello%20Belubeari%20Exim,%20I%20need%20a%20quote%20for%20{title.replace(' ', '%20')}." class="btn-shimmer btn-magnetic bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-heading font-bold uppercase tracking-wider px-5 py-3 rounded-lg shadow transition flex items-center gap-1.5">
                    <i class="fa-brands fa-whatsapp"></i> WhatsApp Quote
                  </a>
                </div>
              </div>
            </div>

          </div>

          <!-- RIGHT / STICKY SIDEBAR (4 Cols) -->
          <div class="lg:col-span-4 space-y-8">
            
            <!-- Widget 1: All Products Menu List -->
            <div class="reveal-init bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden sticky top-24">
              <div class="bg-[#111111] text-white p-4 border-b border-slate-800 flex justify-between items-center">
                <div>
                  <h4 class="font-heading font-bold text-base uppercase tracking-wider text-white">Our Products</h4>
                  <span class="text-[10px] text-sky-400 uppercase tracking-widest font-semibold block mt-0.5">12 Core Product Lines</span>
                </div>
                <i class="fa-solid fa-boxes-stacked text-sky-400"></i>
              </div>
              <ul class="divide-y divide-slate-100 max-h-[460px] overflow-y-auto">
                {sidebar_prod_links}
              </ul>

              <!-- Widget 2: Enquiry Now Form inside sidebar -->
              <div class="p-6 bg-slate-50 border-t border-slate-200">
                <div class="flex items-center gap-2 mb-3">
                  <i class="fa-solid fa-paper-plane text-[#0284c7]"></i>
                  <h4 class="font-heading font-bold text-base text-slate-900 uppercase">Enquiry Now</h4>
                </div>
                <p class="text-xs text-slate-500 mb-4 font-sans">Request technical catalog & wholesale price list for {title}.</p>
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
                  <button type="submit" class="btn-shimmer btn-magnetic w-full bg-[#0284c7] hover:bg-sky-700 text-white text-xs font-heading font-bold uppercase tracking-wider py-2.5 rounded shadow transition">
                    Send Instant Inquiry
                  </button>
                </form>
              </div>

              <!-- Widget 3: Direct Trade Desk -->
              <div class="p-6 bg-gradient-to-br from-[#111111] to-slate-900 text-white border-t border-slate-800 text-center">
                <div class="w-12 h-12 rounded-full bg-sky-600/30 text-sky-400 flex items-center justify-center mx-auto mb-3 text-xl border border-sky-500/30">
                  <i class="fa-solid fa-phone-volume"></i>
                </div>
                <h5 class="font-heading font-bold text-sm uppercase tracking-wide text-white">Direct Trade Desk</h5>
                <p class="text-xs text-slate-400 mt-1 mb-3 font-sans">Speak directly with our senior bearing & belt specialist:</p>
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

    with open(os.path.join(out_dir, f"{slug}.html"), 'w', encoding='utf-8') as f_out:
        f_out.write(page_html)

print("Successfully generated all 12 individual product pages with exact gallery, features, applications, and sidebar!")

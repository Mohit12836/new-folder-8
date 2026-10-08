import glob

files = glob.glob('*.html')
print(f"Updating emails and preloader tagline across {len(files)} files...")

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Replace any sales@belubeariexim.com with belubeariexim@gmail.com
    content = content.replace('sales@belubeariexim.com', 'belubeariexim@gmail.com')
    
    # 2. Clean up any duplicate mailto links if they were side-by-side
    content = content.replace(
        '<a href="mailto:belubeariexim@gmail.com" class="hover:text-white font-medium">belubeariexim@gmail.com</a><br><a href="mailto:belubeariexim@gmail.com" class="hover:text-white text-slate-400">belubeariexim@gmail.com</a>',
        '<a href="mailto:belubeariexim@gmail.com" class="hover:text-white font-medium text-sky-400">belubeariexim@gmail.com</a>'
    )
    content = content.replace(
        '<a href="mailto:belubeariexim@gmail.com" class="hover:text-white font-medium">belubeariexim@gmail.com</a><br>\n                <a href="mailto:belubeariexim@gmail.com" class="hover:text-white text-slate-400">belubeariexim@gmail.com</a>',
        '<a href="mailto:belubeariexim@gmail.com" class="hover:text-white font-medium text-sky-400">belubeariexim@gmail.com</a>'
    )
    
    # 3. Update Preloader Tagline to match official logo text: "BELT • LUBRICANT • AUR • BEARING"
    content = content.replace(
        'BEARINGS • BELTS • INDUSTRIAL SOLUTIONS',
        'BELT • LUBRICANT • AUR • BEARING'
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("All files updated successfully!")

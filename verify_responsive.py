import glob
html_files = glob.glob('*.html')
html_files = [f for f in html_files if f != 'enhance_animations.html']

print('=== RESPONSIVE.CSS LINKED ===')
for f in sorted(html_files):
    with open(f, 'r', encoding='utf-8') as fh:
        c = fh.read()
    linked = 'responsive.css' in c
    viewport = 'viewport' in c
    print(('OK' if linked else 'MISSING') + '  ' + ('VP' if viewport else '--') + '  ' + f)

print()
print('=== RESPONSIVE.CSS SIZE ===')
with open('responsive.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(str(len(lines)) + ' lines, ' + str(sum(len(l) for l in lines)) + ' chars')

print()
print('=== KEY BREAKPOINTS IN responsive.css ===')
with open('responsive.css', 'r', encoding='utf-8') as f:
    css = f.read()
import re
bps = re.findall(r'@media[^{]+', css)
for bp in bps:
    print(' ', bp.strip())

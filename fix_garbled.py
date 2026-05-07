#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the garbled section
start_marker = '<!-- AYURVEDIC TREATMENTS -->'
end_marker = '</section>\n<!-- '  # Just before the WHY CHOOSE US comment

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print(f'ERROR: Could not find markers. start={start_idx}, end={end_idx}')
    exit(1)

# end_idx points to </section>\n<!-- so we need to advance past </section>
# Find the actual </section> that closes the ayur-treatments section
# We need to find the </section> that comes after start_idx
section_end = content.find('</section>', start_idx)
if section_end == -1:
    print('ERROR: Could not find closing </section>')
    exit(1)
# Move past </section>\n
section_end = section_end + len('</section>') + 1  # +1 for newline

print(f'Found garbled section from {start_idx} to {section_end}')

# Replacement content
replacement = '''<!-- NATURE IMAGE SEPARATOR — between treatments carousel and why-us -->
<div style="width:100%;height:420px;overflow:hidden;position:relative;z-index:5;line-height:0">
  <img src="nature.jpg" alt="Nature — Shanthi Wellness" style="width:100%;height:100%;object-fit:cover;object-position:center;display:block"/>
  <div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(255,255,255,0.18) 0%,transparent 30%,transparent 70%,rgba(255,255,255,0.18) 100%);pointer-events:none"></div>
</div>

<!-- =•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•
     WHY CHOOSE US'''

# Replace
new_content = content[:start_idx] + replacement + '\n' + content[section_end:]

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('✓ Replaced garbled section with nature.jpg separator')
print(f'  Removed {section_end - start_idx} characters')
print(f'  Added {len(replacement)} characters')

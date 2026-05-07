#!/usr/bin/env python
# -*- coding: utf-8 -*-

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all <!-- ORANGE DIVIDER --> with nature.jpg image separator
nature_separator = '''<!-- NATURE IMAGE SEPARATOR -->
<div style="width:100%;height:320px;overflow:hidden;position:relative;z-index:5;line-height:0">
  <img src="nature.jpg" alt="" style="width:100%;height:100%;object-fit:cover;object-position:center;display:block"/>
  <div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(255,255,255,0.20) 0%,transparent 25%,transparent 75%,rgba(255,255,255,0.20) 100%);pointer-events:none"></div>
</div>'''

old_divider = '<!-- ORANGE DIVIDER -->\n<div class="orange-divider"></div>'
count = content.count(old_divider)
print(f'Found {count} orange dividers')

new_content = content.replace(old_divider, nature_separator)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Replaced {count} orange dividers with nature.jpg separators')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Remove all NATURE IMAGE SEPARATOR blocks
# Pattern: comment + div block (with nested div)
pattern = r'<!-- NATURE IMAGE SEPARATOR[^>]*-->\n<div[^>]*>\n  <img[^/]*/>\n  <div[^>]*></div>\n</div>\n'

matches = re.findall(pattern, content)
print(f'Found {len(matches)} separator blocks')

new_content = re.sub(pattern, '', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Removed all remaining nature.jpg separators')

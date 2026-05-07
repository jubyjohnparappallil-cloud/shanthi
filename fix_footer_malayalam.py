#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fix the garbled Malayalam text in the footer India branch section.
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# The garbled sequences need to be decoded: they are UTF-8 bytes read as Latin-1
# then re-encoded as UTF-8. We fix by encoding as Latin-1 then decoding as UTF-8.

def fix_garbled(text):
    """Fix double-encoded UTF-8 text."""
    try:
        return text.encode('latin-1').decode('utf-8')
    except Exception:
        return text

# Find the India branch footer block
india_start = content.find('<li><strong>\u00e0\u00b4\u00ae')
if india_start == -1:
    # Try another approach - find the garbled strong tag
    india_start = content.find('India Branch</h5>')
    if india_start == -1:
        print('ERROR: Could not find India Branch section')
        exit(1)
    # Find the first <li> after it
    li_start = content.find('<li><strong>', india_start)
    print(f'li_start: {li_start}')
    print('garbled text:', repr(content[li_start:li_start+200]))
else:
    li_start = india_start

# Extract the garbled name
name_start = content.find('<li><strong>', content.find('India Branch</h5>'))
name_end = content.find('</strong></li>', name_start) + len('</strong></li>')
garbled_name = content[name_start + len('<li><strong>'):name_end - len('</strong></li>')]
print('Garbled name:', repr(garbled_name))

# Fix it
try:
    fixed_name = garbled_name.encode('latin-1').decode('utf-8')
    print('Fixed name:', fixed_name)
except Exception as e:
    print('Error fixing name:', e)
    fixed_name = 'വയലാരിക്കത്ത് ആയുർവേദ വെൽനസ് & നഴ്സിംഗ് ഹോം'
    print('Using hardcoded:', fixed_name)

# Also fix the address line
addr_start = content.find('<li>\u00e0\u00b4\u009c\u00e0\u00b4\u00a8', name_end)
if addr_start != -1:
    addr_end = content.find('</li>', addr_start) + len('</li>')
    garbled_addr = content[addr_start + len('<li>'):addr_end - len('</li>')]
    print('Garbled addr:', repr(garbled_addr))
    try:
        fixed_addr = garbled_addr.encode('latin-1').decode('utf-8')
        print('Fixed addr:', fixed_addr)
    except Exception as e:
        print('Error fixing addr:', e)
        fixed_addr = 'ജനതാ മുക്ക്, എടവ, വർക്കല, കേരളം – 695311'
else:
    print('Address line not found with that pattern')
    fixed_addr = None

# Now do the replacements
new_content = content.replace(
    '<li><strong>' + garbled_name + '</strong></li>',
    '<li><strong>' + fixed_name + '</strong></li>'
)

if fixed_addr and addr_start != -1:
    garbled_addr_full = content[addr_start + len('<li>'):addr_end - len('</li>')]
    new_content = new_content.replace(
        '<li>' + garbled_addr_full + '</li>',
        '<li>' + fixed_addr + '</li>'
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Done!')

#!/usr/bin/env python
# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the first NATURE IMAGE SEPARATOR block and remove it
start = content.find('<!-- NATURE IMAGE SEPARATOR')
if start == -1:
    print('ERROR: not found')
    exit(1)

# Find the end of this div block
end = content.find('</div>\n\n<!-- =', start)
if end == -1:
    end = content.find('</div>\n\n<!-- =', start)
if end == -1:
    # try without double newline
    end = content.find('</div>', start)
    end = content.find('</div>', end + 1)  # second closing div (the overlay)
    end = content.find('</div>', end + 1)  # outer closing div

end = end + len('</div>') + 1  # include the newline after

print(f'Removing from {start} to {end}')
print('Removed block:')
print(repr(content[start:end]))

new_content = content[:start] + content[end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Done - removed first nature separator')

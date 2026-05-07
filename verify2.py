with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()
print('Locations section found:', 'id="locations"' in c)
print('Old DXB cards removed:', 'DXB' not in c)
print('Google Maps iframes:', c.count('maps/embed'))
print('Olive green footer:', '1a2e14' in c)
print('Old brown footer class gone:', '<footer class="footer">' not in c)
print('Footer vayalarikam link:', 'vayalarikam.com' in c)
print('File size:', len(c), 'chars')

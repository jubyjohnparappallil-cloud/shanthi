with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# The "" is two curly quotes encoded as latin-1 in utf-8 context
# Replace the br tag approach - just remove the <br/> and fix the dash
import re
c = re.sub(
    r'Where time-honoured Ayurvedic traditions meet contemporary medicine [^\n<]*<br/>\s*\n\s*restoring balance',
    'Where time-honoured Ayurvedic traditions meet contemporary medicine \u2014 restoring balance',
    c
)
print('Fixed' if 'restoring balance of body' in c else 'ERROR')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, glob

html_files = glob.glob('*.html')
link_tag = '<link rel="stylesheet" href="responsive.css" />'

for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'responsive.css' in content:
        print(f'SKIP {fname} (already linked)')
        continue
    # Insert as last stylesheet before </head>
    if '</head>' in content:
        content = content.replace('</head>', link_tag + '\n</head>')
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'OK   {fname}')
    else:
        print(f'WARN {fname} — no </head> found')

print('\nDone!')

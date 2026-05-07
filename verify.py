with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
checks = [
    ('particles-js', 'Particles container'),
    ('scroll-progress', 'Scroll progress bar'),
    ('marquee-strip-wrap', 'Marquee strip'),
    ('grad-text', 'Gradient text'),
    ('cursor-glow', 'Cursor glow'),
    ('rv-up', 'Reveal animations'),
    ('Enhanced Animations Script', 'Animation script'),
    ('shimmerSlide', 'Shimmer effect'),
    ('counterObs', 'Counter animation'),
    ('magnetic', 'Magnetic buttons'),
    ('lift', 'Lift cards'),
    ('atm-carousel', 'Atmara carousel'),
    ('fpb-wrap', 'Parallax bands'),
]
for key, name in checks:
    found = key in content
    status = 'OK' if found else 'MISSING'
    print(status + ' -- ' + name)
print('\nFile size: ' + str(len(content)) + ' chars')

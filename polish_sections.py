#!/usr/bin/env python
# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─── 1. ADD MARQUEE STRIP AFTER HERO ───
marquee_html = '''
<!-- ═══ MARQUEE STRIP ═══ -->
<div class="marquee-strip-wrap" style="background:#6B8C3E;padding:12px 0;overflow:hidden;position:relative;z-index:5">
  <div class="marquee-inner" style="display:flex;gap:0;animation:marqueeScroll 28s linear infinite;white-space:nowrap;width:max-content">
    <span class="marquee-item">✦ Ayurveda</span>
    <span class="marquee-item">✦ Panchakarma</span>
    <span class="marquee-item">✦ Shirodhara</span>
    <span class="marquee-item">✦ Pizhichil</span>
    <span class="marquee-item">✦ Homeopathy</span>
    <span class="marquee-item">✦ Physiotherapy</span>
    <span class="marquee-item">✦ Abhyanga</span>
    <span class="marquee-item">✦ Kizhi</span>
    <span class="marquee-item">✦ Nasyam</span>
    <span class="marquee-item">✦ Wellness</span>
    <span class="marquee-item">✦ Ayurveda</span>
    <span class="marquee-item">✦ Panchakarma</span>
    <span class="marquee-item">✦ Shirodhara</span>
    <span class="marquee-item">✦ Pizhichil</span>
    <span class="marquee-item">✦ Homeopathy</span>
    <span class="marquee-item">✦ Physiotherapy</span>
    <span class="marquee-item">✦ Abhyanga</span>
    <span class="marquee-item">✦ Kizhi</span>
    <span class="marquee-item">✦ Nasyam</span>
    <span class="marquee-item">✦ Wellness</span>
  </div>
</div>
<style>
.marquee-item{font-family:'Raleway',sans-serif;font-size:0.72rem;font-weight:700;letter-spacing:0.22em;text-transform:uppercase;color:rgba(255,255,255,0.90);padding:0 32px}
@keyframes marqueeScroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.marquee-strip-wrap:hover .marquee-inner{animation-play-state:paused}
</style>

'''

# Insert after the hero section (after </section> of prem-hero)
hero_end = '</section>\n\n<!-- =\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022=\u2022\n     ABOUT SECTION'
if 'marquee-strip-wrap' not in content:
    # Find the about section comment
    about_comment_idx = content.find('ABOUT SECTION')
    if about_comment_idx != -1:
        # Find the start of the comment block
        comment_start = content.rfind('<!--', 0, about_comment_idx)
        content = content[:comment_start] + marquee_html + content[comment_start:]
        print('✓ Added marquee strip after hero')
    else:
        print('WARNING: Could not find ABOUT SECTION comment')

# ─── 2. ADD GRADIENT CLASS TO em TAGS IN SECTION HEADINGS ───
import re

def add_grad_to_em(match):
    em_content = match.group(1)
    # Don't double-add
    if 'grad-text' in em_content:
        return match.group(0)
    return '<em class="grad-text">' + em_content + '</em>'

# Only in section-heading h2 tags
def process_heading(match):
    heading = match.group(0)
    # Replace em tags inside this heading
    heading = re.sub(r'<em(?:[^>]*)>(.*?)</em>', add_grad_to_em, heading)
    return heading

content = re.sub(r'<h2 class="section-heading[^"]*"[^>]*>.*?</h2>', process_heading, content, flags=re.DOTALL)
print('✓ Added gradient class to section heading em tags')

# ─── 3. ADD LIFT CLASS TO TREATMENT MENU CARDS ───
content = content.replace('class="treatment-menu-card reveal"', 'class="treatment-menu-card reveal lift"')
print('✓ Added lift class to treatment menu cards')

# ─── 4. ADD LIFT CLASS TO TESTIMONIAL CARDS ───
content = content.replace('class="testimonial-card reveal"', 'class="testimonial-card reveal lift"')
content = content.replace('class="testimonial-card testimonial-card--featured reveal"', 'class="testimonial-card testimonial-card--featured reveal lift"')
print('✓ Added lift class to testimonial cards')

# ─── 5. ADD LIFT CLASS TO PHOTO BANNER PANELS ───
content = content.replace('class="pb-panel"', 'class="pb-panel lift"')
print('✓ Added lift class to photo banner panels')

# ─── 6. ENHANCE ABOUT SECTION BACKGROUND ───
about_section = '<section class="about section-pad" id="about">'
about_enhanced = '<section class="about section-pad" id="about" style="background:linear-gradient(135deg,#faf8f4 0%,#f0f7e8 50%,#faf8f4 100%)">'
content = content.replace(about_section, about_enhanced)
print('✓ Enhanced about section background')

# ─── 7. ENHANCE TESTIMONIALS BACKGROUND ───
test_section = '<section class="testimonials section-pad" id="testimonials">'
test_enhanced = '<section class="testimonials section-pad" id="testimonials" style="background:linear-gradient(160deg,#faf8f4 0%,#f5f0e8 100%)">'
content = content.replace(test_section, test_enhanced)
print('✓ Enhanced testimonials section background')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\n✅ Section polish complete!')

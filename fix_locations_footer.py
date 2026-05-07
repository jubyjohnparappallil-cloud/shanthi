#!/usr/bin/env python
# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─── 1. REPLACE LOCATIONS SECTION ───
loc_start = content.find('<section style="padding:80px 0;background:linear-gradient(160deg,#2e4228')
loc_end = content.find('</section>', loc_start) + len('</section>')
# Also grab the responsive style block after it
style_after = content.find('<style>\n@media(max-width:900px){\n  .locations-home-grid', loc_end)
if style_after != -1:
    style_end = content.find('</style>', style_after) + len('</style>')
    loc_end = style_end

print(f'Locations section: {loc_start} to {loc_end}')

new_locations = '''<!-- OUR LOCATIONS — Maps only -->
<section id="locations" style="padding:80px 0;background:linear-gradient(160deg,#1e3018 0%,#2e4a22 50%,#1e3018 100%);position:relative;overflow:hidden">
  <!-- Subtle leaf texture -->
  <div style="position:absolute;inset:0;background:url('herbal.jpg') center/cover no-repeat;opacity:0.06;pointer-events:none"></div>

  <div class="container" style="position:relative;z-index:2">
    <!-- Header -->
    <div class="section-header rv-up" style="text-align:center;margin-bottom:52px">
      <p class="section-eyebrow" style="color:#8dc26f!important">Find Us</p>
      <h2 class="section-heading" style="color:#fff!important">Our <em style="color:#c8a84b;font-style:italic;-webkit-text-fill-color:#c8a84b;background:none;animation:none">Locations</em></h2>
      <div class="gold-divider centered" style="background:#c8a84b!important;margin:16px auto 0"></div>
    </div>

    <!-- Two maps side by side -->
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;max-width:1000px;margin:0 auto 40px">

      <!-- Dubai Map -->
      <div class="rv-left" style="border-radius:20px;overflow:hidden;box-shadow:0 12px 48px rgba(0,0,0,0.40);position:relative">
        <div style="position:absolute;top:14px;left:14px;z-index:10;background:rgba(30,48,24,0.90);backdrop-filter:blur(8px);color:#fff;font-family:'Raleway',sans-serif;font-size:0.72rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;padding:7px 14px;border-radius:50px;border:1px solid rgba(141,194,111,0.35)">
          🇦🇪 Dubai
        </div>
        <a href="https://maps.google.com/?q=Hor+Al+Anz+East+Dubai+Royal+House+Mezzanine+M19+15C+Street" target="_blank" rel="noopener"
           style="position:absolute;bottom:14px;right:14px;z-index:10;background:#6B8C3E;color:#fff;font-family:'Raleway',sans-serif;font-size:0.70rem;font-weight:700;letter-spacing:0.10em;text-transform:uppercase;padding:7px 16px;border-radius:50px;text-decoration:none;display:flex;align-items:center;gap:5px">
          📍 Directions
        </a>
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3607.5!2d55.3347!3d25.2697!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e5f5d3e5f5d3e5f%3A0x0!2sHor+Al+Anz+East%2C+Dubai!5e0!3m2!1sen!2sae!4v1"
          style="width:100%;height:380px;border:0;display:block;filter:saturate(0.9)"
          loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade" title="Dubai Branch Map">
        </iframe>
      </div>

      <!-- Sharjah Map -->
      <div class="rv-right" style="border-radius:20px;overflow:hidden;box-shadow:0 12px 48px rgba(0,0,0,0.40);position:relative">
        <div style="position:absolute;top:14px;left:14px;z-index:10;background:rgba(30,48,24,0.90);backdrop-filter:blur(8px);color:#fff;font-family:'Raleway',sans-serif;font-size:0.72rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;padding:7px 14px;border-radius:50px;border:1px solid rgba(141,194,111,0.35)">
          🇦🇪 Sharjah
        </div>
        <a href="https://maps.google.com/?q=Al+Estiqlal+Street+Bu+Shaghara+Sharjah+Shanthi+Ayurveda" target="_blank" rel="noopener"
           style="position:absolute;bottom:14px;right:14px;z-index:10;background:#6B8C3E;color:#fff;font-family:'Raleway',sans-serif;font-size:0.70rem;font-weight:700;letter-spacing:0.10em;text-transform:uppercase;padding:7px 16px;border-radius:50px;text-decoration:none;display:flex;align-items:center;gap:5px">
          📍 Directions
        </a>
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3607.2!2d55.3894!3d25.3462!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3e5f5f5f5f5f5f5f%3A0x0!2sBu+Shaghara%2C+Sharjah!5e0!3m2!1sen!2sae!4v1"
          style="width:100%;height:380px;border:0;display:block;filter:saturate(0.9)"
          loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade" title="Sharjah Branch Map">
        </iframe>
      </div>

    </div>

    <!-- Contact page link -->
    <div style="text-align:center">
      <a href="contact.html" style="display:inline-flex;align-items:center;gap:8px;padding:12px 32px;border:1.5px solid rgba(200,168,75,0.55);color:#c8a84b;border-radius:50px;font-size:0.82rem;font-weight:700;text-decoration:none;font-family:'Raleway',sans-serif;letter-spacing:0.10em;text-transform:uppercase;transition:all 0.3s ease" onmouseover="this.style.background='rgba(200,168,75,0.12)'" onmouseout="this.style.background=''">
        View Full Contact Page →
      </a>
    </div>
  </div>
</section>

<style>
@media(max-width:700px){
  #locations .container > div[style*="grid-template-columns:1fr 1fr"]{grid-template-columns:1fr!important}
  #locations iframe{height:280px!important}
}
</style>
'''

content = content[:loc_start] + new_locations + content[loc_end:]
print('✓ Replaced locations section with maps-only version')

# ─── 2. REPLACE FOOTER ───
footer_start = content.find('<footer class="footer">')
footer_end = content.find('</footer>') + len('</footer>')
print(f'Footer: {footer_start} to {footer_end}')

new_footer = '''<!-- FOOTER — olive green theme -->
<footer style="background:linear-gradient(160deg,#1a2e14 0%,#243d1c 50%,#1a2e14 100%);position:relative;overflow:hidden">

  <!-- Subtle texture -->
  <div style="position:absolute;inset:0;background:url('herbal.jpg') center/cover no-repeat;opacity:0.05;pointer-events:none"></div>

  <!-- Top border accent -->
  <div style="height:3px;background:linear-gradient(90deg,transparent,#6B8C3E,#c8a84b,#6B8C3E,transparent)"></div>

  <div class="container" style="position:relative;z-index:2;padding:64px 0 40px">
    <div style="display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr;gap:48px;align-items:start">

      <!-- Brand column -->
      <div>
        <a href="#home" style="display:inline-block;margin-bottom:20px">
          <img src="logo.png" alt="Shanthi Wellness" style="height:70px;width:auto;object-fit:contain;filter:brightness(1.1)" />
        </a>
        <p style="font-family:'Lato',sans-serif;font-size:0.85rem;color:rgba(255,255,255,0.65);line-height:1.8;margin-bottom:24px;max-width:260px">
          Authentic Ayurveda, Homeopathy &amp; Physiotherapy. A branch of Vayalarikathu Ayurvedic Nursing Home, Kerala, Est. 1980.
        </p>
        <!-- Social icons -->
        <div style="display:flex;gap:10px">
          <a href="#" aria-label="Facebook" style="width:36px;height:36px;border-radius:50%;border:1px solid rgba(107,140,62,0.40);display:flex;align-items:center;justify-content:center;transition:all 0.3s ease" onmouseover="this.style.background='#6B8C3E';this.style.borderColor='#6B8C3E'" onmouseout="this.style.background='';this.style.borderColor='rgba(107,140,62,0.40)'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M18 2H15C13.7 2 12.4 2.5 11.5 3.5C10.5 4.4 10 5.7 10 7V10H7V14H10V22H14V14H17L18 10H14V7C14 6.7 14.1 6.4 14.3 6.2C14.6 6 14.8 5.9 15 5.9H18V2Z" stroke="rgba(255,255,255,0.75)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
          <a href="#" aria-label="Instagram" style="width:36px;height:36px;border-radius:50%;border:1px solid rgba(107,140,62,0.40);display:flex;align-items:center;justify-content:center;transition:all 0.3s ease" onmouseover="this.style.background='#6B8C3E';this.style.borderColor='#6B8C3E'" onmouseout="this.style.background='';this.style.borderColor='rgba(107,140,62,0.40)'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none"><rect x="2" y="2" width="20" height="20" rx="5" stroke="rgba(255,255,255,0.75)" stroke-width="1.5"/><circle cx="12" cy="12" r="4" stroke="rgba(255,255,255,0.75)" stroke-width="1.5"/><circle cx="17.5" cy="6.5" r="1" fill="rgba(255,255,255,0.75)"/></svg>
          </a>
          <a href="https://wa.me/971528434127" aria-label="WhatsApp" style="width:36px;height:36px;border-radius:50%;border:1px solid rgba(107,140,62,0.40);display:flex;align-items:center;justify-content:center;transition:all 0.3s ease" onmouseover="this.style.background='#25D366';this.style.borderColor='#25D366'" onmouseout="this.style.background='';this.style.borderColor='rgba(107,140,62,0.40)'">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none"><path d="M21 11.5C21 16.7 16.7 21 11.5 21C9.8 21 8.2 20.5 6.8 19.7L3 21L4.3 17.2C3.5 15.8 3 14.2 3 12.5C3 7.3 7.3 3 12.5 3C17.7 3 22 7.3 22 12.5" stroke="rgba(255,255,255,0.75)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
          </a>
        </div>
      </div>

      <!-- Sharjah -->
      <div>
        <h5 style="font-family:'Raleway',sans-serif;font-size:0.68rem;font-weight:800;letter-spacing:0.22em;text-transform:uppercase;color:#8dc26f;margin-bottom:18px">🇦🇪 Sharjah</h5>
        <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:10px">
          <li style="font-family:'Lato',sans-serif;font-size:0.82rem;color:rgba(255,255,255,0.60);line-height:1.6">Al Estiqlal St, Bu Shaghara, Sharjah</li>
          <li><a href="tel:+97165558429" style="font-family:'Lato',sans-serif;font-size:0.82rem;color:rgba(255,255,255,0.75);text-decoration:none;transition:color 0.2s" onmouseover="this.style.color='#8dc26f'" onmouseout="this.style.color='rgba(255,255,255,0.75)'">+971 6 555 8429</a></li>
          <li><a href="https://wa.me/971528434127" style="font-family:'Lato',sans-serif;font-size:0.82rem;color:rgba(255,255,255,0.75);text-decoration:none;transition:color 0.2s" onmouseover="this.style.color='#8dc26f'" onmouseout="this.style.color='rgba(255,255,255,0.75)'">WA: +971 52 843 4127</a></li>
        </ul>
      </div>

      <!-- Dubai -->
      <div>
        <h5 style="font-family:'Raleway',sans-serif;font-size:0.68rem;font-weight:800;letter-spacing:0.22em;text-transform:uppercase;color:#8dc26f;margin-bottom:18px">🇦🇪 Dubai</h5>
        <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:10px">
          <li style="font-family:'Lato',sans-serif;font-size:0.82rem;color:rgba(255,255,255,0.60);line-height:1.6">Royal House, M19, 15C St, Hor Al Anz East, Dubai</li>
          <li><a href="tel:+97142255133" style="font-family:'Lato',sans-serif;font-size:0.82rem;color:rgba(255,255,255,0.75);text-decoration:none;transition:color 0.2s" onmouseover="this.style.color='#8dc26f'" onmouseout="this.style.color='rgba(255,255,255,0.75)'">+971 4 225 5133</a></li>
          <li><a href="https://wa.me/971544630447" style="font-family:'Lato',sans-serif;font-size:0.82rem;color:rgba(255,255,255,0.75);text-decoration:none;transition:color 0.2s" onmouseover="this.style.color='#8dc26f'" onmouseout="this.style.color='rgba(255,255,255,0.75)'">WA: +971 54 463 0447</a></li>
        </ul>
      </div>

      <!-- India -->
      <div>
        <h5 style="font-family:'Raleway',sans-serif;font-size:0.68rem;font-weight:800;letter-spacing:0.22em;text-transform:uppercase;color:#8dc26f;margin-bottom:18px">🇮🇳 India</h5>
        <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:10px">
          <li style="font-family:'Lato',sans-serif;font-size:0.82rem;color:rgba(255,255,255,0.60);line-height:1.6">വയലാരിക്കത്ത് ആയുർവേദ<br/>Varkala, Kerala – 695311</li>
          <li><a href="tel:+917902700875" style="font-family:'Lato',sans-serif;font-size:0.82rem;color:rgba(255,255,255,0.75);text-decoration:none;transition:color 0.2s" onmouseover="this.style.color='#8dc26f'" onmouseout="this.style.color='rgba(255,255,255,0.75)'">+91 79027 00875</a></li>
          <li><a href="https://www.vayalarikam.com" target="_blank" rel="noopener" style="font-family:'Lato',sans-serif;font-size:0.82rem;color:rgba(255,255,255,0.75);text-decoration:none;transition:color 0.2s" onmouseover="this.style.color='#8dc26f'" onmouseout="this.style.color='rgba(255,255,255,0.75)'">vayalarikam.com</a></li>
        </ul>
      </div>

    </div>
  </div>

  <!-- Footer bottom bar -->
  <div style="border-top:1px solid rgba(107,140,62,0.20);padding:20px 0;position:relative;z-index:2">
    <div class="container" style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px">
      <p style="font-family:'Lato',sans-serif;font-size:0.78rem;color:rgba(255,255,255,0.40);margin:0">© 2025 Shanthi Wellness Medical Center. All rights reserved.</p>
      <p style="font-family:'Lato',sans-serif;font-size:0.78rem;color:rgba(255,255,255,0.35);margin:0">A branch of Vayalarikathu Ayurvedic Nursing Home, Kerala, Est. 1980.</p>
    </div>
  </div>

</footer>

<style>
@media(max-width:900px){
  footer > div.container > div[style*="grid-template-columns"]{grid-template-columns:1fr 1fr!important;gap:32px!important}
}
@media(max-width:560px){
  footer > div.container > div[style*="grid-template-columns"]{grid-template-columns:1fr!important}
}
</style>
'''

content = content[:footer_start] + new_footer + content[footer_end:]
print('✓ Replaced footer with olive green theme')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\n✅ Done!')

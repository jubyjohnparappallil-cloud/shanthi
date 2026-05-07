#!/usr/bin/env python
# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the carousel section boundaries
start_marker = '<section class="circle-carousel-section section-pad" id="services">'
end_marker = '</section>'

start = content.find(start_marker)
if start == -1:
    print('ERROR: start not found')
    exit(1)

# Find the closing </section> after start
end = content.find(end_marker, start)
if end == -1:
    print('ERROR: end not found')
    exit(1)
end = end + len(end_marker)

print(f'Replacing carousel from {start} to {end}')
print(f'Old length: {end - start}')

new_carousel = '''<!-- TREATMENTS CARD CAROUSEL — Atmara style -->
<section class="atm-carousel-section section-pad" id="services">
  <div class="container">
    <div class="section-header reveal" data-aos="fade-up" data-aos-duration="800">
      <p class="section-eyebrow">Our Treatments</p>
      <h2 class="section-heading">Classical <em>Ayurvedic Therapies</em></h2>
      <div class="gold-divider centered"></div>
      <p class="section-sub">Ancient healing therapies administered by expert practitioners for complete wellness.</p>
    </div>

    <!-- Carousel track -->
    <div class="atm-carousel-wrap">
      <button class="atm-arrow atm-arrow-prev" id="atmPrev" aria-label="Previous">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M15 18l-6-6 6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>

      <div class="atm-carousel-viewport" id="atmViewport">
        <div class="atm-carousel-track" id="atmTrack">

          <!-- Nasyam -->
          <div class="atm-card">
            <div class="atm-card-img">
              <img src="Nasyam.jpg" alt="Nasyam" />
              <div class="atm-card-overlay">
                <div class="atm-card-overlay-inner">
                  <h3 class="atm-card-overlay-title">Nasyam</h3>
                  <p class="atm-card-overlay-desc">Herbal juices and medicated oils administered through the nostrils. Highly effective for paralysis, headaches, sinusitis and mental disorders. Duration: 7–14 days.</p>
                  <a href="#appointment" class="atm-card-overlay-btn">Book Now</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Shirovasthi -->
          <div class="atm-card">
            <div class="atm-card-img">
              <img src="shirovasthi.jpg" alt="Shirovasthi" />
              <div class="atm-card-overlay">
                <div class="atm-card-overlay-inner">
                  <h3 class="atm-card-overlay-title">Shirovasthi</h3>
                  <p class="atm-card-overlay-desc">Medicated oil retained in a leather cap on the head. Very effective for headache, hair fall, burning sensation and diseases of the ear, nose and throat.</p>
                  <a href="#appointment" class="atm-card-overlay-btn">Book Now</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Pizhichil -->
          <div class="atm-card">
            <div class="atm-card-img">
              <img src="pizhichil.jpg" alt="Pizhichil" />
              <div class="atm-card-overlay">
                <div class="atm-card-overlay-inner">
                  <h3 class="atm-card-overlay-title">Pizhichil</h3>
                  <p class="atm-card-overlay-desc">Lukewarm medicated oil poured over the body — the king of Kerala therapies. Highly effective for Spondylosis, Hemiplegia, Arthritis and body rejuvenation.</p>
                  <a href="#appointment" class="atm-card-overlay-btn">Book Now</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Dhara -->
          <div class="atm-card">
            <div class="atm-card-img">
              <img src="Dhara.jpg" alt="Dhara" />
              <div class="atm-card-overlay">
                <div class="atm-card-overlay-inner">
                  <h3 class="atm-card-overlay-title">Dhara</h3>
                  <p class="atm-card-overlay-desc">Continuous pouring of warm medicated liquids over the body or forehead. Induces deep relaxation, calms the nervous system and relieves stress-related conditions.</p>
                  <a href="#appointment" class="atm-card-overlay-btn">Book Now</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Abhyanga -->
          <div class="atm-card">
            <div class="atm-card-img">
              <img src="kizhi.jpg" alt="Abhyanga" />
              <div class="atm-card-overlay">
                <div class="atm-card-overlay-inner">
                  <h3 class="atm-card-overlay-title">Abhyanga</h3>
                  <p class="atm-card-overlay-desc">Full-body warm medicated oil massage that nourishes tissues, improves circulation and promotes deep relaxation. A cornerstone of Ayurvedic daily care.</p>
                  <a href="#appointment" class="atm-card-overlay-btn">Book Now</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Panchakarma -->
          <div class="atm-card">
            <div class="atm-card-img">
              <img src="ritual3.jpg" alt="Panchakarma" />
              <div class="atm-card-overlay">
                <div class="atm-card-overlay-inner">
                  <h3 class="atm-card-overlay-title">Panchakarma</h3>
                  <p class="atm-card-overlay-desc">The classical five-fold purification therapy — comprehensive detoxification and rejuvenation. Removes deep-seated toxins and restores the body's natural balance.</p>
                  <a href="#appointment" class="atm-card-overlay-btn">Book Now</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Kizhi -->
          <div class="atm-card">
            <div class="atm-card-img">
              <img src="herbal.jpg" alt="Kizhi" />
              <div class="atm-card-overlay">
                <div class="atm-card-overlay-inner">
                  <h3 class="atm-card-overlay-title">Kizhi</h3>
                  <p class="atm-card-overlay-desc">Herbal poultice massage using warm bundles of medicinal herbs, leaves and powders. Relieves pain, stiffness and inflammation in joints and muscles.</p>
                  <a href="#appointment" class="atm-card-overlay-btn">Book Now</a>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>

      <button class="atm-arrow atm-arrow-next" id="atmNext" aria-label="Next">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none"><path d="M9 18l6-6-6-6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
      </button>
    </div>

    <!-- Dots -->
    <div class="atm-dots" id="atmDots"></div>
  </div>
</section>

<style>
/* ── ATMARA-STYLE TREATMENT CAROUSEL ── */
.atm-carousel-section { background: #faf8f4; }

.atm-carousel-wrap {
  position: relative;
  display: flex;
  align-items: center;
  margin-top: 48px;
}

.atm-carousel-viewport {
  overflow: hidden;
  width: 100%;
}

.atm-carousel-track {
  display: flex;
  gap: 20px;
  transition: transform 0.55s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform;
}

/* ── CARD ── */
.atm-card {
  flex: 0 0 calc(33.333% - 14px);
  min-width: 0;
  cursor: pointer;
}

.atm-card-img {
  position: relative;
  width: 100%;
  aspect-ratio: 3 / 4;
  border-radius: 20px;
  overflow: hidden;
  background: #1a1a1a;
}

.atm-card-img img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.6s ease;
}

/* Always-visible dark gradient at bottom */
.atm-card-img::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.10) 45%, transparent 70%);
  z-index: 1;
  pointer-events: none;
}

/* ── OVERLAY — slides up on hover/click ── */
.atm-card-overlay {
  position: absolute;
  inset: 0;
  z-index: 3;
  display: flex;
  align-items: flex-end;
  pointer-events: none;
}

.atm-card-overlay-inner {
  width: 100%;
  background: linear-gradient(to top, rgba(10,20,8,0.94) 0%, rgba(10,20,8,0.82) 60%, transparent 100%);
  padding: 28px 24px 24px;
  transform: translateY(calc(100% - 56px));
  transition: transform 0.45s cubic-bezier(0.4, 0, 0.2, 1);
  pointer-events: auto;
}

/* On hover or .active — slide fully up */
.atm-card:hover .atm-card-overlay-inner,
.atm-card.active .atm-card-overlay-inner {
  transform: translateY(0);
}

/* Zoom image on hover */
.atm-card:hover .atm-card-img img,
.atm-card.active .atm-card-img img {
  transform: scale(1.06);
}

.atm-card-overlay-title {
  font-family: 'Cinzel', serif;
  font-size: 1.05rem;
  font-weight: 600;
  color: #fff;
  margin: 0 0 10px;
  line-height: 1.3;
}

.atm-card-overlay-desc {
  font-family: 'Lato', sans-serif;
  font-size: 0.84rem;
  color: rgba(255,255,255,0.88);
  line-height: 1.7;
  margin: 0 0 16px;
  opacity: 0;
  transform: translateY(10px);
  transition: opacity 0.35s ease 0.1s, transform 0.35s ease 0.1s;
}

.atm-card:hover .atm-card-overlay-desc,
.atm-card.active .atm-card-overlay-desc {
  opacity: 1;
  transform: translateY(0);
}

.atm-card-overlay-btn {
  display: inline-flex;
  align-items: center;
  font-family: 'Raleway', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  text-decoration: none;
  padding: 9px 22px;
  background: #6B8C3E;
  color: #fff;
  border-radius: 50px;
  opacity: 0;
  transform: translateY(8px);
  transition: opacity 0.3s ease 0.18s, transform 0.3s ease 0.18s, background 0.2s;
}

.atm-card:hover .atm-card-overlay-btn,
.atm-card.active .atm-card-overlay-btn {
  opacity: 1;
  transform: translateY(0);
}

.atm-card-overlay-btn:hover { background: #4e6a2a; }

/* ── ARROWS ── */
.atm-arrow {
  flex-shrink: 0;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: 1.5px solid rgba(107,140,62,0.35);
  background: #fff;
  color: #6B8C3E;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.25s ease;
  z-index: 10;
  box-shadow: 0 4px 16px rgba(0,0,0,0.10);
}
.atm-arrow:hover { background: #6B8C3E; color: #fff; border-color: #6B8C3E; }
.atm-arrow-prev { margin-right: 16px; }
.atm-arrow-next { margin-left: 16px; }

/* ── DOTS ── */
.atm-dots {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 32px;
}
.atm-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: rgba(107,140,62,0.25);
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  padding: 0;
}
.atm-dot.active {
  background: #6B8C3E;
  width: 24px;
  border-radius: 4px;
}

/* ── RESPONSIVE ── */
@media (max-width: 900px) {
  .atm-card { flex: 0 0 calc(50% - 10px); }
}
@media (max-width: 560px) {
  .atm-card { flex: 0 0 calc(85% - 10px); }
  .atm-arrow { width: 38px; height: 38px; }
  .atm-arrow-prev { margin-right: 8px; }
  .atm-arrow-next { margin-left: 8px; }
}
</style>

<script>
(function() {
  var track    = document.getElementById('atmTrack');
  var viewport = document.getElementById('atmViewport');
  var prevBtn  = document.getElementById('atmPrev');
  var nextBtn  = document.getElementById('atmNext');
  var dotsWrap = document.getElementById('atmDots');
  if (!track || !viewport) return;

  var cards   = Array.prototype.slice.call(track.querySelectorAll('.atm-card'));
  var total   = cards.length;
  var current = 0;
  var perView = 3;
  var gap     = 20;
  var autoTimer = null;

  function getPerView() {
    var w = window.innerWidth;
    if (w <= 560) return 1;
    if (w <= 900) return 2;
    return 3;
  }

  function getCardWidth() {
    return cards[0] ? cards[0].offsetWidth : 300;
  }

  function buildDots() {
    if (!dotsWrap) return;
    dotsWrap.innerHTML = '';
    perView = getPerView();
    var count = Math.max(1, total - perView + 1);
    for (var i = 0; i < count; i++) {
      var d = document.createElement('button');
      d.className = 'atm-dot' + (i === 0 ? ' active' : '');
      d.setAttribute('aria-label', 'Slide ' + (i + 1));
      (function(idx) {
        d.addEventListener('click', function() { goTo(idx); resetAuto(); });
      })(i);
      dotsWrap.appendChild(d);
    }
  }

  function updateDots() {
    if (!dotsWrap) return;
    dotsWrap.querySelectorAll('.atm-dot').forEach(function(d, i) {
      d.classList.toggle('active', i === current);
    });
  }

  function goTo(idx) {
    perView = getPerView();
    var cardW = getCardWidth();
    var maxIdx = Math.max(0, total - perView);
    current = Math.max(0, Math.min(idx, maxIdx));
    var offset = current * (cardW + gap);
    track.style.transform = 'translateX(-' + offset + 'px)';
    updateDots();
  }

  function next() {
    perView = getPerView();
    goTo(current >= Math.max(0, total - perView) ? 0 : current + 1);
  }
  function prev() {
    perView = getPerView();
    goTo(current <= 0 ? Math.max(0, total - perView) : current - 1);
  }

  function resetAuto() {
    clearInterval(autoTimer);
    autoTimer = setInterval(next, 4000);
  }

  if (prevBtn) prevBtn.addEventListener('click', function() { prev(); resetAuto(); });
  if (nextBtn) nextBtn.addEventListener('click', function() { next(); resetAuto(); });

  /* Touch swipe */
  var touchX = 0;
  track.addEventListener('touchstart', function(e) { touchX = e.touches[0].clientX; }, { passive: true });
  track.addEventListener('touchend', function(e) {
    var diff = touchX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 40) { diff > 0 ? next() : prev(); resetAuto(); }
  }, { passive: true });

  /* Click = toggle .active (for touch); mouseleave = remove active */
  cards.forEach(function(card) {
    card.addEventListener('click', function() {
      var isActive = card.classList.contains('active');
      cards.forEach(function(c) { c.classList.remove('active'); });
      if (!isActive) card.classList.add('active');
    });
    card.addEventListener('mouseleave', function() {
      card.classList.remove('active');
    });
  });

  /* Pause on hover */
  viewport.addEventListener('mouseenter', function() { clearInterval(autoTimer); });
  viewport.addEventListener('mouseleave', resetAuto);

  window.addEventListener('resize', function() { buildDots(); goTo(current); });

  buildDots();
  goTo(0);
  resetAuto();
})();
</script>'''

new_content = content[:start] + new_carousel + content[end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Carousel replaced successfully! New length: {len(new_carousel)}')

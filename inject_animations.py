#!/usr/bin/env python
# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ─── 1. ADD PARTICLES CONTAINER TO HERO ───
# Insert <div id="particles-js"> as first child of .prem-hero section
hero_canvas = '<canvas id="heroCanvas"'
particles_html = '<div id="particles-js" style="position:absolute;inset:0;z-index:2;pointer-events:none"></div>\n\n  '
if 'particles-js' not in content:
    content = content.replace(hero_canvas, particles_html + hero_canvas)
    print('✓ Added particles container to hero')

# ─── 2. ADD SCROLL PROGRESS BAR + ENHANCED STYLES TO <HEAD> ───
enhanced_styles = '''
  <!-- Enhanced Animations CSS -->
  <style id="enhanced-anim-css">
  /* ── SCROLL PROGRESS BAR ── */
  .scroll-progress{position:fixed;top:0;left:0;width:0%;height:3px;background:linear-gradient(90deg,#6B8C3E,#8dc26f,#c89a4a);z-index:999999;transition:width 0.1s linear;box-shadow:0 0 8px rgba(107,140,62,0.6)}

  /* ── FLOATING PARTICLES ── */
  #particles-js{position:absolute;inset:0;z-index:2;pointer-events:none}

  /* ── GRADIENT ANIMATED TEXT ── */
  .grad-text{background:linear-gradient(135deg,#6B8C3E 0%,#8dc26f 40%,#c89a4a 70%,#6B8C3E 100%);background-size:300% auto;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:gradShift 5s ease infinite}
  @keyframes gradShift{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}

  /* ── REVEAL ANIMATIONS ── */
  .rv-up{opacity:0;transform:translateY(50px);transition:opacity 0.9s cubic-bezier(0.4,0,0.2,1),transform 0.9s cubic-bezier(0.4,0,0.2,1)}
  .rv-up.vis{opacity:1;transform:translateY(0)}
  .rv-left{opacity:0;transform:translateX(-50px);transition:opacity 0.9s ease,transform 0.9s ease}
  .rv-left.vis{opacity:1;transform:translateX(0)}
  .rv-right{opacity:0;transform:translateX(50px);transition:opacity 0.9s ease,transform 0.9s ease}
  .rv-right.vis{opacity:1;transform:translateX(0)}
  .rv-scale{opacity:0;transform:scale(0.88);transition:opacity 0.8s ease,transform 0.8s ease}
  .rv-scale.vis{opacity:1;transform:scale(1)}
  .rv-blur{opacity:0;filter:blur(12px);transition:opacity 1s ease,filter 1s ease}
  .rv-blur.vis{opacity:1;filter:blur(0)}

  /* ── STAGGER DELAYS ── */
  .d1{transition-delay:0.1s!important}
  .d2{transition-delay:0.2s!important}
  .d3{transition-delay:0.3s!important}
  .d4{transition-delay:0.4s!important}
  .d5{transition-delay:0.5s!important}
  .d6{transition-delay:0.6s!important}

  /* ── CARD LIFT ── */
  .lift{transition:transform 0.35s cubic-bezier(0.4,0,0.2,1),box-shadow 0.35s ease!important}
  .lift:hover{transform:translateY(-10px)!important;box-shadow:0 24px 60px rgba(107,140,62,0.22)!important}

  /* ── GLOW BUTTONS ── */
  .prem-btn-primary,.atm-card-overlay-btn,.fpb-btn,.nav-drawer-appt{position:relative;overflow:hidden}
  .prem-btn-primary::after,.atm-card-overlay-btn::after,.fpb-btn::after{content:'';position:absolute;top:50%;left:50%;width:0;height:0;border-radius:50%;background:rgba(255,255,255,0.25);transform:translate(-50%,-50%);transition:width 0.5s ease,height 0.5s ease}
  .prem-btn-primary:hover::after,.atm-card-overlay-btn:hover::after,.fpb-btn:hover::after{width:300px;height:300px}

  /* ── SECTION DIVIDER LINES ── */
  .section-pad{position:relative}

  /* ── FLOATING BADGE ANIMATION ── */
  @keyframes floatBadge{0%,100%{transform:translateY(0) rotate(-2deg)}50%{transform:translateY(-12px) rotate(2deg)}}
  .about-stack-badge{animation:floatBadge 4s ease-in-out infinite!important}

  /* ── SHIMMER ON IMAGES ── */
  .atm-card-img,.pb-panel,.about-webgl-wrap{position:relative;overflow:hidden}
  .atm-card-img::before,.pb-panel::before{content:'';position:absolute;top:0;left:-100%;width:60%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.12),transparent);z-index:10;pointer-events:none;animation:shimmerSlide 4s ease infinite}
  @keyframes shimmerSlide{0%{left:-100%}100%{left:200%}}

  /* ── HERO CONTENT GLOW ── */
  .prem-heading{text-shadow:0 0 80px rgba(107,140,62,0.3),0 4px 32px rgba(0,0,0,0.6)!important}

  /* ── SCROLL INDICATOR PULSE ── */
  .prem-scroll-line{animation:scrollPulse 2s ease-in-out infinite!important}
  @keyframes scrollPulse{0%,100%{opacity:0.3;transform:scaleY(0.8)}50%{opacity:1;transform:scaleY(1.2)}}

  /* ── TESTIMONIAL CARDS ── */
  .testimonial-card{transition:transform 0.35s ease,box-shadow 0.35s ease!important}
  .testimonial-card:hover{transform:translateY(-8px) scale(1.02)!important;box-shadow:0 20px 60px rgba(107,140,62,0.18)!important}

  /* ── TREATMENT MENU CARDS ── */
  .treatment-menu-card{transition:transform 0.35s ease,box-shadow 0.35s ease,border-color 0.35s ease!important}
  .treatment-menu-card:hover{transform:translateY(-8px)!important;box-shadow:0 20px 50px rgba(107,140,62,0.20)!important;border-color:rgba(107,140,62,0.4)!important}

  /* ── PHOTO BANNER PANELS ── */
  .pb-panel{transition:transform 0.4s ease,box-shadow 0.4s ease!important}
  .pb-panel:hover{transform:scale(1.03)!important;box-shadow:0 20px 60px rgba(0,0,0,0.25)!important}

  /* ── WHY-US IMAGE ── */
  .why-image img{transition:transform 0.6s ease!important}
  .why-image:hover img{transform:scale(1.04)!important}

  /* ── ABOUT IMAGE ── */
  .about-webgl-img{transition:transform 0.6s ease!important}
  .about-webgl-wrap:hover .about-webgl-img{transform:scale(1.03)!important}

  /* ── STAT NUMBERS GLOW ── */
  .prem-stat-num,.stat-num,.fpb-num{transition:color 0.3s ease,text-shadow 0.3s ease}
  .prem-stat:hover .prem-stat-num,.stat-item:hover .stat-num{color:#8dc26f!important;text-shadow:0 0 20px rgba(141,194,111,0.5)!important}

  /* ── NAVBAR SCROLL EFFECT ── */
  .navbar.scrolled{box-shadow:0 4px 30px rgba(107,140,62,0.20)!important}

  /* ── CURSOR GLOW ── */
  .cursor-glow{position:fixed;width:300px;height:300px;border-radius:50%;background:radial-gradient(circle,rgba(107,140,62,0.06) 0%,transparent 70%);pointer-events:none;z-index:0;transform:translate(-50%,-50%);transition:left 0.1s ease,top 0.1s ease}

  /* ── SECTION EYEBROW ANIMATION ── */
  .section-eyebrow,.pg-section-eyebrow{position:relative;display:inline-block}
  .section-eyebrow::after,.pg-section-eyebrow::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:1px;background:#6B8C3E;transition:width 0.6s ease}
  .section-header:hover .section-eyebrow::after{width:100%}

  /* ── GOLD DIVIDER ANIMATION ── */
  .gold-divider{transition:width 0.6s ease!important}
  .section-header:hover .gold-divider{width:80px!important}

  /* ── PATTERN BACKGROUND FOR SECTIONS ── */
  .about.section-pad{background-image:radial-gradient(circle,rgba(107,140,62,0.04) 1px,transparent 1px);background-size:28px 28px}
  .why-us.section-pad{background-image:radial-gradient(circle,rgba(107,140,62,0.04) 1px,transparent 1px);background-size:28px 28px}

  /* ── SMOOTH SECTION TRANSITIONS ── */
  section{transition:background 0.5s ease}

  /* ── FOOTER HOVER LINKS ── */
  .footer-contact-list a{transition:color 0.2s ease,letter-spacing 0.2s ease!important}
  .footer-contact-list a:hover{color:#8dc26f!important;letter-spacing:0.02em!important}
  </style>
'''

# Insert before </head>
if 'enhanced-anim-css' not in content:
    content = content.replace('</head>', enhanced_styles + '</head>')
    print('✓ Added enhanced animation styles to <head>')

# ─── 3. ADD ENHANCED ANIMATION SCRIPT BEFORE </BODY> ───
enhanced_script = '''
<!-- ═══ ENHANCED ANIMATIONS SCRIPT ═══ -->
<script>
(function() {
  'use strict';

  /* ── SCROLL PROGRESS BAR ── */
  var bar = document.createElement('div');
  bar.className = 'scroll-progress';
  document.body.appendChild(bar);
  window.addEventListener('scroll', function() {
    var h = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    bar.style.width = (window.pageYOffset / h * 100) + '%';
  }, { passive: true });

  /* ── CURSOR GLOW ── */
  var glow = document.createElement('div');
  glow.className = 'cursor-glow';
  document.body.appendChild(glow);
  document.addEventListener('mousemove', function(e) {
    glow.style.left = e.clientX + 'px';
    glow.style.top = e.clientY + 'px';
  }, { passive: true });

  /* ── PARTICLES IN HERO ── */
  if (typeof particlesJS !== 'undefined') {
    var pDiv = document.getElementById('particles-js');
    if (pDiv) {
      particlesJS('particles-js', {
        particles: {
          number: { value: 55, density: { enable: true, value_area: 900 } },
          color: { value: ['#8dc26f', '#c89a4a', '#ffffff'] },
          shape: { type: 'circle' },
          opacity: { value: 0.35, random: true, anim: { enable: true, speed: 0.8, opacity_min: 0.1 } },
          size: { value: 2.5, random: true },
          line_linked: { enable: true, distance: 130, color: '#6B8C3E', opacity: 0.15, width: 1 },
          move: { enable: true, speed: 0.8, direction: 'none', random: true, out_mode: 'out' }
        },
        interactivity: {
          detect_on: 'canvas',
          events: { onhover: { enable: true, mode: 'grab' }, onclick: { enable: true, mode: 'push' }, resize: true },
          modes: { grab: { distance: 160, line_linked: { opacity: 0.4 } }, push: { particles_nb: 3 } }
        }
      });
    }
  }

  /* ── INTERSECTION OBSERVER REVEALS ── */
  var revealObs = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting) {
        e.target.classList.add('vis');
        revealObs.unobserve(e.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.rv-up,.rv-left,.rv-right,.rv-scale,.rv-blur').forEach(function(el) {
    revealObs.observe(el);
  });

  /* ── ADD REVEAL CLASSES TO EXISTING ELEMENTS ── */
  // Section headers
  document.querySelectorAll('.section-header').forEach(function(el) {
    if (!el.classList.contains('rv-up')) el.classList.add('rv-up');
  });

  // About section
  var aboutImg = document.querySelector('.about-images');
  var aboutTxt = document.querySelector('.about-text');
  if (aboutImg) { aboutImg.classList.add('rv-left'); revealObs.observe(aboutImg); }
  if (aboutTxt) { aboutTxt.classList.add('rv-right'); revealObs.observe(aboutTxt); }

  // Treatment cards
  document.querySelectorAll('.atm-card').forEach(function(el, i) {
    el.classList.add('rv-scale', 'd' + Math.min(i + 1, 6));
    revealObs.observe(el);
  });

  // Testimonial cards
  document.querySelectorAll('.testimonial-card').forEach(function(el, i) {
    el.classList.add('rv-up', 'd' + Math.min(i + 1, 6));
    revealObs.observe(el);
  });

  // Photo banner panels
  document.querySelectorAll('.pb-panel').forEach(function(el, i) {
    el.classList.add('rv-scale', 'd' + Math.min(i + 1, 6));
    revealObs.observe(el);
  });

  // Treatment menu cards
  document.querySelectorAll('.treatment-menu-card').forEach(function(el, i) {
    el.classList.add('rv-up', 'd' + Math.min(i + 1, 6));
    revealObs.observe(el);
  });

  // FPB bands
  document.querySelectorAll('.fpb-band').forEach(function(el) {
    el.classList.add('rv-up');
    revealObs.observe(el);
  });

  // Why-us rows
  document.querySelectorAll('.why-row').forEach(function(el) {
    el.classList.add('rv-up');
    revealObs.observe(el);
  });

  // Footer columns
  document.querySelectorAll('.footer-col').forEach(function(el, i) {
    el.classList.add('rv-up', 'd' + Math.min(i + 1, 6));
    revealObs.observe(el);
  });

  /* ── COUNTER ANIMATION ── */
  var counterObs = new IntersectionObserver(function(entries) {
    entries.forEach(function(e) {
      if (e.isIntersecting && !e.target.dataset.counted) {
        e.target.dataset.counted = '1';
        var el = e.target;
        var raw = el.textContent;
        var num = parseInt(raw.replace(/[^0-9]/g, ''));
        var suffix = raw.replace(/[0-9]/g, '').trim();
        if (!num) return;
        var start = 0;
        var dur = 1800;
        var startTime = null;
        function step(ts) {
          if (!startTime) startTime = ts;
          var progress = Math.min((ts - startTime) / dur, 1);
          var ease = 1 - Math.pow(1 - progress, 3);
          el.textContent = Math.floor(ease * num) + suffix;
          if (progress < 1) requestAnimationFrame(step);
          else el.textContent = num + suffix;
        }
        requestAnimationFrame(step);
        counterObs.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('.prem-stat-num, .stat-num, .fpb-num').forEach(function(el) {
    counterObs.observe(el);
  });

  /* ── MAGNETIC BUTTONS ── */
  document.querySelectorAll('.prem-btn, .atm-arrow, .fpb-btn, .float-wa-btn').forEach(function(btn) {
    btn.addEventListener('mousemove', function(e) {
      var r = btn.getBoundingClientRect();
      var x = (e.clientX - r.left - r.width / 2) * 0.25;
      var y = (e.clientY - r.top - r.height / 2) * 0.25;
      btn.style.transform = 'translate(' + x + 'px,' + y + 'px)';
    });
    btn.addEventListener('mouseleave', function() {
      btn.style.transform = '';
    });
  });

  /* ── NAVBAR SCROLL EFFECT ── */
  var navbar = document.getElementById('navbar');
  window.addEventListener('scroll', function() {
    if (navbar) {
      if (window.pageYOffset > 50) navbar.classList.add('scrolled');
      else navbar.classList.remove('scrolled');
    }
  }, { passive: true });

  /* ── SMOOTH ANCHOR SCROLL ── */
  document.querySelectorAll('a[href^="#"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var href = this.getAttribute('href');
      if (href.length < 2) return;
      var target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ── HERO PARALLAX ON MOUSE MOVE ── */
  var hero = document.querySelector('.prem-hero');
  var heroContent = document.getElementById('premHeroContent');
  if (hero && heroContent) {
    hero.addEventListener('mousemove', function(e) {
      var r = hero.getBoundingClientRect();
      var x = (e.clientX - r.left) / r.width - 0.5;
      var y = (e.clientY - r.top) / r.height - 0.5;
      heroContent.style.transform = 'translate(' + (x * 18) + 'px,' + (y * 10) + 'px)';
    });
    hero.addEventListener('mouseleave', function() {
      heroContent.style.transform = '';
    });
  }

  /* ── INIT AOS ── */
  if (typeof AOS !== 'undefined') {
    AOS.init({ duration: 900, easing: 'ease-out-cubic', once: true, offset: 60 });
  }

  console.log('✨ All animations active');
})();
</script>
'''

# Insert before </body>
if 'Enhanced Animations Script' not in content:
    content = content.replace('</body>', enhanced_script + '\n</body>')
    print('✓ Added enhanced animation script before </body>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\n✅ All enhancements injected successfully!')

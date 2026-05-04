/**
 * Shanthi Wellness — script.js (clean single-file rewrite)
 */

/* ═══════════════════════════════════════════════════════
   1. DRAWER MENU — single authoritative implementation
═══════════════════════════════════════════════════════ */
(function () {
  var toggle   = document.getElementById('navToggle');
  var drawer   = document.getElementById('navDrawer');
  var overlay  = document.getElementById('navOverlay');
  var closeBtn = document.getElementById('navDrawerClose');

  if (!toggle || !drawer) return;

  function openDrawer() {
    drawer.classList.add('open');
    if (overlay) overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    drawer.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
    document.body.style.overflow = '';
  }

  toggle.addEventListener('click', function (e) {
    e.stopPropagation();
    drawer.classList.contains('open') ? closeDrawer() : openDrawer();
  });

  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  if (overlay)  overlay.addEventListener('click', closeDrawer);

  drawer.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', closeDrawer);
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeDrawer();
  });
})();


/* ═══════════════════════════════════════════════════════
   2. NAVBAR SCROLL GLASS EFFECT
═══════════════════════════════════════════════════════ */
(function () {
  var navbar = document.getElementById('navbar');
  if (!navbar) return;
  function onScroll() {
    navbar.classList.toggle('scrolled', window.scrollY > 60);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();


/* ═══════════════════════════════════════════════════════
   3. SMOOTH SCROLL (accounts for fixed navbar height)
═══════════════════════════════════════════════════════ */
(function () {
  document.querySelectorAll('a[href^="#"]').forEach(function (link) {
    link.addEventListener('click', function (e) {
      var href = this.getAttribute('href');
      if (!href || href === '#') return;
      var target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      var navbar = document.getElementById('navbar');
      var navH   = navbar ? navbar.offsetHeight : 130;
      var top    = target.getBoundingClientRect().top + window.scrollY - navH - 10;
      window.scrollTo({ top: top, behavior: 'smooth' });
    });
  });
})();


/* ═══════════════════════════════════════════════════════
   4. REVEAL ANIMATIONS + FORCE ABOUT SECTION VISIBLE
═══════════════════════════════════════════════════════ */
(function () {
  /* Force about section images visible immediately — never wait for scroll */
  var forceVisible = [
    '.about-img-main', '.about-img-secondary',
    '.about-images', '.about-img-frame',
    '.about .reveal', '.about-images.reveal', '.about-text.reveal'
  ];
  forceVisible.forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el) {
      el.classList.add('visible');
      el.style.cssText += ';opacity:1!important;transform:none!important;animation:none!important;visibility:visible!important';
    });
  });

  var revealEls = document.querySelectorAll('.reveal');

  if (!('IntersectionObserver' in window)) {
    revealEls.forEach(function (el) { el.classList.add('visible'); });
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.10, rootMargin: '0px 0px -40px 0px' });

  revealEls.forEach(function (el) { observer.observe(el); });
})();


/* ═══════════════════════════════════════════════════════
   5. STAGGERED REVEAL FOR GRID CHILDREN
═══════════════════════════════════════════════════════ */
(function () {
  if (!('IntersectionObserver' in window)) return;
  var containers = document.querySelectorAll(
    '.services-grid, .treatments-grid, .treatments-menu-grid, .testimonials-grid, .contact-grid'
  );
  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.querySelectorAll('.reveal').forEach(function (child, i) {
          setTimeout(function () { child.classList.add('visible'); }, i * 120);
        });
        obs.unobserve(entry.target);
      }
    });
  }, { threshold: 0.08 });
  containers.forEach(function (c) { obs.observe(c); });
})();


/* ═══════════════════════════════════════════════════════
   6. ACTIVE NAV LINK HIGHLIGHTING
═══════════════════════════════════════════════════════ */
(function () {
  var allNavLinks = document.querySelectorAll('.nav-link, .nav-drawer-link');
  var navbar      = document.getElementById('navbar');
  var sectionIds  = [];

  allNavLinks.forEach(function (link) {
    var href = link.getAttribute('href');
    if (href && href.startsWith('#') && href.length > 1) {
      var id = href.replace('#', '');
      if (sectionIds.indexOf(id) === -1) sectionIds.push(id);
    }
  });

  function updateActive() {
    var navH = navbar ? navbar.offsetHeight + 40 : 170;
    var activeId = sectionIds[0];
    sectionIds.forEach(function (id) {
      var el = document.getElementById(id);
      if (!el) return;
      if (el.getBoundingClientRect().top <= navH) activeId = id;
    });
    allNavLinks.forEach(function (link) {
      var href = link.getAttribute('href');
      if (href) link.classList.toggle('active', href === '#' + activeId);
    });
  }

  window.addEventListener('scroll', updateActive, { passive: true });
  updateActive();
})();


/* ═══════════════════════════════════════════════════════
   7. APPOINTMENT FORM
═══════════════════════════════════════════════════════ */
(function () {
  var form = document.getElementById('appointmentForm');
  if (!form) return;

  var dateInput = document.getElementById('date');
  if (dateInput) {
    var today = new Date();
    dateInput.min = today.getFullYear() + '-' +
      String(today.getMonth() + 1).padStart(2, '0') + '-' +
      String(today.getDate()).padStart(2, '0');
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var name    = document.getElementById('name').value.trim();
    var phone   = document.getElementById('phone').value.trim();
    var service = document.getElementById('service').value;
    var dateEl  = document.getElementById('date');
    var date    = dateEl ? dateEl.value : '1';

    if (!name || !phone || !service || !date) {
      showMsg('Please fill in all required fields.', 'error');
      return;
    }

    var btn  = form.querySelector('button[type="submit"]');
    var orig = btn.innerHTML;
    btn.innerHTML = '<span>Sending…</span>';
    btn.disabled  = true;

    setTimeout(function () {
      btn.innerHTML = '<span>✓ Booking Confirmed!</span>';
      btn.style.background = 'linear-gradient(135deg,#2d7a5a,#3a9e72)';
      showMsg('Thank you, ' + name + '! We will contact you shortly.', 'success');
      form.reset();
      setTimeout(function () {
        btn.innerHTML = orig;
        btn.disabled  = false;
        btn.style.background = '';
      }, 4000);
    }, 1500);
  });

  function showMsg(text, type) {
    var old = form.querySelector('.form-message');
    if (old) old.remove();
    var msg = document.createElement('div');
    msg.className = 'form-message';
    msg.textContent = text;
    msg.style.cssText = 'margin-top:16px;padding:14px 20px;border-radius:10px;font-size:0.9rem;text-align:center;' +
      (type === 'success'
        ? 'background:rgba(45,122,90,0.2);border:1px solid rgba(45,122,90,0.4);color:#7ecba0;'
        : 'background:rgba(200,90,26,0.15);border:1px solid rgba(200,90,26,0.3);color:#e07a3c;');
    form.appendChild(msg);
    setTimeout(function () {
      msg.style.transition = 'opacity 0.4s';
      msg.style.opacity = '0';
      setTimeout(function () { if (msg.parentNode) msg.remove(); }, 400);
    }, 5000);
  }
})();


/* ═══════════════════════════════════════════════════════
   8. COUNTER ANIMATION FOR STATS
═══════════════════════════════════════════════════════ */
(function () {
  var statNums = document.querySelectorAll('.stat-num');
  if (!statNums.length || !('IntersectionObserver' in window)) return;

  function animateCounter(el) {
    var text = el.textContent;
    var num  = parseInt(text.replace(/\D/g, ''), 10);
    if (isNaN(num)) return;
    var suffix   = text.replace(/[\d]/g, '').replace(/\s/g, '');
    var duration = 1800;
    var start    = performance.now();
    function update(now) {
      var p = Math.min((now - start) / duration, 1);
      var e = 1 - Math.pow(1 - p, 3);
      el.innerHTML = Math.round(e * num) + '<sup>' + suffix + '</sup>';
      if (p < 1) requestAnimationFrame(update);
    }
    requestAnimationFrame(update);
  }

  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) { animateCounter(entry.target); obs.unobserve(entry.target); }
    });
  }, { threshold: 0.5 });

  statNums.forEach(function (el) { obs.observe(el); });
})();


/* ═══════════════════════════════════════════════════════
   9. CIRCULAR TREATMENT CAROUSEL
═══════════════════════════════════════════════════════ */
(function () {
  var track    = document.getElementById('ccTrack');
  var viewport = document.getElementById('ccViewport');
  var prevBtn  = document.getElementById('ccPrev');
  var nextBtn  = document.getElementById('ccNext');
  var dotsWrap = document.getElementById('ccDots');
  if (!track || !viewport) return;

  var items   = track.querySelectorAll('.cc-item');
  var total   = items.length;
  var current = 0;
  var timer   = null;

  function pv() {
    return window.innerWidth <= 600 ? 1 : window.innerWidth <= 900 ? 2 : 3;
  }

  function iw() {
    var gap = 32;
    return (viewport.offsetWidth - gap * (pv() - 1)) / pv();
  }

  function goTo(idx) {
    var maxIdx = Math.max(0, total - pv());
    current = Math.max(0, Math.min(idx, maxIdx));
    track.style.transform = 'translateX(-' + (current * (iw() + 32)) + 'px)';
    updateDots();
    /* Highlight center item */
    var center = current + Math.floor(pv() / 2);
    items.forEach(function (item, i) {
      item.classList.toggle('cc-active', i === center);
    });
  }

  function buildDots() {
    if (!dotsWrap) return;
    dotsWrap.innerHTML = '';
    var count = Math.max(1, total - pv() + 1);
    for (var i = 0; i < count; i++) {
      var d = document.createElement('button');
      d.className = 'cc-dot' + (i === 0 ? ' active' : '');
      d.setAttribute('aria-label', 'Slide ' + (i + 1));
      (function (idx) {
        d.addEventListener('click', function () { stopAuto(); goTo(idx); startAuto(); });
      })(i);
      dotsWrap.appendChild(d);
    }
  }

  function updateDots() {
    if (!dotsWrap) return;
    dotsWrap.querySelectorAll('.cc-dot').forEach(function (d, i) {
      d.classList.toggle('active', i === current);
    });
  }

  function startAuto() {
    timer = setInterval(function () {
      goTo(current >= Math.max(0, total - pv()) ? 0 : current + 1);
    }, 3500);
  }

  function stopAuto() { clearInterval(timer); }

  if (prevBtn) prevBtn.addEventListener('click', function () { stopAuto(); goTo(current - 1); startAuto(); });
  if (nextBtn) nextBtn.addEventListener('click', function () { stopAuto(); goTo(current + 1); startAuto(); });

  track.addEventListener('mouseenter', stopAuto);
  track.addEventListener('mouseleave', startAuto);

  var touchX = 0;
  track.addEventListener('touchstart', function (e) { touchX = e.touches[0].clientX; stopAuto(); }, { passive: true });
  track.addEventListener('touchend', function (e) {
    var diff = touchX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 40) goTo(diff > 0 ? current + 1 : current - 1);
    startAuto();
  }, { passive: true });

  window.addEventListener('resize', function () { buildDots(); goTo(current); });

  buildDots();
  goTo(0);
  startAuto();
})();


/* ═══════════════════════════════════════════════════════
   10. AYURVEDIC TREATMENT CARDS — click to reveal
═══════════════════════════════════════════════════════ */
function toggleAyurCard(card) {
  var desc  = card.querySelector('.ayur-card-desc');
  var front = card.querySelector('.ayur-card-front');
  if (!desc) return;

  var isOpen = desc.style.display === 'block';

  document.querySelectorAll('.ayur-card').forEach(function (c) {
    var d = c.querySelector('.ayur-card-desc');
    var f = c.querySelector('.ayur-card-front');
    if (d) d.style.display = 'none';
    if (f) f.style.display = 'flex';
    c.style.transform   = '';
    c.style.boxShadow   = '0 6px 24px rgba(196,168,130,0.15)';
    c.style.borderColor = '';
  });

  if (!isOpen) {
    desc.style.display  = 'block';
    if (front) front.style.display = 'none';
    card.style.transform   = 'translateY(-6px)';
    card.style.boxShadow   = '0 20px 50px rgba(196,168,130,0.30)';
    card.style.borderColor = '#C4A882';
    setTimeout(function () { card.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }, 100);
  }
}

document.addEventListener('click', function (e) {
  if (!e.target.closest('.ayur-card')) {
    document.querySelectorAll('.ayur-card').forEach(function (c) {
      var d = c.querySelector('.ayur-card-desc');
      var f = c.querySelector('.ayur-card-front');
      if (d) d.style.display = 'none';
      if (f) f.style.display = 'flex';
      c.style.transform   = '';
      c.style.boxShadow   = '0 6px 24px rgba(196,168,130,0.15)';
      c.style.borderColor = '';
    });
  }
});


/* ═══════════════════════════════════════════════════════
   11. FADE-IN KEYFRAME
═══════════════════════════════════════════════════════ */
(function () {
  var s = document.createElement('style');
  s.textContent = '@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}';
  document.head.appendChild(s);
})();

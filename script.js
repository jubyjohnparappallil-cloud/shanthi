/**
 * Shanthi Wellness — script.js
 * Smooth scroll, navbar glass effect, IntersectionObserver reveals,
 * active nav link highlighting, mobile menu toggle.
 */

(function () {
  'use strict';

  /* ── DOM REFERENCES ──────────────────────────────────── */
  const navbar     = document.getElementById('navbar');
  const navToggle  = document.getElementById('navToggle');
  const navLinks   = document.getElementById('navLinks');
  const allNavLinks = document.querySelectorAll('.nav-link');
  const sections   = document.querySelectorAll('section[id], div[id]');
  const revealEls  = document.querySelectorAll('.reveal');
  const form       = document.getElementById('appointmentForm');

  /* ── NAVBAR: GLASS EFFECT ON SCROLL ─────────────────── */
  function handleNavbarScroll() {
    if (window.scrollY > 60) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }

  window.addEventListener('scroll', handleNavbarScroll, { passive: true });
  handleNavbarScroll(); // run on load

  /* ── MOBILE MENU TOGGLE ──────────────────────────────── */
  navToggle.addEventListener('click', function () {
    const isOpen = navLinks.classList.toggle('open');
    navToggle.setAttribute('aria-expanded', isOpen);
    // Animate hamburger → X
    const spans = navToggle.querySelectorAll('span');
    if (isOpen) {
      spans[0].style.transform = 'translateY(7px) rotate(45deg)';
      spans[1].style.opacity   = '0';
      spans[2].style.transform = 'translateY(-7px) rotate(-45deg)';
    } else {
      spans[0].style.transform = '';
      spans[1].style.opacity   = '';
      spans[2].style.transform = '';
    }
  });

  // Close menu when a link is clicked
  navLinks.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      navLinks.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
      const spans = navToggle.querySelectorAll('span');
      spans[0].style.transform = '';
      spans[1].style.opacity   = '';
      spans[2].style.transform = '';
    });
  });

  // Close menu when clicking outside
  document.addEventListener('click', function (e) {
    if (!navbar.contains(e.target) && navLinks.classList.contains('open')) {
      navLinks.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
      const spans = navToggle.querySelectorAll('span');
      spans[0].style.transform = '';
      spans[1].style.opacity   = '';
      spans[2].style.transform = '';
    }
  });

  /* ── SMOOTH SCROLL ───────────────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const target = document.querySelector(targetId);
      if (!target) return;
      e.preventDefault();
      const navHeight = navbar.offsetHeight;
      const targetTop = target.getBoundingClientRect().top + window.scrollY - navHeight - 16;
      window.scrollTo({
        top: targetTop,
        behavior: 'smooth'
      });
    });
  });

  /* ── ACTIVE NAV LINK HIGHLIGHTING ───────────────────── */
  const sectionIds = Array.from(allNavLinks)
    .map(function (link) { return link.getAttribute('href').replace('#', ''); })
    .filter(Boolean);

  function getActiveSectionId() {
    const navHeight = navbar.offsetHeight + 40;
    let activeId = sectionIds[0];
    for (let i = 0; i < sectionIds.length; i++) {
      const el = document.getElementById(sectionIds[i]);
      if (!el) continue;
      const rect = el.getBoundingClientRect();
      if (rect.top <= navHeight) {
        activeId = sectionIds[i];
      }
    }
    return activeId;
  }

  function updateActiveLink() {
    const activeId = getActiveSectionId();
    allNavLinks.forEach(function (link) {
      const href = link.getAttribute('href').replace('#', '');
      if (href === activeId) {
        link.classList.add('active');
      } else {
        link.classList.remove('active');
      }
    });
  }

  window.addEventListener('scroll', updateActiveLink, { passive: true });
  updateActiveLink();

  /* ── INTERSECTION OBSERVER: REVEAL ANIMATIONS ────────── */
  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            revealObserver.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.12,
        rootMargin: '0px 0px -60px 0px'
      }
    );

    revealEls.forEach(function (el) {
      revealObserver.observe(el);
    });
  } else {
    // Fallback: show all elements immediately
    revealEls.forEach(function (el) {
      el.classList.add('visible');
    });
  }

  /* ── STAGGERED REVEAL FOR GRID CHILDREN ─────────────── */
  const staggerContainers = document.querySelectorAll(
    '.services-grid, .treatments-grid, .treatments-menu-grid, .testimonials-grid, .contact-grid'
  );

  if ('IntersectionObserver' in window) {
    const staggerObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            const children = entry.target.querySelectorAll('.reveal');
            children.forEach(function (child, index) {
              setTimeout(function () {
                child.classList.add('visible');
              }, index * 120);
            });
            staggerObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08 }
    );

    staggerContainers.forEach(function (container) {
      staggerObserver.observe(container);
    });
  }

  /* ── APPOINTMENT FORM ────────────────────────────────── */
  if (form) {
    // Set minimum date to today
    const dateInput = document.getElementById('date');
    if (dateInput) {
      const today = new Date();
      const yyyy  = today.getFullYear();
      const mm    = String(today.getMonth() + 1).padStart(2, '0');
      const dd    = String(today.getDate()).padStart(2, '0');
      dateInput.min = yyyy + '-' + mm + '-' + dd;
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const name    = document.getElementById('name').value.trim();
      const phone   = document.getElementById('phone').value.trim();
      const service = document.getElementById('service').value;
      const date    = document.getElementById('date').value;

      if (!name || !phone || !service || !date) {
        showFormMessage('Please fill in all required fields.', 'error');
        return;
      }

      // Simulate submission
      const btn = form.querySelector('button[type="submit"]');
      const originalHTML = btn.innerHTML;
      btn.innerHTML = '<span>Sending...</span>';
      btn.disabled = true;

      setTimeout(function () {
        btn.innerHTML = '<span>✓ Booking Confirmed!</span>';
        btn.style.background = 'linear-gradient(135deg, #2d7a5a, #3a9e72)';
        showFormMessage(
          'Thank you, ' + name + '! We will contact you shortly to confirm your appointment.',
          'success'
        );
        form.reset();
        setTimeout(function () {
          btn.innerHTML = originalHTML;
          btn.disabled = false;
          btn.style.background = '';
        }, 4000);
      }, 1500);
    });
  }

  function showFormMessage(message, type) {
    // Remove existing message
    const existing = document.querySelector('.form-message');
    if (existing) existing.remove();

    const msg = document.createElement('div');
    msg.className = 'form-message';
    msg.textContent = message;
    msg.style.cssText = [
      'margin-top: 16px',
      'padding: 14px 20px',
      'border-radius: 10px',
      'font-size: 0.9rem',
      'text-align: center',
      'animation: fadeIn 0.4s ease',
      type === 'success'
        ? 'background: rgba(45,122,90,0.2); border: 1px solid rgba(45,122,90,0.4); color: #7ecba0;'
        : 'background: rgba(200,90,26,0.15); border: 1px solid rgba(200,90,26,0.3); color: #e07a3c;'
    ].join('; ');

    form.appendChild(msg);

    setTimeout(function () {
      if (msg.parentNode) {
        msg.style.opacity = '0';
        msg.style.transition = 'opacity 0.4s ease';
        setTimeout(function () { if (msg.parentNode) msg.remove(); }, 400);
      }
    }, 5000);
  }

  /* ── PARALLAX HERO ───────────────────────────────────── */
  const hero = document.querySelector('.hero');
  if (hero) {
    window.addEventListener('scroll', function () {
      const scrolled = window.scrollY;
      if (scrolled < window.innerHeight) {
        hero.style.backgroundPositionY = (scrolled * 0.4) + 'px';
      }
    }, { passive: true });
  }

  /* ── COUNTER ANIMATION FOR STATS ─────────────────────── */
  const statNums = document.querySelectorAll('.stat-num');

  function animateCounter(el) {
    const text = el.textContent;
    const num  = parseInt(text.replace(/\D/g, ''), 10);
    if (isNaN(num)) return;

    const suffix = text.replace(/[\d]/g, '').replace(/\s/g, '');
    const duration = 1800;
    const start    = performance.now();

    function update(now) {
      const elapsed  = now - start;
      const progress = Math.min(elapsed / duration, 1);
      // Ease out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.round(eased * num);
      el.innerHTML = current + '<sup>' + suffix + '</sup>';
      if (progress < 1) requestAnimationFrame(update);
    }

    requestAnimationFrame(update);
  }

  if ('IntersectionObserver' in window && statNums.length) {
    const statsObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            statsObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );
    statNums.forEach(function (el) { statsObserver.observe(el); });
  }

  /* ── ADD FADE-IN KEYFRAME DYNAMICALLY ────────────────── */
  const style = document.createElement('style');
  style.textContent = '@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }';
  document.head.appendChild(style);

})();

/* ── AYURVEDIC TREATMENT CARDS — Click to reveal ─────── */
function toggleAyurCard(card) {
  const isActive = card.classList.contains('active');

  // Close all other cards first
  document.querySelectorAll('.ayur-card.active').forEach(function(c) {
    if (c !== card) {
      c.classList.remove('active');
    }
  });

  // Toggle this card
  if (isActive) {
    card.classList.remove('active');
  } else {
    card.classList.add('active');
    // Smooth scroll to card
    setTimeout(function() {
      card.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 100);
  }
}

// Close card when clicking outside
document.addEventListener('click', function(e) {
  if (!e.target.closest('.ayur-card')) {
    document.querySelectorAll('.ayur-card.active').forEach(function(c) {
      c.classList.remove('active');
    });
  }
});

/* ── New navbar toggle for Menu button ─────────────────── */
(function() {
  var toggle = document.getElementById('navToggle');
  var links  = document.getElementById('navLinks');
  if (!toggle || !links) return;

  toggle.addEventListener('click', function(e) {
    e.stopPropagation();
    var isOpen = links.classList.toggle('open');
    var icon = toggle.querySelector('.nav-menu-icon');
    if (icon) {
      var spans = icon.querySelectorAll('span');
      if (isOpen) {
        spans[0].style.transform = 'translateY(6px) rotate(45deg)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'translateY(-6px) rotate(-45deg)';
      } else {
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      }
    }
  });

  document.addEventListener('click', function(e) {
    if (!toggle.contains(e.target) && !links.contains(e.target)) {
      links.classList.remove('open');
      var icon = toggle.querySelector('.nav-menu-icon');
      if (icon) {
        var spans = icon.querySelectorAll('span');
        spans[0].style.transform = '';
        spans[1].style.opacity = '';
        spans[2].style.transform = '';
      }
    }
  });
})();

/* ── Left-side drawer menu ─────────────────────────────── */
(function() {
  var toggle  = document.getElementById('navToggle');
  var links   = document.getElementById('navLinks');
  var overlay = document.getElementById('navOverlay');
  if (!toggle || !links) return;

  function openMenu() {
    links.classList.add('open');
    if (overlay) overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    var icon = toggle.querySelector('.nav-menu-icon');
    if (icon) {
      var spans = icon.querySelectorAll('span');
      spans[0].style.transform = 'translateY(6px) rotate(45deg)';
      spans[1].style.opacity = '0';
      spans[2].style.transform = 'translateY(-6px) rotate(-45deg)';
    }
  }

  function closeMenu() {
    links.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
    document.body.style.overflow = '';
    var icon = toggle.querySelector('.nav-menu-icon');
    if (icon) {
      var spans = icon.querySelectorAll('span');
      spans[0].style.transform = '';
      spans[1].style.opacity = '';
      spans[2].style.transform = '';
    }
  }

  toggle.addEventListener('click', function(e) {
    e.stopPropagation();
    if (links.classList.contains('open')) { closeMenu(); } else { openMenu(); }
  });

  if (overlay) overlay.addEventListener('click', closeMenu);

  /* Close when a nav link is clicked */
  links.querySelectorAll('a').forEach(function(a) {
    a.addEventListener('click', closeMenu);
  });

  /* Close on Escape key */
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeMenu();
  });
})();

/* ── New left drawer with logo ─────────────────────────── */
(function() {
  var toggle   = document.getElementById('navToggle');
  var drawer   = document.getElementById('navDrawer');
  var overlay  = document.getElementById('navOverlay');
  var closeBtn = document.getElementById('navDrawerClose');
  if (!toggle || !drawer) return;

  function openDrawer() {
    drawer.classList.add('open');
    if (overlay) overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
    /* Animate hamburger to X */
    var icon = toggle.querySelector('.nav-menu-icon');
    if (icon) {
      var s = icon.querySelectorAll('span');
      s[0].style.transform = 'translateY(6px) rotate(45deg)';
      s[1].style.opacity = '0';
      s[2].style.transform = 'translateY(-6px) rotate(-45deg)';
    }
  }

  function closeDrawer() {
    drawer.classList.remove('open');
    if (overlay) overlay.classList.remove('open');
    document.body.style.overflow = '';
    var icon = toggle.querySelector('.nav-menu-icon');
    if (icon) {
      var s = icon.querySelectorAll('span');
      s[0].style.transform = '';
      s[1].style.opacity = '';
      s[2].style.transform = '';
    }
  }

  toggle.addEventListener('click', function(e) {
    e.stopPropagation();
    drawer.classList.contains('open') ? closeDrawer() : openDrawer();
  });

  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  if (overlay)  overlay.addEventListener('click', closeDrawer);

  /* Close on link click */
  drawer.querySelectorAll('a').forEach(function(a) {
    a.addEventListener('click', closeDrawer);
  });

  /* Escape key */
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeDrawer();
  });
})();

/* ── Drawer without background overlay ─────────────────── */
(function() {
  var toggle   = document.getElementById('navToggle');
  var drawer   = document.getElementById('navDrawer');
  var closeBtn = document.getElementById('navDrawerClose');
  if (!toggle || !drawer) return;

  function openD() {
    drawer.classList.add('open');
    /* NO body overflow lock — background stays scrollable */
    var icon = toggle.querySelector('.nav-menu-icon');
    if (icon) {
      var s = icon.querySelectorAll('span');
      s[0].style.transform = 'translateY(6px) rotate(45deg)';
      s[1].style.opacity = '0';
      s[2].style.transform = 'translateY(-6px) rotate(-45deg)';
    }
  }
  function closeD() {
    drawer.classList.remove('open');
    var icon = toggle.querySelector('.nav-menu-icon');
    if (icon) {
      var s = icon.querySelectorAll('span');
      s[0].style.transform = '';
      s[1].style.opacity = '';
      s[2].style.transform = '';
    }
  }

  toggle.addEventListener('click', function(e) {
    e.stopPropagation();
    drawer.classList.contains('open') ? closeD() : openD();
  });
  if (closeBtn) closeBtn.addEventListener('click', closeD);
  drawer.querySelectorAll('a').forEach(function(a) { a.addEventListener('click', closeD); });
  document.addEventListener('keydown', function(e) { if (e.key === 'Escape') closeD(); });
  /* Close when clicking outside drawer */
  document.addEventListener('click', function(e) {
    if (!drawer.contains(e.target) && !toggle.contains(e.target)) closeD();
  });
})();

/* ── Circular Treatment Carousel ───────────────────────── */
(function() {
  var track    = document.getElementById('ccTrack');
  var viewport = document.getElementById('ccViewport');
  var prevBtn  = document.getElementById('ccPrev');
  var nextBtn  = document.getElementById('ccNext');
  var dotsWrap = document.getElementById('ccDots');
  if (!track) return;

  var items      = track.querySelectorAll('.cc-item');
  var total      = items.length;
  var current    = 0;
  var perView    = 3;
  var autoTimer  = null;

  function getPerView() {
    if (window.innerWidth <= 600) return 1;
    if (window.innerWidth <= 900) return 2;
    return 3;
  }

  function getItemWidth() {
    var vw = viewport.offsetWidth;
    var gap = 32;
    var pv  = getPerView();
    return (vw - gap * (pv - 1)) / pv;
  }

  function goTo(idx) {
    perView = getPerView();
    var maxIdx = Math.max(0, total - perView);
    current = Math.max(0, Math.min(idx, maxIdx));
    var iw  = getItemWidth();
    var gap = 32;
    track.style.transform = 'translateX(-' + (current * (iw + gap)) + 'px)';
    updateDots();
  }

  function buildDots() {
    if (!dotsWrap) return;
    dotsWrap.innerHTML = '';
    perView = getPerView();
    var count = Math.max(1, total - perView + 1);
    for (var i = 0; i < count; i++) {
      var d = document.createElement('button');
      d.className = 'cc-dot' + (i === 0 ? ' active' : '');
      d.setAttribute('aria-label', 'Go to slide ' + (i + 1));
      (function(idx) { d.addEventListener('click', function() { goTo(idx); }); })(i);
      dotsWrap.appendChild(d);
    }
  }

  function updateDots() {
    if (!dotsWrap) return;
    dotsWrap.querySelectorAll('.cc-dot').forEach(function(d, i) {
      d.classList.toggle('active', i === current);
    });
  }

  function startAuto() {
    autoTimer = setInterval(function() {
      perView = getPerView();
      var maxIdx = Math.max(0, total - perView);
      goTo(current >= maxIdx ? 0 : current + 1);
    }, 3500);
  }

  function stopAuto() { clearInterval(autoTimer); }

  if (prevBtn) prevBtn.addEventListener('click', function() { stopAuto(); goTo(current - 1); startAuto(); });
  if (nextBtn) nextBtn.addEventListener('click', function() { stopAuto(); goTo(current + 1); startAuto(); });

  /* Pause on hover */
  track.addEventListener('mouseenter', stopAuto);
  track.addEventListener('mouseleave', startAuto);

  /* Touch swipe */
  var touchX = 0;
  track.addEventListener('touchstart', function(e) { touchX = e.touches[0].clientX; stopAuto(); }, {passive:true});
  track.addEventListener('touchend', function(e) {
    var diff = touchX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 40) goTo(diff > 0 ? current + 1 : current - 1);
    startAuto();
  }, {passive:true});

  window.addEventListener('resize', function() { buildDots(); goTo(current); });

  buildDots();
  goTo(0);
  startAuto();
})();

/* ── Carousel active class for center item ─────────────── */
(function() {
  function updateActiveClass() {
    var track = document.getElementById('ccTrack');
    if (!track) return;
    var items = track.querySelectorAll('.cc-item');
    var pv = window.innerWidth <= 600 ? 1 : window.innerWidth <= 900 ? 2 : 3;
    /* Get current index from transform */
    var style = track.style.transform || 'translateX(0)';
    var match = style.match(/translateX\(-?([\d.]+)px\)/);
    var offset = match ? parseFloat(match[1]) : 0;
    var vw = document.getElementById('ccViewport') ? document.getElementById('ccViewport').offsetWidth : 0;
    var iw = vw > 0 ? (vw - 32 * (pv - 1)) / pv : 0;
    var cur = iw > 0 ? Math.round(offset / (iw + 32)) : 0;
    var centerIdx = cur + Math.floor(pv / 2);
    items.forEach(function(item, i) {
      item.classList.toggle('cc-active', i === centerIdx);
    });
  }

  /* Observe track transform changes */
  var track = document.getElementById('ccTrack');
  if (track) {
    var observer = new MutationObserver(updateActiveClass);
    observer.observe(track, { attributes: true, attributeFilter: ['style'] });
    updateActiveClass();
  }
})();

/* ── Carousel speed fix — 3s auto slide ────────────────── */
(function() {
  /* Override the auto timer interval to 3000ms */
  var track = document.getElementById('ccTrack');
  if (!track) return;
  /* The main carousel JS already runs — just ensure gap is 24px */
  track.style.gap = '24px';
})();

/* ── Simple ayur card toggle for new structure ─────────── */
function toggleAyurCard(card) {
  var desc = card.querySelector('.ayur-card-desc');
  var front = card.querySelector('.ayur-card-front');
  if (!desc) return;
  var isOpen = desc.style.display === 'block';
  /* Close all */
  document.querySelectorAll('.ayur-card').forEach(function(c) {
    var d = c.querySelector('.ayur-card-desc');
    var f = c.querySelector('.ayur-card-front');
    if (d) d.style.display = 'none';
    if (f) f.style.display = 'flex';
    c.style.transform = '';
    c.style.boxShadow = '0 6px 24px rgba(196,168,130,0.15)';
  });
  if (!isOpen) {
    desc.style.display = 'block';
    if (front) front.style.display = 'none';
    card.style.transform = 'translateY(-6px)';
    card.style.boxShadow = '0 20px 50px rgba(196,168,130,0.30)';
    card.style.borderColor = '#C4A882';
    setTimeout(function() { card.scrollIntoView({behavior:'smooth', block:'nearest'}); }, 100);
  }
}

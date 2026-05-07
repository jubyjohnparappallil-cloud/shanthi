#!/usr/bin/env python
# -*- coding: utf-8 -*-
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

drop_section = '''
<!-- ═══════════════════════════════════════════════════════
     THREE.JS OIL DROP SPLATTER ANIMATION SECTION
     Full-width canvas with nature.jpg background
     Drops fall, hit surface, create ripple splashes
═══════════════════════════════════════════════════════ -->
<section id="drop-anim-section" style="position:relative;width:100%;height:520px;overflow:hidden;background:#0a1a08">

  <!-- Background image -->
  <div id="drop-bg" style="position:absolute;inset:0;background:url('nature.jpg') center/cover no-repeat;opacity:0.55;z-index:0"></div>

  <!-- Dark overlay for depth -->
  <div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(5,15,5,0.45) 0%,rgba(5,15,5,0.20) 50%,rgba(5,15,5,0.55) 100%);z-index:1;pointer-events:none"></div>

  <!-- Three.js canvas -->
  <canvas id="dropCanvas" style="position:absolute;inset:0;width:100%;height:100%;z-index:2;display:block"></canvas>

  <!-- Text overlay -->
  <div style="position:absolute;inset:0;z-index:3;display:flex;flex-direction:column;align-items:center;justify-content:center;pointer-events:none;text-align:center;padding:0 24px">
    <p style="font-family:'Raleway',sans-serif;font-size:0.68rem;font-weight:800;letter-spacing:0.32em;text-transform:uppercase;color:#8dc26f;margin-bottom:14px;text-shadow:0 2px 12px rgba(0,0,0,0.6)">The Essence of Healing</p>
    <h2 style="font-family:'Cinzel',serif;font-size:clamp(1.8rem,4vw,3.2rem);font-weight:700;color:#fff;line-height:1.25;margin-bottom:16px;text-shadow:0 4px 32px rgba(0,0,0,0.7)">
      Every Drop,<br/><em style="color:#c8a84b;font-style:italic">A Healing Ritual</em>
    </h2>
    <p style="font-family:'Lato',sans-serif;font-size:0.95rem;color:rgba(255,255,255,0.78);max-width:480px;line-height:1.8;text-shadow:0 2px 8px rgba(0,0,0,0.5)">
      Warm medicated oils, carefully prepared from ancient formulas, flow in a continuous stream — the heart of Ayurvedic healing.
    </p>
  </div>

</section>

<script>
/* ═══ THREE.JS OIL DROP SPLATTER ANIMATION ═══ */
(function() {
  if (typeof THREE === 'undefined') return;

  var canvas = document.getElementById('dropCanvas');
  if (!canvas) return;

  /* ── SCENE SETUP ── */
  var W = canvas.offsetWidth || window.innerWidth;
  var H = canvas.offsetHeight || 520;
  canvas.width  = W;
  canvas.height = H;

  var renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true });
  renderer.setSize(W, H);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setClearColor(0x000000, 0);

  var scene  = new THREE.Scene();
  var camera = new THREE.OrthographicCamera(-W/2, W/2, H/2, -H/2, 0.1, 1000);
  camera.position.z = 100;

  /* ── RESIZE ── */
  window.addEventListener('resize', function() {
    W = canvas.offsetWidth || window.innerWidth;
    H = canvas.offsetHeight || 520;
    canvas.width  = W;
    canvas.height = H;
    renderer.setSize(W, H);
    camera.left   = -W/2; camera.right  = W/2;
    camera.top    = H/2;  camera.bottom = -H/2;
    camera.updateProjectionMatrix();
  });

  /* ── MATERIALS ── */
  function makeMat(color, opacity, emissive) {
    return new THREE.MeshBasicMaterial({
      color: color,
      transparent: true,
      opacity: opacity,
      depthWrite: false,
      blending: THREE.AdditiveBlending
    });
  }

  /* ── DROP CLASS ── */
  var drops = [];
  var ripples = [];
  var splashes = [];

  function Drop() {
    this.x = (Math.random() - 0.5) * W * 0.9;
    this.y = H / 2 + 40;                        // start above top
    this.vy = -(2.5 + Math.random() * 3.5);     // fall speed
    this.size = 3 + Math.random() * 5;
    this.alpha = 0.7 + Math.random() * 0.3;
    this.color = Math.random() > 0.4 ? 0x8dc26f : (Math.random() > 0.5 ? 0xc8a84b : 0xaad4ff);
    this.trail = [];
    this.alive = true;
    this.floorY = -(H / 2) + 60 + (Math.random() - 0.5) * 80; // hit floor

    // Mesh: elongated ellipse for drop shape
    var geo = new THREE.CircleGeometry(this.size, 12);
    this.mesh = new THREE.Mesh(geo, makeMat(this.color, this.alpha));
    this.mesh.scale.y = 1.8; // elongate
    this.mesh.position.set(this.x, this.y, 1);
    scene.add(this.mesh);

    // Trail geometry (line)
    var trailGeo = new THREE.BufferGeometry();
    var pts = [];
    for (var i = 0; i < 8; i++) pts.push(this.x, this.y + i * 4, 0);
    trailGeo.setAttribute('position', new THREE.Float32BufferAttribute(pts, 3));
    var trailMat = new THREE.LineBasicMaterial({ color: this.color, transparent: true, opacity: 0.25, blending: THREE.AdditiveBlending });
    this.trail = new THREE.Line(trailGeo, trailMat);
    scene.add(this.trail);
  }

  Drop.prototype.update = function() {
    this.y += this.vy;
    this.mesh.position.y = this.y;

    // Update trail
    var pts = [];
    for (var i = 0; i < 8; i++) {
      pts.push(this.x, this.y + i * Math.abs(this.vy) * 0.8, 0);
    }
    this.trail.geometry.setAttribute('position', new THREE.Float32BufferAttribute(pts, 3));
    this.trail.geometry.attributes.position.needsUpdate = true;

    // Hit floor
    if (this.y <= this.floorY) {
      this.alive = false;
      spawnRipple(this.x, this.floorY, this.size, this.color);
      spawnSplash(this.x, this.floorY, this.size, this.color);
      scene.remove(this.mesh);
      scene.remove(this.trail);
    }
  };

  /* ── RIPPLE CLASS ── */
  function Ripple(x, y, size, color) {
    this.x = x; this.y = y;
    this.r = size * 0.5;
    this.maxR = size * (8 + Math.random() * 6);
    this.alpha = 0.7;
    this.color = color;
    this.alive = true;

    var geo = new THREE.RingGeometry(this.r, this.r + 1.5, 32);
    this.mesh = new THREE.Mesh(geo, makeMat(this.color, this.alpha));
    this.mesh.position.set(this.x, this.y, 2);
    this.mesh.scale.y = 0.35; // flatten to ellipse on surface
    scene.add(this.mesh);
  }

  Ripple.prototype.update = function() {
    this.r += 1.8;
    this.alpha -= 0.018;
    if (this.alpha <= 0 || this.r >= this.maxR) {
      this.alive = false;
      scene.remove(this.mesh);
      return;
    }
    // Rebuild ring geometry
    scene.remove(this.mesh);
    var geo = new THREE.RingGeometry(this.r, this.r + Math.max(1, 2.5 - this.r * 0.04), 32);
    this.mesh = new THREE.Mesh(geo, makeMat(this.color, this.alpha));
    this.mesh.position.set(this.x, this.y, 2);
    this.mesh.scale.y = 0.35;
    scene.add(this.mesh);
  };

  /* ── SPLASH PARTICLE CLASS ── */
  function SplashParticle(x, y, color) {
    this.x = x; this.y = y;
    var angle = Math.random() * Math.PI; // upward arc
    var speed = 1.5 + Math.random() * 4;
    this.vx = Math.cos(angle) * speed * (Math.random() > 0.5 ? 1 : -1);
    this.vy = Math.sin(angle) * speed * 1.2;
    this.gravity = -0.18;
    this.size = 1.2 + Math.random() * 2.5;
    this.alpha = 0.8 + Math.random() * 0.2;
    this.color = color;
    this.alive = true;

    var geo = new THREE.CircleGeometry(this.size, 8);
    this.mesh = new THREE.Mesh(geo, makeMat(this.color, this.alpha));
    this.mesh.position.set(this.x, this.y, 3);
    scene.add(this.mesh);
  }

  SplashParticle.prototype.update = function() {
    this.vy += this.gravity;
    this.x  += this.vx;
    this.y  += this.vy;
    this.alpha -= 0.022;
    this.mesh.material.opacity = Math.max(0, this.alpha);
    this.mesh.position.set(this.x, this.y, 3);
    if (this.alpha <= 0) {
      this.alive = false;
      scene.remove(this.mesh);
    }
  };

  /* ── SPAWN HELPERS ── */
  function spawnRipple(x, y, size, color) {
    for (var i = 0; i < 3; i++) {
      setTimeout(function(xx, yy, ss, cc) {
        ripples.push(new Ripple(xx, yy, ss, cc));
      }.bind(null, x, y, size * (1 + i * 0.6), color), i * 80);
    }
  }

  function spawnSplash(x, y, size, color) {
    var count = Math.floor(6 + size * 2);
    for (var i = 0; i < count; i++) {
      splashes.push(new SplashParticle(x, y, color));
    }
  }

  /* ── SPAWN DROPS ON INTERVAL ── */
  var dropTimer = 0;
  var dropInterval = 28; // frames between drops

  /* ── AMBIENT FLOATING PARTICLES ── */
  var ambients = [];
  for (var i = 0; i < 40; i++) {
    (function() {
      var geo = new THREE.CircleGeometry(0.8 + Math.random() * 1.5, 8);
      var col = [0x8dc26f, 0xc8a84b, 0xaad4ff, 0xffffff][Math.floor(Math.random() * 4)];
      var mesh = new THREE.Mesh(geo, makeMat(col, 0.15 + Math.random() * 0.2));
      mesh.position.set(
        (Math.random() - 0.5) * W,
        (Math.random() - 0.5) * H,
        0.5
      );
      mesh.userData = {
        vx: (Math.random() - 0.5) * 0.3,
        vy: (Math.random() - 0.5) * 0.3
      };
      scene.add(mesh);
      ambients.push(mesh);
    })();
  }

  /* ── ANIMATION LOOP ── */
  var frame = 0;
  var isVisible = false;

  // Only animate when section is in view
  var section = document.getElementById('drop-anim-section');
  var visObs = new IntersectionObserver(function(entries) {
    isVisible = entries[0].isIntersecting;
  }, { threshold: 0.1 });
  if (section) visObs.observe(section);

  function animate() {
    requestAnimationFrame(animate);
    if (!isVisible) return;

    frame++;

    /* Spawn new drop */
    dropTimer++;
    if (dropTimer >= dropInterval) {
      dropTimer = 0;
      dropInterval = 20 + Math.floor(Math.random() * 30);
      drops.push(new Drop());
    }

    /* Update drops */
    drops = drops.filter(function(d) {
      if (d.alive) { d.update(); return true; }
      return false;
    });

    /* Update ripples */
    ripples = ripples.filter(function(r) {
      if (r.alive) { r.update(); return true; }
      return false;
    });

    /* Update splashes */
    splashes = splashes.filter(function(s) {
      if (s.alive) { s.update(); return true; }
      return false;
    });

    /* Animate ambient particles */
    ambients.forEach(function(m) {
      m.position.x += m.userData.vx;
      m.position.y += m.userData.vy;
      // Wrap around
      if (m.position.x >  W/2) m.position.x = -W/2;
      if (m.position.x < -W/2) m.position.x =  W/2;
      if (m.position.y >  H/2) m.position.y = -H/2;
      if (m.position.y < -H/2) m.position.y =  H/2;
    });

    renderer.render(scene, camera);
  }

  animate();
  console.log('💧 Drop animation running');
})();
</script>

'''

# Insert before the treatments carousel section
insert_before = '<!-- no background switching JS needed -->\n<!-- TREATMENTS CARD CAROUSEL'
if insert_before in content:
    content = content.replace(insert_before, drop_section + insert_before)
    print('Inserted drop animation before treatments carousel')
else:
    # Try alternate
    insert_before2 = '<!-- TREATMENTS CARD CAROUSEL'
    idx = content.find(insert_before2)
    if idx != -1:
        content = content[:idx] + drop_section + content[idx:]
        print('Inserted drop animation before treatments carousel (alt)')
    else:
        print('ERROR: Could not find insertion point')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done!')

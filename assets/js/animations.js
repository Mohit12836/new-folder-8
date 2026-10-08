/**
 * ============================================================================
 * BELUBEARI EXIM INDUSTRIAL SOLUTIONS - GOD-LEVEL ANIMATION ENGINE JS
 * Vanilla JS, Zero-Bloat, 60fps GPU-Accelerated Hardware Motion
 * ============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  initSitePreloader();
  initFacebookHeroSlider();
  initBrandBannerSlider();
  initScrollReveal();
  initOdometerCounters();
  init3DTiltAndSpotlight();
  initHeroParticleCanvas();
  initMagneticButtons();
  initLiveSocialProofToast();
  initProductGallerySwitcher();
  initSoundEffects();
});

/* --------------------------------------------------------------------------
 * 1. SCROLL-DRIVEN REVEAL OBSERVER
 * -------------------------------------------------------------------------- */
function initScrollReveal() {
  const revealElements = document.querySelectorAll('.reveal-init');
  if (!revealElements.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        obs.unobserve(entry.target);
      }
    });
  }, {
    root: null,
    rootMargin: '0px 0px -40px 0px',
    threshold: 0.12
  });

  revealElements.forEach(el => observer.observe(el));
}

/* --------------------------------------------------------------------------
 * 2. LIVE ODOMETER NUMBER COUNTER
 * -------------------------------------------------------------------------- */
function initOdometerCounters() {
  const counters = document.querySelectorAll('[data-counter-target]');
  if (!counters.length) return;

  const countObserver = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseFloat(el.getAttribute('data-counter-target')) || 0;
        const prefix = el.getAttribute('data-counter-prefix') || '';
        const suffix = el.getAttribute('data-counter-suffix') || '';
        const duration = parseInt(el.getAttribute('data-counter-duration')) || 1800;
        
        let startTimestamp = null;
        const step = (timestamp) => {
          if (!startTimestamp) startTimestamp = timestamp;
          const progress = Math.min((timestamp - startTimestamp) / duration, 1);
          // Ease-out cubic formula
          const easeOut = 1 - Math.pow(1 - progress, 3);
          const current = Math.floor(easeOut * target);
          
          el.innerText = `${prefix}${current.toLocaleString('en-IN')}${suffix}`;
          if (progress < 1) {
            window.requestAnimationFrame(step);
          } else {
            el.innerText = `${prefix}${target.toLocaleString('en-IN')}${suffix}`;
          }
        };
        window.requestAnimationFrame(step);
        obs.unobserve(el);
      }
    });
  }, { threshold: 0.3 });

  counters.forEach(c => countObserver.observe(c));
}

/* --------------------------------------------------------------------------
 * 3. 3D TILT & MOUSE SPOTLIGHT ENGINE
 * -------------------------------------------------------------------------- */
function init3DTiltAndSpotlight() {
  const tiltCards = document.querySelectorAll('.tilt-card, .spotlight-card, .animated-border-card');
  
  tiltCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      // Update mouse position for spotlight radial gradient
      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);

      if (card.classList.contains('tilt-card')) {
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotateX = ((y - centerY) / centerY) * -6;
        const rotateY = ((x - centerX) / centerX) * 6;
        
        card.style.transform = `perspective(1000px) rotateX(${rotateX.toFixed(2)}deg) rotateY(${rotateY.toFixed(2)}deg) translateY(-4px)`;
      }
    });

    card.addEventListener('mouseleave', () => {
      if (card.classList.contains('tilt-card')) {
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0)';
      }
    });
  });
}

/* --------------------------------------------------------------------------
 * 4. HERO FLOATING PARTICLES CANVAS
 * -------------------------------------------------------------------------- */
function initHeroParticleCanvas() {
  const canvas = document.getElementById('hero-particle-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let width, height;
  let particles = [];
  const particleCount = window.innerWidth < 768 ? 24 : 50;

  function resize() {
    const parent = canvas.parentElement;
    width = canvas.width = parent.offsetWidth;
    height = canvas.height = parent.offsetHeight;
  }
  resize();
  window.addEventListener('resize', resize);

  class Particle {
    constructor() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.vx = (Math.random() - 0.5) * 0.6;
      this.vy = (Math.random() - 0.5) * 0.6;
      this.radius = Math.random() * 2 + 1;
      this.alpha = Math.random() * 0.5 + 0.2;
    }
    update() {
      this.x += this.vx;
      this.y += this.vy;
      if (this.x < 0 || this.x > width) this.vx *= -1;
      if (this.y < 0 || this.y > height) this.vy *= -1;
    }
    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(56, 189, 248, ${this.alpha})`;
      ctx.fill();
    }
  }

  for (let i = 0; i < particleCount; i++) {
    particles.push(new Particle());
  }

  function render() {
    ctx.clearRect(0, 0, width, height);
    for (let i = 0; i < particles.length; i++) {
      particles[i].update();
      particles[i].draw();

      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < 110) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(2, 132, 199, ${(1 - dist / 110) * 0.25})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(render);
  }
  render();
}

/* --------------------------------------------------------------------------
 * 5. MAGNETIC BUTTONS
 * -------------------------------------------------------------------------- */
function initMagneticButtons() {
  const btns = document.querySelectorAll('.btn-magnetic');
  btns.forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      btn.style.transform = `translate(${x * 0.25}px, ${y * 0.25}px)`;
    });
    btn.addEventListener('mouseleave', () => {
      btn.style.transform = 'translate(0, 0)';
    });
  });
}

/* --------------------------------------------------------------------------
 * 6. LIVE SOCIAL PROOF INQUIRY TOAST
 * -------------------------------------------------------------------------- */
function initLiveSocialProofToast() {
  const inquiries = [
    { location: "Pune, Maharashtra", text: "Automobile Plant requested quote for SKF Deep Groove Bearings", time: "3 mins ago" },
    { location: "Ahmedabad, Gujarat", text: "Textile Unit placed inquiry for Megadyne Timing Belts", time: "7 mins ago" },
    { location: "Surat, Gujarat", text: "Engineering firm ordered High-Temp Conveyor Belts", time: "12 mins ago" },
    { location: "Jamshedpur, Jharkhand", text: "Steel Works requested technical specs for Timken Bearings", time: "15 mins ago" },
    { location: "Chennai, Tamil Nadu", text: "Hydropower Plant verified stock for Industrial Oil & Grease", time: "19 mins ago" },
    { location: "Faridabad, Haryana", text: "CNC Workshop requested quote for Linear Motion Guides", time: "25 mins ago" },
    { location: "Mumbai, Maharashtra", text: "Bulk wholesale order received for Rubber Cots & Aprons", time: "32 mins ago" }
  ];

  let toast = document.getElementById('social-proof-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'social-proof-toast';
    document.body.appendChild(toast);
  }

  let index = 0;
  function showToast() {
    const item = inquiries[index];
    index = (index + 1) % inquiries.length;

    toast.innerHTML = `
      <div class="toast-icon">
        <i class="fa-solid fa-bolt text-sm"></i>
      </div>
      <div class="flex-1 min-w-0">
        <div class="flex items-center justify-between gap-2">
          <span class="text-xs font-bold text-sky-400 truncate">${item.location}</span>
          <span class="text-[10px] text-slate-400 whitespace-nowrap">${item.time}</span>
        </div>
        <p class="text-[11px] text-slate-200 line-clamp-2 mt-0.5 leading-snug">${item.text}</p>
      </div>
      <button onclick="document.getElementById('social-proof-toast').classList.remove('toast-active')" class="text-slate-400 hover:text-white text-xs ml-1 focus:outline-none">
        <i class="fa-solid fa-xmark"></i>
      </button>
    `;

    toast.classList.add('toast-active');
    setTimeout(() => {
      toast.classList.remove('toast-active');
    }, 5500);
  }

  // Initial delay 4s, then repeat every 18s
  setTimeout(() => {
    showToast();
    setInterval(showToast, 18000);
  }, 4000);
}

/* --------------------------------------------------------------------------
 * 7. PRODUCT VARIANT GALLERY LIVE SWAPPER
 * -------------------------------------------------------------------------- */
function initProductGallerySwitcher() {
  const mainStageImg = document.querySelector('.hero-stage img');
  const thumbs = document.querySelectorAll('.gallery-thumb-item img');

  if (!mainStageImg || !thumbs.length) return;

  thumbs.forEach(thumb => {
    const parentCard = thumb.closest('.gallery-thumb-item') || thumb.parentElement;
    
    function switchImg() {
      if (mainStageImg.src === thumb.src) return;
      mainStageImg.style.opacity = '0.3';
      mainStageImg.style.transform = 'scale(0.96)';
      
      setTimeout(() => {
        mainStageImg.src = thumb.src;
        mainStageImg.style.opacity = '1';
        mainStageImg.style.transform = 'scale(1)';
      }, 150);

      document.querySelectorAll('.gallery-thumb-item').forEach(c => c.classList.remove('ring-2', 'ring-[#0284c7]', 'border-[#0284c7]'));
      parentCard.classList.add('ring-2', 'ring-[#0284c7]');
    }

    parentCard.addEventListener('click', switchImg);
    parentCard.addEventListener('mouseenter', switchImg);
  });
}

/* --------------------------------------------------------------------------
 * 8. 3-SECOND CINEMATIC SITE OPENING PRELOADER
 * -------------------------------------------------------------------------- */
function initSitePreloader() {
  const preloader = document.getElementById('site-preloader');
  if (!preloader) return;

  const bar = preloader.querySelector('.preloader-progress-bar');
  const percentText = preloader.querySelector('.preloader-percent-text');

  let start = null;
  const duration = 2400; // 2.4 seconds bar fill, 3.0s total

  function frame(timestamp) {
    if (!start) start = timestamp;
    const progress = Math.min((timestamp - start) / duration, 1);
    const ease = 1 - Math.pow(1 - progress, 2.5);
    const pct = Math.floor(ease * 100);

    if (bar) bar.style.width = `${pct}%`;
    if (percentText) percentText.innerText = `${pct}%`;

    if (progress < 1) {
      window.requestAnimationFrame(frame);
    } else {
      setTimeout(() => {
        preloader.classList.add('preloader-hidden');
        setTimeout(() => {
          preloader.style.display = 'none';
        }, 600);
      }, 500);
    }
  }

  window.requestAnimationFrame(frame);

  // Instant dismissal on user click
  preloader.addEventListener('click', () => {
    preloader.classList.add('preloader-hidden');
    setTimeout(() => { preloader.style.display = 'none'; }, 600);
  });
}

/* --------------------------------------------------------------------------
 * 9. FULL-WIDTH 5-SLIDE COVER HERO SHOWCASE CONTROLLER
 * -------------------------------------------------------------------------- */
function initFacebookHeroSlider() {
  const section = document.getElementById('hero-carousel-section');
  if (!section) return;

  const slides = section.querySelectorAll('.fb-slide');
  const dots = section.querySelectorAll('.cover-dot');
  const slideCounter = document.getElementById('hero-slide-counter');
  let currentIdx = 0;
  let timer = null;

  function showSlide(index) {
    if (!slides.length) return;
    const prevIdx = currentIdx;
    currentIdx = (index + slides.length) % slides.length;

    // Previous slide stays underneath during 2s Iris mask expansion
    slides.forEach((slide, i) => {
      slide.classList.remove('prev-active');
      if (i === prevIdx && prevIdx !== currentIdx) {
        slide.classList.add('prev-active');
      }
      slide.classList.remove('active');
    });

    // Trigger 2-second Iris reveal on new active slide
    const nextSlide = slides[currentIdx];
    void nextSlide.offsetWidth; // DOM Reflow
    nextSlide.classList.add('active');

    // Clean up previous slide layer after 2s reveal completes
    setTimeout(() => {
      slides.forEach((s, i) => {
        if (i !== currentIdx) s.classList.remove('prev-active');
      });
    }, 2050);

    dots.forEach((dot, i) => {
      if (i === currentIdx) {
        dot.classList.add('active');
        dot.classList.remove('bg-slate-600');
        dot.style.width = window.innerWidth < 640 ? '16px' : '24px';
        dot.style.backgroundColor = '#0284c7';
      } else {
        dot.classList.remove('active');
        dot.classList.add('bg-slate-600');
        dot.style.width = window.innerWidth < 640 ? '4px' : '8px';
        dot.style.backgroundColor = '';
      }
    });

    if (slideCounter) {
      slideCounter.textContent = `0${currentIdx + 1} / 0${slides.length}`;
    }
  }

  window.nextHeroSlide = function() {
    showSlide(currentIdx + 1);
    startAutoPlay();
  };

  window.prevHeroSlide = function() {
    showSlide(currentIdx - 1);
    startAutoPlay();
  };

  window.goToHeroSlide = function(idx) {
    showSlide(idx);
    startAutoPlay();
  };

  function startAutoPlay() {
    stopAutoPlay();
    timer = setInterval(() => {
      showSlide(currentIdx + 1);
    }, 5000);
  }

  function stopAutoPlay() {
    if (timer) clearInterval(timer);
  }

  // Touch swipe support for mobile auto-fit
  let touchStartX = 0;
  let touchEndX = 0;

  section.addEventListener('touchstart', (e) => {
    touchStartX = e.changedTouches[0].screenX;
    stopAutoPlay();
  }, { passive: true });

  section.addEventListener('touchend', (e) => {
    touchEndX = e.changedTouches[0].screenX;
    const diff = touchEndX - touchStartX;
    if (Math.abs(diff) > 45) {
      if (diff < 0) {
        showSlide(currentIdx + 1); // Swipe left -> Next
      } else {
        showSlide(currentIdx - 1); // Swipe right -> Prev
      }
    }
    startAutoPlay();
  }, { passive: true });

  section.addEventListener('mouseenter', stopAutoPlay);
  section.addEventListener('mouseleave', startAutoPlay);

  startAutoPlay();
}

/* --------------------------------------------------------------------------
 * MOBILE NAVIGATION DRAWER CONTROLLER
 * -------------------------------------------------------------------------- */
function toggleMobileNavDrawer() {
  const drawer = document.getElementById('mobile-nav-drawer');
  const icon = document.getElementById('mobile-menu-icon');
  if (!drawer) return;
  drawer.classList.toggle('hidden');
  if (icon) {
    if (drawer.classList.contains('hidden')) {
      icon.className = 'fa-solid fa-bars text-lg text-slate-800';
    } else {
      icon.className = 'fa-solid fa-xmark text-lg text-[#0284c7]';
    }
  }
}
window.toggleMobileNavDrawer = toggleMobileNavDrawer;

/* --------------------------------------------------------------------------
 * 10. UNDER-NAVBAR ANIMATED BRAND PICTURE CAROUSEL
 * -------------------------------------------------------------------------- */
function initBrandBannerSlider() {
  const slider = document.getElementById('brand-hero-slider');
  if (!slider) return;

  const slides = slider.querySelectorAll('.brand-slide');
  const dots = slider.querySelectorAll('.brand-slider-dot');
  const prevBtn = slider.querySelector('.brand-slider-prev');
  const nextBtn = slider.querySelector('.brand-slider-next');

  if (!slides.length) return;

  let current = 0;
  let timer = null;

  function showSlide(index) {
    slides.forEach((s, i) => {
      s.classList.toggle('is-active', i === index);
    });
    dots.forEach((d, i) => {
      d.classList.toggle('is-active', i === index);
    });
    current = index;
  }

  function nextSlide() {
    let next = (current + 1) % slides.length;
    showSlide(next);
  }

  function prevSlide() {
    let prev = (current - 1 + slides.length) % slides.length;
    showSlide(prev);
  }

  function startAutoPlay() {
    stopAutoPlay();
    timer = setInterval(nextSlide, 4500);
  }

  function stopAutoPlay() {
    if (timer) clearInterval(timer);
  }

  if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); startAutoPlay(); });
  if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); startAutoPlay(); });

  dots.forEach((dot, idx) => {
    dot.addEventListener('click', () => {
      showSlide(idx);
      startAutoPlay();
    });
  });

  slider.addEventListener('mouseenter', stopAutoPlay);
  slider.addEventListener('mouseleave', startAutoPlay);

  startAutoPlay();
}

/* --------------------------------------------------------------------------
 * 11. PROCEDURAL WEB AUDIO SOUND SYNTHESIZER (Magical Audio Feedback)
 * -------------------------------------------------------------------------- */
let audioCtx = null;

function getAudioContext() {
  if (!audioCtx) {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    if (AudioContext) audioCtx = new AudioContext();
  }
  if (audioCtx && audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
  return audioCtx;
}

// Gentle harmonic chime on hover
function playHoverSound() {
  try {
    const ctx = getAudioContext();
    if (!ctx) return;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = 'triangle';
    osc.frequency.setValueAtTime(540, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.08);

    gain.gain.setValueAtTime(0.035, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.08);

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start();
    osc.stop(ctx.currentTime + 0.08);
  } catch (e) {}
}

// Crisp glass click on tap / click
function playClickSound() {
  try {
    const ctx = getAudioContext();
    if (!ctx) return;
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(750, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(180, ctx.currentTime + 0.09);

    gain.gain.setValueAtTime(0.06, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.09);

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start();
    osc.stop(ctx.currentTime + 0.09);
  } catch (e) {}
}

function initSoundEffects() {
  const interactiveElements = document.querySelectorAll('.box-btn-glowing, .btn-shine, .btn-shimmer, nav a, .pulse-ring-container');
  interactiveElements.forEach(el => {
    el.addEventListener('mouseenter', playHoverSound, { passive: true });
    el.addEventListener('click', playClickSound, { passive: true });
  });
}

document.addEventListener('DOMContentLoaded', () => {
  const button = document.querySelector('#hamburger');
  const menu = document.querySelector('#mobile-nav');
  if (!button || !menu) return;
  const setOpen = (open, focus = false) => {
    menu.hidden = !open;
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    if (focus) button.focus();
  };
  button.addEventListener('click', () => setOpen(menu.hidden));
  document.addEventListener('click', event => {
    if (!menu.hidden && !menu.contains(event.target) && !button.contains(event.target)) setOpen(false);
  });
  menu.addEventListener('click', event => { if (event.target.closest('a')) setOpen(false); });
  document.addEventListener('keydown', event => { if (event.key === 'Escape' && !menu.hidden) setOpen(false, true); });
  const desktop = window.matchMedia('(min-width: 801px)');
  desktop.addEventListener('change', event => { if (event.matches) setOpen(false); });
});

document.addEventListener('DOMContentLoaded', () => {
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('[data-publication-carousel]').forEach(carousel => {
    const slides = [...carousel.querySelectorAll('.research-paper')];
    const controls = carousel.querySelector('.paper-controls');
    const toggle = carousel.querySelector('[data-paper-toggle]');
    const count = carousel.querySelector('.paper-count');
    let index = 0;
    let paused = reducedMotion.matches;
    let visible = false;
    let hovered = false;
    let timer;
    const schedule = () => {
      clearTimeout(timer);
      toggle.textContent = paused ? 'Play' : 'Pause';
      toggle.setAttribute('aria-label', paused ? 'Start automatic publication rotation' : 'Pause automatic publication rotation');
      if (!paused && visible && !hovered && !document.hidden) {
        timer = setTimeout(() => show(index + 1), 9000);
      }
    };
    const show = next => {
      index = (next + slides.length) % slides.length;
      slides.forEach((slide, i) => {
        slide.classList.toggle('is-active', i === index);
        slide.setAttribute('aria-hidden', String(i !== index));
        slide.inert = i !== index;
      });
      count.textContent = `${index + 1} / ${slides.length}`;
      schedule();
    };
    carousel.classList.add('is-enhanced');
    controls.hidden = false;
    carousel.querySelector('[data-paper-prev]').addEventListener('click', () => { paused = true; show(index - 1); });
    carousel.querySelector('[data-paper-next]').addEventListener('click', () => { paused = true; show(index + 1); });
    toggle.addEventListener('click', () => { paused = !paused; schedule(); });
    carousel.addEventListener('mouseenter', () => { hovered = true; schedule(); });
    carousel.addEventListener('mouseleave', () => { hovered = false; schedule(); });
    carousel.addEventListener('focusin', event => {
      if (event.target !== toggle) { paused = true; schedule(); }
    });
    document.addEventListener('visibilitychange', schedule);
    reducedMotion.addEventListener('change', () => { if (reducedMotion.matches) { paused = true; schedule(); } });
    new IntersectionObserver(entries => {
      visible = entries[0].isIntersecting;
      schedule();
    }, {threshold:0.25}).observe(carousel);
    show(0);
  });
});

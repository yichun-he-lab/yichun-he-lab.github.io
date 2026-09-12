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

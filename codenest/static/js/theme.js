const root = document.documentElement;
const saved = localStorage.getItem('theme') || 'light';
root.setAttribute('data-theme', saved);

const btn = document.getElementById('theme-toggle');
if (btn) {
  btn.addEventListener('click', () => {
    const next = root.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    root.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
  });
}

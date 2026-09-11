(function () {
  var root = document.documentElement;

  var themeBtn = document.getElementById('theme-toggle');
  function isDark() {
    var t = root.dataset.theme;
    if (t) return t === 'dark';
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function syncThemeLabel() { themeBtn.textContent = isDark() ? 'Light' : 'Dark'; }
  themeBtn.addEventListener('click', function () {
    var next = isDark() ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('qme-theme', next); } catch (e) {}
    syncThemeLabel();
  });
  syncThemeLabel();

  Array.prototype.slice.call(document.querySelectorAll('.copy-cmd')).forEach(function (btn) {
    var timer;
    btn.addEventListener('click', function () {
      var cmd = btn.getAttribute('data-cmd');
      if (navigator.clipboard) navigator.clipboard.writeText(cmd).catch(function () {});
      btn.textContent = 'Copied';
      clearTimeout(timer);
      timer = setTimeout(function () { btn.textContent = 'Copy'; }, 1800);
    });
  });

  var form = document.getElementById('invite-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      }).then(function (r) {
        if (!r.ok) throw new Error('send failed');
        form.hidden = true;
        document.getElementById('invite-done').hidden = false;
      }).catch(function () {
        btn.disabled = false;
        btn.textContent = 'Something went wrong. Try again.';
      });
    });
  }
})();

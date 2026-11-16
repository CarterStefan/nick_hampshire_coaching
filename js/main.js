// Solidify the fixed navbar once the page is scrolled. A 24px sentinel at the
// top of the page stops intersecting as soon as the user scrolls past it.
(function () {
  var navbar = document.querySelector('.navbar');
  if (!navbar || !('IntersectionObserver' in window)) return;
  var sentinel = document.createElement('div');
  sentinel.setAttribute('aria-hidden', 'true');
  sentinel.style.cssText = 'position:absolute;top:0;left:0;width:1px;height:24px;pointer-events:none';
  document.body.prepend(sentinel);
  new IntersectionObserver(function (entries) {
    navbar.classList.toggle('scrolled', !entries[0].isIntersecting);
  }).observe(sentinel);
})();

// Contact form: inline errors instead of browser bubbles, then a sending state.
(function () {
  var form = document.querySelector('.contact-form form');
  if (!form) return;
  form.addEventListener('submit', function (event) {
    if (!form.checkValidity()) {
      event.preventDefault();
      form.classList.add('was-validated');
      var firstInvalid = form.querySelector(':invalid');
      if (firstInvalid) firstInvalid.focus();
      return;
    }
    var button = form.querySelector('button[type="submit"]');
    button.disabled = true;
    button.textContent = 'Sending…';
  });
})();

// YouTube facade: load the player only when someone asks for it.
(function () {
  document.querySelectorAll('.video-facade-link').forEach(function (link) {
    link.addEventListener('click', function (event) {
      event.preventDefault();
      var iframe = document.createElement('iframe');
      iframe.src = 'https://www.youtube-nocookie.com/embed/' + link.dataset.videoId + '?autoplay=1';
      iframe.title = link.getAttribute('aria-label').replace('Play video: ', '');
      iframe.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      iframe.allowFullscreen = true;
      link.replaceWith(iframe);
      iframe.focus();
    });
  });
})();

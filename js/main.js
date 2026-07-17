// Solidify the fixed navbar once the page is scrolled.
(function () {
  var navbar = document.querySelector('.navbar');
  if (!navbar) return;
  function update() {
    navbar.classList.toggle('scrolled', window.scrollY > 24);
  }
  update();
  window.addEventListener('scroll', update, { passive: true });
})();

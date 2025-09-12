// translate.js

function googleTranslateElementInit() {
  new google.translate.TranslateElement(
    { pageLanguage: 'en', includedLanguages: 'en,es' },
    'google_translate_element'
  );
}

function translatePage(lang) {
  setCookie('googtrans', '/en/' + lang, 1);
  var select = document.querySelector("select.goog-te-combo");
  if (select) {
    select.value = lang;
    select.dispatchEvent(new Event("change"));
  }
}

function setCookie(name, value, days) {
  var d = new Date();
  d.setTime(d.getTime() + days * 24 * 60 * 60 * 1000);
  document.cookie = name + "=" + value + ";" + "expires=" + d.toUTCString() + ";path=/";
}

// Optional: auto-apply saved language on load
window.addEventListener("load", function () {
  var select = document.querySelector("select.goog-te-combo");
  var cookieLang = getCookie("googtrans");
  if (cookieLang && select) {
    var lang = cookieLang.split("/")[2]; // extract language code
    select.value = lang;
    select.dispatchEvent(new Event("change"));
  }
});

function getCookie(name) {
  var match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
  if (match) return match[2];
  return null;
}

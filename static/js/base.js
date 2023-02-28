let href = document.location.href
let aArray = document.querySelectorAll('a.nav-link')
aArray.forEach(function(a) {
  if (a.href == href) {
    a.classList.add("active");
  }
})
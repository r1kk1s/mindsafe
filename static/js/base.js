let aArray = document.querySelectorAll('a.nav-link')
aArray.forEach((a) => {
  if (a.href == document.location.href) {
    a.classList.add("active");
  }
})

let navbar = document.querySelector('nav')
function someFunc() {
  let w = window.innerWidth;
  if (w < 1100) {
    navbar.classList.remove("navbar-expand-lg");
  }
}

window.addEventListener('resize', function() {
  someFunc();
});
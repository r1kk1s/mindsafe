let aArray = document.querySelectorAll('a.nav-link')
aArray.forEach((a) => {
  if (a.href == document.location.href) {
    a.classList.add("active");
  }
})

let aArrayFooter = document.querySelectorAll('a.nav-link.px-2')
aArray.forEach((a) => {
  if (a.href == document.location.href) {
    a.classList.remove("text-muted");
  }
})

let navbar = document.querySelector('nav');
function hideNavbar() {
  if (window.innerWidth < 1250) {
    navbar.classList.remove("navbar-expand-lg");
  }

};
function showNavbar() {
  if (window.innerWidth > 1250 && !navbar.classList.contains("navbar-expand-lg")) {
    navbar.classList.add("navbar-expand-lg");
  }
};

let auth = document.querySelector('.auth')
function hideAuth() {
  if (window.innerWidth < 710) {
    auth.classList.add("collapse", "navbar-collapse");
    auth.setAttribute("id", "navbarCollapse");
  }
}
function showAuth() {
  if (window.innerWidth > 710) {
    auth.classList.remove("collapse", "navbar-collapse");
    auth.removeAttribute("id");
  }
}

document.addEventListener('DOMContentLoaded', function() {
  hideNavbar();
});

window.addEventListener('resize', function() {
  showNavbar();
  showAuth();
  hideNavbar();
  hideAuth();
});



let aArray = document.querySelectorAll('a.nav-link')
aArray.forEach((a) => {
  if (a.href == document.location.href) {
    a.classList.add("active");
  }
})

let navbar = document.querySelector('nav');
function hideNavbar() {
  if (window.innerWidth < 1150) {
    navbar.classList.remove("navbar-expand-lg");
    aArray.forEach((a) => {
      a.classList.add("coll");
    })
  }

};
function showNavbar() {
  if (window.innerWidth > 1150 && !navbar.classList.contains("navbar-expand-lg")) {
    navbar.classList.add("navbar-expand-lg");
  }
};

document.addEventListener('DOMContentLoaded', function() {
  hideNavbar();
});

window.addEventListener('resize', function() {
  showNavbar();
  hideNavbar();
});

// let dateTimeInput = document.querySelector('input.datetimepicker');
// dateTimeInput.setAttribute("readonly", true)


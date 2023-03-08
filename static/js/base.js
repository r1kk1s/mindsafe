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
  if (window.innerWidth < 1116) {
    navbar.classList.remove("navbar-expand-lg");
  }

};

function showNavbar() {
  if (window.innerWidth > 1116 && !navbar.classList.contains("navbar-expand-lg")) {
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

// function onEntry(entry) {
//   entry.forEach(change => {
//     if (change.isIntersecting) {
//       change.target.classList.remove('not-visible');
//     }
//   });
// }
// let options = { threshold: [0.5] };
// let observer = new IntersectionObserver(onEntry, options);
// let elements = document.querySelectorAll('.not-visible');
// for (let elm of elements) {
//   observer.observe(elm);
// }
// for (let rec of records) {
//   observer.observe(rec);
// }
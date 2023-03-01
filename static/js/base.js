let aArray = document.querySelectorAll('a.nav-link')
aArray.forEach((a) => {
  if (a.href == document.location.href) {
    a.classList.add("active");
  }
})
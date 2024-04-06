
const expand_btn = document.querySelector(".expand-btn");
const img = expand_btn.querySelector("img");
const sidebarTopH1 = document.querySelector(".sidebar-top h1");

let activeIndex;

expand_btn.addEventListener("click", () => {
  document.body.classList.toggle("collapsed");
  // Directly toggle the display property of the h1 element
  if (document.body.classList.contains("collapsed")) {
    sidebarTopH1.style.display = "none";
  } else {
    sidebarTopH1.style.display = ""; // Revert to the default by clearing the inline style
  }
});

const current = window.location.href;

const allLinks = document.querySelectorAll(".sidebar-links a");
const topLinks = document.querySelectorAll(".sidebar-top a");

allLinks.forEach((elem) => {
  elem.addEventListener('click', function() {
    const hrefLinkClick = elem.href;

    allLinks.forEach((link) => {
      if (link.href == hrefLinkClick){
        link.classList.add("active");
      } else {
        link.classList.remove('active');
      }
    });
    

  })
});



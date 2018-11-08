const chk = document.getElementById("check-theme");
const bg = document.getElementsByTagName("body")[0];

if (!localStorage.getItem("theme")) localStorage.setItem("theme", "light");
chk.checked = localStorage.getItem("theme") === "dark";

getTheme = () => {
  localStorage.setItem("theme", chk.checked ? "dark" : "light");
  bg.className = localStorage.getItem("theme");
};

bg.className = localStorage.getItem("theme");

$(() => {
  $("#accordion").accordion();
});

// Loading Page

animateValue = (id, start, end, duration) => {
  let range = end - start,
    current = start,
    increment = end > start ? 1 : -1,
    stepTime = Math.abs(Math.floor(duration / range)),
    obj = $(id);

  let timer = setInterval(() => {
    current += increment;
    $(obj).text(current + "%");
    if (current == end) clearInterval(timer);
  }, stepTime);
};

const width = 100,
  perfData = window.performance.timing,
  EstimatedTime = -(perfData.loadEventEnd - perfData.navigationStart),
  time = parseInt((EstimatedTime / 1000) % 60) * 100;

$(".loadbar").animate({ width: width + "%" }, time);

const PercentageID = $("#percent"),
  start = 0,
  end = 100,
  duration = time;

animateValue(PercentageID, start, end, duration);

setTimeout(() => {
  $(".preloader-wrap").fadeOut(300);
}, time);

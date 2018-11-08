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

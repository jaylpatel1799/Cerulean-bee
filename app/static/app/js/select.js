var select = document.querySelector("select");
const value = select.getAttribute("aria-selected");

select.value = value;

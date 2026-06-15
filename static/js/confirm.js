document.addEventListener("click", function (e) {
  const el = e.target.closest("[data-confirm]");
  if (!el) return;

  const msg = el.getAttribute("data-confirm") || "¿Seguro que deseas eliminar?";
  if (!confirm(msg)) e.preventDefault();
});


function emite_alerta() {
  alert("Vem que vem!!!");
}

logo = document.getElementsByTagName("img")[0];

logo.onclick = emite_alerta;

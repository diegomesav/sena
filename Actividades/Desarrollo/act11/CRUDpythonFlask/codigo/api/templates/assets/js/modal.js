function agregar() {
  clean()
  abrirFormulario()
}

function abrirFormulario() {
    htmlModal = document.getElementById("modal");
    htmlModal.setAttribute("class", "modale opened");
  }
  
  function cerrarModal() {
    htmlModal = document.getElementById("modal");
    htmlModal.setAttribute("class", "modale");
  } 

  function clean() {
    document.getElementById('txtId').value = ''
    document.getElementById('txtUsuario').value = ''
    document.getElementById('txtPassword').value = ''
  }
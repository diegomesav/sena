document.addEventListener("DOMContentLoaded", init);
const URL_API = "http://localhost:3000/api/";

//creamos una variable global para almacenar usuarios
let usuarios = [];

function init() {
    verUsuarios();
}

// Funcion ver usuarios ******************************************
async function verUsuarios() {
    // obtenemos la ruta
    let url = URL_API + "usuarios";

     // realizamos peticion
    let response = await fetch(url, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
    });
    usuarios = await response.json();

    // generamos estructura HTML
    let html = "";
    for (usuario of usuarios) {
        let row = `
        <tr>+2.
            <td>${usuario.id}</td>
            <td>${usuario.usuario}</td>
            <td>${usuario.password}</td>
            <td>
                <a href="#" onclick="editarUsuario(${usuario.id})" class="myButton">Editar</a>
                <a href="#" onclick="eliminarUsuario(${usuario.id})" class="btnDelete">Eliminar</a>
            </td>
        </tr>`;
        html = html + row;
    }

    //añadimos html a la vista
    document.querySelector("#usuarios > tbody").outerHTML = html;
}

// funcion guardar usuarios ************************************
async function guardarUsuario() {
    // generamos estructura JSON
    let data = {
        usuario: document.getElementById("txtUsuario").value,
        password: document.getElementById("txtPassword").value,
    };

    let id = document.getElementById("txtId").value;

    // validamos si se desea modificar usuario
    if (id != "") {
        data.id = id;
    }

    // enviamos la peticion al servidor
    let url = URL_API + "usuarios";
    let response = await fetch(url, {
        method: "POST",
        body: JSON.stringify(data),
        headers: {
        "Content-Type": "application/json",
        },
    });

    let respuesta = await response.json();

    if (respuesta[0] == "True") {
        alert("Usuario Guardado exitosamente");
    } else {
        alert("Hubo un error");
    }

    //recargamos la pagina para ver los cambios
     window.location.reload();
}

// funcion eliminar usuarios *************************************
async function eliminarUsuario(id) {
    respuesta = confirm("¿Está seguro de eliminarlo?");
    if (respuesta) {
        var url = URL_API + "usuarios/" + id;
        let response = await fetch(url, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
        });

        let respuesta = await response.json();

        if (respuesta[0] == "True") {
        alert("Usuario Eliminado exitosamente");
        } else {
        alert("Hubo un error");
        }
        window.location.reload();
    }
}

// funcion editar usuario ***************************************
function editarUsuario(id) {
    abrirFormulario();
    var usuario = usuarios.find((x) => x.id == id);
    document.getElementById("txtId").value = usuario.id;
    document.getElementById("txtUsuario").value = usuario.usuario;
    document.getElementById("txtPassword").value = usuario.password;
}

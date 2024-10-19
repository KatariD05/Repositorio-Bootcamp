let x = "Iniciar sesión"

const cambio = (x) => {
    x.innerText = "Cerrar Sesion";
}

let contador = 0;

const meGusta = (element) => {
    contador++;
    element.innerText = contador + " me gusta";
};

const hide = (x) => {
    x.remove();
}
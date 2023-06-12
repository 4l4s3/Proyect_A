// Crea una función para que se muestre el contenido desplegable del registro y inicio para el usuario
const tarjeta = document.getElementById('tarjeta')
const enlaceTarjeta = document.getElementById('enlaceTarjeta')
const cerrarTarjeta = document.getElementById('enlaceTarjeta')
var abierto =  false;
function mostrarTarjetaUser(event) {
    event.preventDefault(); // Evitar el comportamiento predeterminado del enlace
    tarjeta.style.display = 'block'; // Mostrar la tarjeta
    abierto = true;
  }

  // Función para cerrar la tarjeta
  function cerrar() {
    tarjeta.style.display = 'none'; // Ocultar la tarjeta
    abierto = false
  }

  // Agregar event listener al enlace para mostrar la tarjeta o cerrarlaW

  enlaceTarjeta.addEventListener('click',function(event) {
   if (abierto === false){
    mostrarTarjetaUser(event)
   }else{
    cerrar()
   }
  });
  

// Crea una función para que se muestre el contenido desplegable del nav editanto boostrap
const navButton = document.querySelector('.navbar-toggler');
const navDropdown = document.querySelector('.nav-dropdown');

navButton.addEventListener('click', function() {
    navDropdown.classList.toggle('show');
});

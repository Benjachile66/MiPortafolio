/**
 * Easy selector helper function
 */
const select = (el, all = false) => {
  el = el.trim();
  if (all) {
    return [...document.querySelectorAll(el)];
  } else {
    return document.querySelector(el);
  }
};

const typed = select('.typed');

if (typed) {
  let typed_strings = typed.getAttribute('data-typed-items');
  typed_strings = typed_strings.split(',');
  new Typed('.typed', {
    strings: typed_strings,
    loop: true,
    typeSpeed: 100,
    backSpeed: 50,
    backDelay: 2000,
  });
}


 // Obtener una referencia al elemento <div> que contiene la imagen de fondo
const backgroundDiv = document.getElementById('bckground');

// Arreglo con las rutas de las imágenes de fondo
const backgroundImages = [
  "static/CSS/img/background1.jpg",
  "static/CSS/img/background2.jpg",
];

// Función para obtener un número aleatorio entre 0 y el número de imágenes disponibles
function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

// Obtener un índice aleatorio para seleccionar una imagen aleatoria del arreglo
const randomIndex = getRandomInt(backgroundImages.length);

// Obtener la ruta de la imagen aleatoria
const randomBackgroundImage = backgroundImages[randomIndex];

// Establecer la imagen de fondo en el <div>
//backgroundDiv.style.backgroundImage = `url("${randomBackgroundImage}")`;
function changeBackgroundImage() {
  const randomBackgroundImage = backgroundImages[Math.floor(Math.random() * backgroundImages.length)];
  document.body.style.backgroundImage = `url("${randomBackgroundImage}")`;

  // Agrega una clase al body según el background image seleccionado
  if (randomBackgroundImage.includes("background1.jpg")) {
    document.body.classList.add("background-1");
  } else if (randomBackgroundImage.includes("background2.jpg")) {
    document.body.classList.add("background-2");
  }
}

// Llamamos a la función para cambiar el background image al cargar la página
changeBackgroundImage();

console.log(randomIndex)
console.log(backgroundDiv.style.backgroundImage)

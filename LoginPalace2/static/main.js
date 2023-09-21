//Esta declaración hace que se puedan guardar los contadores de likes
const likeCounts = {};

//Esta función carga los el número del contador que hay almacenado, en dado que no lo haya se inicia desde 0
function loadLikes() {
    //Al ser muchos botones con el mismo estilo css, hasta ahora 12, con js realizar una lista de todos esos botones
    const heartButtons = document.querySelectorAll(".heart-btn");

    //Este se encarga de recorrer cada botón al cargar la pagina para ver cuanto es el npumero de contadores en el almacenamiento
    heartButtons.forEach(button => {
        const imageId = button.dataset.imageId;
        const storedLikes = localStorage.getItem(imageId);

        if (storedLikes) {
            likeCounts[imageId] = parseInt(storedLikes);
            updateLikeCount(imageId);
        } else {
            likeCounts[imageId] = 0;
        }
    });
}

//Con esta función se actualiza el contador de corazon
function updateLikeCount(imageId) {
    const likeCountElement = document.querySelector(`[data-image-id="${imageId}"] .numb`);
    likeCountElement.textContent = likeCounts[imageId];
}

//Esta función maneja el clic al botón donde, incrementa, actualiza y almacena el contador de corazon
function handleLikeClick(imageId) {
    const button = document.querySelector(`[data-image-id="${imageId}"]`);
    if (button.classList.contains("liked")) {
        likeCounts[imageId]--;
    } else {
        likeCounts[imageId]++;
    }
    button.classList.toggle("liked");
    updateLikeCount(imageId);
    //Se guarda el contador de corazones en el almacenamiento de la compu
    localStorage.setItem(imageId, likeCounts[imageId].toString());
}

// Se agrega un event listener (escuchador) a todos los botones de corazones
const heartButtons = document.querySelectorAll(".heart-btn");
heartButtons.forEach(button => {
    const imageId = button.dataset.imageId;
    button.addEventListener("click", () => {
        handleLikeClick(imageId);
    });
});

// esto carga los contadores de corazones al volver a cargar la página
loadLikes();

// Selecciona el botón o enlace para abrir el popup y el propio popup
const openPopupButton = document.querySelector(".open-popup");
const popup = document.querySelector(".popup");

// Verifica si los elementos se encontraron
if (openPopupButton && popup) {
    // Agrega un evento de clic al botón o enlace
    openPopupButton.addEventListener("click", (event) => {
        event.preventDefault(); // Evita que el enlace siga su href por defecto
        popup.style.display = "block"; // Muestra el popup cambiando su estilo
    });
}



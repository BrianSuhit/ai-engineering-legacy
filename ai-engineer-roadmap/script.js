// --- LÓGICA DE CARGA DE DATOS ---
let contentDatabase = {};

document.addEventListener('DOMContentLoaded', () => {
    fetch('roadmap.json')
        .then(response => response.json())
        .then(data => {
            contentDatabase = data;
        })
        .catch(error => {
            console.error("Error al cargar el contenido del roadmap:", error);
            contentDatabase.default = {
                title: "Error de Carga",
                body: "<p>No se pudo cargar la información. Por favor, intenta recargar la página.</p>"
            };
        });
});


// --- LÓGICA DEL MODAL ---
const modal = document.getElementById('modal');
const modalTitle = document.getElementById('modal-title');
const modalBody = document.getElementById('modal-body');

// Función que llama el HTML
function openModal(key) {
    // Buscamos en la base de datos, si no existe, usamos default
    const data = contentDatabase[key] || contentDatabase["default"];

    modalTitle.innerText = data.title;
    modalBody.innerHTML = data.body;
    
    modal.style.display = 'flex'; 
}

function closeModal() {
    modal.style.display = 'none'; 
}

// Cerrar si clic afuera
window.addEventListener('click', (e) => {
    if (e.target === modal) {
        closeModal();
    }
});
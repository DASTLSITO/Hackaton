// Llamar a la API y mostrar la imagen en un elemento <img>
const imgElement = document.getElementById('miImagen'); // <img id="miImagen">

fetch('http://127.0.0.1:8000/generateImg')
  .then(response => {
    if (!response.ok) {
      throw new Error('Error al obtener la imagen');
    }
    return response.blob(); // Convertir la respuesta a un Blob (para imágenes)
  })
  .then(blob => {
    const imageUrl = URL.createObjectURL(blob);
    imgElement.src = imageUrl; // Asignar la URL de la imagen al elemento <img>
  })
  .catch(error => {
    console.error('Error:', error);
  });



  document.getElementById('miImagen').addEventListener('click', function(event) {
    // Obtiene las coordenadas relativas a la imagen
    const rect = this.getBoundingClientRect();
    
    // Calcula las coordenadas (X, Y) dentro de la imagen
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;
    
    console.log(`Coordenadas (X, Y): ${x}, ${y}`);
    
    // Opcional: Muestra las coordenadas en la página
    const coordenadasElement = document.createElement('div');
    coordenadasElement.textContent = `Click en: ${Math.round(x)}, ${Math.round(y)}`;
    coordenadasElement.style.position = 'absolute';
    coordenadasElement.style.left = `${event.clientX}px`;
    coordenadasElement.style.top = `${event.clientY}px`;
    coordenadasElement.style.background = 'white';
    coordenadasElement.style.padding = '5px';
    coordenadasElement.style.border = '1px solid black';
    
    document.body.appendChild(coordenadasElement);
    
    // Elimina el elemento después de 2 segundos (opcional)
    setTimeout(() => {
        document.body.removeChild(coordenadasElement);
    }, 2000);
});
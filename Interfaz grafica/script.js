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
const img = this;
            const rect = img.getBoundingClientRect();
            
            // Dimensiones del área de mapa (excluyendo márgenes)
            const mapWidth = 118.4 - 108; // 9° de ancho
            const mapHeight = 31.7 - 22.2;      // 9° de alto
            
            // Margenes estimados (ajustar según tu imagen)
            const marginLeft = 0.15 * rect.width;   // 15% del ancho
            const marginRight = 0.15 * rect.width;
            const marginTop = 0.15 * rect.height;   // 15% del alto
            const marginBottom = 0.15 * rect.height;
            
            // Área clickeable
            const clickableWidth = rect.width - marginLeft - marginRight;
            const clickableHeight = rect.height - marginTop - marginBottom;
            
            // Coordenadas relativas al área de mapa
            const x = event.clientX - rect.left - marginLeft;
            const y = event.clientY - rect.top - marginTop;
            
            // Solo calcular si el click está dentro del área del mapa
            const lon = 118.4 - (x / clickableWidth) * mapWidth;
                
                // Calcular latitud (eje Y - invertido porque el Y de la imagen va hacia abajo)
                const lat= 31.7 - (y / clickableHeight) * mapHeight;

                fetch(`http://127.0.0.1:8000/getPointsByCoord?lat=${lat}&lon=-${lon}`)
                .then(async (response) => {
                  if (!response.ok) {
                    throw new Error('Error al obtener la imagen');
                  }
                  return response.json(); // Convertir la respuesta a un Blob (para imágenes)
                })
                .then(data => {
                  // Decodificar la imagen
                  const imageUrl = `data:image/png;base64,${data.image}`;
                  document.getElementById('miImagen').src = imageUrl;

                  // Mostrar datos
                  console.log("Datos recibidos:", data.datos);
                  
                    // Crear tarjeta con datos
                    const datos = data.datos;
                    document.getElementById('sidebar').innerHTML = 'Información'

                    console.log(datos)
                  for(let i = 0; i < datos.length; i++){
                    const cardHTML = `
                      <div class="card">
                        <h4>Datos de la coordenada</h4>
                        <p><strong>Fecha:</strong> ${datos[i][0]}</p>
                        <p><strong>Temperatura:</strong> ${datos[i][1]}</p>
                        <p><strong>Salinidad:</strong> ${datos[i][2]}</p>
                        <p><strong>Productividad:</strong> ${datos[i][3]}</p>
                      </div>
                    `;

                    // Insertar en el aside
                    document.getElementById('sidebar').innerHTML +=  cardHTML;
                  }
                })
                .catch(error => {
                  console.error('Error:', error);
                });
                
                // // Mostrar coordenadas
                const coordenadasElement = document.createElement('div');
                coordenadasElement.textContent = `lat: ${lon}, lon: ${lat}`;
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
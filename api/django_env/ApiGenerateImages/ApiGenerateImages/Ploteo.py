import csv
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from io import BytesIO
# Leer el archivo CSV
def generarImg():
    try:
        # Leer el archivo CSV
        with open('/home/dastl/Documents/HACKATON/api/django_env/ApiGenerateImages/ApiGenerateImages/dataset_presencias.csv', 'r') as archivo_csv:
            reader = csv.reader(archivo_csv)
            next(reader)  # Omitir encabezado (dentro del bloque with!)

            coordenadas = []
            for fila in reader:
                if len(fila) >= 2:
                    latitud = float(fila[0])
                    longitud = float(fila[1])
                    coordenadas.append([longitud, latitud])

        # Verificar que hay datos
        if not coordenadas:
            raise ValueError("El CSV no contiene coordenadas válidas")

        # Separar coordenadas
        longitudes, latitudes = zip(*coordenadas)

        # Crear el gráfico
        fig = plt.figure(figsize=(10, 5))
        ax = plt.axes(projection=ccrs.PlateCarree())
        ax.set_extent([-118.5, -108, 21, 33], crs = ccrs.PlateCarree())
        ax.add_feature(cfeature.BORDERS, linestyle=':')
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.LAND, edgecolor='black')
        ax.add_feature(cfeature.LAKES, edgecolor='black')
        ax.add_feature(cfeature.RIVERS)
        ax.gridlines(draw_labels=True)
        ax.scatter(longitudes, latitudes, color='red', marker='o', s=10, transform=ccrs.PlateCarree())

        # Guardar en un buffer de memoria (sin tocar disco)
        buffer = BytesIO()
        plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
        plt.close()
        buffer.seek(0)  # Rebobinar el buffer
        return buffer

    except Exception as e:
        print(f"Error al generar imagen: {str(e)}")
        raise  # Re-lanza la excepción para manejarla en la vista
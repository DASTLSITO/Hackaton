# import csv   # Formato del archivo Comma Separated Vector
# import matplotlib.pyplot as plt # Librería para plotear
# import cartopy.crs as ccrs # Cartopy librería para mapas
# import cartopy.feature as cfeature
from io import BytesIO
from .Ploteo import generarImg

# # Abre el archivo CSV y lee solo las filas después del encabezado
# def obtenerMapaPuntosEspecificos(lat, lon):

#     with open('/home/dastl/Documents/HACKATON/api/django_env/ApiGenerateImages/ApiGenerateImages/dataset_presencias.csv', 'r') as archivo_csv:
#         reader = csv.reader(archivo_csv)
#         # Omitir la primera línea (el encabezado)
#         next(reader)

#         coordenadas = []
#         masDatos = []

#         # Procesar las filas restantes
#         for fila in reader:
#             if len(fila) >= 2:
#                 lat_fila = float(fila[0])
#                 lon_fila = float(fila[1])
#                 lat_num = float(lat)       # Asegurar que `lat` y `lon` sean números
#                 lon_num = float(lon)
    
#                 if (lat_fila - 1 <= lat_num <= lat_fila + 1) and (lon_fila - 1 <= lon_num <= lon_fila + 1):
#                     latitud = float(fila[0])
#                     longitud = float(fila[1])
                    
#                     coordenadas.append([longitud, latitud])  # Asegúrate de que el orden sea (longitud, latitud)
#                     tiempo = fila[2]
#                     temperatura = float(fila[4])
#                     humedad = float(fila[5])
#                     presion = float(fila[6])
#                     masDatos.append([tiempo, temperatura, humedad, presion])  # Guardar los demás datos de la fila

#     # Separar las coordenadas en listas de longitud y latitud
#     if len(coordenadas) != 0:
#         longitudes, latitudes = zip(*coordenadas)

#         # Crear un gráfico con Cartopy
#         fig = plt.figure(figsize=(10, 5))
#         ax = plt.axes(projection=ccrs.PlateCarree())
#         ax.set_extent([-118.5, -108, 21, 33], crs=ccrs.PlateCarree())

#         # Añadir características del mapa
#         ax.add_feature(cfeature.BORDERS, linestyle=':')
#         ax.add_feature(cfeature.COASTLINE)
#         ax.add_feature(cfeature.LAND, edgecolor='black')
#         ax.add_feature(cfeature.LAKES, edgecolor='black')
#         ax.add_feature(cfeature.RIVERS)

#         # Graficar las coordenadas
#         ax.scatter(longitudes, latitudes, color='red', marker='o', s=10, transform=ccrs.PlateCarree())

#         buffer = BytesIO()
#         plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
#         plt.close()
#         buffer.seek(0)  # Rebobinar el buffer
#         return buffer
    
#     return generarImg()

#seleccion de puntos
import csv   #Formato del archivo Comma Separated Vector
import matplotlib.pyplot as plt #libreria para plotear
import cartopy.crs as ccrs #cartopy libreria para mapas
import cartopy.feature as cfeature

def obtenerMapaPuntosEspecificos(lat, lon):
    # Abre el archivo CSV y lee solo las filas después del encabezado
    with open('/home/dastl/Documents/HACKATON/api/django_env/ApiGenerateImages/ApiGenerateImages/dataset_presencias.csv', 'r') as archivo_csv:
        reader = csv.reader(archivo_csv)
        # Omitir la primera línea (el encabezado)
        next(reader)

        coordenadas = []
        masDatos = []
        # Procesar las filas restantes
        for fila in reader:
            lat_fila = float(fila[0])  # Convertir a float
            lon_fila = float(fila[1])
            lat_num = float(lat)       # Asegurar que `lat` y `lon` sean números
            lon_num = float(lon)
            
            if (lat_fila - 0.2 <= lat_num <= lat_fila + 0.2) and (lon_fila - 0.2 <= lon_num <= lon_fila + 0.2):

                coordenadas.append([lon_fila, lat_fila])  # Asegúrate de que el orden sea (longitud, latitud)
                print(f"{lat_fila}, {lon_fila}, {lat_num}, {lon_num}")              

                tiempo = fila[2]
                temperatura = float(fila[4])
                salinidad = float(fila[5])
                productividad = float(fila[6])
                masDatos.append([tiempo, temperatura, salinidad, productividad])  # Guardar los demás datos de la fila

    # Separar las coordenadas en listas de longitud y latitud
    if(len(coordenadas) == 0):
        return (generarImg(), [])

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
    print(longitudes, latitudes)
    ax.scatter(longitudes, latitudes, color='red', marker='o', s=10, transform=ccrs.PlateCarree())

    # Guardar en un buffer de memoria (sin tocar disco)
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
    plt.close()
    buffer.seek(0)  # Rebobinar el buffer
    return (buffer, masDatos)

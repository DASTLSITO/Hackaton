import csv
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Leer el archivo CSV
def generarImg():
    with open('/home/dastl/Documents/HACKATON/api/django_env/ApiGenerateImages/ApiGenerateImages/dataset_presencias.csv', 'r') as archivo_csv:
        reader = csv.reader(archivo_csv)
    next(reader)  # Omitir encabezado

    coordenadas = []
    for fila in reader:
        if len(fila) >= 2:
            latitud = float(fila[0])
            longitud = float(fila[1])
            coordenadas.append([longitud, latitud])

    # Separar coordenadas
    longitudes, latitudes = zip(*coordenadas)

    # Crear el gráfico
    fig = plt.figure(figsize=(10, 5))
    ax = plt.axes(projection=ccrs.PlateCarree())

    # Añadir características del mapa
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.LAND, edgecolor='black')
    ax.add_feature(cfeature.LAKES, edgecolor='black')
    ax.add_feature(cfeature.RIVERS)
    ax.gridlines(draw_labels=True)

    # Graficar puntos
    ax.scatter(longitudes, latitudes, color='red', marker='o', s=10, transform=ccrs.PlateCarree())

    # Guardar la imagen en lugar de mostrarla
    plt.savefig('mapa_presencias.png', dpi=300, bbox_inches='tight')
    plt.close()  # Cierra la figura para liberar memoria


# def generar_mapa():
#     # Leer datos del CSV (ajusta la ruta según tu proyecto)
#     with open('dataset_presencias.csv', 'r') as archivo_csv:
#         reader = csv.reader(archivo_csv)
#         next(reader)  # Saltar encabezado
#         coordenadas = []
#         for fila in reader:
#             if len(fila) >= 2:
#                 latitud, longitud = float(fila[0]), float(fila[1])
#                 coordenadas.append([longitud, latitud])

#     # Crear figura y mapa
#     fig = plt.figure(figsize=(10, 5))
#     ax = plt.axes(projection=ccrs.PlateCarree())
#     ax.add_feature(cfeature.BORDERS, linestyle=':')
#     ax.add_feature(cfeature.COASTLINE)
#     ax.add_feature(cfeature.LAND, edgecolor='black')
#     ax.add_feature(cfeature.RIVERS)
#     ax.gridlines(draw_labels=True)

#     # Graficar puntos (desempaqueta coordenadas)
#     if coordenadas:
#         longitudes, latitudes = zip(*coordenadas)
#         ax.scatter(longitudes, latitudes, color='red', marker='o', s=10, transform=ccrs.PlateCarree())

#     # Guardar la imagen en un buffer de memoria (no en disco)
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
#     plt.close()  # Liberar memoria de matplotlib
#     buffer.seek(0)  # Rebobinar el buffer al inicio

#     return buffer
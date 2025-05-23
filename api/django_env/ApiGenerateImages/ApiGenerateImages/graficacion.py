import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np  #operaciones numericas y manejo de arrays
from scipy.stats import gaussian_kde
from io import BytesIO

#recibe?

# def graficarProbabilidades(probabilidades, datosProporcionados):

#     longitudes, latitudes = zip(*datosProporcionados) #asterisko "unpack", se convierte en [lon, lan], [lon1, lan1]

#     fig = plt.figure(figsize=(12, 8))
#     ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

#     # Add features to the map
#     ax.add_feature(cfeature.BORDERS, linestyle=':')
#     ax.add_feature(cfeature.COASTLINE)
#     ax.add_feature(cfeature.LAND, edgecolor='black')
#     ax.add_feature(cfeature.LAKES, edgecolor='black')
#     ax.add_feature(cfeature.RIVERS)

#     # Añadir características del mapa
#     ax.coastlines()
#     ax.gridlines(draw_labels=True)

#     scatter = ax.scatter(longitudes, latitudes, 
#                         c=probabilidades,
#                         cmap='hot', s=50,
#                         vmin=0, vmax=1,  # Fija el rango de 0-1
#                         transform=ccrs.PlateCarree())

#     # Graficar las coordenadas
#     ax.scatter(longitudes, latitudes, color='red', marker='o', s=10, transform=ccrs.PlateCarree())

#     # Crear un mapa de calor
#     xy = np.vstack([longitudes, latitudes])
#     kde = gaussian_kde(xy)
#     xmin, xmax = ax.get_xlim()
#     ymin, ymax = ax.get_ylim()
#     xi, yi = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
#     zi = kde(np.vstack([xi.flatten(), yi.flatten()])).reshape(xi.shape)

#     land = ax.add_feature(cfeature.LAND,
#                         facecolor = 'beige',  # Color correspondiente a vmin=0ç
#                         edgecolor='black',
#                         zorder=2)  # Asegura que esté sobre el mapa de calor

#     # 3. Añadir otras características
#     ax.add_feature(cfeature.COASTLINE, zorder=3)
#     ax.add_feature(cfeature.BORDERS, linestyle=':', zorder=3)

#     # Graficar el mapa de calor
#     contour = ax.contourf(xi, yi, zi, levels=20, cmap='Blues', transform=ccrs.PlateCarree())
#     plt.colorbar(contour, ax=ax, orientation='vertical', label='Probabilidad?')

#     # Mostrar el gráfico
#     #plt.title('Probabilidad de Presencias')
#     #plt.show()


#     # Añadir barra de color
#     plt.colorbar(scatter, label='Probabilidad de presencia')
#     plt.title('Predicción de presencia en coordenadas geográficas')

#     buffer = BytesIO()
#     plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
#     plt.close()
#     buffer.seek(0)

#     return buffer
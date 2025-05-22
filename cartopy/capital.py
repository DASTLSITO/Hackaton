import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Create a new figure
fig = plt.figure(figsize=(10, 10))

# Define the projection
ax = plt.axes(projection=ccrs.Mercator())

# Set the extent to focus on Mexico
ax.set_extent([-118, -86, 14, 33], crs=ccrs.PlateCarree())

# Add features to the map
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.LAKES, edgecolor='black')
ax.add_feature(cfeature.RIVERS)
ax.add_feature(cfeature.STATES, linewidth=0.5)

# Add gridlines
ax.gridlines(draw_labels=True)

# Add a title
plt.title('Mapa de México')

# Coordinates for Mexico City
mexico_city_coords = (-99.133209, 19.432608)
la_paz_coords = (-110.310833, 24.14222)

# Add a marker for Mexico City
plt.scatter(mexico_city_coords[0], mexico_city_coords[1], color='red', s=50, label='Ciudad de México', zorder=5, transform=ccrs.Geodetic())
plt.scatter(la_paz_coords[0], la_paz_coords[1], color='blue', s=50, label='La Paz', zorder=5, transform=ccrs.Geodetic())

# Add a label for Mexico City
plt.text(mexico_city_coords[0] + 0.5, mexico_city_coords[1], 'CDMX', fontsize=12, ha='left', color='black', transform=ccrs.Geodetic())
plt.text(la_paz_coords[0] + 0.5, la_paz_coords[1], 'LPZ', fontsize=12, ha='left', color='black', transform=ccrs.Geodetic())
capitals = {
    'Aguascalientes': (-102.88417, 21.87917),
    'Tijuana': (-117.00371,32.5027 ),
    'Campeche': (-90.52554,19.84667 ),
    'Tuxtla Gutiérrez': (-93.21667,16.73333 ),
    'Chihuahua': (-106.08889,28.63528),
    'Saltillo': (-101.0053,25.42321),
    'Colima': (-103.61667,19.2075),
    'Durango': (-104.86667,24.04333),
    'Guanajuato': (-101.26389,20.93417),
    'Chilpancingo': (-99.53333,17.53333),
    'Pachuca': (-98.46667,20.11667),
    'Guadalajara': (-103.39182,20.66682),
    'Toluca': (-99.66667,19.2575),
    'Morelia': (-101.18443,19.70078),
    'Tepic': (-104.86667,21.51667),
    'Monterrey': (-100.31847,25.67507),
    'Oaxaca': (-96.73333,17.06667),
    'Puebla': (-98.20346,19.03793),
    'Queretaro': (-100.38806,20.58806),
    'Chetumal': (-88.33333,18.53333),
    'San Luis Potosí': (-100.96667,22.15333),
    'Culiacán': (-107.41667,24.78333),
    'Hermosillo': (-110.97732,29.1026),
    'Villahermosa': (-92.93333,18.08333),
    'Ciudad Victoria': (-99.14599,23.74174),
    'Taxcala': (-98.18333, 19.26667),
    'Xalapa': (-96.93333, 19.5333),
    'Mérida': (-89.61696, 20.97537),
    'Zacatecas': (-102.66667, 22.78333)
}

# Extract the coordinates for scatter plot
lon_capitals = [lon for lon, lat in capitals.values()]
lat_capitals = [lat for lon, lat in capitals.values()]
state_names = list(capitals.keys())

# Scatter plot for the capitals
plt.scatter(lon_capitals, lat_capitals, color='green', s=30, zorder=5, transform=ccrs.Geodetic(), label='Capitales')

# Show the legend
plt.legend()

# Show the plot
plt.show()

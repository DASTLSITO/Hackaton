import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Create a new figure with a specified size
plt.figure()

# Create a map with the PlateCarree projection
ax = plt.axes(projection=ccrs.PlateCarree())
la_paz_coords = (-110.310833, 24.14222)
# Set the extent to focus on Mexico
ax.set_extent([-110.460833, -110.260833, 24.04222, 24.24222], crs=ccrs.PlateCarree())

# Add features to the map
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.LAKES, edgecolor='black')
ax.add_feature(cfeature.RIVERS)

# Add gridlines
ax.gridlines(draw_labels=True)

# Add title
plt.title('Mapa de La Paz,BCS')

# Show the plot
plt.show()

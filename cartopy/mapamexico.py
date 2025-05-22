import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Create a new figure with a specified size
plt.figure(figsize=(10, 10))

# Create a map with the PlateCarree projection
ax = plt.axes(projection=ccrs.PlateCarree())

# Set the extent to focus on Mexico
ax.set_extent([-118, -86, 14, 33], crs=ccrs.PlateCarree())

# Add features to the map
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.LAKES, edgecolor='black')
ax.add_feature(cfeature.RIVERS)

# Add gridlines
ax.gridlines(draw_labels=True)

# Add title
plt.title('Map of Mexico')

# Show the plot
plt.show()

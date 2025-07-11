# -*- coding: utf-8 -*-
"""UHI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gBDVDVbaD0TY8yq_xdwclfSNqdcYma8x

# Urban Heat Island Detection & Cooling Infrastructure Mapping – Pune City

**Duration:** May 2025 – Present  
**Tech Stack:** Python, Google Colab, Landsat 9 TIRS, GeoJSON, OSM Overpass API  
**Libraries:** `geopandas`, `osmnx`, `rasterio`, `rasterstats`, `scikit-learn`, `matplotlib`, `numpy`

This project identifies Urban Heat Island (UHI) zones in Pune by integrating satellite-derived land surface temperature with vector data of green and blue spaces, offering insights into urban cooling strategies.

# Phase 1: Extract Green and Water Bodies using Overpass API
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install leafmap numpy matplotlib geopandas rasterio folium shapely geemap osmnx streamlit --quiet

!pip install --upgrade osmnx

# Step 2: Load Pune AOI from GeoJSON
import geopandas as gpd

# Load Pune boundary
aoi = gpd.read_file('/content/drive/MyDrive/UHI/pune_boundary.geojson')

# Ensure it's in WGS84
aoi = aoi.to_crs(epsg=4326)

# Plot to check
aoi.plot(edgecolor='red', facecolor='none')

import geopandas as gpd
import pandas as pd
import osmnx as ox

# Load AOI GeoJSON
aoi = gpd.read_file("/content/drive/MyDrive/UHI/pune_boundary.geojson")
aoi = aoi.to_crs(epsg=4326)
aoi_polygon = aoi.geometry.iloc[0]

# Define rich tag filters
green_tags = {
    'leisure': ['park', 'garden', 'recreation_ground'],
    'landuse': ['grass', 'recreation_ground', 'forest'],
    'natural': ['wood', 'scrub', 'grassland']
}

water_tags = {
    'natural': ['water'],
    'water': True,
    'waterway': True
}

# Use features_from_polygon (reliable version)
green_gdf = ox.features_from_polygon(aoi_polygon, tags=green_tags)
water_gdf = ox.features_from_polygon(aoi_polygon, tags=water_tags)

# Drop null geometries
green_gdf = green_gdf[green_gdf.geometry.notnull()]
water_gdf = water_gdf[water_gdf.geometry.notnull()]

# Add label column
green_gdf["type"] = "green_space"
water_gdf["type"] = "water_body"

# Combine and clip
combined = gpd.GeoDataFrame(pd.concat([green_gdf, water_gdf], ignore_index=True), crs="EPSG:4326")
combined_clipped = gpd.clip(combined, aoi)

# Export with full tags and attributes
combined_clipped.to_file("/content/drive/MyDrive/UHI/pune_green_water_fulltags.geojson", driver="GeoJSON")

"""## Retrieve and Visualize Urban LST

"""

import geemap
import ee
import geopandas as gpd

ee.Authenticate()
# Replace 'your-google-cloud-project-id' with your actual project ID
try:
    ee.Initialize(project='your-google-cloud-project-id here')
except ee.EEException as e:
    print(f"Earth Engine initialization failed: {e}")

# # Convert aoi to EE Feature
roi = geemap.geopandas_to_ee(aoi)

# Load Landsat 9 LST ImageCollection
collection = ee.ImageCollection('LANDSAT/LC09/C02/T1_L2')\
    .filterBounds(roi)\
    .filterDate('2025-03-01', '2025-05-31')\
    .filter(ee.Filter.lt('CLOUD_COVER', 5))

# Take median image
image = collection.median()

# Convert DN to LST (Kelvin to Celsius)
mult = 0.00341802
add = 149.0

# Calculate LST and mask invalid values
lst = image.select('ST_B10')\
    .multiply(mult)\
    .add(add)\
    .subtract(273.15)\
    .rename('LST')

# Mask LST values <= 0 (often invalid) and NaN
lst_masked = lst.updateMask(lst.gt(0))  # masks values ≤ 0

# Clip to ROI
lst_clipped = lst_masked.clip(roi)

# Export and Visualize only valid LST pixels on the map
geemap.ee_export_image(lst_clipped, filename='/content/drive/MyDrive/UHI/LST_cleaned.tif', region=roi.geometry(), scale=30, file_per_band=False)
Map = geemap.Map(center=[18.52, 73.85], zoom=11)

# Add cooling features to map
cooling_infrastructure = '/content/drive/MyDrive/UHI/pune_green_water_fulltags.geojson'
cooling_infrastructure_gdf = gpd.read_file(cooling_infrastructure)
cooling_infrastructure_gdf = cooling_infrastructure_gdf.to_crs(epsg=4326)
Map.addLayer(geemap.geopandas_to_ee(cooling_infrastructure_gdf), {'color': 'aqua'}, "Cooling Infrastructure")
# Add masked LST layer to map
Map.addLayer(lst_clipped, {"min": 20, "max": 45, "palette": ['blue', 'limegreen', 'yellow', 'red']}, "LST Masked")
Map

"""# Phase 2: Load and Mask Land Surface Temperature Raster"""

import rasterio
from rasterio.mask import mask
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
from shapely.geometry import mapping

# Read the raster (LST) and clip it using AOI bounds
with rasterio.open("/content/drive/MyDrive/UHI/LST_cleaned.tif") as lst_src:
    aoi_bounds = [mapping(geom) for geom in aoi.geometry]  # Fixing the geometry extraction
    masked_lst, masked_transform = mask(lst_src, aoi_bounds, crop=True)
    masked_lst = masked_lst[0]

# Replace 0 or invalid values with np.nan
masked_lst = np.where(masked_lst <= 0, np.nan, masked_lst)

# Mask NaN values for a cleaner plot
masked_array = ma.masked_invalid(masked_lst)

# Plotting
plt.figure(figsize=(8, 8))
plt.imshow(masked_array, cmap='hot')
plt.title("Masked LST for Pune AOI", fontsize=14)
plt.axis('off')

cbar = plt.colorbar(label="Land Surface Temperature (LST)")
cbar.ax.tick_params(labelsize=10)

plt.savefig("/content/drive/MyDrive/UHI/masked_LST_cleaned.png", bbox_inches='tight', dpi=300, transparent=True)
plt.show()

"""# Phase 3: Zonal Statistics – Mean LST for Cooling Features"""

!pip install rasterstats --quiet

# Phase 3: Zonal Statistics – Mean LST for Cooling Features
from rasterstats import zonal_stats
import geopandas as gpd

# Ensure geometries are valid and in same CRS as raster
combined_clipped = combined_clipped.to_crs(lst_src.crs)

# Run zonal statistics using masked LST and transform
zs = zonal_stats(
    vectors=combined_clipped,
    raster=masked_lst,
    affine=masked_transform,
    stats=['mean'],
    nodata=lst_src.nodata,
    geojson_out=False  # Only return stats, not geometries
)

# Attach mean LST to GeoDataFrame
combined_clipped['mean_LST'] = [stat['mean'] for stat in zs]

# Remove features without valid LST values
combined_clipped = combined_clipped.dropna(subset=['mean_LST'])

# Save to GeoJSON for reuse
combined_clipped.to_file("/content/drive/MyDrive/UHI/pune_cooling_with_LST.geojson", driver="GeoJSON")

# ---- Visualization ----
# Convert GeoDataFrame to Earth Engine object
cooling_combined_ee = geemap.geopandas_to_ee(combined_clipped)

# Add layers to the map
# Map.addLayer(cooling_combined_ee, {'color': 'aqua'}, "Cooling Infrastructure (Polygons)")
Map.addLayer(cooling_combined_ee, {'color': 'aqua'}, "Mean LST for Cooling Infra")

# Display final map
Map

"""# Phase 4: Urban Heat Island Classification with KMeans"""

# Phase 4: Urban Heat Island Classification with KMeans

# 🔧 Required Libraries
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np
import rasterio
import matplotlib.pyplot as plt

# Step 1: Prepare the masked LST pixel values for clustering
pixels = masked_lst.flatten()
pixels = pixels[~np.isnan(pixels)].reshape(-1, 1)  # Remove NaNs and reshape for scaler

# Step 2: Normalize the pixel values
scaler = StandardScaler()
pixels_scaled = scaler.fit_transform(pixels)

# Step 3: Apply KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42, n_init='auto')
kmeans.fit(pixels_scaled)

# Step 4: Rebuild labels array with original shape, filling with NaNs where masked
labels = np.full(masked_lst.shape, np.nan)
flat_idx = ~np.isnan(masked_lst)
labels[flat_idx] = kmeans.labels_

# Step 5: Optional - Mask cluster 0 if it corresponds to background or low LST values
print("Unique cluster labels found (excluding NaNs):", np.unique(labels[~np.isnan(labels)]))

labels_masked = np.where(labels == 0, np.nan, labels)  # Mask cluster 0 if needed

# Step 6: Plot UHI clusters with Matplotlib
plt.figure(figsize=(10, 8))
plt.imshow(labels_masked, cmap='hot')
plt.title("Urban Heat Island Zones (KMeans Clustering)")
plt.colorbar(label='UHI Cluster (Cool ➝ Hot)')
plt.axis('off')
plt.savefig("/content/drive/MyDrive/UHI/phase4_kmeans_clusters.png", dpi=300)
plt.show()

# Step 7: Save clustered raster to GeoTIFF with appropriate metadata
cluster_raster_path = "/content/drive/MyDrive/UHI/kmeans_uhi_clusters.tif"

# Update metadata for output raster
out_meta = lst_src.meta.copy()
out_meta.update({
    "driver": "GTiff",
    "dtype": "float32",
    "count": 1,
    "height": labels_masked.shape[0],
    "width": labels_masked.shape[1],
    "transform": masked_transform,
    "nodata": np.nan
})

# Save the clustered labels as float32 GeoTIFF
with rasterio.open(cluster_raster_path, "w", **out_meta) as dest:
    dest.write(labels_masked.astype('float32'), 1)

print(f"Clustered UHI raster saved to: {cluster_raster_path}")

!pip install localtileserver

"""# Phase 5 - Visualization of final outputs"""

import geemap
import geopandas as gpd
import rasterio
import ee
from branca.colormap import linear

# Initialize geemap Map centered on Pune
Map = geemap.Map(center=[18.52, 73.85], zoom=11)

# Load Pune Boundary layer
pune_boundary_path = gpd.read_file("/content/drive/MyDrive/UHI/pune_boundary.geojson")
pune_boundary_to_crs = pune_boundary_path.to_crs(epsg=4326)
pune_boundary_ee = geemap.geopandas_to_ee(pune_boundary_to_crs)
Map.addLayer(pune_boundary_ee, {'color': 'black', 'opacity': 0.5}, "Pune Boundary")

# Clip to ROI
lst_clipped = lst_masked.clip(roi)

# Export and Visualize only valid LST pixels on the map
Map.addLayer(lst_clipped, {"min": 20, "max": 45, "palette": ['blue', 'limegreen', 'yellow', 'red']}, "Land Surface Temperature (LST)")

# Load and Add UHI KMeans Cluster GeoTIFF
cluster_raster_path = "/content/drive/MyDrive/UHI/kmeans_uhi_clusters.tif"
Map.add_raster(cluster_raster_path, colormap='hot', layer_name="UHI KMeans Clusters", opacity=0.7)

# Legend for UHI Clusters
cluster_names = {
    'Cool Zone': '#fee08b',              # light yellow
    'Moderate Heat Zone': '#fdae61',     # orange
    'High Heat Zone': '#f46d43',         # dark orange
    'Extreme Heat Zone': '#d73027',      # red
}
Map.add_legend(title="UHI Cluster Zones", labels=list(cluster_names.keys()), colors=list(cluster_names.values()))

# Load and Add Cooling Infrastructure with LST
cooling_geojson_path = "/content/drive/MyDrive/UHI/pune_cooling_with_LST.geojson"
cooling_gdf_final = gpd.read_file(cooling_geojson_path)
cooling_gdf_final = cooling_gdf_final.to_crs(epsg=4326)
cooling_ee_final = geemap.geopandas_to_ee(cooling_gdf_final)
Map.addLayer(cooling_ee_final, {'color': 'aqua', 'opacity': 0.5}, "Cooling Infrastructure")
Map


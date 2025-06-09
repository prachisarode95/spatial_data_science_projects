# Urban Heat Island Mapping & Cooling Features Detection – Pune, India

## 📌 Project Overview
This project detects and visualizes Urban Heat Islands (UHIs) in Pune using Landsat 9 LST data and OpenStreetMap features like green and water bodies. It includes data preprocessing, zonal statistics, K-Means clustering, and map exports.

## 📂 Project Structure
- `Landsat_LST_Pune.tif`: Clipped LST raster for Pune
- `pune_cooling_features.geojson`: Extracted green + blue infrastructure
- `pune_cooling_with_LST.geojson`: Enriched with zonal mean LST
- `phase2_masked_LST.png`: Visual of masked LST raster
- `kmeans_uhi_clusters.tif`: Final classified UHI zones
- `phase4_kmeans_clusters.png`: PNG map of UHI clusters
- `notebook.ipynb`: Complete Google Colab notebook

## 🛠️ Tools & Libraries
- Python (Google Colab)
- geemap, rasterio, numpy, sklearn, rasterstats, matplotlib
- Landsat 9 LST data
- OpenStreetMap + Overpass API

## 🌱 Outputs
- Interactive heat maps showing urban heat and cooling features
- GeoTIFFs and GeoJSONs for urban planning and research

## ✅ Final Visual Outputs
- Classified UHI zones using `K-Means` algorithm
- Mean LST per urban green/water body

## 📊 Final Outputs

| Output File                     | Description                                  |
| ------------------------------ | -------------------------------------------- |
| `pune_cooling_features.geojson` | Extracted green and water bodies (cooling features) |
| `pune_cooling_with_LST.geojson` | Cooling features enriched with zonal mean LST values |
| `phase2_masked_LST.png`         | Visualization of masked LST raster showing study area temperature |
| `phase4_kmeans_clusters.png`    | Final UHI zone classification map using KMeans clustering |
| `kmeans_uhi_clusters.tif`       | GeoTIFF raster of classified UHI zones for GIS and analysis |


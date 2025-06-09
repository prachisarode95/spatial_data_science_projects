# Urban Heat Island Mapping & Cooling Features Detection – Pune, India

## 📌 Project Overview
This project detects and visualizes Urban Heat Islands (UHIs) in Pune City in May 2025 using Landsat 9 LST data and OpenStreetMap features like green and water bodies. It includes data preprocessing, zonal statistics, K-Means clustering, and mapping.

## 📂 Project Structure
    /Urban_Heat_Island_Detection
    ├── uhi.py
    ├── UHID.md
    ├── UHI 
        └── Raw/
            ├── pune_boundary.geojson 
        └── Outputs/
            ├── pune_green_water_fulltags.geojson       
            ├── pune_cooling_with_LST.geojson
            ├── LST.tif
            ├── LST_cleaned.tif
            └── kmeans_uhi_clusters.tif
       └── PNG/
            ├── masked_LST_cleaned.png
            └── phase4_kmeans_clusters.png


## 🛠️ Tools & Libraries
- GEE Python API (Google Colab)
- geemap, geopandas, rasterio, numpy, sklearn, rasterstats, matplotlib
- Landsat 9 LST data
- OpenStreetMap + Overpass API

## 📊 Final Outputs

| Output File                     | Description                                  |
| ------------------------------ | -------------------------------------------- |
| `pune_cooling_with_LST.geojson` | Cooling features enriched with zonal mean LST values |
| `kmeans_uhi_clusters.tif`       | GeoTIFF raster of classified UHI zones for GIS and analysis |


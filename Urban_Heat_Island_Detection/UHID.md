# 🌆 Urban Heat Island Detection & Cooling Features Mapping  – Pune, India

## 📌 Project Overview
This project aims to detect and analyze Urban Heat Islands (UHIs) in Pune City using Landsat 9 thermal satellite data and OpenStreetMap (OSM) features. The goal is to identify UHI hotspots and assess the effectiveness of existing cooling infrastructure (green spaces and water bodies) during May 2025, a peak summer month in India.

The entire workflow is implemented using open-source geospatial Python libraries and visualized through a reproducible pipeline.

---

## 📂 Project Structure
```
/Urban_Heat_Island_Detection
├── uhi.py                           # Main Python script
├── UHID.md                          # Project documentation
├── UHI
│   ├── Raw/
│   │   ├── pune_boundary.geojson    # Study area boundary
│   ├── Outputs/
│   │   ├── pune_green_water_fulltags.geojson   # Green & water features
│   │   ├── pune_cooling_with_LST.geojson       # Features enriched with LST
│   │   ├── LST.tif                            # Original LST raster
│   │   ├── LST_cleaned.tif                    # Preprocessed/masked raster
│   │   └── kmeans_uhi_clusters.tif            # Classified UHI zones
│   └── PNG/
│       ├── masked_LST_cleaned.png             # Cleaned LST preview
│       └── phase4_kmeans_clusters.png         # UHI clustering visualization
```
---

## 🛠️ Tools & Libraries
- **Google Earth Engine (GEE) Python API** (via Google Colab)

- **Python Libraries**: `geemap`, `geopandas`, `rasterio`, `numpy`, `sklearn`, `rasterstats`, `matplotlib`

- **Data Sources**:

  - Landsat 9 Surface Temperature (LST)

  - OpenStreetMap (OSM) features via Overpass API

---

## 🚀 Workflow Breakdown

- Phase 1: Study Area Setup
Defined Pune city boundary using geojson file.

Fetched OSM features (green zones, water bodies) using overpass queries.

- Phase 2: Land Surface Temperature (LST) Data Processing
Downloaded Landsat 9 LST data via Google Earth Engine.

Preprocessed and cleaned raster data to remove invalid values and apply city boundary mask.

- Phase 3: Zonal Statistics
Calculated mean LST values for each green and water body feature using rasterstats.zonal_stats().

Merged statistics with vector features to assess their cooling efficiency.

- Phase 4: Urban Heat Island Classification
Applied K-Means clustering on the cleaned LST raster to classify areas into temperature zones (cool to hot).

Exported results as a new raster GeoTIFF file for spatial analysis.

- Phase 5: Visualization & Output
Generated heatmap overlays and feature-enriched maps.

Exported final GeoTIFF and GeoJSON files for GIS integration or further analysis.

---

## 📊 Final Outputs

| Output File                     | Description                                  |
| ------------------------------ | -------------------------------------------- |
| `pune_cooling_with_LST.geojson` | Cooling features enriched with zonal mean LST values |
| `kmeans_uhi_clusters.tif`       | GeoTIFF raster of classified UHI zones for GIS and analysis |
| `masked_LST_cleaned.png`       | Visual preview of cleaned LST raster |
| `phase4_kmeans_clusters.png`   | Heatmap showing different UHI zones for Pune city |

---

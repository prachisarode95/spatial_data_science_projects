# Urban Heat Risk and Cooling Access Dashboard: Pune City

## 🧭 Project Goal
To identify urban heat zones and evaluate the accessibility of cooling infrastructure in Pune city.

## 🛠️ Tech Stack
- QGIS (spatial preprocessing and classification)
- Streamlit (interactive dashboard)
- Python (geopandas, pandas, folium, matplotlib, shapely)

## 📂 Data Sources
- MODIS LST (via NASA)
- NDVI (Sentinel-2 via EO Browser)
- Pune Ward Boundaries (PMC)
- OpenStreetMap (parks, water bodies)
- Population Density (Census of India or WorldPop)

## 🗺️ Dashboard Features
- Heat Risk Mapping
- NDVI (green cover) layers
- Population overlay with filter options
- Cooling infrastructure buffer zones
- Accessibility statistics

## 📈 Methodology
- Step-by-step QGIS preprocessing
- NDVI and LST thresholding
- Zonal statistics per ward
- Accessibility buffer analysis

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## 📌 Results and Screenshots
(Embed exported maps + dashboard GIFs)

## 🗺️ Dashboard Link
[🔗 Live Streamlit Dashboard](#under development)

## 📷 Preview
_Screenshots of Carto Builder dashboard_(#under development)

## 🧠 Insights and Policy Suggestions
- Priority wards for heat adaptation
- Gaps in cooling infrastructure

## 📚 References
(List of sources and tools)

## 📁 Folder Structure
```
urban-heat-risk-pune/
│
├── README.md                      ← Overview, methodology, results, usage
├── requirements.txt               ← Python + Streamlit dependencies
├── data/
│   ├── raw/
│   │   ├── LST_MODIS_Pune.tif
│   │   ├── Pune_Ward_Boundaries.shp
│   │   ├── OSM_Parks_Water.geojson
│   │   └── Population_Density.csv
│   ├── processed/
│   │   ├── heat_zones.gpkg
│   │   └── green_index_ndvi.gpkg
│   └── external/                  ← Downloaded sources and citations
│
├── notebooks/
│   └── preprocessing_qgis_steps.md
│
├── app/
│   ├── streamlit_app.py           ← Dashboard UI code
│   └── heatmap_utils.py           ← Helper functions for spatial data
│
├── outputs/
│   ├── screenshots/
│   └── map_exports/
│
└── docs/
    └── methodology.md             ← Heat risk classification, buffer logic

```

## 📜 License
MIT License


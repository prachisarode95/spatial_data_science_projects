# 🌆 Climate-Resilient Urban Planning: Urban Heat Island Detection & Cooling Infrastructure Mapping

## Overview
An interactive GeoAI application built with Google Earth Engine, SAMGeo, Streamlit, and OSM data for detecting Urban Heat Islands (UHIs) and overlaying cooling infrastructure like parks, water bodies, and green spaces.

## 🔍 Project Goals
Urban Heat Islands (UHIs) increase the temperature in dense urban areas due to concrete surfaces, reduced vegetation, and human activities. This project aims to support climate-resilient urban planning by:

1. Detecting UHIs from Land Surface Temperature (LST) satellite data

2. Identifying nearby cooling infrastructures (parks, lakes, forests) using OpenStreetMap

3. Visualizing spatial patterns through an interactive web app

4. Allowing users to upload their own LST GeoTIFFs and run GeoSAM segmentation
---
## 🛠️ Tech Stack

| Component        | Technology                                                              |
| ---------------- | ----------------------------------------------------------------------- |
| **LST Data**     | Google Earth Engine (MODIS or Landsat)                                  |
| **Segmentation** | [SAMGeo](https://github.com/opengeos/samgeo) using Meta AI’s SAM model  |
| **Mapping**      | [leafmap](https://github.com/opengeos/leafmap), \[folium], \[geopandas] |
| **Web App**      | [Streamlit](https://streamlit.io/)                                      |
| **OSM Data**     | [osmnx](https://github.com/gboeing/osmnx)                               |

---
## 🚀 Methodology
✅ Extract Urban Heat Islands using normalized LST
✅ Use GeoSAM to segment hot regions
✅ Overlay cooling zones (parks, gardens, water bodies, etc.) from OpenStreetMap
✅ Upload your own GeoTIFF LST image and run segmentation
✅ Download generated UHI zones as GeoJSON
✅ Fully interactive Streamlit map viewer using leafmap

---
## 📂 Folder Structure
```
urban-heat-geosam-pune/
│
├── data/
│   └── aoi.geojson
├── notebooks/
│   └── uhi_segmentation.ipynb  ← Google Colab-compatible
├── app/
│   └── app.py # Streamlit web app
├── outputs/
│   └── lst_normalized_pune.tif        # Preprocessed LST for Pune
│   └── uhi_zones.geojson              # Extracted UHI polygons
    └── cooling_infrastructure.geojson # OSM-based green/cooling zones
    └── sam_vit_h.pth                  # SAM checkpoint
├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
├── .streamlit/
│   └── config.toml
├── logo.png
```
---

## 🗺️ Dashboard Features
✅ Key Tools:
 - `streamlit` – Web app UI

- `leafmap` or `maplibre` – Map interactivity

- `samgeo` – GeoSAM segmentation

- `geopandas`, `rasterio`, `folium` – Data I/O and processing

## 🧱 Dashboard Architecture:

| Section                          | Description                                      |
| -------------------------------- | ------------------------------------------------ |
| 🗺️ Map Viewer                   | Toggle UHI and cooling layers                    |
| 🗂️ LST Upload + Auto-Processing | Upload GeoTIFF → Normalize → Segment with GeoSAM |
| 📥 Download Outputs              | Download GeoJSON of UHI polygons                 |

---
## 📦 Setup Instructions
```
1. Clone the Repository
bash
git clone https://github.com/your-username/uhi-streamlit-dashboard.git
cd uhi-streamlit-dashboard
```
```
2. Create a Virtual Environment (Optional)
bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
```
3. Install Dependencies
bash
pip install -r requirements.txt
```
```
4. Download SAM Checkpoint
bash
wget https://huggingface.co/sam-hq/sam-hq/resolve/main/sam_vit_h_4b8939.pth -O sam_vit_h.pth
```
```
5. Run the App
bash
streamlit run app.py
```
---
## 📌 Results & 📷 Preview
(Embed exported maps + dashboard GIFs)

## 🌐 Live App
[🔗 Try it here:](https://your-streamlit-app-url)

## ✅ Final Output
🖼️ An interactive dashboard with:

🔴 UHI Zones

🌳 Cooling Zones

📤 Upload your own LST maps

🧠 GeoSAM segmentation

📥 Download resulting GeoJSONs

---
## 🧠 Insights and Policy Suggestions
- Priority wards for heat adaptation
- Gaps in cooling infrastructure
- Proximity of UHI zones to cooling zones
- Underserved urban areas with green infrastructure
- Candidates for green infrastructure expansion

## 📥 Upload Your LST Data
Upload a normalized LST GeoTIFF (values between 0–1)

Click the Run GeoSAM button to generate UHI polygons

View and download the result in the map interface

## 🔍 Future Enhancements
🔄 Add support for batch processing multiple cities

📊 Include UHI severity scoring and ranking

🧭 Add spatial analysis: distance from UHI to nearest cooling zones

🛰️ Integrate real-time MODIS data via GEE API

---
## 🤝 Credits
- `SAMGeo` by [Qiusheng Wu](https://github.com/opengeos/segment-geospatial)

- `leafmap`, `geemap`, and `osmnx` open-source communities

- Satellite data from NASA `MODIS` and `Landsat`

- `OpenStreetMap` contributors

## 📜 License
This project is licensed under the MIT License. See LICENSE for more info.

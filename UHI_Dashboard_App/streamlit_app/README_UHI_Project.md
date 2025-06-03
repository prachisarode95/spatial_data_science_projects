
# 🌆 Climate-Resilient Urban Planning – Pune (2025)

This project identifies Urban Heat Island (UHI) zones in Pune using remote sensing data and builds an interactive, bilingual Streamlit dashboard for exploring cooling infrastructure, vegetation stress, and climate adaptation recommendations.

> **Author**: Prachi  
> **Tools Used**: Google Earth Engine, GeoPandas, Rasterio, Leafmap, Streamlit, matplotlib, numpy

---

## 🚀 Project Overview

Urban areas like Pune experience elevated surface temperatures due to dense built-up areas and reduced green spaces—a phenomenon known as the **Urban Heat Island (UHI)** effect. This project aims to:

- Detect UHI hotspots using satellite LST data
- Identify zones with low vegetation (NDVI)
- Analyze gaps in green/cooling infrastructure
- Recommend interventions to improve climate resilience
- Provide an interactive dashboard for public/stakeholder engagement

---

## 🧭 Project Workflow

### 🔹 Phase 1: Data Collection & Preprocessing

- **Satellite Data Used**:
  - Landsat 9 Surface Temperature (LST)
  - Sentinel-2 NDVI
- **AOI**: Pune Municipal Region
- Clipped and cleaned using Google Earth Engine
- Exported raster assets to Google Drive

### 🔹 Phase 2: Raster Analysis

- Created **mean LST raster** and **mean NDVI raster**
- Thresholded LST > 35°C to generate UHI binary mask
- Labeled mask zones: No UHI (0), Moderate UHI (1), High UHI (2)

### 🔹 Phase 3: Raster to Vector Conversion

- Used `rasterio` + `shapes()` to convert UHI mask raster to GeoJSON zones
- Simplified geometries with `shapely`
- Mapped NDVI < 0.2 zones as vegetation-stressed areas

### 🔹 Phase 4: Streamlit Dashboard

- Built interactive map with:
  - UHI zones
  - Cooling centers
  - Green spaces
  - Built-up areas
  - Population density
- Features:
  - 📌 Coordinate bookmarking
  - 📊 Heat risk analysis
  - 🌐 Language toggle: English & Marathi
  - 📥 GeoJSON/CSV export buttons

### 🔹 Phase 5: GeoJSON Optimization

- Cleaned and merged layers
- Ensured topology correctness
- Validated geometries and projections for WebMap use

---

## 🖥️ Dashboard Features

| Feature                      | Status       |
|-----------------------------|--------------|
| Interactive Map (Leafmap)   | ✅ Implemented |
| Raster + Vector Layer Toggle| ✅ Implemented |
| Language Toggle              | ✅ English/Marathi |
| Analysis Summary + Charts   | ✅ Plotly & Matplotlib |
| Recommendations Tab         | ✅ With Action Points |
| Export to GeoJSON/CSV       | ✅ Download buttons |
| Coordinate Bookmarking      | ✅ Manual Input |

---

## 📸 Screenshots

![Map View](figures/uhi_vs_cooling_access.png)

> Heat risk distribution and cooling center access

---

## 🗂️ Data Sources

- [USGS Earth Explorer (Landsat 9 LST)](https://earthexplorer.usgs.gov/)
- [Sentinel-2 NDVI from Copernicus Open Access Hub](https://scihub.copernicus.eu/dhus)

---

## ⚙️ Installation

Clone this repo and install required libraries:

```bash
git clone https://github.com/yourusername/urban-heat-dashboard
cd urban-heat-dashboard
pip install -r requirements.txt
```

Run the app locally:

```bash
streamlit run app.py
```

---

## 🌐 Deployment

The dashboard is deployable on:
- [Streamlit Cloud](https://streamlit.io/cloud)
- [Hugging Face Spaces](https://huggingface.co/spaces)
- [Render](https://render.com)

---

## 🙌 Acknowledgements

- Qiusheng Wu – for [Leafmap](https://github.com/giswqs/leafmap)
- Pune Municipal GIS Open Data
- Sentinel Hub and USGS data repositories

---

## 📄 License

This project is open-source under the MIT License.

---

### 💡 Future Work

- Integrate user-defined AOI tools
- Add real-time mobile heat data if available
- Machine learning-based LST estimation

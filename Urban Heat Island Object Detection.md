# 🌆 Climate-Resilient Urban Planning – Heat Island Detection and Cooling Infrastructure Mapping

A complete end-to-end GeoAI project that identifies Urban Heat Island (UHI) hotspots and maps cooling infrastructure using open-source geospatial tools. The study focuses on **Pune, India** during the **pre-monsoon season (March–May 2024)**, leveraging **Landsat 9 LST data**, **OpenStreetMap features**, and a **Streamlit dashboard** to recommend climate-adaptive urban planning strategies.

---

## 🚀 Project Goals

- Detect urban heat stress zones using satellite-derived Land Surface Temperature (LST).
- Map existing cooling infrastructure (green spaces and water bodies).
- Identify underserved areas lacking thermal comfort.
- Visualize results in an interactive Streamlit dashboard for urban planning and policy interventions.

---

## 🛰️ Tech Stack

| Type | Tools Used |
|------|------------|
| Remote Sensing | Landsat 9 (LST Band 10) |
| Spatial Analysis | `geemap`, `rasterio`, `numpy`, `folium`, `shapely` `GeoJSON` |
| OpenStreetMap | `osmnx`, `openstreetmap` |
| Dashboard | `Streamlit`, `ngrok` |
| Development | Google Colab, Python  |

---

## 📁 Project Structure

```bash
urban-heat-dashboard/
│
├── Phase1_UHI_LST_Pune_MarMay2024.ipynb          # Retrieve and visualize LST
├── Phase2_UHI_CoolingInfra_Pune_MarMay2024.ipynb # Extract cooling infra (OSM)
├── Phase3_UHI_InfraGap_Analysis_Pune.ipynb       # UHI and buffer gap analysis
├── UHI_Dashboard_Streamlit_ngrok_Colab.ipynb     # Streamlit deployment setup
│
├── uhi_dashboard.py                               # Streamlit dashboard code
├── assets/
│   ├── pune_boundary.geojson
│   ├── pune_lst_stats.geojson
│   ├── pune_cooling_buffer_200m.geojson
│   └── uhi_hotspots.geojson
│
└── README.md
---
## 🚀 Methodology

## ✅ Key Outputs
- 🔥 Urban Heat Island Map using Landsat-derived LST

- 🌳 Buffered Cooling Zones (200m radius from parks/water bodies)

- ⚠️ Hotspot Areas Without Cooling Infrastructure

- 📊 Interactive Dashboard with layers, stats, and recommendations
---

## 📺 Streamlit Dashboard
🌐 Hosted via ngrok (for Colab-based preview)

To run locally:
```
bash
streamlit run uhi_dashboard.py
```
To run in Colab with tunnel:

1. Upload uhi_dashboard.py and asset files.

2. Use the notebook UHI_Dashboard_Streamlit_ngrok_Colab.ipynb.

## 📷 Preview
<!-- Replace with screenshot -->

📝 Methodology
LST Retrieval: Filter Landsat 9 imagery using geemap, extract Band 10 (thermal), and compute mean LST.

Cooling Infra Extraction: Use osmnx and OSM tags to extract parks, gardens, and water bodies.

Gap Analysis: Identify UHI hotspots > mean + 1 std, and buffer cooling infra by 200m to detect gaps.

Visualization: Streamlit dashboard with togglable map layers and intervention guidance.

## 🔍 Future Enhancements
- Incorporate demographic layers (e.g., elderly population density)

- Predict UHI trends using ML-based time series models

- Recommend greening potential sites using parcel-level data
- 🔄 Add support for batch processing multiple cities

- 📊 Include UHI severity scoring and ranking

- 🧭 Add spatial analysis: distance from UHI to nearest cooling zones

- 🛰️ Integrate real-time MODIS data via GEE API

## 🧠 Insights and Policy Suggestions
- Priority wards for heat adaptation
- Gaps in cooling infrastructure
- Proximity of UHI zones to cooling zones
- Underserved urban areas with green infrastructure
- Candidates for green infrastructure expansion

## ✨ Acknowledgements
[USGS EarthExplorer](https://earthexplorer.usgs.gov/) for Landsat data

[OpenStreetMap](https://www.openstreetmap.org/#map=4/21.84/82.79) for cooling infrastructure data

[Qiusheng Wu](https://github.com/giswqs) for geemap and leafmap libraries
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

📤 Upload your LST maps

📥 Download resulting GeoJSONs

---
💬 Author
👩‍💻 Prachi – GIS & Remote Sensing Analyst
🔗 [LinkedIn](https://www.linkedin.com/in/prachisarode95) • Medium Blog (coming soon)
---
## 📜 License
This project is licensed under the MIT License. See LICENSE for more info.
---

### ✅ Next Steps

- Save the above as `README.md` in your project repo.
- Add a thumbnail image named `dashboard_preview.png` to your `assets/` folder.
- Push the repo to GitHub and you're ready to share!


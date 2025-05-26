# Urban Heat Island Object Detection using GeoSAM on Landsat-derived LST in Pune

## 🧭 Project Goal
Use Google Colab + Leafmap + Samgeo (GeoSAM) to:

- Extract Land Surface Temperature (LST) using Landsat 8 over Pune

- Run object detection using the Segment Anything Model (GeoSAM)

- Visualize results on an interactive leafmap

- Deploy the whole result in a Streamlit app

---

## 🛠️ Tech Stack
| Task                            | Tool              |
| ------------------------------- | ----------------- |
| Data download + preprocessing   | Google Colab      |
| Object segmentation (UHI zones) | SAMGeo            |
| Mapping + interactivity         | Leafmap           |
| Dashboard UI                    | Streamlit         |

---

## 📂 Folder Structure
```
urban-heat-geosam-pune/
│
├── data/
│   └── aoi.geojson
├── notebooks/
│   └── urban_heat_detection.ipynb  ← Google Colab-compatible
├── app/
│   └── streamlit_app.py
├── outputs/
│   └── lst_image.tif
│   └── geosam_masked.geojson
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
├── logo.png
```
---

## 📂 Data Sources

## 🗺️ Dashboard Features

## 📈 Methodology

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app/streamlit_app.py
```

## 📌 Results and  📷 Preview
(Embed exported maps + dashboard GIFs)

## 🗺️ Dashboard Link
[🔗 Live Streamlit Dashboard](#under development)

##

## 🧠 Insights and Policy Suggestions
- Priority wards for heat adaptation
- Gaps in cooling infrastructure

## 📚 References
(List of sources and tools)

## 📁 Folder Structure

## 📜 License
MIT License


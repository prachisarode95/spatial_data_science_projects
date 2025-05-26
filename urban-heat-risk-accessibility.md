# Climate-Resilient Urban Planning – Heat Island Detection & Cooling Infrastructure Mapping

## 🧭 Project Goal
Detect Urban Heat Islands (UHIs) using thermal imagery (e.g., Landsat 8), segment them using SAMGeo, and map public cooling infrastructure using Streamlit + Leafmap for interactive exploration.

---

## 🛠️ Tech Stack
| Task                            | Tool              |
| ------------------------------- | ----------------- |
| Data download + preprocessing   | Google Colab      |
| Object segmentation (UHI zones) | SAMGeo            |
| Mapping + interactivity         | Leafmap, MapLibre |
| Dashboard UI                    | Streamlit         |

---

## 📂 Folder Structure
```
urban_heat_dashboard/
├── data/
│   ├── aoi.geojson
│   └── cooling_points.geojson  # Optional
├── notebooks/
│   └── colab_uhi_segmentation.ipynb
├── app/
│   └── streamlit_app.py
├── assets/
│   └── uhi_mask.tif
│   └── lst_image.tif
├── requirements.txt
├── README.md
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


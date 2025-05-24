# Urban Heat Risk Zones & Cooling Infrastructure Accessibility in Pune

## 🧭 Project Objective
This project identifies urban heat risk zones in Pune based on land surface temperature (LST), vegetation cover, and population vulnerability. It evaluates public access to cooling infrastructure like parks and water bodies and presents the findings through an interactive Carto dashboard.

## 📌 Key Questions
- Where are the heat-vulnerable zones in Pune?
- Which areas lack access to green or cooling infrastructure?
- How can this be used for climate-resilient urban planning?

## 🔧 Tools & Stack
- QGIS (processing, analysis)
- Carto Builder (interactive storytelling dashboard)
- OpenStreetMap (cooling resources)
- MODIS LST, Sentinel NDVI (remote sensing)
- Pune ward boundaries + census data

## 📁 Folder Structure
```
urban-heat-risk-accessibility-qgis-carto-pune/
│
├── README.md                  # Project overview and steps
├── data/
│   ├── raw/                   # Original datasets (MODIS, OSM, Census)
│   ├── processed/             # Cleaned, clipped, georeferenced data
│   └── metadata/              # Source details, license info
│
├── qgis_project/
│   ├── project.qgz            # Main QGIS project file
│   ├── style/                 # QGIS layer styles (e.g., heat zones, buffers)
│   └── processing_models/     # ModelBuilder or scripts used
│
├── carto_output/
│   ├── .carto_files/          # Layers published to Carto
│   ├── screenshots/           # Map visuals for README/docs
│   └── dashboard_link.txt     # Published dashboard URL
│
├── scripts/
│   └── preprocess_data.qmd    # Optional Python/Jupyter QGIS processing
│
├── reports/
│   └── policy_brief.pdf       # Optional insights PDF
│
└── LICENSE
```

## 🗺️ Dashboard Link
[🔗 Live Carto Dashboard](#under development)

## 🚀 Workflow
1. Download and prepare data in QGIS
2. Classify LST and NDVI to identify heat zones and green deficits
3. Join population data and highlight high-risk areas
4. Map public cooling infrastructure (parks, lakes)
5. Analyze accessibility with 500m buffers
6. Style layers and publish via Carto QGIS plugin
7. Build interactive dashboard in Carto Builder

## 📷 Preview
_Screenshots of Carto Builder dashboard_(#under development)

## 📜 License
MIT License


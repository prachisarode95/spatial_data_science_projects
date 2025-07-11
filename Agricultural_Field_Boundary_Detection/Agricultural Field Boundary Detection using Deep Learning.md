# Agricultural Field Boundary Detection using Deep Learning

![Remote Sensing | Deep Learning | Agriculture](https://img.shields.io/badge/Remote_Sensing-Sentinel--2-green?style=flat&logo=googleearthengine) ![Deep Learning](https://img.shields.io/badge/Deep_Learning-U--Net-blue?style=flat&logo=tensorflow) ![Status](https://img.shields.io/badge/Project-Work_in_Progress-yellow)

## Project Overview

This project demonstrates a fully automated workflow to detect agricultural field boundaries using high-resolution **Sentinel-2 imagery** and **OpenStreetMap farmland labels**, combined with a **U-Net-based semantic segmentation model**. It is tailored to highlight my applied geospatial and machine learning skills for real-world agricultural monitoring tasks.

**Key Objective**:  
To build an end-to-end pipeline that extracts field-level parcel boundaries from satellite imagery, enabling downstream applications such as crop type mapping, yield analysis, and precision agriculture.

---

## Why this Project?

Manual delineation of field boundaries is time-consuming and inconsistent across regions. This project showcases how **remote sensing data** combined with **deep learning** can automate boundary detection with scalability and precision — a highly sought-after skill in agriculture, climate tech, and geospatial AI roles.

---

## Area of Interest

- **Region**: Occitanie, France 🇫🇷
- **AOI Source**: `OpenStreetMap` administrative boundaries
- **Imagery**: Cloud-free Sentinel-2 RGB composite from Google Earth Engine
- **Labels**: OSM `landuse=farmland` polygons

---

## Tech Stack

| Category             | Tools & Libraries |
|----------------------|------------------|
| Satellite Data       | Sentinel-2 (GEE) |
| Label Source         | OpenStreetMap    |
| Image Clipping       | Geopandas, Rasterio |
| Tiling & Masking     | NumPy, Pillow, Scikit-image |
| Deep Learning Model  | TensorFlow / Keras (U-Net) |
| Visualization        | Matplotlib, PIL |
| Deployment (Planned) | Streamlit Cloud |

---

## Project Workflow

### Phase 1: Data Acquisition (Planned)
- Downloaded Sentinel-2 imagery via Google Earth Engine Python API.
- Extracted farmland polygons from OpenStreetMap using `osmnx` and `geopandas`.

### Phase 2: Image–Mask Dataset Preparation (Planned)
- Clipped Sentinel-2 RGB composite to farmland AOI.
- Rasterized farmland polygons to binary masks.
- Generated 512×512 image–mask tile pairs with proper padding for model input.

### Phase 3: Model Training (Planned)
- Training a U-Net model on image–mask tiles using `TensorFlow/Keras`.
- Will evaluate performance using accuracy, IoU (Intersection-over-Union), and F1 score.

### Phase 4: Post-Processing & Vectorization (Planned)
- Convert predicted masks to vector shapefiles.
- Clean boundaries using morphological operations.
- Evaluate spatial overlap with ground truth polygons.

### Phase 5: Visualization & Deployment (Planned)
- Build an interactive dashboard to visualize results.
- Deploy via Streamlit on Hugging Face Spaces or GEE App.

---

## Project Structure To Be
```
field-boundary-detection/
│
├── Phase1_AOI_Selection_and_Image_Download/
│
├── field_boundary_dataset/
│ ├── images/
│ └── masks/
│
├── model_training/
│ ├── unet_model.py
│ └── train_unet.ipynb
│
├── README.md
└── requirements.txt
```
---

## Skills To Be Demonstrated

- Remote sensing data preprocessing using Python
- Raster-vector operations and tiling large satellite images
- Semantic segmentation for geospatial image analysis
- Applying open-source ML models to real-world geospatial problems
- Preparing datasets for model training and visualizing spatial outputs

---

## Status

- **Initiated**: Soon to be started with Phase 1 & 2
- Final goal: Deploy field boundary predictions for real-world AOIs
---

## Acknowledgements

- [Google Earth Engine](https://earthengine.google.com/)
- [OpenStreetMap](https://www.openstreetmap.org/)
- [Keras U-Net Guide](https://github.com/zhixuhao/unet)

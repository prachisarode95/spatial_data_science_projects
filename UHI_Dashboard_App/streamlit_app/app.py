# app.py final with mapping functions

import streamlit as st
import geopandas as gpd
import rasterio
import numpy as np
import leafmap.foliumap as leafmap

# Title
st.set_page_config(layout="wide")
st.title("🗺️ Urban Heat Detection Mapping")

st.sidebar.title("🗂️ Map Layers")
st.markdown("This interactive map shows urban heat patterns in Pune using vector and raster layers.")

# File paths (adjust if needed)
critical_zones_path = "assets/critical_zones.geojson"
green_spaces_path = "assets/pune_green_spaces.geojson"
water_bodies_path = "assets/pune_water_bodies.geojson"
low_ndvi_zones_path = "assets/low_ndvi_zones.geojson"
uhi_zones_path = "assets/uhi_zones.geojson"
mean_LST_path = "assets/mean_LST_Pune.tif"
mean_NDVI_path = "assets/mean_NDVI_Pune.tif"
uhi_hotspots_path = "assets/uhi_hotspots.tif"

# Load map
m = leafmap.Map(center=[18.52, 73.85], zoom=12, draw_control=False, measure_control=False)
m.add_basemap("OpenStreetMap")

# Vector Layers
if st.sidebar.checkbox("Show Critical Zones", True):
    gdf = gpd.read_file(critical_zones_path)
    m.add_gdf(gdf, "Critical Zones", info_mode="on_click",
              style={"color": "red", "weight": 2, "fillOpacity": 0.4})

if st.sidebar.checkbox("Show Green Spaces", True):
    gdf = gpd.read_file(green_spaces_path)
    m.add_gdf(gdf, "Green Spaces", info_mode="on_click",
              style={"color": "green", "weight": 1.5, "fillOpacity": 0.5})

if st.sidebar.checkbox("Show Water Bodies", False):
    gdf = gpd.read_file(water_bodies_path)
    m.add_gdf(gdf, "Water Bodies", info_mode="on_click",
              style={"color": "blue", "weight": 1.5, "fillOpacity": 0.4})

if st.sidebar.checkbox("Show Low NDVI Zones", False):
    gdf = gpd.read_file(low_ndvi_zones_path)
    m.add_gdf(gdf, "Low NDVI Zones", info_mode="on_click",
              style={"color": "orange", "weight": 1.5, "fillOpacity": 0.5})

if st.sidebar.checkbox("Show UHI Hotspots", True):
    gdf = gpd.read_file(uhi_hotspots_path)
    m.add_gdf(gdf, "UHI Hotspots", info_mode="on_click",
              style={"color": "#800000", "weight": 2, "fillOpacity": 0.6})

if st.sidebar.checkbox("Show UHI Zones", False):
    gdf = gpd.read_file(uhi_zones_path)
    m.add_gdf(gdf, "UHI Zones", info_mode="on_click",
              style={"color": "#FF00FF", "weight": 1.5, "fillOpacity": 0.5})

# Raster Layers
if st.sidebar.checkbox("Show Mean LST (inferno)", True):
    m.add_raster(mean_LST_path, layer_name="Mean LST", colormap="inferno", opacity=0.7)

if st.sidebar.checkbox("Show Mean NDVI (YlGn)", False):
    m.add_raster(mean_NDVI_path, layer_name="Mean NDVI", colormap="YlGn", opacity=0.6)

# Stats for raster (optional)
def raster_stats(path):
    with rasterio.open(path) as src:
        band = src.read(1)
        nodata = src.nodata if src.nodata is not None else 0
        band = np.ma.masked_equal(band, nodata)
        return {
            "Min": round(float(band.min()), 2),
            "Max": round(float(band.max()), 2),
            "Mean": round(float(band.mean()), 2)
        }

if st.sidebar.checkbox("Show LST Stats", False):
    stats = raster_stats(mean_LST_path)
    st.sidebar.markdown("**LST Stats:**")
    st.sidebar.json(stats)

if st.sidebar.checkbox("Show NDVI Stats", False):
    stats = raster_stats(mean_NDVI_path)
    st.sidebar.markdown("**NDVI Stats:**")
    st.sidebar.json(stats)

# Legend
legend_dict = {
    "Critical Zones": "red",
    "Green Spaces": "green",
    "Water Bodies": "blue",
    "Low NDVI Zones": "orange",
    "UHI Hotspots": "#800000",
    "UHI Zones": "#FF00FF"
}
m.add_legend(title="Map Legend", legend_dict=legend_dict)

# Display the map
m.to_streamlit(height=700)

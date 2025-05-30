import streamlit as st
import leafmap.foliumap as leafmap
import geopandas as gpd
import os

st.set_page_config(layout="wide")

st.title("🌆 Climate-Resilient Urban Planning – Heat Island Detection (Pune, Mar–May 2024)")
st.markdown("Visualize Land Surface Temperature (LST), cooling infrastructure, and underserved UHI zones in Pune.")

# Load layers
boundary = gpd.read_file("assets/pune_boundary.geojson")
hotspots = gpd.read_file("assets/pune_hotspots_35C.geojson")
buffer = gpd.read_file("assets/pune_cooling_buffer_200m.geojson")
underserved = gpd.read_file("assets/pune_hotspots_outside_buffer.geojson")

# Initialize map
m = leafmap.Map(center=[18.52, 73.85], zoom=11)

# Add layers
m.add_gdf(boundary, layer_name="Pune City Boundary")
m.add_raster("assets/pune_LST_C_mar_may2024.tif", layer_name="LST (°C)")
m.add_gdf(hotspots, layer_name="UHI Hotspots >35°C", style={"color": "red", "fillOpacity": 0.3})
m.add_gdf(buffer, layer_name="Cooling Buffer (200m)", style={"color": "blue", "fillOpacity": 0.2})
m.add_gdf(underserved, layer_name="Hotspots Outside Buffer", style={"color": "orange", "fillOpacity": 0.4})

# Display map
m.to_streamlit(height=600)

# Recommendations Section
st.subheader("📌 Recommendations")
st.markdown("""
- **High priority zones:** Areas with high temperature outside the 200m buffer should be targeted.
- **Proposed actions:**
  - Add urban green infrastructure (parks, tree-lined streets)
  - Create or restore water bodies
  - Retrofit rooftops with reflective paint or green roofs

You can export these underserved zones as GeoJSON for planners or city officials.
""")

# Stats
st.subheader("📊 Summary Stats")
st.markdown(f"- Total UHI zones identified: **{len(hotspots)}**")
st.markdown(f"- UHI zones outside cooling buffer: **{len(underserved)}**")

# Export button (optional)
geojson_bytes = underserved.to_json().encode()
st.download_button("📥 Download Underserved UHI Zones (GeoJSON)", data=geojson_bytes, file_name="uhi_outside_buffer.geojson", mime="application/geo+json")

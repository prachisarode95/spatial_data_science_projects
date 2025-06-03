import streamlit as st
from streamlit_option_menu import option_menu
import leafmap.foliumap as leafmap
import geopandas as gpd
import pandas as pd
import plotly.express as px
from io import BytesIO
import base64

# -------------------
# App Configuration
# -------------------
st.set_page_config(page_title="Urban Heat Island Dashboard", layout="wide")

# -------------------
# Sidebar Controls
# -------------------
with st.sidebar:
    st.image("logo.png", width=150)
    selected_lang = option_menu("Language", ["English", "Marathi"], icons=["globe", "globe2"],
                                menu_icon="cast", default_index=0)
    st.header("Filter Options")
    date_options = ["2023-05-01", "2023-06-01"]  # Example dates
    selected_date = st.selectbox("Select Observation Date", date_options)
    uhi_threshold = st.slider("UHI Threshold (\u00b0C)", 30, 50, 35)
    layers_to_show = st.multiselect(
        "Select Layers to Display",
        ["UHI Zones", "Cooling Centers", "Green Spaces", "Built-up Areas", "Population Density"],
        default=["UHI Zones", "Cooling Centers"]
    )

# -------------------
# Language Dictionary (Simple)
# -------------------
if selected_lang == "Marathi":
    lang = {
        "title": "\ud83c\udf06 हवामान-लवचिक शहरी नियोजन डॅशबोर्ड",
        "subtitle": "उष्णता बेट शोध आणि शीतकरण पायाभूत सुविधा मॅपिंग",
        "map_tab": "\ud83d\udccd नकाशा दृश्य",
        "analysis_tab": "\ud83d\udcca विश्लेषण सारांश",
        "reco_tab": "\ud83e\uddf9 शिफारसी",
        "about_tab": "\ud83d\udcdc प्रकल्प बद्दल",
    }
else:
    lang = {
        "title": "\ud83c\udf06 Climate-Resilient Urban Planning Dashboard",
        "subtitle": "Detecting Urban Heat Islands & Mapping Cooling Infrastructure in Pune",
        "map_tab": "\ud83d\udccd Map Viewer",
        "analysis_tab": "\ud83d\udcca Analysis Summary",
        "reco_tab": "\ud83e\uddf9 Interventions",
        "about_tab": "\ud83d\udcdc About Project",
    }

# -------------------
# Header
# -------------------
st.title(lang["title"])
st.markdown(f"**{lang['subtitle']}**")

# -------------------
# Tabs Layout
# -------------------
tab1, tab2, tab3, tab4 = st.tabs([
    lang["map_tab"],
    lang["analysis_tab"],
    lang["reco_tab"],
    lang["about_tab"]
])

# -------------------
# Tab 1: Map Viewer
# -------------------
with tab1:
    st.subheader(lang["map_tab"])
    m = leafmap.Map(center=(18.5204, 73.8567), zoom=11)

    if "UHI Zones" in layers_to_show:
        m.add_geojson("data/uhi_zones.geojson", layer_name="UHI Zones", info_mode="on_hover")
    if "Cooling Centers" in layers_to_show:
        m.add_geojson("data/cooling_centers_cleaned.geojson", layer_name="Cooling Centers")
    if "Green Spaces" in layers_to_show:
        m.add_geojson("data/green_space_cleaned.geojson", layer_name="Green Spaces")
    if "Built-up Areas" in layers_to_show:
        m.add_geojson("data/builtup_cleaned.geojson", layer_name="Built-up Areas")
    if "Population Density" in layers_to_show:
        m.add_raster("data/pop_density.tif", layer_name="Population Density")

    m.add_basemap("CartoDB.Positron")
    m.to_streamlit(width=1000, height=600)

    # Bookmark button
    coords = st.text_input("📌 Bookmark Coordinates (lat, lon)", "18.5204, 73.8567")
    if st.button("🔖 Save Bookmark"):
        st.success(f"Bookmark saved for location: {coords}")

# -------------------
# Tab 2: Analysis Summary
# -------------------
with tab2:
    st.subheader(lang["analysis_tab"])

    # Example metrics - replace with real calculations
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total UHI Zones", 142)
        st.metric("Avg UHI Intensity (\u00b0C)", 37.2)
    with col2:
        st.metric("Cooling Centers Mapped", 55)
        st.metric("Total Green Space (sq.km)", 21.6)

    st.markdown("### Heat Risk Distribution")
    df_heat = pd.DataFrame({"Zone": ["High", "Moderate", "Low"], "Count": [45, 67, 30]})
    st.plotly_chart(px.bar(df_heat, x="Zone", y="Count", color="Zone"))

    st.markdown("### UHI Zone vs Cooling Access")
    st.image("figures/uhi_vs_cooling_access.png")

# -------------------
# Tab 3: Recommendations
# -------------------
with tab3:
    st.subheader(lang["reco_tab"])

    st.markdown("**🔴 High-Risk Zones (Red UHI)**")
    st.markdown("- Add green infrastructure\n- Provide temporary cooling centers\n- Promote rooftop gardens")

    st.markdown("**🟠 Moderate-Risk Zones (Orange UHI)**")
    st.markdown("- Improve street-level airflow\n- Encourage reflective rooftops")

    st.markdown("**🟢 Cool Zones**")
    st.markdown("- Maintain existing green cover\n- Prevent rapid land use changes")

    # Export functionality
    st.download_button("📤 Download GeoJSON", data=open("data/final_layers.geojson", "rb"), file_name="final_layers.geojson")
    df_csv = pd.read_csv("data/final_table.csv")
    st.download_button("📤 Download Summary CSV", df_csv.to_csv(index=False), file_name="summary.csv")

# -------------------
# Tab 4: About Project
# -------------------
with tab4:
    st.subheader(lang["about_tab"])
    st.markdown("""
    This project identifies Urban Heat Island (UHI) zones in Pune city using Landsat 9 LST data
    and overlays cooling infrastructure like green spaces and cooling centers.

    **Objectives:**
    - Detect high-temperature zones
    - Map climate adaptation infrastructure
    - Support evidence-based urban planning

    **Tools Used:** Geemap, Leafmap, Streamlit, GeoPandas, Rasterio

    **Created by:** Prachi | [GitHub](https://github.com/yourusername/urban-heat-dashboard)
    """)

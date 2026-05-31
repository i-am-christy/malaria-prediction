import streamlit as st
import plotly.express as px
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from app.utils.map_data import get_state_risk_data

st.title("🗺️ Malaria Risk Map - Nigeria")
st.markdown("State-level malaria positivity rates derived from NMIS 2021 data.")

df = get_state_risk_data()
fig = px.scatter_mapbox(
    df,
    lat="latitude", lon="longitude",
    size="positivity_rate", color="positivity_rate",
    hover_name="state",
    hover_data={"risk_level": True, "positivity_rate": True, "latitude": False, "longitude": False},
    color_continuous_scale="Reds",
    zoom=5, center={"lat": 9.0, "lon": 8.0},
    mapbox_style="carto-positron"
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig, use_container_width=True)

st.dataframe(
    df[["state", "positivity_rate", "risk_level"]]
    .sort_values(by="positivity_rate", ascending=False)
    .reset_index(drop=True)
)
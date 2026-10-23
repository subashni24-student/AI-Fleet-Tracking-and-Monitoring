import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fleet Monitoring", layout="wide")

st.title("AI-Powered Vehicle Tracking")
st.subheader("Fleet Monitoring Dashboard")

vehicles = {
    "Vehicle ID": ["V001", "V005"],
    "Speed (km/h)": [85, 55],
    "Fuel (%)": [90, 25],
    "Latitude": [11.6643, 10.7905],
    "Longitude": [78.1460, 78.7047]
}

df = pd.DataFrame(vehicles)

col1, col2, col3 = st.columns(3)
col1.metric("Total Vehicles", len(df))
col2.metric("High Speed Alerts", int((df["Speed (km/h)"] > 80).sum()))
col3.metric("Low Fuel Alerts", int((df["Fuel (%)"] < 30).sum()))

st.subheader("Vehicle Details")
st.dataframe(df, use_container_width=True)

st.subheader("Vehicle Locations")
st.map(df.rename(columns={"Latitude": "lat", "Longitude": "lon"}))

st.subheader("Vehicle Alerts")

for _, vehicle in df.iterrows():
    if vehicle["Speed (km/h)"] > 80:
        st.error(f'{vehicle["Vehicle ID"]}: HIGH SPEED ALERT')
    if vehicle["Fuel (%)"] < 30:
        st.warning(f'{vehicle["Vehicle ID"]}: LOW FUEL ALERT')
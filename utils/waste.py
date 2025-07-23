import streamlit as st
from sample_data import waste_data
from utils.common import load_or_sample, plot_timeseries
import numpy as np

def waste_dashboard():
    st.header("Waste Generation & Minimization")
    df = load_or_sample("Waste", waste_data, "Upload waste data or use sample data.")
    if df is not None:
        st.success("Data Loaded")
        st.write("Last 5 records:", df.tail())
        plot_timeseries(df, ["slag_ton", "dust_ton", "wastewater_m3"], "Waste Streams", "Tonnes / m3")

        st.subheader("KPIs")
        st.metric("Total Slag (t)", f"{df['slag_ton'].sum():.1f}")
        st.metric("Total Dust (t)", f"{df['dust_ton'].sum():.2f}")
        st.metric("Total Wastewater (m3)", f"{df['wastewater_m3'].sum():.1f}")

        st.subheader("Optimization Suggestion")
        if df["slag_ton"].mean() > 9:
            st.warning("High slag generation – consider better separation or process tuning.")
        else:
            st.success("Slag generation is under control.")

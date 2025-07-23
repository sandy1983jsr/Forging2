import streamlit as st
from sample_data import water_data
from utils.common import load_or_sample, plot_timeseries
import numpy as np

def water_dashboard():
    st.header("Water Consumption & Optimization")
    df = load_or_sample("Water", water_data, "Upload water meters or use sample data.")
    if df is not None:
        st.success("Data Loaded")
        st.write("Last 5 records:", df.tail())
        plot_timeseries(df, ["water_in_m3", "water_out_m3"], "Water In/Out", "m3")

        st.subheader("KPIs")
        total_in = df["water_in_m3"].sum()
        total_out = df["water_out_m3"].sum()
        loss = total_in - total_out
        st.metric("Total Inflow (m3)", f"{total_in:.1f}")
        st.metric("Total Outflow (m3)", f"{total_out:.1f}")
        st.metric("Net Loss (evap/leak, m3)", f"{loss:.1f}")

        st.subheader("Optimization Suggestion")
        if loss/total_in > 0.12:
            st.warning("High water loss (>12%) – check for leaks or excessive evaporation.")
        else:
            st.success("Water loss within acceptable range.")

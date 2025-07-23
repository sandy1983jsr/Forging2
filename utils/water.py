import streamlit as st
import numpy as np
import plotly.express as px
from sample_data import water_data
from utils.common import unified_data_loader

def water_dashboard():
    st.header("Water Consumption & Optimization")
    df = unified_data_loader("Water", water_data)
    if df is not None:
        st.success("Data Loaded")
        st.write(df.tail())
        fig = px.line(df, x="timestamp", y=["water_in_m3", "water_out_m3"], title="Water In/Out", labels={"value":"m3"})
        st.plotly_chart(fig, use_container_width=True)

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

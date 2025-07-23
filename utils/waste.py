import streamlit as st
import numpy as np
import plotly.express as px
from sample_data import waste_data
from utils.common import unified_data_loader

def waste_dashboard():
    st.header("Waste Generation & Minimization")
    df = unified_data_loader("Waste", waste_data)
    if df is not None:
        st.success("Data Loaded")
        st.write(df.tail())
        fig = px.line(df, x="timestamp", y=["slag_ton", "dust_ton", "wastewater_m3"],
                      title="Waste Streams", labels={"value":"Tonnes / m3"})
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("KPIs")
        st.metric("Total Slag (t)", f"{df['slag_ton'].sum():.1f}")
        st.metric("Total Dust (t)", f"{df['dust_ton'].sum():.2f}")
        st.metric("Total Wastewater (m3)", f"{df['wastewater_m3'].sum():.1f}")

        st.subheader("Optimization Suggestion")
        if df["slag_ton"].mean() > 9:
            st.warning("High slag generation – consider better separation or process tuning.")
        else:
            st.success("Slag generation is under control.")

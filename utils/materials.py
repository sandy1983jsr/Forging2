import streamlit as st
from sample_data import materials_data
from utils.common import load_or_sample, plot_timeseries
import numpy as np

def materials_dashboard():
    st.header("Materials Use & Optimization")
    df = load_or_sample("Materials", materials_data, "Upload materials data or use sample data.")
    if df is not None:
        st.success("Data Loaded")
        st.write("Last 5 records:", df.tail())
        plot_timeseries(df, ["scrap_in_ton", "alloy_addition_ton", "output_steel_ton"], "Materials Flow", "Tonnes")

        st.subheader("KPIs")
        yield_ = df["output_steel_ton"].sum() / df["scrap_in_ton"].sum()
        st.metric("Yield (output/scrap)", f"{yield_:.2%}")
        st.metric("Total Scrap Used (t)", f"{df['scrap_in_ton'].sum():.1f}")
        st.metric("Total Alloy Added (t)", f"{df['alloy_addition_ton'].sum():.1f}")
        st.metric("Total Steel Output (t)", f"{df['output_steel_ton'].sum():.1f}")

        st.subheader("Optimization Suggestion")
        if yield_ < 0.95:
            st.warning("Yield below 95% – investigate scrap quality or process losses.")
        else:
            st.success("Yield is good.")

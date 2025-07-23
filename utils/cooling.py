import streamlit as st
from sample_data import cooling_data
from utils.common import load_or_sample, plot_timeseries
import numpy as np

def cooling_dashboard():
    st.header("Cooling System Optimization")
    df = load_or_sample("Cooling", cooling_data, "Upload cooling data or use sample data.")
    if df is not None:
        st.success("Data Loaded")
        st.write("Last 5 records:", df.tail())
        plot_timeseries(df, ["chilled_water_inflow_m3", "chilled_water_outflow_m3"], "Chilled Water Flows", "m3")
        plot_timeseries(df, ["cooling_power_MW"], "Cooling Power", "MW")

        st.subheader("KPIs")
        eff = df["chilled_water_outflow_m3"].sum() / df["chilled_water_inflow_m3"].sum()
        st.metric("Cooling Efficiency (m3 out/in)", f"{eff:.2%}")
        st.metric("Total Cooling Power (MWh)", f"{df['cooling_power_MW'].sum():.1f}")

        st.subheader("Optimization Suggestion")
        if eff<0.9:
            st.warning("Cooling efficiency below 90% – check for losses or fouling.")
        else:
            st.success("Cooling efficiency is high.")

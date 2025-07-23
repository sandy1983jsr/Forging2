import streamlit as st
import numpy as np
import plotly.express as px
from sample_data import cooling_data
from utils.common import unified_data_loader

def cooling_dashboard():
    st.header("Cooling System Optimization")
    df = unified_data_loader("Cooling", cooling_data)
    if df is not None:
        st.success("Data Loaded")
        st.write(df.tail())
        fig1 = px.line(df, x="timestamp", y=["chilled_water_inflow_m3", "chilled_water_outflow_m3"],
                       title="Chilled Water Flows", labels={"value":"m3"})
        st.plotly_chart(fig1, use_container_width=True)
        fig2 = px.line(df, x="timestamp", y="cooling_power_MW", title="Cooling Power", labels={"value":"MW"})
        st.plotly_chart(fig2, use_container_width=True)

        st.subheader("KPIs")
        eff = df["chilled_water_outflow_m3"].sum() / df["chilled_water_inflow_m3"].sum()
        st.metric("Cooling Efficiency (m3 out/in)", f"{eff:.2%}")
        st.metric("Total Cooling Power (MWh)", f"{df['cooling_power_MW'].sum():.1f}")

        st.subheader("Optimization Suggestion")
        if eff < 0.9:
            st.warning("Cooling efficiency below 90% – check for losses or fouling.")
        else:
            st.success("Cooling efficiency is high.")

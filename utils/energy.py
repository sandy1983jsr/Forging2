import streamlit as st
from sample_data import energy_data
from utils.common import load_or_sample, plot_timeseries
import numpy as np

def energy_dashboard():
    st.header("Electric Arc Furnace (EAF) – Electricity Optimization")
    df = load_or_sample("EAF Energy", energy_data, "Upload EAF meters or use sample data.")
    if df is not None:
        st.success("Data Loaded")
        st.write("Last 5 records:", df.tail())
        plot_timeseries(df, ["EAF1_MWh", "EAF2_MWh", "EAF3_MWh"], "EAF Power Usage", "MWh")

        st.subheader("KPIs")
        st.metric("Total EAF1 (MWh)", f"{df['EAF1_MWh'].sum():.1f}")
        st.metric("Total EAF2 (MWh)", f"{df['EAF2_MWh'].sum():.1f}")
        st.metric("Total EAF3 (MWh)", f"{df['EAF3_MWh'].sum():.1f}")
        st.metric("Total EAFs (MWh)", f"{df[['EAF1_MWh','EAF2_MWh','EAF3_MWh']].sum().sum():.1f}")

        st.subheader("Optimization Suggestion")
        mean = df[["EAF1_MWh","EAF2_MWh","EAF3_MWh"]].mean()
        best_eaf = mean.idxmin()
        st.info(f"**Best performing EAF:** {best_eaf} (lowest avg energy/MWh)")
        st.write("Consider scheduling maintenance for EAF with highest mean consumption.")

        st.subheader("Efficiency/Anomalies")
        zscore = (df[["EAF1_MWh","EAF2_MWh","EAF3_MWh"]] - mean)/df[["EAF1_MWh","EAF2_MWh","EAF3_MWh"]].std()
        anomalies = df[(np.abs(zscore)>2).any(axis=1)]
        if not anomalies.empty:
            st.warning(f"Possible anomalies: {len(anomalies)} records")
            st.dataframe(anomalies)
        else:
            st.success("No major anomalies detected.")

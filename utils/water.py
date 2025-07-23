import streamlit as st
from sample_data import gas_data
from utils.common import load_or_sample, plot_timeseries
import numpy as np

def gas_dashboard():
    st.header("RLNG Furnace – Gas Optimization")
    df = load_or_sample("RLNG Gas", gas_data, "Upload RLNG gas data or use sample data.")
    if df is not None:
        st.success("Data Loaded")
        st.write("Last 5 records:", df.tail())
        plot_timeseries(df, ["RLNG_MMBTU"], "RLNG Gas Use", "MMBTU")

        st.subheader("KPIs")
        st.metric("Total RLNG (MMBTU)", f"{df['RLNG_MMBTU'].sum():.1f}")
        st.metric("Mean RLNG/hr", f"{df['RLNG_MMBTU'].mean():.2f}")

        st.subheader("Optimization Suggestion")
        if df['RLNG_MMBTU'].mean() > 210:
            st.warning("High average RLNG use – check furnace tuning or preheating.")
        else:
            st.success("RLNG use within expected range.")

        st.subheader("Anomaly Detection")
        zscore = (df["RLNG_MMBTU"]-df["RLNG_MMBTU"].mean())/df["RLNG_MMBTU"].std()
        anomalies = df[np.abs(zscore)>2]
        if not anomalies.empty:
            st.warning(f"High RLNG use detected in {len(anomalies)} records.")
            st.dataframe(anomalies)
        else:
            st.success("No major anomalies detected.")

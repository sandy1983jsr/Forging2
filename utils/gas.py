import streamlit as st
import numpy as np
import plotly.express as px
from sample_data import gas_data
from utils.common import unified_data_loader

def gas_dashboard():
    st.header("RLNG Furnace – Gas Optimization")
    df = unified_data_loader("Gas", gas_data)
    if df is not None:
        st.success("Data Loaded")
        st.write(df.tail())
        fig = px.line(df, x="timestamp", y="RLNG_MMBTU", title="RLNG Gas Use", labels={"value":"MMBTU"})
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("KPIs")
        st.metric("Total RLNG (MMBTU)", f"{df['RLNG_MMBTU'].sum():.1f}")
        st.metric("Mean RLNG/hr", f"{df['RLNG_MMBTU'].mean():.2f}")

        st.subheader("Optimization Suggestion")
        if df['RLNG_MMBTU'].mean() > 210:
            st.warning("High RLNG use – check furnace tuning or preheating.")
        else:
            st.success("RLNG use within expected range.")

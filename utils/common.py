import pandas as pd
import streamlit as st

def unified_data_loader(label, generator_func, helptext="Upload CSV, connect SCADA, or use sample data"):
    st.write(helptext)
    method = st.radio(
        f"{label} Data Source",
        options=["Upload CSV", "Connect SCADA", "Sample Data"],
        horizontal=True,
        key=f"{label}_method"
    )
    df = None
    if method == "Upload CSV":
        uploaded = st.file_uploader(f"Upload {label} CSV", type=["csv"], key=f"{label}_csv")
        if uploaded:
            df = pd.read_csv(uploaded)
    elif method == "Connect SCADA":
        st.info("Simulated SCADA connection. Replace this with real SCADA integration.")
        if st.button(f"Load {label} from SCADA", key=f"{label}_scada"):
            df = generator_func()  # Simulate SCADA with sample data for now
    elif method == "Sample Data":
        if st.button(f"Generate Sample {label} Data", key=f"{label}_sample"):
            df = generator_func()
    return df

import pandas as pd
import plotly.express as px
import streamlit as st

def load_or_sample(file_label, generator_func, helptext="Upload CSV or use sample data"):
    st.write(helptext)
    uploaded = st.file_uploader(f"Upload {file_label} CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        if st.button(f"Use Sample {file_label} Data"):
            df = generator_func()
        else:
            df = None
    return df

def plot_timeseries(df, ycols, title, ylabel):
    fig = px.line(df, x="timestamp", y=ycols, title=title, labels={"value": ylabel})
    st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sample_data import materials_data
from utils.common import unified_data_loader

def make_material_sankey(df):
    sources = ["Scrap", "Alloy", "Steel Output", "Steel Output"]
    targets = ["Steel Output", "Steel Output", "Waste", "Billet"]
    values = [
        df["scrap_in_ton"].sum(),
        df["alloy_addition_ton"].sum(),
        (df["scrap_in_ton"]+df["alloy_addition_ton"]).sum() - df["output_steel_ton"].sum(),  # waste
        df["billet_size_ton"].sum()
    ]
    label = list(set(sources + targets))
    label_idx = {l: i for i, l in enumerate(label)}
    sankey = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=label,
            color="grey"
        ),
        link=dict(
            source=[label_idx[s] for s in sources],
            target=[label_idx[t] for t in targets],
            value=values,
        ))])
    sankey.update_layout(title_text="Material Flow Sankey Diagram", font_size=12)
    return sankey

def materials_dashboard():
    st.header("Materials Use & Optimization")
    df = unified_data_loader("Materials", materials_data)
    if df is not None:
        st.success("Data Loaded")
        st.write(df.tail())
        st.subheader("Material Flows")
        fig = px.line(df, x="timestamp", y=["scrap_in_ton", "alloy_addition_ton", "output_steel_ton"],
                      title="Materials Consumption & Output", labels={"value":"Tonnes"})
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("KPIs")
        yield_ = df["output_steel_ton"].sum() / df["scrap_in_ton"].sum()
        st.metric("Improved Material Yield", f"{yield_:.2%}")
        st.metric("Total Scrap (t)", f"{df['scrap_in_ton'].sum():.1f}")
        st.metric("Total Alloy (t)", f"{df['alloy_addition_ton'].sum():.1f}")
        st.metric("Total Steel Output (t)", f"{df['output_steel_ton'].sum():.1f}")

        st.subheader("Material Saving in Billet Size")
        recommended_billet = df["output_steel_ton"].mean() * 1.02  # 2% safety
        actual_billet = df["billet_size_ton"].mean()
        st.metric("Recommended Billet Size (t)", f"{recommended_billet:.2f}")
        st.metric("Actual Billet Size (t)", f"{actual_billet:.2f}")
        if actual_billet > recommended_billet + 0.1:
            st.warning("Billet size can be reduced to save material.")
        else:
            st.success("Billet sizing is close to optimal.")

        st.subheader("Material Sankey Diagram")
        st.plotly_chart(make_material_sankey(df), use_container_width=True)

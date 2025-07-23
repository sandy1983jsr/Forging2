import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sample_data import energy_data
from utils.common import unified_data_loader

def make_energy_sankey(df):
    # Simulate an energy flow for Sankey
    sources = ["Grid", "Grid", "Grid", "EAF1", "EAF2", "EAF3", "Forging"]
    targets = ["EAF1", "EAF2", "EAF3", "Forging", "Forging", "Forging", "Losses"]
    values = [
        df["EAF1_MWh"].sum(),
        df["EAF2_MWh"].sum(),
        df["EAF3_MWh"].sum(),
        df["forging_hot_energy_MWh"].sum(),  # EAF1 to Forging
        df["forging_hot_energy_MWh"].sum(),  # EAF2 to Forging (simulate)
        df["forging_hot_energy_MWh"].sum(),  # EAF3 to Forging (simulate)
        df["EAF1_MWh"].sum()*0.07 + df["EAF2_MWh"].sum()*0.07 + df["EAF3_MWh"].sum()*0.07  # Losses
    ]
    label = list(set(sources + targets))
    label_idx = {l: i for i, l in enumerate(label)}
    sankey = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=label,
            color="orange"
        ),
        link=dict(
            source=[label_idx[s] for s in sources],
            target=[label_idx[t] for t in targets],
            value=values,
        ))])
    sankey.update_layout(title_text="Energy Flow Sankey Diagram", font_size=12)
    return sankey

def show_fea_results():
    st.subheader("Finite Element Analysis (FEA)")
    st.info("FEA simulation: Effective Stress Distribution in Forging Die (sample)")
    fig = px.imshow(np.random.rand(10, 10), color_continuous_scale="Viridis", aspect="auto",
                    labels={'color':'Stress (MPa)'})
    st.plotly_chart(fig, use_container_width=True)

def show_cfd_results():
    st.subheader("CFD Analysis")
    st.info("CFD simulation: Temperature/Flow in Forging Chamber (sample)")
    fig = px.imshow(np.random.normal(300, 30, (10, 10)), color_continuous_scale="RdBu", aspect="auto",
                    labels={'color':'Temp (°C)'})
    st.plotly_chart(fig, use_container_width=True)

def energy_dashboard():
    st.header("Energy (EAF & Forging) Optimization")
    df = unified_data_loader("Energy", energy_data)
    if df is not None:
        st.success("Data Loaded")
        st.write(df.tail())
        st.subheader("EAF & Forging Energy Consumption")
        fig = px.line(df, x="timestamp", y=["EAF1_MWh", "EAF2_MWh", "EAF3_MWh", "forging_hot_energy_MWh"],
                      title="EAF & Forging Energy Use", labels={"value":"Energy (MWh)"})
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("KPIs & Optimization")
        eaf_total = df[["EAF1_MWh", "EAF2_MWh", "EAF3_MWh"]].sum().sum()
        forging_total = df["forging_hot_energy_MWh"].sum()
        st.metric("Total EAF Energy (MWh)", f"{eaf_total:.1f}")
        st.metric("Total Forging Energy (MWh)", f"{forging_total:.1f}")

        # Energy-Saving Hot Open Die Forging
        st.info("**Energy-Saving Hot Open Die Forging:**\n"
                "- Use optimized temperature control and tool preheating\n"
                "- Minimize idle time\n"
                "- Use waste heat recovery from EAF exhaust\n"
                "- Monitor with real-time sensors for process tuning")

        st.subheader("Energy Flow Sankey Diagram")
        st.plotly_chart(make_energy_sankey(df), use_container_width=True)

        # FEA & CFD
        show_fea_results()
        show_cfd_results()

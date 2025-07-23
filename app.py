import streamlit as st
from utils.energy import energy_dashboard
from utils.gas import gas_dashboard
from utils.water import water_dashboard
from utils.cooling import cooling_dashboard
from utils.materials import materials_dashboard
from utils.waste import waste_dashboard

st.set_page_config(page_title="RKFL Utilities Optimization", layout="wide")
st.sidebar.image("https://img.icons8.com/fluency/48/000000/automation.png", width=48)
st.sidebar.title("RKFL Utilities & Sustainability")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Electricity (EAF)", 
    "Gas (RLNG)", 
    "Water",
    "Cooling",
    "Materials",
    "Waste"
])

with tab1:
    energy_dashboard()

with tab2:
    gas_dashboard()

with tab3:
    water_dashboard()

with tab4:
    cooling_dashboard()

with tab5:
    materials_dashboard()

with tab6:
    waste_dashboard()

import pandas as pd
import numpy as np

def energy_data():
    ts = pd.date_range("2025-01-01", periods=7*24, freq="H")
    return pd.DataFrame({
        "timestamp": ts,
        "EAF1_MWh": np.random.normal(22, 3, len(ts)),
        "EAF2_MWh": np.random.normal(21, 3, len(ts)),
        "EAF3_MWh": np.random.normal(20, 3, len(ts)),
        "forging_hot_energy_MWh": np.random.normal(6, 1, len(ts))
    })

def gas_data():
    ts = pd.date_range("2025-01-01", periods=7*24, freq="H")
    return pd.DataFrame({
        "timestamp": ts,
        "RLNG_MMBTU": np.random.normal(200, 30, len(ts)),
    })

def water_data():
    ts = pd.date_range("2025-01-01", periods=7*24, freq="H")
    return pd.DataFrame({
        "timestamp": ts,
        "water_in_m3": np.random.normal(120, 25, len(ts)),
        "water_out_m3": np.random.normal(110, 20, len(ts)),
    })

def cooling_data():
    ts = pd.date_range("2025-01-01", periods=7*24, freq="H")
    return pd.DataFrame({
        "timestamp": ts,
        "chilled_water_inflow_m3": np.random.normal(95, 10, len(ts)),
        "chilled_water_outflow_m3": np.random.normal(90, 10, len(ts)),
        "cooling_power_MW": np.random.normal(3, 0.3, len(ts)),
    })

def materials_data():
    ts = pd.date_range("2025-01-01", periods=7*24, freq="H")
    billet_sizes = np.random.choice([1.2, 1.5, 2.0], len(ts), p=[0.3, 0.5, 0.2])
    scrap = np.random.normal(50, 8, len(ts))
    steel = scrap * np.random.uniform(0.92, 0.98, len(ts))
    return pd.DataFrame({
        "timestamp": ts,
        "scrap_in_ton": scrap,
        "alloy_addition_ton": np.random.normal(2, 0.5, len(ts)),
        "output_steel_ton": steel,
        "billet_size_ton": billet_sizes
    })

def waste_data():
    ts = pd.date_range("2025-01-01", periods=7*24, freq="H")
    return pd.DataFrame({
        "timestamp": ts,
        "slag_ton": np.random.normal(8, 2, len(ts)),
        "dust_ton": np.random.normal(0.5, 0.1, len(ts)),
        "wastewater_m3": np.random.normal(12, 3, len(ts)),
    })

import pandas as pd
import numpy as np

def get_scada_data():
    # Simulate SCADA/meter data retrieval for demo
    ts = pd.date_range("2024-01-01", periods=30*24, freq="H")
    return pd.DataFrame({
        "timestamp": ts,
        "meter_reading": np.abs(np.random.normal(400, 100, size=len(ts)))  # Simulated kWh
    })

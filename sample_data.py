import pandas as pd
import numpy as np

def generate_sample_data():
    ts = pd.date_range("2024-06-01", periods=7*24, freq="H")
    noise = np.random.normal(0, 15, size=len(ts))
    base = 350 + 30*np.sin(2 * np.pi * ts.hour / 24)
    reading = base + noise
    return pd.DataFrame({
        "timestamp": ts,
        "meter_reading": np.abs(reading)
    })

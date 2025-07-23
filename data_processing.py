import pandas as pd
import numpy as np

def process_data(df):
    # Ensure timestamp and sort
    df = df.copy()
    if "timestamp" in df:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df = df.sort_values("timestamp")
    # Remove duplicates
    df = df.drop_duplicates(subset="timestamp")
    # QC: missing, outlier detection
    n_missing = df["meter_reading"].isnull().sum()
    outlier_thresh = df["meter_reading"].mean() + 3*df["meter_reading"].std()
    n_outliers = (df["meter_reading"] > outlier_thresh).sum()
    qc_report = pd.DataFrame({
        "Metric": ["Missing Values", "Outliers (>3σ)", "Total Records"],
        "Value": [n_missing, n_outliers, len(df)]
    })
    # Fill missing values with linear interpolation
    df["meter_reading"] = df["meter_reading"].interpolate()
    # Remove extreme outliers
    df = df[df["meter_reading"] < outlier_thresh*2]
    return df, qc_report

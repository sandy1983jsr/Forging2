import numpy as np
import pandas as pd
from scipy import stats
from scipy.fft import fft, fftfreq

def run_analyses(df):
    results = {}

    # Descriptive stats
    results["describe"] = df["meter_reading"].describe()

    # Load profile: daily mean, std
    df["date"] = df["timestamp"].dt.date
    daily = df.groupby("date")["meter_reading"].agg(["mean", "std"])
    results["daily_profile"] = daily

    # Hourly profile (average per hour-of-day)
    df["hour"] = df["timestamp"].dt.hour
    hourly = df.groupby("hour")["meter_reading"].agg(["mean", "std"])
    results["hourly_profile"] = hourly

    # Trend analysis: linear regression
    x = np.arange(len(df))
    y = df["meter_reading"].values
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    results["trend"] = {
        "slope": slope, "intercept": intercept,
        "r_value": r_value, "p_value": p_value
    }

    # Anomaly detection: z-score
    zscores = np.abs(stats.zscore(df["meter_reading"]))
    anomaly_idx = np.where(zscores > 3)[0]
    results["anomalies"] = df.iloc[anomaly_idx][["timestamp", "meter_reading"]]

    # Spectral/Fourier analysis
    yf = np.abs(fft(y - np.mean(y)))
    xf = fftfreq(len(y), d=1)  # d=1 hour between samples
    results["fft_freq"] = xf[:len(y)//2]
    results["fft_magnitude"] = yf[:len(y)//2]

    # Correlation with time of day
    results["hour_corr"] = np.corrcoef(df["hour"], df["meter_reading"])[0,1]

    return results

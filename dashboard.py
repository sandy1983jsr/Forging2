import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def show_dashboards(df, results):
    st.header("📊 Scientific & Engineering Dashboards")

    # Time Series Overview
    st.subheader("Time Series Overview")
    fig = px.line(df, x="timestamp", y="meter_reading", labels={"meter_reading": "Meter Reading (kWh)"})
    st.plotly_chart(fig, use_container_width=True)

    # Daily Profile
    st.subheader("Daily Load Profile")
    fig2 = px.line(results["daily_profile"], y="mean", labels={"value": "Mean Meter Reading (kWh)"})
    st.plotly_chart(fig2, use_container_width=True)

    # Hourly Profile
    st.subheader("Average Hourly Profile")
    fig3 = px.line(results["hourly_profile"], y="mean", labels={"value": "Mean Meter Reading (kWh)"})
    st.plotly_chart(fig3, use_container_width=True)

    # Trend Line
    st.subheader("Trend Analysis")
    slope = results["trend"]["slope"]
    st.write(f"Linear trend slope: {slope:.2f} kWh/unit time")
    trend_fig = px.scatter(df, x="timestamp", y="meter_reading", opacity=0.5)
    trend_line = df["meter_reading"].values[0] + slope * (df.index - df.index[0])
    trend_fig.add_traces(go.Scatter(x=df["timestamp"], y=trend_line, mode="lines", name="Trend"))
    st.plotly_chart(trend_fig, use_container_width=True)

    # Anomaly Detection
    st.subheader("Anomaly Detection (Z-score > 3)")
    if not results["anomalies"].empty:
        st.dataframe(results["anomalies"])
        anomaly_fig = px.scatter(df, x="timestamp", y="meter_reading", opacity=0.5)
        anomaly_fig.add_traces(go.Scatter(
            x=results["anomalies"]["timestamp"],
            y=results["anomalies"]["meter_reading"],
            mode="markers",
            marker=dict(color="red", size=10),
            name="Anomalies"
        ))
        st.plotly_chart(anomaly_fig, use_container_width=True)
    else:
        st.write("No significant anomalies detected.")

    # Spectral Analysis
    st.subheader("Fourier/Spectral Analysis")
    freq = results["fft_freq"]
    mag = results["fft_magnitude"]
    spectrum_fig = go.Figure()
    spectrum_fig.add_trace(go.Scatter(x=freq, y=mag, mode="lines", name="FFT"))
    spectrum_fig.update_layout(xaxis_title="Frequency (1/hr)", yaxis_title="Magnitude")
    st.plotly_chart(spectrum_fig, use_container_width=True)

    # Correlation
    st.subheader("Correlation: Meter Reading vs. Hour of Day")
    st.write(f"Correlation coefficient: {results['hour_corr']:.2f}")

    # Descriptive Stats
    st.subheader("Descriptive Statistics")
    st.table(results["describe"])

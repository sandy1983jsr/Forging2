import io
from fpdf import FPDF

def build_pdf_report(df, results):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.set_text_color(255,129,0)  # Orange
    pdf.cell(200, 10, txt="RKFL Scientific & Digital Analysis Report", ln=True, align="C")
    pdf.set_text_color(34,34,34)
    pdf.set_font("Arial", size=10)
    pdf.ln(8)
    pdf.multi_cell(0, 10, "This report summarizes the results of the engineering and scientific analysis performed on the uploaded data. The analyses include data quality assessment, load profiling, anomaly detection, trend and spectral analysis.")
    pdf.ln(4)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Descriptive Statistics", ln=True)
    pdf.set_font("Arial", size=10)
    desc = results["describe"]
    for stat, value in desc.items():
        pdf.cell(0, 8, f"{stat}: {value:.2f}", ln=True)
    pdf.ln(4)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Trend Analysis", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 8, f"Slope: {results['trend']['slope']:.2f} | R-value: {results['trend']['r_value']:.2f} | P-value: {results['trend']['p_value']:.4f}", ln=True)
    pdf.ln(4)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Detected Anomalies", ln=True)
    pdf.set_font("Arial", size=10)
    anomalies = results["anomalies"]
    if anomalies.empty:
        pdf.cell(0, 8, "No significant anomalies detected.", ln=True)
    else:
        for idx, row in anomalies.iterrows():
            pdf.cell(0, 8, f"{row['timestamp']}: {row['meter_reading']:.2f}", ln=True)
    pdf.ln(4)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Spectral Analysis (dominant frequencies)", ln=True)
    pdf.set_font("Arial", size=10)
    freq = results["fft_freq"]
    mag = results["fft_magnitude"]
    dominant = freq[mag.argmax()]
    pdf.cell(0, 8, f"Dominant frequency: {dominant:.4f} 1/hr", ln=True)
    pdf.ln(4)
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Correlation", ln=True)
    pdf.set_font("Arial", size=10)
    pdf.cell(0, 8, f"Meter reading vs. hour of day: r = {results['hour_corr']:.2f}", ln=True)
    pdf.ln(8)
    pdf.set_font("Arial", style="U", size=10)
    pdf.cell(0, 10, "End of Report", ln=True, align="C")
    pdf_bytes = pdf.output(dest='S').encode('latin1')
    return io.BytesIO(pdf_bytes)

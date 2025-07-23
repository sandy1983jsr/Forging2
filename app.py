import streamlit as st
from workflow import WorkflowManager
from scada_module import get_scada_data
from data_processing import process_data
from sample_data import generate_sample_data
from dashboard import show_dashboards
from reporting import build_pdf_report

st.set_page_config(page_title="RKFL Scientific & Digital Dashboard", layout="wide", initial_sidebar_state="expanded")
st.sidebar.image("https://img.icons8.com/fluency/48/000000/automation.png", width=48)
st.sidebar.title("RKFL Workflow")

workflow = WorkflowManager()

# Step 1: Data Ingestion
st.sidebar.subheader("Step 1: Data Source")
data_source = st.sidebar.radio("Select Data Source", ("SCADA/Meter", "Upload CSV", "Sample Data"))
data = None

if workflow.state == "ingest":
    if data_source == "SCADA/Meter":
        st.info("Simulated SCADA/Meter connection. Replace with real API for production.")
        if st.button("Load SCADA/Meter Data"):
            data = get_scada_data()
            workflow.advance("review")
    elif data_source == "Upload CSV":
        uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
        if uploaded_file:
            import pandas as pd
            data = pd.read_csv(uploaded_file)
            workflow.advance("review")
    elif data_source == "Sample Data":
        if st.button("Generate Sample Data"):
            data = generate_sample_data()
            workflow.advance("review")
    st.stop()

# Step 2: Data Review & Preprocessing
if workflow.state == "review":
    st.subheader("Step 2: Data Review & Preprocessing")
    if data is None:
        st.warning("No data loaded. Please go back and select a data source.")
        workflow.reset()
        st.stop()
    st.write("Preview of raw data:")
    st.write(data.head())
    if st.button("Process & Clean Data"):
        processed_data, qc_report = process_data(data)
        workflow.data = processed_data
        workflow.qc_report = qc_report
        workflow.advance("analyze")
    st.stop()

# Step 3: Scientific & Engineering Analysis
if workflow.state == "analyze":
    st.subheader("Step 3: Scientific & Engineering Analysis")
    st.write("Key Data Quality Metrics:")
    st.dataframe(workflow.qc_report)
    from analysis import run_analyses
    analysis_results = run_analyses(workflow.data)
    workflow.analysis_results = analysis_results
    show_dashboards(workflow.data, analysis_results)
    if st.button("Proceed to Reporting"):
        workflow.advance("report")
    st.stop()

# Step 4: Automated Reporting
if workflow.state == "report":
    st.subheader("Step 4: Automated Reporting")
    st.write("Generate a consulting-grade report (PDF) with all key findings, figures, and summary.")
    if st.button("Generate PDF Report"):
        pdf_bytes = build_pdf_report(workflow.data, workflow.analysis_results)
        st.success("Report generated successfully!")
        st.download_button(
            label="Download PDF Report",
            data=pdf_bytes,
            file_name="RKFL_Analysis_Report.pdf",
            mime="application/pdf"
        )
    if st.button("Restart Workflow"):
        workflow.reset()

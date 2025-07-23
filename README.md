# RKFL Scientific & Digital Dashboard

A consulting-grade, end-to-end workflow tool for scientific and engineering time series analysis, designed for meter/SCADA/csv data. Includes data ingestion, cleaning, profiling, anomaly and trend detection, spectral analysis, automated reporting, and workflow automation.

## Features

- **Data Sources:** SCADA/meter (simulated), CSV upload, or random sample data.
- **Automated Workflow:** Stepwise ingestion, review, analysis, reporting.
- **Analysis:** Descriptive stats, quality checks, load profiles, anomaly/trend/spectral/correlation analysis.
- **Dashboards:** Interactive, consulting-grade, with orange/grey/white theme.
- **Reporting:** Automated PDF report generation.
- **Ready for production and extension.**

## Usage

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Customization

- Integrate your own SCADA/meter API in `scada_module.py`.
- Extend analysis in `analysis.py` for your domain.
- Modify reporting in `reporting.py` as needed.

---

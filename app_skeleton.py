import streamlit as st
import numpy as np

# Page configuration
st.set_page_config(
    page_title="TerraSpectra — Hyperspectral Crop Disease Forecasting",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (TerraSpectra Agricultural Aesthetic)
st.markdown("""
<style>
    :root {
        --primary-green: #1B5E20;
        --secondary-green: #4CAF50;
        --light-green: #E8F5E9;
        --accent-gold: #C0CA33;
        --neutral-dark: #212121;
        --neutral-light: #F9FBE7;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 100%);
        padding: 24px;
        border-radius: 12px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .main-header h1 {
        color: #FFFFFF !important;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
    }
    
    .main-header p {
        color: #C8E6C9;
        font-size: 1.05rem;
        margin-top: 6px;
        margin-bottom: 0;
    }
    
    .metric-card {
        background-color: #FFFFFF;
        padding: 16px;
        border-radius: 8px;
        border-left: 4px solid #2E7D32;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        margin-bottom: 12px;
    }
    
    .stSidebar {
        background-color: #F8F9FA;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("https://img.icons8.com/color/96/000000/leaf.png", width=64)
    st.markdown("### **TerraSpectra**")
    st.markdown("*Intelligent Hyperspectral Insights*")
    st.markdown("---")
    
    pages = [
        "1. Overview & Objectives",
        "2. Dataset Explorer",
        "3. Spectral Analysis",
        "4. Disease Prediction",
        "5. Model Performance",
        "6. Temporal Analysis"
    ]
    
    selected_page = st.radio("Navigation", pages, index=0)
    
    st.markdown("---")
    st.markdown("#### **System Telemetry**")
    st.caption("• Primary Target: **Tomato Bacterial Wilt**")
    st.caption("• Sensor: **Specim IQ (VNIR)**")
    st.caption("• Spectral Bands: **180 Usable**")
    st.caption("• Verified Samples: **293 Plants**")
    st.caption("• Version: **v0.2.0 (Day 2 Prototype)**")
    st.markdown("---")
    st.caption("Developed by: Meet | Prince | Shravani | Abdul")

# Page Routing
if selected_page == "1. Overview & Objectives":
    st.markdown("""
    <div class="main-header">
        <h1>TerraSpectra: Hyperspectral Crop Disease Forecasting</h1>
        <p>Scientific Monitoring & Severity Diagnosis via Reflectance Spectroscopy</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Specimens", "293 Plants", "100% Verified")
    with col2:
        st.metric("Spectral Bands", "180 Bands", "400 - 1000 nm")
    with col3:
        st.metric("Severity Levels", "5 Classes", "Healthy to 100% Wilt")
    with col4:
        st.metric("Pixel Profiles", "146,500", "500 / Specimen")
        
    st.markdown("### **Project Core Pillars**")
    st.info("""
    **1. Genuine Hyperspectral Data**: Utilizes physical reflectance spectra across 180 continuous narrowbands (400–1000 nm), capturing sub-visual cellular disruption.
    
    **2. Scientifically Honest Forecasting**: Clearly delineates current-state multi-class disease diagnosis from temporal forecasting, avoiding deceptive static forecasting claims.
    
    **3. Production-Grade ML Architecture**: Integrates baseline, tree-based, and deep 1D-CNN architectures with leakage-free plant-level group cross-validation.
    """)

elif selected_page == "2. Dataset Explorer":
    st.title("📂 Dataset Explorer")
    st.markdown("Inspect metadata, sample distributions, and raw matrix records.")
    
    tab1, tab2 = st.tabs(["Class Breakdown", "Specimen Catalog"])
    with tab1:
        st.markdown("#### **Sample Distribution by Severity Class**")
        classes = ["Level 0 (Healthy)", "Level 1 (Asymptomatic)", "Level 2 (Mild 1-33%)", "Level 3 (Mod 34-66%)", "Level 4 (Sev 67-100%)"]
        counts = [120, 68, 39, 33, 33]
        st.bar_chart(dict(zip(classes, counts)))
    with tab2:
        st.dataframe({
            "Severity Level": ["Level 0", "Level 1", "Level 2", "Level 3", "Level 4"],
            "Clinical Diagnosis": ["Healthy Control", "Infected Asymptomatic", "Mild Wilt", "Moderate Wilt", "Severe Wilt / Necrosis"],
            "Verified Plants": [120, 68, 39, 33, 33],
            "Pixel Vectors Available": [60000, 34000, 19500, 16500, 16500]
        })

elif selected_page == "3. Spectral Analysis":
    st.title("📈 Spectral Signature Explorer")
    st.markdown("Interactive exploration of continuous narrow-band reflectance signatures.")
    
    wavelengths = np.linspace(400, 1000, 180)
    # Mock mean signatures for Day 2 wireframe
    healthy_mock = 0.08 + 0.38 / (1 + np.exp(-(wavelengths - 710) / 20))
    severe_mock = 0.12 + 0.25 / (1 + np.exp(-(wavelengths - 725) / 35))
    
    chart_data = {
        "Wavelength (nm)": wavelengths,
        "Healthy (Level 0)": healthy_mock,
        "Severe Wilt (Level 4)": severe_mock
    }
    st.line_chart(data=chart_data, x="Wavelength (nm)", y=["Healthy (Level 0)", "Severe Wilt (Level 4)"])
    st.caption("Notice the sharp Red Edge inflection (~710 nm) in healthy plants versus flattened incline in wilted specimens.")

elif selected_page == "4. Disease Prediction":
    st.title("🧪 Real-Time Disease Diagnostic Interface")
    st.markdown("Upload a hyperspectral `.mat` specimen vector to evaluate disease severity.")
    
    uploaded_file = st.file_uploader("Upload Hyperspectral Spectrum (.mat format)", type=["mat"])
    if uploaded_file is not None:
        st.success(f"Loaded file: {uploaded_file.name}. Running preprocessing pipeline...")
        st.warning("Prediction models will be active on Day 7 (Baseline Integration).")
    else:
        st.info("Awaiting input data. Upload sample `*_Ave_spe.mat` to predict.")

elif selected_page == "5. Model Performance":
    st.title("📊 Model Benchmark Dashboard")
    st.markdown("Comparative evaluation metrics across classification architectures.")
    st.info("Model benchmarking pipeline will populate on Day 7 through Day 10.")

elif selected_page == "6. Temporal Analysis":
    st.title("⏳ Temporal Disease Progression & Forecasting")
    st.markdown("Analysis of time-series disease progression.")
    st.warning("""
    **Scientific Integrity Notice:** The primary Tomato Bacterial Wilt dataset consists of static observations at specific symptom stages. 
    A separate experimental module analyzing dynamic time-series progression from the Pine Wilt Disease dataset (July 3 – August 8, 2024) is currently under investigation.
    """)


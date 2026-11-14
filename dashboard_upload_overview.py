"""
TerraSpectra Dashboard: Dataset Overview & Upload Interface
Author: Abdul (Backend & Dashboard Specialist)
Day 3 Deliverable: Connects to Meet's Data Loader and Prince's Spectral Reader
"""

import os
import sys
import numpy as np
import pandas as pd
import streamlit as st

# Add main project to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "src")))
from data.loader import HyperspectralDataLoader, SEVERITY_MAPPING, get_wavelength_grid
from data.validator import DataValidator
from preprocessing.spectral_reader import SpectralReader

def render_overview_and_upload(data_dir: str):
    """Renders the interactive dataset overview and spectral upload interface."""
    st.title("📂 Dataset Catalog & Spectral Upload")
    st.markdown("Browse verified tomato plant specimens or upload a custom hyperspectral `.mat` signature.")
    
    loader = HyperspectralDataLoader(data_dir)
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("1. Catalog Inspection")
        try:
            df_meta = loader.scan_dataset()
            st.success(f"Connected to dataset: {len(df_meta)} verified specimens available.")
            
            selected_level = st.selectbox(
                "Filter by Disease Severity Level:",
                options=[-1, 0, 1, 2, 3, 4],
                format_func=lambda x: "All Levels (293)" if x == -1 else f"Level {x}: {SEVERITY_MAPPING[x]}"
            )
            
            if selected_level != -1:
                filtered_df = df_meta[df_meta["severity_level"] == selected_level]
            else:
                filtered_df = df_meta
                
            selected_sample = st.selectbox(
                "Select Specimen to Inspect:",
                options=filtered_df["sample_id"].tolist()
            )
            
            if selected_sample:
                sample_row = df_meta[df_meta["sample_id"] == selected_sample].iloc[0]
                spe = SpectralReader.load_from_mat(sample_row["avg_file"])
                indices = SpectralReader.calculate_vegetation_indices(spe)
                validation = DataValidator.validate_spectrum(spe)
                
                st.markdown(f"**Specimen:** `{selected_sample}` | **Severity:** {sample_row['severity_name']}")
                st.caption(f"Validation Status: {'✅ VALID' if validation['valid'] else '❌ INVALID'}")
                
                # Show key indices
                ic1, ic2, ic3 = st.columns(3)
                ic1.metric("NDVI", f"{indices['NDVI']:.3f}")
                ic2.metric("PRI", f"{indices['PRI']:.3f}")
                ic3.metric("Chlorophyll (CI)", f"{indices['CI_green']:.2f}")
                
                # Plot Spectrum
                chart_data = pd.DataFrame({
                    "Wavelength (nm)": get_wavelength_grid(180),
                    "Reflectance": spe
                })
                st.line_chart(chart_data, x="Wavelength (nm)", y="Reflectance")
                
        except Exception as e:
            st.error(f"Error loading catalog: {str(e)}")
            
    with col2:
        st.subheader("2. Upload Custom Specimen")
        uploaded_file = st.file_uploader("Upload Hyperspectral Spectrum (.mat format)", type=["mat"])
        
        if uploaded_file is not None:
            try:
                uploaded_spe = SpectralReader.load_from_mat(uploaded_file)
                val_res = DataValidator.validate_spectrum(uploaded_spe)
                
                if val_res["valid"]:
                    st.success(f"Successfully parsed 180 bands from `{uploaded_file.name}`")
                    up_indices = SpectralReader.calculate_vegetation_indices(uploaded_spe)
                    
                    uc1, uc2, uc3 = st.columns(3)
                    uc1.metric("Uploaded NDVI", f"{up_indices['NDVI']:.3f}")
                    uc2.metric("Uploaded PRI", f"{up_indices['PRI']:.3f}")
                    uc3.metric("Uploaded CI", f"{up_indices['CI_green']:.2f}")
                    
                    up_chart = pd.DataFrame({
                        "Wavelength (nm)": get_wavelength_grid(180),
                        "Uploaded Spectrum": uploaded_spe
                    })
                    st.line_chart(up_chart, x="Wavelength (nm)", y="Uploaded Spectrum")
                else:
                    st.error(f"Validation Issues: {val_res['issues']}")
            except Exception as e:
                st.error(f"Failed to parse uploaded `.mat` file: {str(e)}")
        else:
            st.info("Drag and drop any `*_Ave_spe.mat` file here to inspect real-time spectral reflectance.")

if __name__ == "__main__":
    raw_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "data", "raw", "tomato_wilt", "Tomato bacterial wilt dataset"))
    render_overview_and_upload(raw_path)


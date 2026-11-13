# UI Navigation & Architecture Specification
**Author:** Abdul (Backend & Dashboard Lead)  
**Date:** 2024-11-12  
**Component:** TerraSpectra Dashboard UI  

---

## 1. Visual Design Philosophy
TerraSpectra uses an **Agricultural Intelligence Palette**:
- **Primary Header Green:** `#1B5E20` (Forest Green - High Authority)
- **Secondary Accent Green:** `#2E7D32` to `#4CAF50` (Leaf Pigment)
- **Background Tones:** `#FFFFFF` (Cards) & `#F8F9FA` (Sidebar / Off-white Canvas)
- **Alert Tones:** `#C8E6C9` (Soft confirmation) & `#FFF3E0` (Scientific limitation warning)

---

## 2. Page Hierarchy & State Flow

```
                                  ┌────────────────────────┐
                                  │   TerraSpectra Main    │
                                  │       (app.py)         │
                                  └───────────┬────────────┘
                                              │
                      ┌───────────────────────┼───────────────────────┐
                      │                       │                       │
             ┌────────▼────────┐    ┌─────────▼────────┐    ┌─────────▼────────┐
             │ 1. Overview &   │    │ 2. Dataset       │    │ 3. Spectral      │
             │    Objectives   │    │    Explorer      │    │    Analysis      │
             └─────────────────┘    └──────────────────┘    └──────────────────┘
                      │                       │                       │
             ┌────────▼────────┐    ┌─────────▼────────┐    ┌─────────▼────────┐
             │ 4. Disease      │    │ 5. Model         │    │ 6. Temporal      │
             │    Prediction   │    │    Performance   │    │    Analysis      │
             └─────────────────┘    └──────────────────┘    └──────────────────┘
```

---

## 3. View Specifications

### View 1: Overview & Objectives
- **Key Metrics:** 4 summary cards (Total Specimens, Spectral Bands, Severity Levels, Pixel Profiles).
- **Core Pillars:** Highlights hyperspectral physics, honest forecasting delineation, and production ML standards.

### View 2: Dataset Explorer
- **Class Breakdown:** Dynamic bar chart of sample counts across all 5 clinical stages.
- **Specimen Catalog:** Interactive data table detailing biological definitions and pixel sample pools.

### View 3: Spectral Analysis
- **Spectral Curves:** Reflectance ($0.0-1.0$) vs Wavelength ($400-1000\text{ nm}$).
- **Comparison Engine:** Overlays healthy vs symptomatic profiles to highlight chlorophyll absorption pits ($670\text{ nm}$) and Red Edge shifts ($700-740\text{ nm}$).

### View 4: Disease Prediction
- **Input Methods:** Drag-and-drop `.mat` file uploader or sample selection dropdown.
- **Workflow:** File upload $\rightarrow$ Validation $\rightarrow$ Preprocessing $\rightarrow$ Model Inference $\rightarrow$ Confidence Gauge & Severity Gauge.

### View 5: Model Performance
- **Visuals:** Confusion matrix heatmaps, ROC-AUC curves, Precision-Recall curves.
- **Table:** Side-by-side comparison of Logistic Regression, Random Forest, SVM, XGBoost, and 1D-CNN.

### View 6: Temporal Analysis
- **Delineation Banner:** Transparently explains the boundary between static classification and temporal time-series forecasting.
- **Pine Wilt Module:** Exploratory time-series tracking over the 11 observation dates.


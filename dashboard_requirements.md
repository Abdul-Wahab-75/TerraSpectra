# Dashboard Requirements — TerraSpectra

## 1. Introduction

This document defines the functional and non-functional requirements for the TerraSpectra Dashboard — an interactive web application for hyperspectral crop disease analysis. The dashboard serves as the primary user interface for exploring spectral datasets, running disease predictions, and evaluating model performance.

## 2. Target Users

### 2.1 Agricultural Researchers
- **Profile:** Scientists studying crop diseases using spectral imaging
- **Needs:** Advanced data exploration, statistical analysis, export capabilities
- **Technical Level:** Moderate — comfortable with scientific plots but not necessarily Python/CLI
- **Key Tasks:** Analyze spectral signatures, compare severity levels, export publication-quality figures

### 2.2 Plant Pathologists
- **Profile:** Domain experts diagnosing plant diseases
- **Needs:** Upload field samples for rapid classification, interpret prediction confidence
- **Technical Level:** Low to moderate — need intuitive UI with clear guidance
- **Key Tasks:** Upload spectral data, get disease severity predictions, review diagnostic confidence

### 2.3 Students & Educators
- **Profile:** Graduate/undergraduate students learning spectral analysis and ML
- **Needs:** Educational walkthroughs, example datasets, model interpretation
- **Technical Level:** Varies — need contextual help and documentation links
- **Key Tasks:** Explore example data, understand model decision-making, learn spectral concepts

---

## 3. Functional Requirements — Page Specifications

### 3.1 Page 1: Overview (Home)

**Purpose:** Landing page introducing TerraSpectra, providing project context, and offering quick navigation to key features.

**Key Components:**
- Hero section with TerraSpectra logo and tagline: "Hyperspectral Intelligence for Crop Disease Detection"
- Project description (2-3 paragraphs on hyperspectral imaging for agriculture)
- Quick stats cards: total samples (293), spectral bands (204), severity levels (5), model accuracy
- Navigation cards linking to each of the other 5 pages with icons and descriptions
- Dataset summary: Tomato Bacterial Wilt overview
- Recent activity or system status indicator

**Data Requirements:**
- Static project metadata (sample counts, band counts)
- Cached model accuracy from latest training run
- Dataset availability status

**User Interactions:**
- Click navigation cards to jump to any page
- Hover over stat cards for tooltips with additional context
- Toggle between light and dark mode (future enhancement)

---

### 3.2 Page 2: Dataset Explorer

**Purpose:** Enable users to browse, filter, and understand the spectral dataset before analysis.

**Key Components:**
- Dataset statistics panel: sample count per severity class, class distribution bar chart
- Interactive data table with sortable columns (Sample ID, Severity Level, Wavelength Count)
- Class distribution visualization (bar chart or pie chart)
- Sample preview: select a sample to see its spectral signature plotted
- Filter controls: filter by severity level (0–4), by wavelength range
- Data quality indicators: missing values, outliers flagged
- Download filtered data as CSV

**Data Requirements:**
- Full dataset loaded from `.mat` files via `scipy.io.loadmat`
- Severity labels array (293 samples)
- Spectral matrix (293 × 204)
- Wavelength axis (204 values, 350nm–2500nm typical range)

**User Interactions:**
- Select severity classes to filter the table
- Click a row to plot that sample's spectral curve
- Adjust wavelength range slider to zoom into regions of interest
- Export filtered subset as CSV
- Toggle between raw and normalized spectral values

---

### 3.3 Page 3: Spectral Analysis

**Purpose:** Provide deep spectral visualization and comparison tools for understanding disease signatures.

**Key Components:**
- Mean spectral signature plot per severity class (5 curves, color-coded)
- Individual sample overlay plot (select multiple samples)
- Difference spectrum viewer: select two classes and plot Δ reflectance
- Wavelength importance heatmap (from ML feature importance scores)
- Vegetation index calculator (NDVI, PRI, etc. where applicable)
- Statistical band comparison: box plots of reflectance at user-selected wavelengths
- Annotation tools: mark key absorption features

**Data Requirements:**
- Full spectral matrix (293 × 204)
- Severity labels for grouping
- Pre-computed mean and standard deviation per class
- Feature importance scores (from trained models, loaded from cache)
- Wavelength axis for x-axis labels

**User Interactions:**
- Select/deselect severity classes to show/hide curves
- Hover over spectral plot for wavelength + reflectance tooltip
- Click wavelength to see box plot of that band's distribution across classes
- Select two classes for difference spectrum
- Zoom and pan on all plots
- Download plots as PNG/SVG for publications

---

### 3.4 Page 4: Disease Prediction

**Purpose:** Allow users to upload new spectral data and receive disease severity predictions from trained models.

**Key Components:**
- File upload widget (accepts `.mat`, `.csv`, `.npy` formats)
- Upload validation panel: file format check, band count verification, value range check
- Model selection dropdown (Random Forest, SVM, XGBoost — whichever are trained)
- Prediction results display:
  - Predicted severity class with confidence percentage
  - Confidence bar chart across all 5 classes
  - SHAP/feature importance waterfall for this specific prediction
- Batch prediction mode: upload multiple samples, get results table
- Prediction history log (session-based)

**Data Requirements:**
- Trained model files (`.joblib` or `.pkl`) loaded via `st.cache_resource`
- Scaler/preprocessor fitted on training data
- SHAP explainer (pre-computed or on-demand)
- Uploaded sample data (validated to 204 bands)

**User Interactions:**
- Drag-and-drop or browse to upload spectral file
- Select model from dropdown
- Click "Predict" to run inference
- View per-sample results with confidence breakdown
- Download prediction results as CSV
- Clear upload and reset

---

### 3.5 Page 5: Model Performance

**Purpose:** Display training and evaluation metrics for all trained models, enabling model comparison.

**Key Components:**
- Model comparison table: accuracy, precision, recall, F1-score, AUC for each model
- Confusion matrix heatmap (selectable per model)
- ROC curves (multi-class, one-vs-rest) overlaid for all models
- Precision-Recall curves per class
- Cross-validation results: box plots of fold-wise accuracy
- Training history plot (for neural network if applicable)
- Feature importance ranking (top 20 wavelengths) per model
- Model metadata: training date, hyperparameters, dataset version

**Data Requirements:**
- Saved evaluation metrics (JSON or pickle) per model
- Confusion matrix arrays
- ROC/PR curve data (FPR, TPR, thresholds per class)
- Cross-validation fold scores
- Feature importance arrays
- Model training metadata

**User Interactions:**
- Select models to compare (checkboxes)
- Click confusion matrix cell for misclassified sample details
- Toggle between micro/macro/weighted averaging for metrics
- Switch between ROC and PR curve views
- Download comparison report as PDF or CSV
- Sort feature importance by rank

---

### 3.6 Page 6: Temporal Analysis

**Purpose:** Explore temporal or progression-based patterns in disease severity, including early detection insights.

**Key Components:**
- Severity progression visualization (if temporal data available)
- Spectral change tracking across severity levels (as proxy for temporal progression)
- Early detection analysis: which spectral bands diverge earliest between healthy (0) and early disease (1)
- Key wavelength identification for early warning
- Pine Wilt dataset integration (if temporal data structure allows)
- Literature references on temporal spectral monitoring

**Data Requirements:**
- Spectral data organized by severity level (as temporal proxy)
- Statistical tests for early-diverging bands
- Pine Wilt dataset (if structured temporally)
- Pre-computed early detection metrics

**User Interactions:**
- Select severity levels to compare progression
- Identify top-N earliest discriminating wavelengths
- View band-by-band statistical significance (p-values)
- Toggle between Tomato Wilt and Pine Wilt datasets
- Export early detection report

---

## 4. Non-Functional Requirements

### 4.1 Responsive Layout
- Dashboard must render correctly at screen widths from 1024px to 2560px
- Sidebar collapses gracefully on smaller viewports
- Charts resize dynamically with container width
- Mobile/tablet support is a lower priority (desktop-first)

### 4.2 Visual Design & Color Palette
| Role | Color Code | Usage |
|------|-----------|-------|
| Primary | `#1B5E20` | Dark green — headers, sidebar, primary buttons |
| Secondary | `#4CAF50` | Medium green — active states, highlights, chart accents |
| Accent | `#81C784` | Light green — hover states, secondary elements |
| Background | `#FAFAFA` | Off-white — page background |
| Text Primary | `#212121` | Near-black — body text, labels |
| Text Secondary | `#757575` | Gray — captions, secondary text |
| Error | `#D32F2F` | Red — error messages, validation failures |
| Warning | `#F57C00` | Orange — warnings, low-confidence predictions |
| Success | `#388E3C` | Green — success confirmations |

### 4.3 Scientific Visualization Quality
- All plots must include axis labels with units (e.g., "Wavelength (nm)", "Reflectance")
- Font size ≥ 12pt for axis labels, ≥ 10pt for tick labels
- Legend placement must not obscure data
- Export at 300 DPI for publication use
- Consistent color coding across all pages (severity 0 = green → severity 4 = red)

### 4.4 Accessibility
- Minimum contrast ratio 4.5:1 for text (WCAG AA)
- Color-blind-friendly palette option for plots
- Alt text for all visual elements
- Keyboard navigation support for core workflows

---

## 5. Error Handling Requirements

### 5.1 File Upload Errors
| Error Condition | User Message | Action |
|----------------|-------------|--------|
| Unsupported file format | "Please upload a .mat, .csv, or .npy file." | Reject upload, show example format |
| Wrong number of spectral bands | "Expected 204 spectral bands, found {N}." | Reject, suggest data format |
| Missing values in data | "Data contains {N} missing values. Please clean before uploading." | Warn, offer to proceed with imputation |
| File too large (>100MB) | "File exceeds 100MB limit." | Reject upload |
| Corrupted file | "Unable to read file. Please check the format." | Reject with troubleshooting link |

### 5.2 Model Errors
| Error Condition | User Message | Action |
|----------------|-------------|--------|
| No model loaded | "No trained model found. Please train a model first." | Link to model training docs |
| Model version mismatch | "Model expects {N} features, data has {M}." | Suggest retraining or data adjustment |
| Prediction timeout | "Prediction timed out. Try reducing batch size." | Offer retry with smaller batch |

### 5.3 Data Errors
| Error Condition | User Message | Action |
|----------------|-------------|--------|
| Dataset not found | "Dataset file not found at expected path." | Show setup instructions |
| Memory overflow | "Dataset too large for available memory." | Suggest sampling or chunked loading |

---

## 6. Performance Considerations

### 6.1 Loading Times
- Initial page load: < 3 seconds (cached state)
- Dataset loading (293 × 204 matrix): < 1 second
- Chart rendering: < 2 seconds per plot
- Single prediction: < 500ms
- Batch prediction (100 samples): < 5 seconds

### 6.2 Caching Strategy
- Dataset arrays cached with `st.cache_data` (TTL: session lifetime)
- ML models cached with `st.cache_resource` (loaded once, reused)
- Computed statistics (means, std, feature importance) cached per session
- Plot objects not cached (re-rendered on parameter change for freshness)

### 6.3 Memory Management
- Maximum concurrent dataset size in memory: 500MB
- Lazy loading for Pine Wilt dataset (load on page visit, not on app start)
- Garbage collection hint after large batch predictions
- Session state cleanup on page navigation where possible

### 6.4 Concurrent Users
- Target: 5–10 concurrent users for local/Docker deployment
- Streamlit Cloud: subject to platform limits (1GB RAM free tier)
- No shared state between user sessions (each session independent)

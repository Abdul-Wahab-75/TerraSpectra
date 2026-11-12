# Technology Research — TerraSpectra Dashboard

## 1. Framework Comparison

### 1.1 Candidates Evaluated

We evaluated three Python-native dashboard frameworks for the TerraSpectra project:

| Criteria | Streamlit | Dash (Plotly) | Gradio |
|----------|-----------|---------------|--------|
| **Learning Curve** | Very Low | Moderate | Very Low |
| **Python-Native** | ✅ 100% Python | ✅ Python (Flask-based) | ✅ 100% Python |
| **Rapid Prototyping** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Multipage Support** | ✅ Built-in (`pages/` dir) | ✅ Via `dash.page_registry` | ❌ Tabs only |
| **Custom Styling** | Moderate (CSS injection) | Full (CSS/Bootstrap) | Limited |
| **Interactive Charts** | Via Plotly/Altair/Bokeh | Plotly native | Plotly via `gr.Plot` |
| **File Upload** | ✅ `st.file_uploader` | ✅ `dcc.Upload` | ✅ `gr.File` |
| **Session State** | ✅ `st.session_state` | ✅ `dcc.Store` / callbacks | ❌ Limited |
| **Widgets** | ⭐⭐⭐⭐⭐ (sliders, selects, etc.) | ⭐⭐⭐⭐ (via Dash components) | ⭐⭐⭐ (ML-focused) |
| **Deployment** | Streamlit Cloud, Docker | Heroku, Docker, any WSGI | HF Spaces, Docker |
| **Community/Docs** | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐⭐ Good | ⭐⭐⭐⭐ Good |
| **ML Integration** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ (built for ML) |
| **Scalability** | Moderate | High (production-grade) | Low-Moderate |
| **Callback Model** | Top-to-bottom rerun | Explicit callbacks | Event listeners |

### 1.2 Detailed Analysis

#### Streamlit
**Strengths:**
- Fastest path from Python script to interactive app
- No frontend/JavaScript knowledge required
- Built-in multipage support via `pages/` directory convention
- Rich widget library: sliders, selectboxes, file uploaders, data editors
- `st.session_state` for stateful interactions across reruns
- Native `st.plotly_chart()`, `st.pyplot()`, and `st.altair_chart()` for plotting
- Automatic hot-reload during development
- Large ecosystem of community components (`streamlit-aggrid`, `streamlit-option-menu`, etc.)

**Weaknesses:**
- Top-to-bottom execution model can cause performance issues on complex pages
- Limited CSS customization without hacks (though `st.markdown` with `unsafe_allow_html` works)
- Not ideal for very high-concurrency production deployments (single-threaded per session)
- Sidebar is the primary navigation mechanism (no top navbars natively)

#### Dash (Plotly)
**Strengths:**
- Production-grade framework (used at enterprise scale)
- Full CSS/Bootstrap control over layout
- Explicit callback system gives fine-grained control over reactivity
- Plotly is the native charting library — tightest integration
- Can serve as a proper web application with authentication, databases, etc.

**Weaknesses:**
- Steeper learning curve: requires understanding callback decorators, component IDs, and state management
- More boilerplate code for simple dashboards
- Slower prototyping cycle compared to Streamlit
- Callback debugging can be complex for many interconnected components

#### Gradio
**Strengths:**
- Purpose-built for ML model demos
- Extremely fast to create inference UIs (upload → predict → display)
- Built-in model comparison interfaces (A/B testing)
- Hugging Face Spaces integration for free deployment

**Weaknesses:**
- Not designed for multi-page data exploration dashboards
- Limited layout customization
- Tab-based navigation only (no true multipage routing)
- Less suitable for complex data exploration workflows
- Session state management is minimal

### 1.3 Decision: Streamlit ✅

**Streamlit is selected** as the primary framework for TerraSpectra because:

1. **Rapid Prototyping:** Our team (4 members, 5-day sprint) needs the fastest path to a working dashboard. Streamlit's script-to-app model is unmatched.
2. **Python-Native:** All team members are Python developers. No need for JavaScript, HTML, or CSS expertise.
3. **Built-in Multipage:** The `pages/` directory convention maps directly to our 6-page requirement.
4. **Widget Library:** Sliders for wavelength selection, file uploaders for spectral data, selectboxes for model selection — all available out of the box.
5. **ML Integration:** `st.cache_resource` for model loading, easy integration with scikit-learn, joblib, and SHAP.
6. **Community:** Extensive documentation, tutorials, and community components for scientific dashboards.

---

## 2. Visualization Library Selection

### 2.1 Plotly vs Matplotlib

| Criteria | Plotly | Matplotlib |
|----------|--------|------------|
| **Interactivity** | ✅ Zoom, pan, hover, click | ❌ Static by default |
| **Web Integration** | ✅ Native HTML/JS rendering | Requires `mpld3` or image export |
| **Spectral Plots** | ✅ Hover shows wavelength + value | ❌ No hover |
| **3D Visualization** | ✅ Built-in | ✅ Via `mpl_toolkits` |
| **Heatmaps** | ✅ Interactive | ✅ Static |
| **Publication Quality** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Streamlit Support** | ✅ `st.plotly_chart` | ✅ `st.pyplot` |
| **Learning Curve** | Moderate | Low (widely known) |

### 2.2 Decision: Plotly Primary + Matplotlib for Export

- **Plotly** for all interactive dashboard charts: spectral curves, confusion matrices, ROC curves, box plots, bar charts
- **Matplotlib/Seaborn** as a secondary option for static, publication-quality figure exports (300 DPI PNG/SVG)
- This dual approach gives users interactive exploration in the browser AND downloadable publication figures

### 2.3 Key Plotly Features We'll Use
- `plotly.graph_objects` for fine-grained chart control
- `plotly.express` for quick exploratory plots
- `plotly.subplots.make_subplots` for multi-panel layouts
- Custom color scales matching TerraSpectra palette
- `fig.update_layout(template="plotly_white")` as base theme, customized with our green palette

---

## 3. Streamlit Session State Management

### 3.1 What is Session State?
Streamlit reruns the entire script on every user interaction. `st.session_state` is a dictionary-like object that persists data across reruns within a single user session.

### 3.2 Our Session State Strategy

```python
# Session state keys we'll manage:
st.session_state.keys_plan = {
    # Data
    "dataset_loaded": bool,          # Whether the main dataset is in memory
    "spectral_data": np.ndarray,     # (293, 204) spectral matrix
    "severity_labels": np.ndarray,   # (293,) label array
    "wavelengths": np.ndarray,       # (204,) wavelength axis
    
    # User selections
    "selected_classes": list,        # Currently selected severity classes
    "selected_model": str,           # Active model for prediction
    "wavelength_range": tuple,       # (min, max) wavelength filter
    
    # Uploads
    "uploaded_file": bytes,          # Raw uploaded file data
    "upload_validated": bool,        # Whether upload passed validation
    "uploaded_spectra": np.ndarray,  # Parsed spectral data from upload
    
    # Predictions
    "prediction_results": dict,      # Latest prediction output
    "prediction_history": list,      # Log of past predictions in session
    
    # Models
    "models_loaded": dict,           # {model_name: model_object}
    "model_metrics": dict,           # Cached evaluation metrics
}
```

### 3.3 Initialization Pattern
```python
def init_session_state():
    defaults = {
        "dataset_loaded": False,
        "selected_classes": [0, 1, 2, 3, 4],
        "selected_model": "Random Forest",
        "prediction_history": [],
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
```

---

## 4. File Upload Handling for Spectral Data

### 4.1 Supported Formats
| Format | Extension | Library | Description |
|--------|-----------|---------|-------------|
| MATLAB | `.mat` | `scipy.io.loadmat` | Primary format for research datasets |
| CSV | `.csv` | `pandas.read_csv` | Tabular spectral data (rows=samples, cols=bands) |
| NumPy | `.npy` | `numpy.load` | Binary array format for pre-processed data |

### 4.2 Upload → Validation → Parse Pipeline
```
User uploads file
    ↓
Check file extension → reject if unsupported
    ↓
Check file size → reject if > 100MB
    ↓
Parse file based on format
    ↓
Validate shape: must have 204 columns (spectral bands)
    ↓
Validate values: check for NaN, negative, or extreme outliers
    ↓
Store in st.session_state["uploaded_spectra"]
    ↓
Ready for prediction
```

### 4.3 Implementation Sketch
```python
uploaded = st.file_uploader(
    "Upload spectral data",
    type=["mat", "csv", "npy"],
    help="Upload a .mat, .csv, or .npy file with 204 spectral bands per sample."
)

if uploaded is not None:
    try:
        if uploaded.name.endswith(".mat"):
            data = scipy.io.loadmat(uploaded)
            # Extract spectral array (key name TBD from dataset inspection)
            spectra = data["spectra"]  # placeholder key
        elif uploaded.name.endswith(".csv"):
            spectra = pd.read_csv(uploaded).values
        elif uploaded.name.endswith(".npy"):
            spectra = np.load(uploaded)
        
        # Validate
        if spectra.shape[1] != 204:
            st.error(f"Expected 204 bands, got {spectra.shape[1]}.")
        else:
            st.session_state["uploaded_spectra"] = spectra
            st.success(f"Loaded {spectra.shape[0]} samples × {spectra.shape[1]} bands.")
    except Exception as e:
        st.error(f"Failed to read file: {e}")
```

---

## 5. Deployment Options

### 5.1 Option Comparison

| Deployment | Cost | Setup Effort | Scalability | Best For |
|-----------|------|-------------|-------------|----------|
| **Local (`streamlit run`)** | Free | Minimal | Single user | Development, demos |
| **Streamlit Cloud** | Free tier (1GB RAM) | Low (GitHub connect) | Limited | Public sharing, demos |
| **Docker** | Server cost | Moderate | Good | Team deployment, reproducibility |
| **Cloud VM (GCP/AWS)** | ~$5-50/mo | Moderate | Good | Production, custom domain |

### 5.2 Recommended Deployment Strategy

**Development Phase (Days 1-4):** Local development with `streamlit run app.py`

**Demo/Presentation (Day 5):**
- Primary: Streamlit Cloud (free, easy sharing via URL)
- Backup: Docker container for offline demo

**Production (Post-project):**
- Dockerized deployment on a cloud VM
- Dockerfile included in repository for reproducibility

### 5.3 Docker Configuration Plan
```dockerfile
# Planned Dockerfile structure
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 6. Additional Libraries

| Library | Purpose | Version |
|---------|---------|---------|
| `streamlit` | Dashboard framework | ≥1.28 |
| `plotly` | Interactive charts | ≥5.18 |
| `matplotlib` | Static figure export | ≥3.7 |
| `seaborn` | Statistical plots | ≥0.12 |
| `numpy` | Array operations | ≥1.24 |
| `pandas` | Data manipulation | ≥2.0 |
| `scipy` | `.mat` file loading | ≥1.11 |
| `scikit-learn` | ML models | ≥1.3 |
| `joblib` | Model serialization | ≥1.3 |
| `shap` | Model interpretability | ≥0.42 |
| `streamlit-option-menu` | Custom sidebar navigation | ≥0.3 |
| `Pillow` | Image processing for logos | ≥10.0 |

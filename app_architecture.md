# Application Architecture — TerraSpectra Dashboard

## 1. Multipage Streamlit Structure

### 1.1 Directory Layout

```
Abdul/
├── app.py                          # Main entry point (streamlit run app.py)
├── pages/
│   ├── 1_📊_Overview.py            # Home / landing page
│   ├── 2_📁_Dataset_Explorer.py    # Browse and filter dataset
│   ├── 3_🔬_Spectral_Analysis.py   # Spectral visualization and comparison
│   ├── 4_🔮_Disease_Prediction.py  # Upload → predict workflow
│   ├── 5_📈_Model_Performance.py   # Metrics, confusion matrix, ROC
│   └── 6_⏱️_Temporal_Analysis.py   # Temporal/progression analysis
├── components/
│   ├── __init__.py
│   ├── sidebar.py                  # Custom sidebar rendering
│   ├── header.py                   # TerraSpectra branded header
│   ├── footer.py                   # Footer with credits
│   ├── metrics_card.py             # Reusable stat card component
│   └── spectral_plot.py            # Reusable spectral plotting functions
├── utils/
│   ├── __init__.py
│   ├── data_loader.py              # Dataset loading and parsing
│   ├── validators.py               # Upload validation logic
│   ├── preprocessing.py            # Data normalization, scaling
│   ├── prediction.py               # Model inference wrapper
│   └── visualization.py            # Plotly chart builders
├── config/
│   ├── __init__.py
│   ├── theme.py                    # Color palette, fonts, constants
│   ├── paths.py                    # File path constants
│   └── settings.py                 # App settings (page config, etc.)
├── models/                         # Trained model files (loaded at runtime)
│   ├── random_forest.joblib
│   ├── svm_model.joblib
│   ├── xgboost_model.joblib
│   └── scaler.joblib               # Fitted StandardScaler
├── assets/
│   ├── logo.png                    # TerraSpectra logo
│   └── style.css                   # Custom CSS overrides
├── .streamlit/
│   └── config.toml                 # Streamlit theme configuration
├── requirements.txt                # Dashboard-specific dependencies
└── Dockerfile                      # Container deployment
```

### 1.2 Entry Point (`app.py`)

```python
import streamlit as st
from config.theme import apply_theme
from config.settings import PAGE_CONFIG
from utils.data_loader import load_dataset

# Page configuration (must be first Streamlit command)
st.set_page_config(**PAGE_CONFIG)

# Apply custom theme
apply_theme()

# Initialize session state
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.dataset_loaded = False
    st.session_state.prediction_history = []
    st.session_state.selected_classes = [0, 1, 2, 3, 4]

# Main page content (redirects to Overview)
st.switch_page("pages/1_📊_Overview.py")
```

### 1.3 Streamlit Theme Configuration (`.streamlit/config.toml`)

```toml
[theme]
primaryColor = "#4CAF50"
backgroundColor = "#FAFAFA"
secondaryBackgroundColor = "#E8F5E9"
textColor = "#212121"
font = "sans serif"

[server]
maxUploadSize = 100
enableCORS = false

[browser]
gatherUsageStats = false
```

---

## 2. Session State Management Plan

### 2.1 State Categories

Session state is organized into logical groups to prevent naming collisions and support cleanup.

```python
# State schema organized by category
SESSION_STATE_SCHEMA = {
    # === DATA STATE ===
    "data.loaded": False,               # bool: dataset availability flag
    "data.spectral_matrix": None,       # np.ndarray: (293, 204)
    "data.severity_labels": None,       # np.ndarray: (293,)
    "data.wavelengths": None,           # np.ndarray: (204,)
    "data.metadata": None,             # dict: dataset metadata
    
    # === USER SELECTIONS ===
    "ui.selected_classes": [0, 1, 2, 3, 4],  # list: active severity filters
    "ui.selected_model": "Random Forest",     # str: active model name
    "ui.wavelength_range": (350, 2500),       # tuple: wavelength filter bounds
    "ui.view_mode": "raw",                    # str: "raw" or "normalized"
    "ui.active_page": "Overview",             # str: current page name
    
    # === UPLOAD STATE ===
    "upload.file_data": None,           # bytes: raw uploaded file
    "upload.validated": False,          # bool: validation passed
    "upload.parsed_spectra": None,      # np.ndarray: parsed spectral data
    "upload.error_message": None,       # str: validation error (if any)
    
    # === PREDICTION STATE ===
    "predict.results": None,            # dict: latest prediction output
    "predict.history": [],              # list[dict]: session prediction log
    "predict.shap_values": None,        # np.ndarray: SHAP explanations
    
    # === MODEL STATE ===
    "models.loaded": {},                # dict: {name: model_object}
    "models.metrics": {},               # dict: {name: metrics_dict}
    "models.scaler": None,             # object: fitted StandardScaler
}
```

### 2.2 State Initialization Function

```python
def initialize_session_state():
    """Initialize all session state variables with defaults.
    Called once at app startup. Safe to call multiple times (idempotent).
    """
    for key, default in SESSION_STATE_SCHEMA.items():
        if key not in st.session_state:
            if isinstance(default, (list, dict)):
                st.session_state[key] = default.copy()
            else:
                st.session_state[key] = default
```

### 2.3 State Persistence Across Pages

Streamlit's multipage architecture preserves `st.session_state` across page navigation. Key behaviors:
- State survives page switches (user navigates Overview → Dataset → Spectral)
- State resets on browser refresh (no server-side persistence)
- Each browser tab gets an independent session
- State is NOT shared between concurrent users

---

## 3. Model Loading Strategy

### 3.1 Cached Model Loading

Models are loaded once per session using `st.cache_resource` to avoid reloading on every page rerun.

```python
import joblib
import streamlit as st
from pathlib import Path

MODEL_DIR = Path("models")

@st.cache_resource
def load_model(model_name: str):
    """Load a trained model from disk. Cached across reruns.
    
    Args:
        model_name: One of 'random_forest', 'svm', 'xgboost'
    
    Returns:
        Loaded scikit-learn model object
    
    Raises:
        FileNotFoundError: If model file doesn't exist
    """
    model_path = MODEL_DIR / f"{model_name}.joblib"
    if not model_path.exists():
        raise FileNotFoundError(
            f"Model file not found: {model_path}. "
            f"Please train the model first (see Shravani's ML pipeline)."
        )
    return joblib.load(model_path)


@st.cache_resource
def load_scaler():
    """Load the fitted StandardScaler. Cached across reruns."""
    scaler_path = MODEL_DIR / "scaler.joblib"
    if not scaler_path.exists():
        raise FileNotFoundError("Scaler not found. Train a model first.")
    return joblib.load(scaler_path)


@st.cache_resource
def load_all_models():
    """Load all available models into a dictionary."""
    models = {}
    for model_file in MODEL_DIR.glob("*.joblib"):
        if model_file.stem != "scaler":
            models[model_file.stem] = joblib.load(model_file)
    return models
```

### 3.2 Model Loading Flow

```
App Start
    ↓
User navigates to Prediction or Model Performance page
    ↓
load_all_models() called (st.cache_resource)
    ↓
First call: loads from disk → caches in memory
    ↓
Subsequent calls: returns cached objects (instant)
    ↓
Models available for prediction / metric display
```

### 3.3 Model Availability Check

```python
def get_available_models() -> list[str]:
    """Return list of trained model names available on disk."""
    model_dir = Path("models")
    if not model_dir.exists():
        return []
    return [
        f.stem for f in model_dir.glob("*.joblib") 
        if f.stem != "scaler"
    ]
```

---

## 4. Data Caching Strategy

### 4.1 `st.cache_data` vs `st.cache_resource`

| Decorator | Use For | Serialization | Thread Safety |
|-----------|---------|---------------|---------------|
| `st.cache_data` | Data objects (DataFrames, arrays, dicts) | Copies returned (safe) | ✅ Each call gets a copy |
| `st.cache_resource` | ML models, DB connections, heavy objects | Shared reference (fast) | ⚠️ Shared across sessions |

### 4.2 Dataset Caching

```python
@st.cache_data
def load_spectral_dataset(data_path: str) -> dict:
    """Load and parse the spectral dataset from .mat file.
    
    Returns:
        dict with keys: 'spectra', 'labels', 'wavelengths', 'metadata'
    """
    import scipy.io as sio
    
    mat_data = sio.loadmat(data_path)
    
    return {
        "spectra": mat_data["spectra"],          # (293, 204)
        "labels": mat_data["labels"].flatten(),  # (293,)
        "wavelengths": mat_data["wavelengths"].flatten(),  # (204,)
        "metadata": {
            "n_samples": mat_data["spectra"].shape[0],
            "n_bands": mat_data["spectra"].shape[1],
            "n_classes": len(np.unique(mat_data["labels"])),
        }
    }
```

### 4.3 Computed Statistics Caching

```python
@st.cache_data
def compute_class_statistics(spectra: np.ndarray, labels: np.ndarray) -> dict:
    """Pre-compute mean and std spectra per severity class.
    
    Returns:
        dict: {class_id: {"mean": array, "std": array, "count": int}}
    """
    stats = {}
    for cls in np.unique(labels):
        mask = labels == cls
        cls_spectra = spectra[mask]
        stats[int(cls)] = {
            "mean": cls_spectra.mean(axis=0),
            "std": cls_spectra.std(axis=0),
            "count": int(mask.sum()),
        }
    return stats
```

### 4.4 Cache Invalidation

- **Dataset cache:** Invalidated only when `data_path` argument changes (rare)
- **Model cache:** Invalidated on app restart or by calling `st.cache_resource.clear()`
- **Statistics cache:** Invalidated when input arrays change (hash-based)
- **Manual clear:** Add a "Clear Cache" button in Settings for development/debugging

---

## 5. File Upload → Validation → Prediction Flow

### 5.1 Complete Pipeline

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│  USER       │     │  VALIDATOR   │     │  PREDICTOR   │
│  UPLOAD     │────▶│              │────▶│              │
│             │     │  Format      │     │  Scale       │
│  .mat       │     │  Shape       │     │  Predict     │
│  .csv       │     │  Values      │     │  Explain     │
│  .npy       │     │  Size        │     │  (SHAP)      │
└─────────────┘     └──────────────┘     └──────────────┘
                           │                     │
                    ┌──────▼──────┐        ┌─────▼──────┐
                    │  ERRORS     │        │  RESULTS   │
                    │  - format   │        │  - class   │
                    │  - shape    │        │  - proba   │
                    │  - values   │        │  - SHAP    │
                    │  - size     │        │  - history │
                    └─────────────┘        └────────────┘
```

### 5.2 Validation Module

```python
from dataclasses import dataclass
from typing import Optional
import numpy as np

@dataclass
class ValidationResult:
    is_valid: bool
    spectra: Optional[np.ndarray]   # Parsed data (if valid)
    n_samples: int = 0
    n_bands: int = 0
    errors: list[str] = None
    warnings: list[str] = None
    
    def __post_init__(self):
        self.errors = self.errors or []
        self.warnings = self.warnings or []


def validate_upload(file_data, filename: str) -> ValidationResult:
    """Validate uploaded spectral data file.
    
    Checks: format, size, shape (204 bands), value range, missing data.
    """
    result = ValidationResult(is_valid=False, spectra=None)
    
    # 1. Format check
    ext = filename.rsplit(".", 1)[-1].lower()
    if ext not in ("mat", "csv", "npy"):
        result.errors.append(f"Unsupported format: .{ext}. Use .mat, .csv, or .npy.")
        return result
    
    # 2. Size check (100MB limit)
    if len(file_data) > 100 * 1024 * 1024:
        result.errors.append("File exceeds 100MB limit.")
        return result
    
    # 3. Parse
    try:
        spectra = parse_spectral_file(file_data, ext)
    except Exception as e:
        result.errors.append(f"Parse error: {e}")
        return result
    
    # 4. Shape check
    if spectra.ndim != 2:
        result.errors.append(f"Expected 2D array, got {spectra.ndim}D.")
        return result
    
    if spectra.shape[1] != 204:
        result.errors.append(f"Expected 204 spectral bands, got {spectra.shape[1]}.")
        return result
    
    # 5. Value checks
    if np.any(np.isnan(spectra)):
        nan_count = np.isnan(spectra).sum()
        result.warnings.append(f"Data contains {nan_count} NaN values.")
    
    if np.any(spectra < 0):
        result.warnings.append("Negative reflectance values detected.")
    
    result.is_valid = True
    result.spectra = spectra
    result.n_samples = spectra.shape[0]
    result.n_bands = spectra.shape[1]
    return result
```

### 5.3 Prediction Module

```python
def predict_samples(
    spectra: np.ndarray,
    model_name: str,
) -> dict:
    """Run prediction on validated spectral data.
    
    Args:
        spectra: (N, 204) array of spectral samples
        model_name: Name of model to use
    
    Returns:
        dict with 'predictions', 'probabilities', 'model_name'
    """
    model = load_model(model_name)
    scaler = load_scaler()
    
    # Scale using training-fitted scaler
    spectra_scaled = scaler.transform(spectra)
    
    # Predict
    predictions = model.predict(spectra_scaled)
    probabilities = model.predict_proba(spectra_scaled)
    
    return {
        "predictions": predictions,           # (N,) class labels
        "probabilities": probabilities,       # (N, 5) probability matrix
        "model_name": model_name,
        "n_samples": spectra.shape[0],
    }
```

---

## 6. Error Handling Architecture

### 6.1 Error Categories and Strategy

```python
from enum import Enum

class ErrorCategory(Enum):
    DATA_LOADING = "data_loading"
    FILE_UPLOAD = "file_upload"
    MODEL_LOADING = "model_loading"
    PREDICTION = "prediction"
    VISUALIZATION = "visualization"
    CONFIGURATION = "configuration"
```

### 6.2 Centralized Error Handler

```python
import streamlit as st
import logging
from functools import wraps

logger = logging.getLogger("terraspectra")

def handle_errors(category: ErrorCategory):
    """Decorator for consistent error handling across the app."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except FileNotFoundError as e:
                logger.error(f"[{category.value}] File not found: {e}")
                st.error(f"🔍 {e}")
                st.info("Please check that the required files are in place.")
            except ValueError as e:
                logger.warning(f"[{category.value}] Validation error: {e}")
                st.warning(f"⚠️ {e}")
            except MemoryError:
                logger.critical(f"[{category.value}] Out of memory")
                st.error("💾 Out of memory. Try reducing the dataset size.")
            except Exception as e:
                logger.exception(f"[{category.value}] Unexpected error")
                st.error(f"❌ An unexpected error occurred: {e}")
                st.info("Please try refreshing the page. If the issue persists, check the logs.")
        return wrapper
    return decorator


# Usage example:
@handle_errors(ErrorCategory.DATA_LOADING)
def load_dataset():
    data = load_spectral_dataset("data/raw/tomato_wilt/dataset.mat")
    return data
```

### 6.3 User-Facing Error Display

```
┌─────────────────────────────────────────────────────┐
│  ❌ Error Level Messages                             │
│                                                      │
│  st.error()    → Red banner — critical failures      │
│  st.warning()  → Yellow banner — recoverable issues  │
│  st.info()     → Blue banner — helpful context       │
│  st.success()  → Green banner — confirmations        │
└─────────────────────────────────────────────────────┘
```

### 6.4 Graceful Degradation Strategy

| Failure | Degradation | User Action |
|---------|-------------|-------------|
| Dataset not found | Show setup instructions, disable data-dependent pages | Follow setup guide |
| Model not trained | Prediction page shows "No models available" with link to training docs | Train model first |
| Plot rendering fails | Show raw data table as fallback | Report issue |
| SHAP computation slow | Show prediction without explanation, offer "Compute SHAP" button | Click to compute |
| Memory limit | Suggest sampling or smaller batch | Reduce input size |

### 6.5 Logging Configuration

```python
import logging

def configure_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
        handlers=[
            logging.FileHandler("terraspectra.log"),
            logging.StreamHandler(),
        ]
    )
```

---

## 7. Integration Points with Other Modules

### 7.1 Dependencies on Other Team Members

| Dependency | Source | What We Need | Format |
|-----------|--------|-------------|--------|
| Spectral dataset | Meet (Data Pipeline) | Loaded, validated .mat files | `scipy.io.loadmat` compatible |
| Wavelength axis | Meet (Data Pipeline) | Array of 204 wavelength values | `np.ndarray` |
| Trained models | Shravani (ML) | Serialized sklearn models | `.joblib` files |
| Fitted scaler | Shravani (ML) | StandardScaler fitted on training data | `.joblib` file |
| Feature importance | Shravani (ML) | Per-model importance scores | JSON or `.npy` |
| Evaluation metrics | Shravani (ML) | Accuracy, F1, confusion matrix, ROC data | JSON |
| Preprocessed data | Prince (Spectral Processing) | Cleaned/normalized spectra | `.npy` or `.mat` |

### 7.2 Interface Contracts

```python
# Expected model interface (from Shravani's ML pipeline)
class ModelContract:
    def predict(self, X: np.ndarray) -> np.ndarray: ...
    def predict_proba(self, X: np.ndarray) -> np.ndarray: ...

# Expected data format (from Meet's data pipeline)
class DataContract:
    spectra: np.ndarray       # shape (N, 204), dtype float64
    labels: np.ndarray        # shape (N,), dtype int, values {0,1,2,3,4}
    wavelengths: np.ndarray   # shape (204,), dtype float64, units nm
```

---

## 8. Performance Optimization Plan

### 8.1 Startup Optimization
- Use `st.cache_resource` for all heavy objects (models, database connections)
- Lazy-load pages: only load page-specific data when user navigates to it
- Precompute class statistics on first dataset load

### 8.2 Runtime Optimization
- Limit data table display to 100 rows with pagination
- Use `st.cache_data` for all computed aggregations
- Debounce slider inputs (use `st.slider` with `key` for state persistence)
- Plotly charts: limit point count to 10,000 for scatter plots

### 8.3 Memory Optimization
- Single copy of dataset in `st.cache_data` (shared across reruns)
- Models in `st.cache_resource` (shared across sessions — read-only)
- Clear prediction history if it exceeds 50 entries
- Pine Wilt dataset loaded on-demand only on Temporal Analysis page

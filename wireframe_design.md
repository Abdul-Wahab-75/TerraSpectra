# Wireframe Design — TerraSpectra Dashboard

## 1. Global Layout Structure

All pages share a consistent layout with sidebar navigation and a branded header.

```
┌──────────────────────────────────────────────────────────────────────┐
│                        BROWSER WINDOW                                │
├────────────┬─────────────────────────────────────────────────────────┤
│            │  ┌─────────────────────────────────────────────────┐    │
│  SIDEBAR   │  │  🌿 TerraSpectra                               │    │
│            │  │  Hyperspectral Crop Disease Analysis            │    │
│  ┌──────┐  │  └─────────────────────────────────────────────────┘    │
│  │ LOGO │  │                                                         │
│  └──────┘  │  ┌─────────────────────────────────────────────────┐    │
│            │  │                                                  │    │
│  ────────  │  │              MAIN CONTENT AREA                   │    │
│  Nav Items │  │                                                  │    │
│  ────────  │  │         (Page-specific content below)            │    │
│  ○ Overview│  │                                                  │    │
│  ○ Dataset │  │                                                  │    │
│  ○ Spectral│  │                                                  │    │
│  ○ Predict │  │                                                  │    │
│  ○ Models  │  │                                                  │    │
│  ○ Temporal│  │                                                  │    │
│            │  │                                                  │    │
│  ────────  │  │                                                  │    │
│  Settings  │  └─────────────────────────────────────────────────┘    │
│  ────────  │                                                         │
│  Theme     │  ┌─────────────────────────────────────────────────┐    │
│  About     │  │  Footer: TerraSpectra © 2024 | Infotact        │    │
│            │  └─────────────────────────────────────────────────┘    │
└────────────┴─────────────────────────────────────────────────────────┘
```

### Sidebar Navigation Design

```
┌────────────────────┐
│  🌿 TerraSpectra   │
│                    │
│  ═══════════════   │
│                    │
│  📊 Overview       │  ← Active page highlighted
│  📁 Dataset        │     with #4CAF50 background
│  🔬 Spectral       │     and white text
│  🔮 Prediction     │
│  📈 Models         │
│  ⏱️ Temporal       │
│                    │
│  ═══════════════   │
│                    │
│  ⚙️ Settings       │
│  ℹ️ About          │
│                    │
│  ───────────────   │
│  v1.0.0            │
│  Day 1 - Research  │
└────────────────────┘
```

---

## 2. Color Scheme Specification

### 2.1 Color Palette

```
PRIMARY        #1B5E20    ████████  Dark Green     — Headers, sidebar bg, primary buttons
SECONDARY      #4CAF50    ████████  Medium Green   — Active nav, highlights, chart accents
ACCENT         #81C784    ████████  Light Green    — Hover states, tags, secondary elements
BACKGROUND     #FAFAFA    ████████  Off-White      — Page background
SURFACE        #FFFFFF    ████████  White          — Cards, panels, containers
TEXT PRIMARY   #212121    ████████  Near-Black     — Body text, headings
TEXT SECONDARY #757575    ████████  Gray           — Captions, labels, metadata
DIVIDER        #E0E0E0    ████████  Light Gray     — Borders, separators
ERROR          #D32F2F    ████████  Red            — Error messages
WARNING        #F57C00    ████████  Orange         — Warnings, caution states
SUCCESS        #388E3C    ████████  Green          — Success, confirmations
```

### 2.2 Severity Level Color Coding (consistent across all pages)

```
Severity 0 (Healthy)     #2E7D32   ████████  Green
Severity 1 (Mild)        #689F38   ████████  Light Green
Severity 2 (Moderate)    #FBC02D   ████████  Yellow
Severity 3 (Severe)      #F57C00   ████████  Orange
Severity 4 (Critical)    #D32F2F   ████████  Red
```

### 2.3 Font Choices

| Usage | Font | Size | Weight |
|-------|------|------|--------|
| Page Title | Inter / Roboto (sans-serif) | 28px | 700 (Bold) |
| Section Heading | Inter / Roboto | 22px | 600 (Semi-bold) |
| Subsection | Inter / Roboto | 18px | 600 |
| Body Text | Inter / Roboto | 14px | 400 (Regular) |
| Captions / Labels | Inter / Roboto | 12px | 400 |
| Code / Data | Fira Code / monospace | 13px | 400 |
| Stat Numbers | Inter / Roboto | 36px | 700 |

---

## 3. Page Wireframes

### 3.1 Page 1: Overview (Home)

```
┌─────────────────────────────────────────────────────────────────┐
│  🌿 TerraSpectra — Hyperspectral Intelligence for Crop Disease │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    HERO SECTION                          │   │
│  │   "Detect crop diseases early using hyperspectral        │   │
│  │    imaging and machine learning"                         │   │
│  │                                                          │   │
│  │   [Get Started →]                                        │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐       │
│  │   293    │  │   204    │  │    5     │  │  ~XX%    │       │
│  │ Samples  │  │  Bands   │  │ Severity │  │ Accuracy │       │
│  │          │  │          │  │  Levels  │  │ (Best)   │       │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘       │
│                                                                 │
│  ┌─────────────────────────┐  ┌─────────────────────────┐      │
│  │  📁 Explore Dataset     │  │  🔬 Spectral Analysis   │      │
│  │  Browse samples and     │  │  Compare spectral       │      │
│  │  class distributions    │  │  signatures by class     │      │
│  │  [Open →]               │  │  [Open →]               │      │
│  └─────────────────────────┘  └─────────────────────────┘      │
│                                                                 │
│  ┌─────────────────────────┐  ┌─────────────────────────┐      │
│  │  🔮 Disease Prediction  │  │  📈 Model Performance   │      │
│  │  Upload spectral data   │  │  Compare ML models and  │      │
│  │  for classification     │  │  evaluation metrics      │      │
│  │  [Open →]               │  │  [Open →]               │      │
│  └─────────────────────────┘  └─────────────────────────┘      │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  ABOUT THIS PROJECT                                      │   │
│  │  TerraSpectra analyzes hyperspectral reflectance data    │   │
│  │  from tomato plants to classify bacterial wilt severity.  │   │
│  │  Dataset: 293 samples × 204 spectral bands (350-2500nm) │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3.2 Page 2: Dataset Explorer

```
┌─────────────────────────────────────────────────────────────────┐
│  📁 Dataset Explorer                                            │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  FILTERS                                                        │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Severity: [☑0] [☑1] [☑2] [☑3] [☑4]                   │   │
│  │  Wavelength Range: |=====[350nm]=========[2500nm]=====| │   │
│  │  View: (●) Raw  (○) Normalized                         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌────────────────────────┐  ┌──────────────────────────────┐  │
│  │  CLASS DISTRIBUTION    │  │  DATASET STATISTICS           │  │
│  │                        │  │                               │  │
│  │  Sev 0: ████████ 85   │  │  Total Samples: 293           │  │
│  │  Sev 1: █████   52    │  │  Spectral Bands: 204          │  │
│  │  Sev 2: ██████  61    │  │  Wavelength: 350–2500nm       │  │
│  │  Sev 3: █████   48    │  │  Classes: 5 (0-4)             │  │
│  │  Sev 4: █████   47    │  │  Format: .mat (MATLAB)        │  │
│  │                        │  │                               │  │
│  └────────────────────────┘  └──────────────────────────────┘  │
│                                                                 │
│  DATA TABLE                                          [⬇ CSV]   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ # │ Sample ID │ Severity │ Band 1  │ Band 2  │ ... │204│   │
│  │───┼───────────┼──────────┼─────────┼─────────┼─────┼───│   │
│  │ 1 │ S_001     │ 0        │ 0.1234  │ 0.1256  │ ... │   │   │
│  │ 2 │ S_002     │ 0        │ 0.1198  │ 0.1201  │ ... │   │   │
│  │ 3 │ S_003     │ 1        │ 0.1345  │ 0.1367  │ ... │   │   │
│  │...│ ...       │ ...      │ ...     │ ...     │ ... │   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  SPECTRAL PREVIEW  (click a row above to plot)                  │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Reflectance                                              │   │
│  │  0.5│         ╱╲                                         │   │
│  │     │    ╱╲  ╱  ╲    ╱╲                                  │   │
│  │  0.3│   ╱  ╲╱    ╲  ╱  ╲                                │   │
│  │     │  ╱          ╲╱    ╲___                             │   │
│  │  0.1│ ╱                      ╲___                        │   │
│  │     └────────────────────────────────→ Wavelength (nm)   │   │
│  │      350     700    1100   1500   2000   2500            │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3.3 Page 3: Spectral Analysis

```
┌─────────────────────────────────────────────────────────────────┐
│  🔬 Spectral Analysis                                           │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  CONTROLS                                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Classes: [☑0 Healthy] [☑1 Mild] [☑2 Mod] [☑3 Sev] [☑4]│   │
│  │  Plot Type: [Mean ± Std ▾]   Show: [☑ Confidence Band]  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  MEAN SPECTRAL SIGNATURES                          [⬇ PNG/SVG] │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Reflectance                                              │   │
│  │  0.6│      ·····                                         │   │
│  │     │    ·· ╱╲ ··                                        │   │
│  │  0.4│   ╱──╱  ╲──╲     ── Sev 0 (green)                 │   │
│  │     │  ╱   ╱    ╲  ╲   ·· Sev 1 (light green)           │   │
│  │  0.2│ ╱   ╱      ╲  ╲  -- Sev 2 (yellow)                │   │
│  │     │╱   ╱        ╲  ╲ -· Sev 3 (orange)                │   │
│  │  0.0│───╱──────────╲──╲ == Sev 4 (red)                   │   │
│  │     └────────────────────────────→ Wavelength (nm)       │   │
│  │      350     700    1100   1500   2000   2500            │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌────────────────────────┐  ┌──────────────────────────────┐  │
│  │  DIFFERENCE SPECTRUM   │  │  BAND IMPORTANCE             │  │
│  │                        │  │                               │  │
│  │  Compare:              │  │  Top 10 Discriminating Bands  │  │
│  │  Class A: [Sev 0 ▾]   │  │  ┌─────────────────────────┐ │  │
│  │  Class B: [Sev 4 ▾]   │  │  │ Band 87: ████████ 0.92  │ │  │
│  │                        │  │  │ Band 134: ███████ 0.85  │ │  │
│  │  Δ Reflectance plot    │  │  │ Band 56: ██████  0.78   │ │  │
│  │  ┌──────────────────┐  │  │  │ Band 201: █████  0.71   │ │  │
│  │  │    ╱╲            │  │  │  │ Band 12: █████   0.69   │ │  │
│  │  │   ╱  ╲   ╱╲     │  │  │  │ ...                      │ │  │
│  │  │──╱────╲─╱──╲──  │  │  │  └─────────────────────────┘ │  │
│  │  │          ╲       │  │  │                               │  │
│  │  └──────────────────┘  │  │  Source: Random Forest        │  │
│  └────────────────────────┘  └──────────────────────────────┘  │
│                                                                 │
│  WAVELENGTH BOX PLOTS  (click a wavelength above)               │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Band 87 (λ = 1050nm)                                    │   │
│  │  Sev 0: ├──[  |  ]──┤                                   │   │
│  │  Sev 1:    ├──[  | ]──┤                                  │   │
│  │  Sev 2:       ├──[ |]──┤                                 │   │
│  │  Sev 3:          ├──[|]──┤                               │   │
│  │  Sev 4:             ├─[|]─┤                              │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3.4 Page 4: Disease Prediction

```
┌─────────────────────────────────────────────────────────────────┐
│  🔮 Disease Prediction                                          │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  UPLOAD & CONFIGURE                                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │   ┌──────────────────────────────────────────────────┐   │   │
│  │   │                                                  │   │   │
│  │   │   📤 Drag and drop spectral data here            │   │   │
│  │   │      or [Browse files]                           │   │   │
│  │   │                                                  │   │   │
│  │   │   Accepted: .mat, .csv, .npy                     │   │   │
│  │   │   Max size: 100MB                                │   │   │
│  │   └──────────────────────────────────────────────────┘   │   │
│  │                                                          │   │
│  │   Model: [Random Forest ▾]    [🔮 Predict]              │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  VALIDATION STATUS                                              │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  ✅ File format: .mat                                    │   │
│  │  ✅ Spectral bands: 204 ✓                                │   │
│  │  ✅ Samples detected: 3                                  │   │
│  │  ✅ Value range: [0.01, 0.89] — normal                   │   │
│  │  ⚠️ No missing values detected                           │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  PREDICTION RESULTS                                             │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Sample 1 of 3                                           │   │
│  │                                                          │   │
│  │  Predicted: ████ SEVERITY 2 (Moderate) — 78.3%           │   │
│  │                                                          │   │
│  │  Confidence Distribution:                                │   │
│  │  Sev 0: ██        8.2%                                   │   │
│  │  Sev 1: ███       12.1%                                  │   │
│  │  Sev 2: █████████████████████████████ 78.3%  ← Predicted│   │
│  │  Sev 3: █         1.0%                                   │   │
│  │  Sev 4: █         0.4%                                   │   │
│  │                                                          │   │
│  │  [← Prev Sample]              [Next Sample →]           │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  FEATURE EXPLANATION (SHAP)                        [⬇ CSV]     │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Top contributing wavelengths for this prediction:       │   │
│  │  Band 87 (1050nm):  ████████████▶  +0.23                │   │
│  │  Band 134 (1680nm): ████████▶      +0.18                │   │
│  │  Band 56 (810nm):   ◀████          -0.12                │   │
│  │  Band 201 (2350nm): ████▶          +0.09                │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3.5 Page 5: Model Performance

```
┌─────────────────────────────────────────────────────────────────┐
│  📈 Model Performance                                           │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  MODEL COMPARISON TABLE                                         │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Model          │ Accuracy │ F1 (wt) │ Precision │Recall │   │
│  │────────────────┼──────────┼─────────┼───────────┼───────│   │
│  │ Random Forest  │ 0.891    │ 0.887   │ 0.893     │ 0.891 │   │
│  │ SVM (RBF)      │ 0.875    │ 0.871   │ 0.879     │ 0.875 │   │
│  │ XGBoost        │ 0.903    │ 0.899   │ 0.907     │ 0.903 │   │
│  │ 1D-CNN         │ 0.856    │ 0.849   │ 0.861     │ 0.856 │   │
│  └─────────────────────────────────────────────────────────┘   │
│  * Values are illustrative; actual metrics from trained models  │
│                                                                 │
│  ┌────────────────────────┐  ┌──────────────────────────────┐  │
│  │  CONFUSION MATRIX      │  │  ROC CURVES                  │  │
│  │                        │  │                               │  │
│  │  Model: [XGBoost ▾]   │  │  ┌───────────────────────┐   │  │
│  │                        │  │  │  TPR                   │   │  │
│  │   P\A│ 0  1  2  3  4  │  │  │  1.0│   ╱─────────     │   │  │
│  │   ───┼────────────────│  │  │     │  ╱  ╱             │   │  │
│  │    0 │ 15  1  0  0  0 │  │  │  0.5│ ╱  ╱              │   │  │
│  │    1 │  1  9  1  0  0 │  │  │     │╱  ╱  ·· diagonal  │   │  │
│  │    2 │  0  1 11  0  0 │  │  │  0.0│──────────→ FPR    │   │  │
│  │    3 │  0  0  1  8  1 │  │  │     AUC: 0.96           │   │  │
│  │    4 │  0  0  0  1  8 │  │  │  └───────────────────────┘   │  │
│  └────────────────────────┘  └──────────────────────────────┘  │
│                                                                 │
│  CROSS-VALIDATION RESULTS                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  5-Fold Stratified CV Accuracy                           │   │
│  │                                                          │   │
│  │  RF:      ├─────[ | ]─────┤   Mean: 0.89 ± 0.03        │   │
│  │  SVM:     ├─────[ |]──────┤   Mean: 0.87 ± 0.04        │   │
│  │  XGBoost: ├──────[| ]─────┤   Mean: 0.90 ± 0.02        │   │
│  │  1D-CNN:  ├────[  | ]─────┤   Mean: 0.85 ± 0.05        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  FEATURE IMPORTANCE (Top 20)                   [⬇ Full List]   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Band 87:  ████████████████████████████████ 0.092       │   │
│  │  Band 134: █████████████████████████████    0.085       │   │
│  │  Band 56:  ████████████████████████         0.078       │   │
│  │  Band 201: ███████████████████████          0.071       │   │
│  │  Band 12:  ██████████████████               0.065       │   │
│  │  ...                                                     │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

### 3.6 Page 6: Temporal Analysis

```
┌─────────────────────────────────────────────────────────────────┐
│  ⏱️ Temporal Analysis                                           │
│  ─────────────────────────────────────────────────────────────  │
│                                                                 │
│  ℹ️ Note: The Tomato Wilt dataset lacks a temporal axis.        │
│  Severity levels are used as a proxy for disease progression.   │
│                                                                 │
│  CONTROLS                                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Dataset: (●) Tomato Wilt  (○) Pine Wilt               │   │
│  │  Analysis: [Progression Proxy ▾]                        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  SEVERITY PROGRESSION (Spectral Change Across Levels)           │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Mean Reflectance                                         │   │
│  │                                                          │   │
│  │  0.5│        ╱╲                                          │   │
│  │     │  0────╱  ╲────0    Healthy → Mild → Mod → ...     │   │
│  │  0.3│  1···╱····╲···1                                    │   │
│  │     │  2--╱------╲--2    Tracks spectral degradation     │   │
│  │  0.1│  3─╱────────╲─3    as disease severity increases   │   │
│  │     │  4╱──────────╲4                                    │   │
│  │     └────────────────────→ Wavelength (nm)               │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  EARLY DETECTION ANALYSIS                                       │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Bands with earliest divergence (Sev 0 vs Sev 1):       │   │
│  │                                                          │   │
│  │  Rank │ Band │ Wavelength │ p-value   │ Effect Size     │   │
│  │  ─────┼──────┼────────────┼───────────┼─────────────    │   │
│  │    1  │  87  │ 1050nm     │ 0.0001    │ 1.23 (large)   │   │
│  │    2  │ 134  │ 1680nm     │ 0.0003    │ 1.18 (large)   │   │
│  │    3  │  56  │  810nm     │ 0.0012    │ 0.95 (large)   │   │
│  │    4  │ 201  │ 2350nm     │ 0.0034    │ 0.82 (large)   │   │
│  │    5  │  12  │  460nm     │ 0.0089    │ 0.67 (medium)  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌────────────────────────┐  ┌──────────────────────────────┐  │
│  │  BAND DIVERGENCE PLOT  │  │  KEY INSIGHTS                │  │
│  │                        │  │                               │  │
│  │  Statistical sig.      │  │  • Near-infrared region       │  │
│  │  across all 204 bands  │  │    (~1000-1100nm) shows       │  │
│  │  (Sev 0 vs Sev 1)     │  │    earliest disease signal    │  │
│  │                        │  │                               │  │
│  │  -log10(p)             │  │  • SWIR bands (~1600-1800nm)  │  │
│  │  5│  ▲   ▲             │  │    are strong secondary       │  │
│  │  3│ ▲ ▲ ▲ ▲   ▲       │  │    indicators                 │  │
│  │  1│▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲   │  │                               │  │
│  │  ─┼──────────→ Band   │  │  • Visible bands (400-700nm)  │  │
│  │   sig. threshold ──    │  │    less discriminative for     │  │
│  └────────────────────────┘  │    early detection             │  │
│                               └──────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Responsive Behavior Notes

### Breakpoints
- **≥1440px:** Full layout with sidebar expanded, 2-column sub-layouts
- **1024–1439px:** Sidebar collapsed by default (hamburger toggle), single-column charts stacked
- **<1024px:** Minimal support — warning banner suggesting desktop for best experience

### Chart Responsiveness
- All Plotly charts use `use_container_width=True` in Streamlit
- Charts resize dynamically with `st.plotly_chart(fig, use_container_width=True)`
- Data tables use `st.dataframe(df, use_container_width=True)` for horizontal scroll

### Navigation
- Sidebar is the primary navigation mechanism (Streamlit native)
- Active page highlighted with secondary color background
- Optional: `streamlit-option-menu` for styled icon-based navigation

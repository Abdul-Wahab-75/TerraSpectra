"""
Abdul - Day 9: Model Performance & Deep Learning Loss History Component
Author: Abdul (Backend & Dashboard Lead)
Visualizes 1D-CNN loss convergence alongside Classical ML Leaderboards.
"""

import os
import sys
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def build_cnn_training_curve_figure(csv_path: str) -> go.Figure:
    """Builds interactive training vs validation loss and accuracy curves."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"History CSV not found: {csv_path}")
        
    df = pd.read_csv(csv_path)
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=("Cross-Entropy Loss Curve", "Accuracy Trajectory (%)"),
        horizontal_spacing=0.12
    )
    
    # Loss subplot
    fig.add_trace(
        go.Scatter(x=df["epoch"], y=df["loss"], mode="lines+markers", name="Training Loss", line=dict(color="#1f77b4", width=2)),
        row=1, col=1
    )
    
    # Accuracy subplot
    fig.add_trace(
        go.Scatter(x=df["epoch"], y=df["accuracy"] * 100, mode="lines+markers", name="Training Acc (%)", line=dict(color="#2ca02c", width=2)),
        row=1, col=2
    )
    
    fig.update_xaxes(title_text="Epoch", row=1, col=1)
    fig.update_xaxes(title_text="Epoch", row=1, col=2)
    fig.update_yaxes(title_text="Cross-Entropy Loss", row=1, col=1)
    fig.update_yaxes(title_text="Accuracy (%)", row=1, col=2)
    
    fig.update_layout(
        title="PyTorch 1D-CNN Training Dynamics",
        template="plotly_white",
        height=450,
        margin=dict(l=40, r=40, t=60, b=40)
    )
    
    return fig

def test_abdul_day9():
    print("Testing Abdul Day 9 Dashboard Component...")
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    csv_path = os.path.join(root_dir, "main project/models/evaluation/cnn_training_history.csv")
    fig = build_cnn_training_curve_figure(csv_path)
    assert fig is not None
    assert len(fig.data) == 2
    print("✔ Abdul Day 9 CNN training curve component test passed!")

if __name__ == "__main__":
    test_abdul_day9()

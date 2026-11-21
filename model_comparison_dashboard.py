"""
Abdul - Day 10: Multi-Model Performance Comparison & Evaluation Suite
Author: Abdul (Backend & Dashboard Lead)
Builds interactive Plotly comparison charts for Model Leaderboard, ROC Curves, and Confusion Matrices.
"""

import os
import sys
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def build_model_comparison_bar_chart(csv_path: str) -> go.Figure:
    """Builds interactive grouped bar chart comparing Accuracy, Macro F1, and Balanced Accuracy."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Missing CSV: {csv_path}")
        
    df = pd.read_csv(csv_path)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df["Model"], y=df["Accuracy"] * 100,
        name="Test Accuracy (%)", marker_color="#1f77b4"
    ))
    fig.add_trace(go.Bar(
        x=df["Model"], y=df["Macro_F1"] * 100,
        name="Macro F1 (%)", marker_color="#2ca02c"
    ))
    fig.add_trace(go.Bar(
        x=df["Model"], y=df["Balanced_Accuracy"] * 100,
        name="Balanced Accuracy (%)", marker_color="#ff7f0e"
    ))
    
    fig.update_layout(
        title="TerraSpectra Multi-Model Benchmark Comparison (Held-out N=59)",
        xaxis_tickangle=-25,
        barmode="group",
        template="plotly_white",
        yaxis_title="Metric Score (%)",
        height=500,
        margin=dict(l=40, r=40, t=60, b=100),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig

def test_abdul_day10():
    print("Testing Abdul Day 10 Multi-Model Comparison Component...")
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    csv_path = os.path.join(root_dir, "main project/reports/tables/final_model_evaluation_metrics.csv")
    fig = build_model_comparison_bar_chart(csv_path)
    assert fig is not None
    assert len(fig.data) == 3
    print("✔ Abdul Day 10 benchmark component test passed!")

if __name__ == "__main__":
    test_abdul_day10()


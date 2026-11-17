"""
Abdul Day 6: PCA Visualization Component Snapshot
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "dashboard")))
from components.pca_viewer import render_pca_analytics

__all__ = ["render_pca_analytics"]


"""
Abdul Day 5: Preprocessing Visualizer Snapshot
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "src")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "dashboard")))
from components.preprocessing_viewer import render_preprocessing_comparison

__all__ = ["render_preprocessing_comparison"]


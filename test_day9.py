"""
Abdul - Day 9 Test Suite
Verifies deep learning dashboard visualization components.
"""

import os
import sys

def run_tests():
    from cnn_dashboard_component import build_cnn_training_curve_figure
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    csv_path = os.path.join(root_dir, "main project/models/evaluation/cnn_training_history.csv")
    fig = build_cnn_training_curve_figure(csv_path)
    assert fig is not None, "Figure generation failed"
    print("ALL ABDUL DAY 9 TESTS PASSED!")

if __name__ == "__main__":
    run_tests()


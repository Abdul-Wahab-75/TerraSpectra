"""
Abdul - Day 10 Test Suite
Verifies multi-model evaluation dashboard comparison components.
"""

import os
import sys

def run_tests():
    from model_comparison_dashboard import build_model_comparison_bar_chart
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
    csv_path = os.path.join(root_dir, "main project/reports/tables/final_model_evaluation_metrics.csv")
    fig = build_model_comparison_bar_chart(csv_path)
    assert fig is not None, "Figure generation failed"
    print("ALL ABDUL DAY 10 TESTS PASSED!")

if __name__ == "__main__":
    run_tests()


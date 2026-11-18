"""
Abdul Day 7: Prediction Interface Page Snapshot
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "dashboard", "pages")))
with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "dashboard", "pages", "03_Disease_Prediction.py")), "r") as f:
    code = f.read()

exec(code)


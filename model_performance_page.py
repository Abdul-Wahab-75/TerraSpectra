"""
Abdul Day 8: Model Performance Page Snapshot
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "dashboard", "pages")))
with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "dashboard", "pages", "04_Model_Performance.py")), "r") as f:
    code = f.read()

exec(code)


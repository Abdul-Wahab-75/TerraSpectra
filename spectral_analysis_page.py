"""
Abdul Day 4: Spectral Analysis Page Snapshot
"""
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "dashboard", "pages")))
# Mirror the main project page
with open(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "dashboard", "pages", "02_Spectral_Analysis.py")), "r") as f:
    code = f.read()

exec(code)


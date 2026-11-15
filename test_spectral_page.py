import os
import sys

def test_page_syntax():
    page_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "dashboard", "pages", "02_Spectral_Analysis.py"))
    assert os.path.exists(page_path), f"Page not found at {page_path}"
    with open(page_path, "r", encoding="utf-8") as f:
        code = f.read()
    compiled = compile(code, page_path, "exec")
    assert compiled is not None
    print("Page 02_Spectral_Analysis syntax and AST compilation verified!")

if __name__ == "__main__":
    test_page_syntax()


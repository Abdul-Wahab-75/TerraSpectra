import os

def test_performance_compilation():
    page_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "dashboard", "pages", "04_Model_Performance.py"))
    assert os.path.exists(page_path), f"Page not found at {page_path}"
    with open(page_path, "r", encoding="utf-8") as f:
        code = f.read()
    compiled = compile(code, page_path, "exec")
    assert compiled is not None
    print("Page 04_Model_Performance compiled successfully with zero syntax errors!")

if __name__ == "__main__":
    test_performance_compilation()


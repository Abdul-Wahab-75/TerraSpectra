import os

def test_prediction_page_compilation():
    page_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "dashboard", "pages", "03_Disease_Prediction.py"))
    assert os.path.exists(page_path), f"Page not found at {page_path}"
    with open(page_path, "r", encoding="utf-8") as f:
        code = f.read()
    compiled = compile(code, page_path, "exec")
    assert compiled is not None
    print("Page 03_Disease_Prediction compiled successfully with zero syntax errors!")

if __name__ == "__main__":
    test_prediction_page_compilation()


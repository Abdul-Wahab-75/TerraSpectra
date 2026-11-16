import os

def test_component_compilation():
    comp_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "main project", "dashboard", "components", "preprocessing_viewer.py"))
    assert os.path.exists(comp_path), f"Component not found at {comp_path}"
    with open(comp_path, "r", encoding="utf-8") as f:
        code = f.read()
    compiled = compile(code, comp_path, "exec")
    assert compiled is not None
    print("Preprocessing comparison component compiled successfully with zero syntax errors!")

if __name__ == "__main__":
    test_component_compilation()


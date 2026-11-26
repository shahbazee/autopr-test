def test_frontend_line_at_end():
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    assert lines, "README.md is empty"
    assert lines[-1] == "Frontend test 2026-11-26"

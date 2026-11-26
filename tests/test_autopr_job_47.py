def test_readme_has_no_typo():
    text = open("README.md").read()
    assert "Thiss" not in text
    assert "testt" not in text

def test_readme_ends_with_frontend_line():
    with open("README.md") as f:
        lines = f.read().splitlines()
    assert lines, "README.md is empty"
    assert lines[-1] == "Frontend test 2026-11-26"

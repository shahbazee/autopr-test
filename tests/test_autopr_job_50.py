import pathlib

def test_readme_content():
    text = pathlib.Path("README.md").read_text()
    assert "Thiss" not in text
    assert "testt" not in text
    assert "This is a test repo for AutoPR." in text
    assert "Fixed by AutoPR" in text

def test_readme_has_no_typo():
    text = open("README.md").read()
    assert "Thiss" not in text
    assert "testt" not in text

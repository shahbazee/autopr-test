def test_readme_has_real_webhook_line():
    with open("README.md", encoding="utf-8") as f:
        lines = f.read().splitlines()
    assert lines, "README.md is empty"
    assert lines[-1] == "Real webhook test", "README.md does not end with 'Real webhook test'"

def test_readme_ends_with_cancel_test():
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    assert lines, "README.md is empty"
    assert lines[-1] == "Cancel test", "README.md should end with 'Cancel test'"

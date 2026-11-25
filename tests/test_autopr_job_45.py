def test_readme_verified_line():
    with open("README.md", "r") as f:
        lines = [line.rstrip("\n") for line in f]
    assert lines, "README.md is empty"
    assert lines[-1] == "Verified via real webhook"

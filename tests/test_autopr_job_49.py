def test_readme_has_follow_up_comment():
    with open("README.md", "r") as f:
        lines = f.read().splitlines()
    assert lines, "README.md is empty"
    assert lines[-1] == "Follow-up comment test", "README.md does not end with the required line"

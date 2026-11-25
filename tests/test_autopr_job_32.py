import pathlib

def test_readme_ends_with_ai_tests_work():
    readme_path = pathlib.Path("README.md")
    assert readme_path.is_file(), "README.md does not exist"

    content = readme_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    assert lines, "README.md is empty"

    # The last line should be exactly 'AI tests work'
    assert lines[-1] == "AI tests work", (
        f"Expected last line to be 'AI tests work', "
        f"but got '{lines[-1]}'"
    )

    # Ensure the line appears somewhere in the file
    assert "AI tests work" in lines, "README.md does not contain 'AI tests work'"

    # Ensure there is no trailing whitespace on the last line
    assert lines[-1].strip() == lines[-1], (
        "Trailing whitespace found on the last line of README.md"
    )

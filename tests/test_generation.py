"""Test the generation of repositories and basic templates."""

import pytest


def test_cases_dir_exists(cases_dir):
    """Check the data dir exists."""
    assert cases_dir.exists()
    assert cases_dir.is_dir()


@pytest.mark.parametrize("case_name", ["test_generation"])
def test_empty_repo(case):
    """Test that creating the input repo succeeds."""

    assert case
    input_repo = case.repo("input")
    input_repo.git_init()
    result = input_repo.git("show")
    assert result

@pytest.mark.parametrize("case_name", ["test_generation"])
def test_copied_repo(case):
    """Test that creating input repo with initial files succeeds."""

    assert case
    source = case.source / "input"
    dest = case.repo("input")
    dest.git_init(source)
    result = dest.git("show")
    assert result

    source_files = [
        f.relative_to(source) for f in source.rglob("*")
        if not str(f).startswith(str(source / ".git"))]
    dest_files = [
        f.relative_to(dest.path) for f in dest.path.rglob("*")
        if not str(f).startswith(str(dest.path / ".git"))]
    assert source_files == dest_files

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
    input_repo = case.repo("project")
    result = input_repo.git("show")
    assert result


@pytest.mark.parametrize("case_name", ["test_generation"])
def test_copied_repo(case, dir_to_dict):
    """Test that creating input repo with initial files succeeds."""

    assert case
    repo = case.repo("project")
    result = repo.git("show")
    assert result

    assert dir_to_dict(repo.source) == dir_to_dict(repo.path)

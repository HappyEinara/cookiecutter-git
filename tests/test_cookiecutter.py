"""Test the generation of repositories and basic templates."""

import pytest


@pytest.mark.parametrize("case_name", ["test_generation"])
def test_cookiecutter_generates(case, dir_to_dict):
    """Test that running cookiecutter works."""

    project_repo = case.repo("project")
    cookiecutter_repo = case.repo("cookiecutter")

    case.run_cookiecutter("template", "project")
    result = dir_to_dict(project_repo.path)
    expected = dir_to_dict(cookiecutter_repo.path)

    assert result == expected

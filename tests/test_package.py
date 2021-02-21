"""Test basic package metadata.

Mainly used to check the cookiecutter template used to initialise this project.
"""

import warnings

import git
import semver

import cookiecutter_git as package


def test_version_exists():
    """Test that the package has a version."""

    assert package.__version__


def test_version_is_valid():
    """Test that the package version is valid semver."""

    assert semver.VersionInfo.isvalid(package.__version__)


def test_version_was_bumped():
    """Test that the release version is semantically lower than current."""
    repo = git.repo.Repo()
    git_description = repo.git.describe(always=True, tags=True)
    released_version = git_description.split(
        '-')[0][1:]  # Split on first hyphen and remove the leading 'v'
    current_version = package.__version__
    try:
        assert (
            semver.VersionInfo.parse(current_version).compare(released_version)
            > 0)
    except ValueError:
        warnings.warn(
            "No valid version tag found. If this is a new project, you can "
            f"ignore this. Git description: '{git_description}'")
        assert (
            semver.VersionInfo.parse(current_version).compare("0.0.0")
            > 0)

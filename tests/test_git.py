"""Test creation of an output repository."""

import os


def test_data_dir_exists(data_dir):
    """Check the data dir exists."""
    assert os.path.isdir(data_dir)


def test_repo_creation(git_cmd):
    """Test that the output repo has successfully been created."""
    result = git_cmd("symbolic-ref HEAD")
    assert result

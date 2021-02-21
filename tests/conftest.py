"""Fixtures for testing the application."""

# pylint: disable=redefined-outer-name

import os
import subprocess

import pytest


@pytest.fixture
def data_dir():
    """Return a directory for test data and output."""
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), "data")


@pytest.fixture
def output_repo(data_dir):
    """Create an output repo for tests if it doesn't exist and return path."""
    repo_path = os.path.join(data_dir, "output")
    if not os.path.isdir(repo_path):
        subprocess.run(["git", "init", repo_path], check=True)
    return repo_path


@pytest.fixture
def git_cmd(output_repo):
    """Run a git command on the test repo."""
    def run(git_command):
        bits = ["git", f"--git-dir={output_repo}/.git"] + git_command.split(
            " "
        )
        result = subprocess.run(
            bits,
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout

    return run

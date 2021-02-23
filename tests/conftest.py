"""Fixtures for testing the application."""

# pylint: disable=redefined-outer-name

import os
from pathlib import Path
import shutil
import shlex
import subprocess

import pytest


CASES_DIR = Path(__file__).parent / "data" / "cases"

class GitError(RuntimeError):
    pass


class Case:
    """A collection of inputs and outputs from which to build repos."""

    class Repo:
        """A repo in the tmp dir."""

        def __init__(self, path):
            self.path = path

        def git_init(self, source_path=None):
            if source_path:
                shutil.copytree(source_path, self.path)
            else:
                self.path.mkdir()
            self.git("init")
            self.git('config user.name "cookiecutter-git tests"')
            self.git('config user.email "cookiecutter-git@einara.com"')
            self.git("add .")
            self.git('commit -m "Initial commit."')

        def git(self, command):
            result, _ = git_command(self.path, command)
            return result

        def __repr__(self):
            return f"{self.__class__.__name__}({self.path})"

    def __init__(self, name, tmp_path):
        """Initialise."""
        self.name = name
        self.source = CASES_DIR / self.name
        self.destination = Path(tmp_path)

    def repo(self, name):
        """Return a repo."""
        return self.Repo(self.destination / name)


@pytest.fixture
def case(case_name, tmp_path):
    return Case(case_name, tmp_path)


@pytest.fixture
def cases_dir():
    return CASES_DIR

def git_command(path, command):
    """Run a git command on the test repo."""
    bits = (
        ["git", f"--git-dir={path}/.git"]
        + shlex.split(command)
    )
    try:
        result = subprocess.run(
            bits,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        raise GitError(f"Git command failed:\n{e.stderr}") from e
    return result.stdout, result.stderr


def dir_to_dict(directory):
    result = {}
    for root, directories, files in os.walk(directory, topdown=False):
        current = result
        for path_element in root.split(os.sep):
            current.setdefault(path_element, {})
            current=current[path_element]
        for d in directories:
            current.setdefault(d, {})
        current.setdefault("_files", {})
        for filename in files:
            with open(os.path.join(root, filename)) as f:
                content = f.read()
                current["_files"][filename] = content
    return result


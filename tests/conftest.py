"""Fixtures for testing the application."""

# pylint: disable=redefined-outer-name

from hashlib import sha1
from pathlib import Path
import shutil
import shlex
import subprocess
from typing import Callable, Optional

from click.testing import CliRunner
import cookiecutter.cli
import pytest


CASES_DIR = Path(__file__).parent / "data" / "cases"


class GitError(RuntimeError):
    """Raised when a Git call fails."""


class Case:
    """A collection of inputs and outputs from which to build repos."""
    # pylint: disable=too-few-public-methods

    class Repo:
        """A repo in the tmp dir."""

        def __init__(self, path: Path, source: Optional[Path] = None):
            """Initialise."""
            self.path = path
            self.source = source

            if self.source:
                shutil.copytree(self.source, self.path)
            else:
                self.path.mkdir()

            self.git("init")
            self.git('config user.name "cookiecutter-git tests"')
            self.git('config user.email "cookiecutter-git@einara.com"')
            self.git("add .")
            self.git('commit -m "Initial commit."')

        def git(self, command):
            """Run a git command on the repo."""
            result, _ = git_command(self.path, command)
            return result

        def __repr__(self):
            return f"{self.__class__.__name__}({self.path})"

    def __init__(self, name, tmp_path):
        """Initialise."""
        self.name = name
        self.source = CASES_DIR / self.name
        self.destination = Path(tmp_path)
        self._repos = {}

    def repo(self, name) -> Repo:
        """Return a repo."""
        if name in self._repos:
            return self._repos[name]
        source = self.source / name
        if source.is_dir():
            repo = self.Repo(
                self.destination / name,
                source=source)
        else:
            repo = self.Repo(
                self.destination / name)
        self._repos[name] = repo
        return repo

    def run_cookiecutter(
                self, template_name, apply_to_name, cookiecutter=cookiecutter):
        """Run cookiecutter (or an equivalent cli) on a project."""

        template = self.repo(template_name).path
        apply_to = self.repo(apply_to_name).path

        result = run_click(
            cookiecutter.cli.main,
            str(template),
            "-o", str(apply_to)
        )
        return result


@pytest.fixture
def case(case_name, tmp_path):
    """Return the specified test case."""
    return Case(case_name, tmp_path)


@pytest.fixture
def cases_dir():
    """Return the data dir for case sources."""
    return CASES_DIR


def git_command(path, command):
    """Run a git command on the test repo."""
    bits = ["git", f"--git-dir={path}/.git"] + shlex.split(command)
    try:
        result = subprocess.run(
            bits,
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as exc:
        raise GitError(f"Git command failed:\n{exc.stderr}") from exc
    return result.stdout, result.stderr


def run_click(click_command, *args):
    """Run a click test"""

    runner = CliRunner()
    result = runner.invoke(click_command, args)
    return result


@pytest.fixture
def dir_to_dict() -> Callable[[Path], dict]:
    """Return a function that represents an entire tree as a dict."""

    def _inner(directory: Path):
        """Convert a directory tree and its file contents into a dict."""

        result: dict = {}
        for path in directory.rglob("*"):
            relative = path.relative_to(directory)
            ancestors = list(relative.parents)
            if str(relative)[:5] == '.git/' or str(relative) == '.git':
                continue
            current = result
            while ancestors:
                part = ancestors.pop()
                current.setdefault(part, {})
                current = current[part]
            if path.is_file():
                current.setdefault("_files", {})
                current["_files"][path.name] = sha1(
                    path.read_bytes()).hexdigest()
        return result
    return _inner

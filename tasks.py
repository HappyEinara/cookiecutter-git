"""Invoke tasks.

Mainly for CI.
"""

import os

import git
from invoke import task

import cookiecutter_git as package


VERSION_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "cookiecutter_git", "VERSION"))


# Exceptions
class DeploymentError(Exception):
    """Raised when deployment must fail for some reason."""
    pass


@task
def bumpversion(context, commit=False, part="patch"):
    current_version = package.__version__
    context.run(
        f"bump2version --list --current-version {current_version} "
        f"{'--commit' if commit else '--no-commit'} "
        f"{part} {VERSION_FILE}")

@task
def tagrelease(context, message=None):
    repo = git.repo.Repo()
    if repo.is_dirty():
        raise DeploymentError("Repo is dirty.")

    release_tag = repo.create_tag(
        f"v{package.__version__}", ref=repo.active_branch,
        message=message if message else None)

    repo.remotes.origin.push(release_tag)

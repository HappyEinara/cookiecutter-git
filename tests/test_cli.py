"""Test the CLI."""

from click.testing import CliRunner
import pytest

import cookiecutter_git
import cookiecutter_git.cli as cli


@pytest.mark.parametrize("verbosity", ["", "-v", "-vv"])
def test_cli_version(verbosity):
    """Test that the CLI returns the version correctly."""

    runner = CliRunner()
    result = runner.invoke(cli.cli, f"{verbosity} version")
    assert result.exit_code == 0
    assert (
        result.output.strip() ==
        cookiecutter_git.__version__)

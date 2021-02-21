"""Command-line interface."""

import logging

import click
import logzero
from logzero import logger

import cookiecutter_git


@click.group()
@click.option("-v", "--verbose", "verbosity", count=True)
@click.pass_context
def cli(context, verbosity):
    """A wrapper around cookie-cutter to provide metadata from the template repo."""

    context.ensure_object(dict)
    context.obj['verbosity'] = verbosity

    if verbosity >= 2:
        logzero.loglevel(logging.DEBUG)
    elif verbosity == 1:
        logzero.loglevel(logging.INFO)
    else:
        logzero.loglevel(logging.WARNING)

    logger.info(
        "cookiecutter-git version %s",
        cookiecutter_git.__version__)

    logger.info("Outputting info messages.")
    logger.debug("Outputting debug messages.")


@cli.command()
def version():
    """Outputs the package version."""
    click.echo(cookiecutter_git.__version__)

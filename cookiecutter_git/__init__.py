"""cookiecutter-git"""
import os

HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "VERSION")) as handle:
    __version__ = handle.read().strip()

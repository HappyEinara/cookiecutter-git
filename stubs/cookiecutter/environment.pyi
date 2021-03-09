from cookiecutter.exceptions import UnknownExtension as UnknownExtension
from jinja2 import Environment
from typing import Any

class ExtensionLoaderMixin:
    def __init__(self, **kwargs: Any) -> None: ...

class StrictEnvironment(ExtensionLoaderMixin, Environment):
    def __init__(self, **kwargs: Any) -> None: ...

from cookiecutter.config import get_user_config as get_user_config
from cookiecutter.exceptions import InvalidModeException as InvalidModeException
from cookiecutter.generate import generate_context as generate_context, generate_files as generate_files
from cookiecutter.prompt import prompt_for_config as prompt_for_config
from cookiecutter.replay import dump as dump, load as load
from cookiecutter.repository import determine_repo_dir as determine_repo_dir
from cookiecutter.utils import rmtree as rmtree
from typing import Any, Optional

logger: Any

def cookiecutter(template: Any, checkout: Optional[Any] = ..., no_input: bool = ..., extra_context: Optional[Any] = ..., replay: bool = ..., overwrite_if_exists: bool = ..., output_dir: str = ..., config_file: Optional[Any] = ..., default_config: bool = ..., password: Optional[Any] = ..., directory: Optional[Any] = ..., skip_if_file_exists: bool = ...): ...

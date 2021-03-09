from cookiecutter.exceptions import ConfigDoesNotExistException as ConfigDoesNotExistException, InvalidConfiguration as InvalidConfiguration
from typing import Any, Optional

logger: Any
USER_CONFIG_PATH: Any
BUILTIN_ABBREVIATIONS: Any
DEFAULT_CONFIG: Any

def merge_configs(default: Any, overwrite: Any): ...
def get_config(config_path: Any): ...
def get_user_config(config_file: Optional[Any] = ..., default_config: bool = ...): ...

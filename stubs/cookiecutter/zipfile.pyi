from cookiecutter.exceptions import InvalidZipRepository as InvalidZipRepository
from cookiecutter.prompt import read_repo_password as read_repo_password
from cookiecutter.utils import make_sure_path_exists as make_sure_path_exists, prompt_and_delete as prompt_and_delete
from typing import Any, Optional

def unzip(zip_uri: Any, is_url: Any, clone_to_dir: str = ..., no_input: bool = ..., password: Optional[Any] = ...): ...

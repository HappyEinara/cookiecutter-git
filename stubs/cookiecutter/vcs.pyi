from cookiecutter.exceptions import RepositoryCloneFailed as RepositoryCloneFailed, RepositoryNotFound as RepositoryNotFound, UnknownRepoType as UnknownRepoType, VCSNotInstalled as VCSNotInstalled
from cookiecutter.utils import make_sure_path_exists as make_sure_path_exists, prompt_and_delete as prompt_and_delete
from typing import Any, Optional

logger: Any
BRANCH_ERRORS: Any

def identify_repo(repo_url: Any): ...
def is_vcs_installed(repo_type: Any): ...
def clone(repo_url: Any, checkout: Optional[Any] = ..., clone_to_dir: str = ..., no_input: bool = ...): ...

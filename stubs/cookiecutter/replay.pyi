from cookiecutter.utils import make_sure_path_exists as make_sure_path_exists
from typing import Any

def get_file_name(replay_dir: Any, template_name: Any): ...
def dump(replay_dir: Any, template_name: Any, context: Any) -> None: ...
def load(replay_dir: Any, template_name: Any): ...

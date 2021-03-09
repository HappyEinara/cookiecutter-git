from cookiecutter.exceptions import (
    FailedHookException as FailedHookException,
    InvalidModeException as InvalidModeException,
    InvalidZipRepository as InvalidZipRepository,
    OutputDirExistsException as OutputDirExistsException,
    RepositoryCloneFailed as RepositoryCloneFailed,
    RepositoryNotFound as RepositoryNotFound,
    UndefinedVariableInTemplate as UndefinedVariableInTemplate,
    UnknownExtension as UnknownExtension,
)
from cookiecutter.log import configure_logger as configure_logger
from cookiecutter.main import cookiecutter as cookiecutter
from typing import Any

def version_msg(): ...
def validate_extra_context(ctx: Any, param: Any, value: Any): ...
def main(
    template: str,
    extra_context: list[str],
    no_input: Any,
    checkout: Any,
    verbose: Any,
    replay: Any,
    overwrite_if_exists: Any,
    output_dir: Any,
    config_file: Any,
    default_config: Any,
    debug_file: Any,
    directory: Any,
    skip_if_file_exists: Any,
) -> None: ...

# flake8: noqa: F401
from ._version import __version__
from .manager import LanguageServerManager
from .serverextension import load_jupyter_server_extension
from .specs.utils import NodeModuleSpec, ShellSpec
from .types import (
    KeyedLanguageServerSpecs,
    LanguageServerManagerAPI,
    LanguageServerSpec,
)


def _jupyter_server_extension_paths():  # pragma: no cover
    return [{"module": "jupyter_lsp"}]

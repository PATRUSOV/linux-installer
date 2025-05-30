from .core import ScriptRunner
from .python import PythonRunner
from typing import Type, Dict

extention_handlers: Dict[str, Type[ScriptRunner]] = {".py": PythonRunner}


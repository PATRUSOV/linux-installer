from .core import ScriptRunner
from typing import Type, Dict

extention_handlers: Dict[str, Type[ScriptRunner]] = {".py": ScriptRunner}

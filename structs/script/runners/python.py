from core import ScriptRunner
from typing import Any
from subprocess import Popen
from pathlib import Path


class PythonRunner(ScriptRunner):
    def __init__(self, path: Path):
        super().__init__(path)

        # TODO: Добавить настройки интерпиритатора

    def run(self) -> Popen[Any]:
        # TODO: Добавить поддержку настроек интерпритатора

        script = Popen(["python", str(self.path)], cwd=self.cwd)

        return script

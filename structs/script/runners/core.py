from abc import abstractmethod, ABC
from pathlib import Path
from typing import Optional, Any
from utils.path import normalize_path, validate_path
import os
from subprocess import Popen


class ScriptRunner(ABC):
    """Вспомогательный абстрактный класс для класса Script.
    Отвечает за запуск скрипта. (не за валидацию и т.д.)"""

    def __init__(self, path: Path) -> None:
        # TODO: Написать доки

        # Путь к исполняемому файлус
        self.path = path

        # script working directory path
        self.cwd: Optional[Path] = None

        # TODO: Добавить дополнительные праметры и сетеры

        ## path to stdin log file
        # self.stdin: Optional[Path] = None

    def set_cwd(self, path: Path | str):
        path = normalize_path(path)
        validate_path(path, permissions=os.W_OK + os.R_OK + os.X_OK, is_file=False)

    @abstractmethod
    def run(self) -> Popen[Any]:
        pass

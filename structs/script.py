from core import Installable
from pathlib import Path
from utils import normalize_path, validate_path


class Script(Installable):
    """Структура отвечает за валидацию и запуск"""

    # TODO: Написать номарльные доки

    def __init__(self, path: str | Path) -> None:
        # TODO: Написать доки
        path = normalize_path(path)
        validate_path(path, permissions=os.X_OK, is_file=True)

        self.path = path

    def install(self) -> None:
        pass

from utils import backup, normalize_path, validate_path, copy
from pathlib import Path
from core import Installable
import os


class Config(Installable):
    # TODO: Написать доки
    def __init__(
        self, source: str | Path, path: str | Path, backup: bool = True
    ) -> None:
        # TODO: Написать доки
        source = normalize_path(source)
        validate_path(source, permissions=os.R_OK, is_file=None)
        self.source: Path = source

        path = normalize_path(path)
        validate_path(path, permissions=os.W_OK, is_file=False)
        self.path: Path = path

        self.backup: bool = backup

    def install(self) -> None:
        if self.backup:
            # TODO: ИСПРАВИТЬ ЭТУ ХРЕНЬ
            try:
                backup(self.path / self.source.name)
            except FileNotFoundError:
                pass

        try:
            copy(self.source, self.path)
        except Exception as e:
            raise RuntimeError(
                f"Не удалось скопировать файл {self.source}. Ошибка: {e}"
            )

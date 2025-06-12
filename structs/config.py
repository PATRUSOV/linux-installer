from utils.path import get_safe_path
from utils.file import backup, copy
from pathlib import Path
from core import Installable
import os


class Config(Installable):
    # TODO: Написать доки
    def __init__(
        self, source: str | Path, path: str | Path, backup: bool = True
    ) -> None:
        # TODO: Написать доки
        self.source: Path = get_safe_path(source, permissions=os.R_OK, is_file=None)

        self.path: Path = get_safe_path(path, permissions=os.W_OK, is_file=False)

        self.backup: bool = backup

    def install(self) -> None:
        if self.backup:
            try:
                backup(self.path / self.source.name)
            except Exception as e:
                print(f"При бекапе существующией конфигурации возникла ошибка: {e}")
                while True:
                    answer = input("Продолжать устнановку? (y, n)").upper()
                    if answer == "N":
                        raise RuntimeError(f"Программа завершена с ошибкой {e}")
                    elif answer == "Y":
                        break
        try:
            copy(self.source, self.path)
        except Exception as e:
            raise RuntimeError(
                f"Не удалось скопировать файл {self.source}. Ошибка: {e}"
            )

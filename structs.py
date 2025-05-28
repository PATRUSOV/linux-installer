from abc import abstractmethod
from typing import Tuple
from pathlib import Path
from utils import validate_path, normalize_path, copy, backup
import os


class Installable:
    @abstractmethod
    def install(self):
        pass

    # TODO: Добавить имя, то есть до переопределения это будет имя класса наследника


class Package(Installable):
    """Базовая структура для устаноки обектов реализующих интерфейс Installable"""

    def __init__(self, *packages: Installable) -> None:
        # TODO: Написать доки
        for package in packages:
            if not isinstance(package, Installable):
                raise TypeError(f"{package} не реализует интерфейс Installable")

        self._packages: Tuple[Installable, ...] = packages

    def install(self) -> None:
        for package in self._packages:
            package.install()


class Config(Installable):
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


class Script(Installable):
    """Структура отвечает за валидацию и запуск"""

    def __init__(self, path: str | Path) -> None:
        # TODO: Написать доки
        path = normalize_path(path)
        validate_path(path, permissions=os.X_OK, is_file=True)

        self.path = path

    def install(self) -> None:
        # TODO: Написать реализацию
        pass

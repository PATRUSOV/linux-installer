from abc import abstractmethod
from typing import List, Tuple
from pathlib import Path
from utils import validate_path, normalize_path, copy, backup
import os

from typing import Optional


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

        self._packages: Tuple[Installable] = packages

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
        validate_path(path, permissions=os.R_OK, is_file=False)
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
            raise RuntimeError(f"Не удалось скопироать файл {self.source}, ошибка: {e}")


class Script(Installable):
    """Структура отвечает за валидацию и запуск"""

    def __init__(self, path: str | Path) -> None:
        # TODO: Написать доки
        path = normalize_path(path)
        validate_path(path, permissions=os.X_OK, is_file=True)

        self.path = path

    def install(self) -> None:
        pass


'''
class Package(BasePackage):
    def __init__(
        self,
        name: str,
        packages: Optional[List[str]] = None,
        preinstall: Optional[str] = None,
        postinstall: Optional[str] = None,
        config: Optional[Config] = None,
    ) -> None:
        """
        Структура для конфигурации установки пакета

        Args:
        name : Имя структуры
        packages : Имена пакетов которые нужно установть
        preinstall : Путь к скрипту звпускающемуся до установки
        postinstall : Путь к путю запускающему посел установки
        """
        self.name: str = name

        self.packages: List = packages

        if preinstall is not None:
            self.preinstall: Path = utils.normalize_path(preinstall)
            utils.validate_path(self.preinstall, os.W_OK, True)

        if postinstall is not None:
            self.postinstall: Path = normalize_path(postinstall)
            validate_path(self.postinstall, os.W_OK, True)

        if config is not None:
            self.config: Config = config

        def _prepare_script(self, path: str) -> Optional[Path]:
            path = normalize_path()
'''

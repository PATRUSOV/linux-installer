from typing import List
from pathlib import Path
import utils


class Config:
    def __init__(self) -> None:
        """Путь к конфигу"""
        self.source: Path = None

        """Путь к папки в которую будет помещен конфиг"""
        self.path: Path = None

        """Бекапить ли существующий конфиг"""
        self.backup: bool = False

    def install(self) -> None:
        if self.backup:
            try:
                utils.backup(self.path / self.source.name)
            except FileNotFoundError:
                pass
        utils.copy(self.source, self.path)


class Package:
    _sub_classes = []

    @classmethod
    def preinstall(cls) -> None:
        """Метод выполняющийся до установки пакета и конфига"""
        pass

    @classmethod
    def postinstall(cls) -> None:
        """Метод который выполняеться после завершения установки"""
        pass

    def __init_subclass__(cls) -> None:
        """Структура с настройкой файла конфигурации пакета"""
        cls.config = Config()

        """Список пакетов для установки"""
        cls.packages = []

        Package._sub_classes.append(cls)

        super().__init_subclass__()

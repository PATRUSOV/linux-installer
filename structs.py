from typing import List
from pathlib import Path
import utils
# TODO: Добавить валидацию путям


class Config:
    # def __init__(self) -> None:
    # """Путь к конфигу"""
    # self.source: Path = None
    #
    # """Путь к папки в которую будет помещен конфиг"""
    # self.path: Path = None
    #
    # """Бекапить ли существующий конфиг"""
    # self.backup: bool = False

    def __init__(self, config_dict: dict):
        self.source = Path(config_dict.get("source"))
        self.path = Path(config_dict.get("path"))
        # FIXME: Разобраться с преобразованием
        self.backup = True if config_dict.get("backup") in ["True", "Yes"] else False

    # TODO: Проверка на None
    def install(self) -> None:
        if self.backup:
            try:
                utils.backup(self.path / self.source.name)
            except FileNotFoundError:
                pass
        utils.copy(self.source, self.path)


class Package:
    # def __init__(
    #
    # self,
    # name: str,
    # packages: List[str] = None,
    # preinstall: Path = None,
    # postinstall: Path = None,
    # ) -> None:
    # """
    # Структура для конфигурации установки пакета
    #
    # Args:
    # name : Имя структуры
    # packages : Имена пакетов которые нужно установть
    # preinstall : Путь к скрипту звпускающемуся до установки
    # postinstall : Путь к путю запускающему посел установки
    # """
    # self.name: str = name
    # self.packages: List[str] = packages
    # self.preinstall: Path = preinstall
    # self.postinstall: Path = postinstall
    # self.config: Config = config

    # FIXME: Починить словари и разобраться с типами
    def __init__(self, package_dict: dict[str, str]) -> None:
        self.name: str = package_dict.get("name")
        self.packages: List[str] = package_dict.get("packages")
        self.preinstall: Path = Path(package_dict.get("preinstall"))
        self.postinstall: Path = Path(package_dict.get("postinstall"))
        self.config: Config = Config(package_dict.get("config"))

        # Проверка на некорректные поля в конфигурации
        for attr in package_dict:
            if attr not in self.__dict__.keys():
                raise ValueError(f"Поле {attr} несуществует, исправьте конфиг.")

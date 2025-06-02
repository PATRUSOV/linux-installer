from pathlib import Path
import os
from typing import Optional


class SafePath:
    # TODO: Доки
    def __init__(
        self,
        path: Path | str,
        *,
        permissions: int,
        is_file: Optional[bool] = None,
    ):
        # TODO: Доки
        # TODO: Добавить флаг strict, то есть нужна ли валидаци или нет
        self._path = self._normalize(path)
        self._permissions = permissions
        self._is_file = is_file
        self._validate()

    def _normalize(self, path: Path | str) -> Path:
        """Разворачивает путь"""

        path = self.__cast_to_path(path)
        path = self.__replace_user(path)
        path = self.__replace_environment_variables(path)
        path = self.__make_absolute(path)

        return path

    def __cast_to_path(self, path: Path | str) -> Path:
        """Приведение к Path"""

        if isinstance(path, str):
            path = Path(path)

        if not isinstance(path, Path):
            raise TypeError(f"Ожидался str или Path, но получен {type(path).__name__}")

        return path

    def __replace_user(self, path: Path) -> Path:
        """Замена ~/ в путе"""
        return path.expanduser()

    def __replace_environment_variables(self, path: Path) -> Path:
        """Замена переменных среды на их значения"""
        # TODO: дописать переменные среды
        # для написния можно использовать regex но в силу незнаия регулярок во избежании говнокода просто навайдкожy функуию заменты, ЛАДНО ВЫУЧУ regex
        path = Path(str(path).replace("$HOME", str(path.home())))

        return path

    def __make_absolute(self, path: Path) -> Path:
        """Разворачивание пути с учетом символических ссылок"""
        return path.resolve(strict=False)

    def _validate(self) -> None:
        """Проверяет путь по критериям из конструктора"""

        self.__check_exists()
        self.__check_permissions()
        self.__check_is_file()

    def __check_exists(self) -> None:
        """Проверка на существование"""
        path = self._path

        if not path.exists():
            raise FileNotFoundError(f"{path} - не существует")

    def __check_permissions(self) -> None:
        """Проверка доступа"""
        path = self._path
        permissions = self._permissions

        if not os.access(path, permissions):
            raise PermissionError(
                f"Не удалось получить доступ к {path} - не хватает прав."
            )

    def __check_is_file(self) -> None:
        """Проверка на файл/дирректорию"""
        path = self._path
        is_file = self._is_file

        if is_file is not None:
            if path.is_file() != is_file:
                raise TypeError(
                    f"{path} не являеться {'файлом' if is_file else 'директорией'}"
                )

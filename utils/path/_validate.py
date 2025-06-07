from pathlib import Path
from utils.func import not_none_arg
import os
from typing import Optional


def validate_path(
    path: Path,
    *,
    silent: bool,
    permissions: Optional[int],
    is_file: Optional[bool],
) -> None:
    """Проверяет путь"""
    # TODO: Добавить описание аргментов в доки

    if not silent:
        _check_exists(path)
        _check_permissions(path, permissions)
        _check_is_file(path, is_file)


def _check_exists(path: Path) -> None:
    """Проверка на существование"""

    if not path.exists():
        raise FileNotFoundError(f"{path} - не существует")


@not_none_arg("permissions")
def _check_permissions(path: Path, permissions: int) -> None:
    """Проверка доступа"""

    if not os.access(path, permissions):
        raise PermissionError(f"Не удалось получить доступ к {path} - не хватает прав.")


@not_none_arg("is_file")
def _check_is_file(path: Path, is_file: bool) -> None:
    """Проверка на файл/дирректорию"""
    if path.is_file() != is_file:
        raise TypeError(f"{path} не являеться {'файлом' if is_file else 'директорией'}")

from pathlib import Path
import os
from utils.path import get_safe_path

# ПРИ ПЕРЕИМЕНОВАНИИ ВО ИЗБЕЖАНИИ БАГОВ НУЖЕН АБСОЛЮТНЫЙ ПУТЬ, get_safe_path() это обеспечивает


def backup(path: Path | str, raw: bool = False) -> None:
    """Добавляет суффик .bak к имени файла"""
    if not raw:
        path = get_safe_path(path, permissions=os.W_OK)

    if path.suffix == ".bak":
        raise ValueError(f"{path.name} уже являеться бекапом")

    path = path.rename(str(path) + ".bak")


def ubackup(path: Path | str, raw: bool = False) -> None:
    """Убирает суффикс .bak у имени файлы"""
    if not raw:
        path = get_safe_path(path, permissions=os.W_OK)

    if path.suffix == ".bak":
        path = path.rename(str(path)[0:-4])
    else:
        raise ValueError(f"{path.name} не являеться бекапом")

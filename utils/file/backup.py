from pathlib import Path
import os
from utils.path import get_safe_path

# ПРИ ПЕРЕИМЕНОВАНИИ ВО ИЗБЕЖАНИИ БАГОВ НУЖЕН АБСОЛЮТНЫЙ ПУТЬ, get_safe_path() это обеспечивает
# FIXME: УБрать валидацию из backup и ubackup


def backup(path: Path | str) -> None:
    # TODO: Добавить доки
    path = get_safe_path(path, permissions=os.W_OK)

    if path.suffix == ".bak":
        raise ValueError(f"{path.name} уже являеться бекапом")

    path = path.rename(str(path) + ".bak")


def ubackup(path: Path | str) -> None:
    # TODO: Добавить доки
    path = get_safe_path(path, permissions=os.W_OK)

    if path.suffix == ".bak":
        path = path.rename(str(path)[0:-4])
    else:
        raise ValueError(f"{path.name} не являеться бекапом")

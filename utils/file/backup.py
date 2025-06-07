from pathlib import Path
import os
from utils.path import get_safe_path


def backup(path: Path | str) -> None:
    path = get_safe_path(path, permissions=os.W_OK)

    if path.suffix == ".bak":
        raise ValueError(f"{path.name} уже являеться бекапом")

    path = path.with_name(path.name + ".bak")


def ubackup(path: Path | str) -> None:
    path = get_safe_path(path, permissions=os.W_OK)

    if path.suffix == ".bak":
        path = path.with_name(path.stem)
    else:
        raise ValueError(f"{path.name} не являеться бекапом")

from pathlib import Path
from utils.path import normalize_path, validate_path
import os


def backup(path: Path | str) -> None:
    # validation
    path = normalize_path(path)
    validate_path(path, permissions=os.W_OK)

    if path.suffix == ".bak":
        raise ValueError(f"{path.name} уже являеться бекапом")

    path = path.with_name(path.name + ".bak")


def ubackup(path: Path | str) -> None:
    # validation
    path = normalize_path(path)
    validate_path(path, permissions=os.W_OK)

    if path.suffix == ".bak":
        path = path.with_name(path.stem)
    else:
        raise ValueError(f"{path.name} не являеться бекапа отсутвует .bak")

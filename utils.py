from pathlib import Path
import shutil


def backup(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Файл {path} не существует")
    elif path.suffix == ".bak":
        return

    path.rename(path.name + ".bak")


def ubackup(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Файл {path} не существует")

    path.rename(path.stem)


def copy(src: Path, dst: Path):
    if src.is_dir():
        shutil.copytree(src, dst)
    elif src.is_file():
        shutil.copy(src, dst)
    else:
        raise ValueError(f"{src} не файл и не директория")

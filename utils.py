from pathlib import Path
import shutil
import os

#TODO: Внедрить normalize_path и validate_path в бекапы (добавить валидацию в общем)

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
        raise ValueError(f"{src} не являеться ни файлом и не директориq")


def normalize_path(path: str | Path) -> Path:
    if isinstance(path, str):
        path = Path(path)

    if not isinstance(path, Path):
        raise TypeError(f"{path} не являеться не str не Path")

    path = path.expanduser()

    path = Path(str(path).replace("$HOME", Path.home()))

    path = path.resolve(strict=False)

    return path


def validate_path(path: Path, permissions: int, is_file: bool | None = None) -> None:
    if not isinstance(path, Path):
        raise TypeError(f"Функция не работает с типом {type(path)}")
    if not path.exists():
        raise FileNotFoundError(f"{path} - не существует")

    if not os.access(path, permissions):
        raise PermissionError(f"Не удалось получить доступ к {path} - не хватает прав.")

    if is_file is not None:
        if path.is_file() != is_file:
            raise TypeError(f"{path} не являеться {"файлом" if is_file else "директорией"})

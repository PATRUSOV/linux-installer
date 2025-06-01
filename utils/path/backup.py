from pathlib import (
    Path,
)  # TODO: Внедрить normalize_path и validate_path в бекапы (добавить валидацию в общем)


def backup(path: Path) -> None:
    # TODO: Добавить silent
    if not path.exists():
        raise FileNotFoundError(f"Файл {path} не существует")
    elif path.suffix == ".bak":
        return

    path.rename(path.name + ".bak")


def ubackup(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Файл {path} не существует")

    path.rename(path.stem)

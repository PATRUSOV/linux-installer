from pathlib import Path
import os


def validate_path(path: Path, permissions: int, is_file: bool | None = None) -> None:
    if not isinstance(path, Path):
        raise TypeError(f"Функция не работает с типом {type(path)}")
    if not path.exists():
        raise FileNotFoundError(f"{path} - не существует")

    if not os.access(path, permissions):
        raise PermissionError(f"Не удалось получить доступ к {path} - не хватает прав.")

    if is_file is not None:
        if path.is_file() != is_file:
            raise TypeError(
                f"{path} не являеться {'файлом' if is_file else 'директорией'}"
            )

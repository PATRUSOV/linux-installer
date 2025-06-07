from pathlib import Path
import os
import re


def normalize_path(path: Path | str) -> Path:
    """Разворачивает путь"""

    path = _cast_to_path(path)
    path = _replace_user(path)
    path = _replace_environment_variables(path)
    path = _make_absolute(path)

    return path


def _cast_to_path(path: Path | str) -> Path:
    """Приведение к Path"""

    if isinstance(path, str):
        path = Path(path)

    if not isinstance(path, Path):
        raise TypeError(f"Ожидался str или Path, но получен {type(path).__name__}")

    return path


def _replace_user(path: Path) -> Path:
    """Замена ~/ в путе"""
    return path.expanduser()


def _replace_environment_variables(path: Path) -> Path:
    """Замена переменных среды на их значения"""
    str_path = str(path)

    def repl(match_obj: re.Match) -> str:
        name = match_obj.group(1) if match_obj.group(1) else match_obj.group(2)
        replaced_name = os.environ.get(name)

        if replaced_name is None:
            raise KeyError(f"Не найдена переменная окружения {name}")

        return replaced_name

    _REG = re.compile(r"\$([A-Za-z_][A-Za-z0-9_]*)|\${([A-Za-z_][A-Za-z0-9_]*)}")

    replaced_str_path = _REG.sub(repl, str_path)

    return Path(replaced_str_path)


def _make_absolute(path: Path) -> Path:
    """Разворачивание пути с учетом символических ссылок"""
    return path.resolve(strict=False)

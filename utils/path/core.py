from pathlib import Path
from _validate import validate_path
from _normalize import normalize_path
from typing import Optional


def get_safe_path(
    path: str | Path,
    *,
    silent: bool = False,
    permissions: Optional[int] = None,
    is_file: Optional[bool] = None,
) -> Path:
    """Нормализует и проверяет путь"""

    path = normalize_path(path)
    validate_path(path, silent=silent, permissions=permissions, is_file=is_file)

    return path

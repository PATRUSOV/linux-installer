from pathlib import Path
import os


def normalize_path(path: str | Path) -> Path:
    if isinstance(path, str):
        path = Path(path)

    if not isinstance(path, Path):
        raise TypeError(f"{path} не являеться не str не Path")

    path = path.expanduser()

    env = os.environ

    # TODO: дописать переменные среды

    path = Path(str(path).replace("$HOME", str(path.home())))
    # TODO: добавить поддержку переменных среды

    path = path.resolve(strict=False)

    return path

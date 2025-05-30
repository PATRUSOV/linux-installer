from core import Installable
from typing import Tuple


class Package(Installable):
    """Базовая структура для устаноки обектов реализующих интерфейс Installable"""

    # TODO: Написать нормальные доки

    def __init__(self, *packages: Installable) -> None:
        # TODO: Написать доки
        for package in packages:
            if not isinstance(package, Installable):
                raise TypeError(f"{package} не реализует интерфейс Installable")

        self._packages: Tuple[Installable, ...] = packages

    def install(self) -> None:
        for package in self._packages:
            package.install()

from abc import abstractmethod, ABC


class Installable(ABC):
    # TODO: Написать доки
    @abstractmethod
    def install(self):
        pass

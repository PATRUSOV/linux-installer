from ABC import abstractmethod


class Installable:
    # TODO: Написать доки
    @abstractmethod
    def install(self):
        pass

    # TODO: Добавить имя, то есть до переопределения это будет имя класса наследника

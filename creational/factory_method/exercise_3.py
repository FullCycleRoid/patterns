from abc import ABC, abstractmethod
from typing import Dict, Callable


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    def getInfo(self) -> str:
        return str(self.__class__.__name__) + ' ' + self.name


class Lion(Animal):
    ...


class Tiger(Animal):
    ...


class Leopard(Animal):
    ...


class Gorilla(Animal):
    ...


class Orangutan(Animal):
    ...


class Chimpanzee(Animal):
    ...


class AnimalCreator(ABC):
    @abstractmethod
    def createAnimal(self, ind: int, name: str) -> Animal: ...

    def getZoo(self, inds, names):
        zoo = []
        for i in range(len(inds)):
            zoo.append(self.createAnimal(inds[i], names[i]))
        return zoo


class CatCreator(AnimalCreator):
    cat_types: Dict[int, Callable] = {
        0: Lion,
        1: Tiger,
        2: Leopard
    }

    def createAnimal(self, ind: int, name: str) -> Animal:
        if ind in self.cat_types:
            return self.cat_types[ind](name)


class ApeCreator(AnimalCreator):
    ape_types: Dict[int, Callable] = {
        0: Gorilla,
        1: Orangutan,
        2: Chimpanzee
    }

    def createAnimal(self, ind: int, name: str) -> Animal:
        return self.ape_types[ind](name)

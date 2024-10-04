from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    def __init__(self, info: int):
        self.info: str = str(info)

    @abstractmethod
    def A(self):
        pass

    def getInfo(self):
        return self.info


class ProductA1(AbstractProductA):
    def A(self) -> None:
        self.info = str(int(self.info) * 2)


class ProductA2(AbstractProductA):
    def A(self) -> None:
        self.info = self.info * 2


class AbstractProductB(ABC):
    def __init__(self, info: int):
        self.info: str = str(info)

    @abstractmethod
    def B(self, objA):
        pass

    def getInfo(self):
        return self.info


class ProductB1(AbstractProductB):
    def B(self, objA: AbstractProductA):
        self.info = str(int(self.info) + int(objA.info))


class ProductB2(AbstractProductB):
    def B(self, objA: AbstractProductA):
        self.info = self.info + objA.info


class AbstractFactory(ABC):
    @abstractmethod
    def createProductA(self, info) -> AbstractProductA:
        pass

    @abstractmethod
    def createProductB(self, info) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    def createProductA(self, info) -> AbstractProductA:
        return ProductA1(info)

    def createProductB(self, info) -> AbstractProductB:
        return ProductB1(info)


class ConcreteFactory2(AbstractFactory):
    def createProductA(self, info) -> AbstractProductA:
        return ProductA2(info)

    def createProductB(self, info) -> AbstractProductB:
        return ProductB2(info)

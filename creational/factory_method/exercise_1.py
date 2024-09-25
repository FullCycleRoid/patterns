from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def getInfo(self): pass

    @abstractmethod
    def transform(self): pass


class ConcreteProduct1(Product):
    def __init__(self, info):
        self.info = info.lower()

    def getInfo(self):
        return self.info

    def transform(self) -> None:
        t = [c for c in self.info if c != ' ']
        self.info = ' '.join(t)


class ConcreteProduct2(Product):
    def __init__(self, info):
        self.info = info.upper()

    def getInfo(self):
        return self.info

    def transform(self) -> None:
        t = [c for c in self.info if c != '*' and c != ' ']
        self.info = '**'.join(t)


class Creator:
    def factoryMethod(self, info) -> Product:
        pass

    def anOperation(self, info) -> str:
        p = self.factoryMethod(info)
        p.transform()
        p.transform()
        return p.getInfo()


class ConcreteCreator1(Creator):
    def factoryMethod(self, info) -> ConcreteProduct1:
        return ConcreteProduct1(info)


class ConcreteCreator2(Creator):
    def factoryMethod(self, info) -> ConcreteProduct2:
        return ConcreteProduct2(info)

from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def algorithmInterface(self, info) -> str:
        pass


class ConcreteStrategyA(Strategy):
    def algorithmInterface(self, info) -> str:
        return info + "A"


class ConcreteStrategyB(Strategy):
    def algorithmInterface(self, info) -> str:
        return info + "B"


class ConcreteStrategyC(Strategy):
    def algorithmInterface(self, info) -> str:
        return info + "C"


class Context(ABC):
    __st: Strategy

    @abstractmethod
    def setStrategy(self, st):
        self.__st = st


    @abstractmethod
    def ContextInterface(self):
        pass


class Context1(Context):
    def setStrategy(self, st):
        self.__st = st


    def ContextInterface(self):
        return self.__st.algorithmInterface('1')


class Context2(Context):
    def setStrategy(self, st):
        self.__st = st

    def ContextInterface(self):
        return self.__st.algorithmInterface('2')

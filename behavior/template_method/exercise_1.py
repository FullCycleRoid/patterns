from abc import abstractmethod


class AbstractClass:
    def BasicOperation1(self):
        return "Boil water"

    @abstractmethod
    def PrimitiveOperation(self):
        return ""

    def BasicOperation2(self):
        return "=Pour into a cup"

    def _HookOperation(self):
        return ""

    def templateMethod(self):
        drink = ''
        drink += self.BasicOperation1()
        drink += self.PrimitiveOperation()
        drink += self.BasicOperation2()
        drink += self._HookOperation()
        return drink


class ConcreteClass1(AbstractClass):

    def PrimitiveOperation(self):
        return "=Brew tea"


class ConcreteClass2(AbstractClass):
    def PrimitiveOperation(self):
        return "=Brew coffee"


class ConcreteClass3(ConcreteClass1):
    def _HookOperation(self):
        return "=Add sugar and lemon»"


class ConcreteClass4(ConcreteClass2):
    def _HookOperation(self):
        return "=Add sugar and milk"

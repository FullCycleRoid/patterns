class ConcreteStrategyA:
    def algorithmInterface(self, info):
        pass
        # Implement the method

# Implement the ConcreteStrategyB
#   and ConcreteStrategyC classes

class Context:
    def setStrategy(self, st):
        self.__st = st

# Implement the Context1 and Context2 descendant classes
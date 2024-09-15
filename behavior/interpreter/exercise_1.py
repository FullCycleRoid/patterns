class Context:
    pass
    # Add the constructor, required fields and methods

class TermConst:
    def __init__(self, value):
        pass
        # Implement the "constructor"

    def interpretA(self, ct):
        pass
        # Implement the method

    def interpretB(self, ct):
        pass
        # Implement the method

    def interpretC(self, ct):
        pass
        # Implement the method

# Implement the TermVar and NontermMath classes

class Client:
    def __init__(self, expr, ct):
        self.__expr = expr
        self.__ct = ct

    def interpretA(self):
        return self.__expr.interpretA(self.__ct)

    def interpretB(self):
        return self.__expr.interpretB(self.__ct)

    def interpretC(self):
        return self.__expr.interpretC(self.__ct)
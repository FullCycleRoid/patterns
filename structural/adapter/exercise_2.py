class Adaptee:
    # Do not change the implementation of the class
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def getAll(self):
        return self.__a, self.__b

    def specificRequest(self):
        return self.__a * self.__b


class ConcreteTarget:
    def __init__(self, a, b):
        pass
        # Implement the "constructor"

    def getA(self):
        pass
        # Implement the method

    def getB(self):
        pass
        # Implement the method

    def request(self):
        pass
        # Implement the method

# Implement the Adapter class;
#   the Adapter class must be
#   a descendant of the Adaptee class
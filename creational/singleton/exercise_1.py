class BaseClass:
    def __init__(self):
        self.__data = 0

    def incData(self, increment):
        self.__data += increment

    def getData(self):
        return self.__data

class Singleton(BaseClass):
    __private_key = object()
    __uniqueInstance = None

    def __init__(self, private_key):
        if private_key != self.__private_key:
            raise Exception("Error")
        super().__init__()

    # Complete the implementation of the class

class Doubleton(BaseClass):
    __private_key = object()
    __instances = [None] * 2

    def __init__(self, private_key):
        if private_key != self.__private_key:
            raise Exception("Error")
        super().__init__()

    # Complete the implementation of the class

class Tenton(BaseClass):
    __private_key = object()
    __instances = [None] * 10

    def __init__(self, private_key):
        if private_key != self.__private_key:
            raise Exception("Error")
        super().__init__()

    # Complete the implementation of the class
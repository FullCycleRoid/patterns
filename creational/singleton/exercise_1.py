class METASingleton(type):
    __uniqueInstance = None

    def __call__(cls, *args, **kwargs):
        if cls != cls.__uniqueInstance:
            cls.__uniqueInstance = super(METASingleton, cls).__call__(*args, **kwargs)
        return cls.__uniqueInstance[cls]


class BaseClass:
    def __init__(self):
        self.__data = 0

    def incData(self, increment):
        self.__data += increment

    def getData(self):
        return self.__data


class Singleton(BaseClass, metaclass=METASingleton):
    __private_key = object()

    def __init__(self, private_key):
        if private_key != self.__private_key:
            raise Exception("Error")
        super().__init__()


class METADoubleton(type):
    __instances = [None] * 2

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(METADoubleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Doubleton(BaseClass, metaclass=METADoubleton):
    __private_key = object()
    __instances = [None] * 2

    def __init__(self, private_key):
        if private_key != self.__private_key:
            raise Exception("Error")
        super().__init__()


class METATenton(type):
    __instances = [None] * 10

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(METATenton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Tenton(BaseClass, metaclass=METATenton):
    __private_key = object()
    __instances = [None] * 10

    def __init__(self, private_key):
        if private_key != self.__private_key:
            raise Exception("Error")
        super().__init__()

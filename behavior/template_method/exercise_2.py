from abc import abstractmethod
from typing import Sequence


class AbstractComparable:

    @abstractmethod
    def compareTo(self, other):
        pass

    @staticmethod
    def indexMax(comp: Sequence['AbstractComparable']) -> int:
        pass

    @staticmethod
    def indexMin(comp: Sequence['AbstractComparable']) -> int:
        pass

    @staticmethod
    def lastIndexMin(comp: Sequence['AbstractComparable']) -> int:
        pass

    @staticmethod
    def lastIndexMax(comp: Sequence['AbstractComparable']) -> int:
        pass


class NumberComparable(AbstractComparable):
    def __init__(self, data: int | str):
        if not data.isdigit():
            data = 0

        self.key: int = int(data)

    def compareTo(self, other):
        pass


class LastNumberComparable(AbstractComparable):
    def __init__(self, data: int | str):
        self.key = len(data)

    def compareTo(self, other):
        pass


class TextComparable(AbstractComparable):
    def __init__(self, data: int | str):
        self.key = str(data)

    def compareTo(self, other):
        pass
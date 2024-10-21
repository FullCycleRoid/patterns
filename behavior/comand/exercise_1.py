from abc import ABC, abstractmethod


class AbstractCommand(ABC):

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommandA(AbstractCommand):
    def __init__(self, recv: 'ReceiverA'):
        self._recv = recv

    def execute(self):
        self._recv.ActionA()


class ConcreteCommandB(AbstractCommand):
    def __init__(self, recv: 'ReceiverB'):
        self._recv = recv

    def execute(self):
        self._recv.ActionB()


class ReceiverA:
    def __init__(self, cli: 'Client', info: str):
        self.info = info
        self._cli = cli

    def ActionA(self):
        self._cli.AddLeft(self.info)


class ReceiverB:
    def __init__(self, cli: 'Client', info: str):
        self.info = info
        self._cli = cli

    def ActionB(self):
        self._cli.AddRight(self.info)


class Invoker:
    def __init__(self, cmd):
        self.__cmd = cmd

    def invoke(self):
        self.__cmd.execute()


class Client:
    def __init__(self):
        self._info = ''

    def GetInfo(self):
        return self._info

    def AddLeft(self, newInfo: str):
        self._info = newInfo + self._info

    def AddRight(self, newInfo: str):
        self._info = self._info + newInfo

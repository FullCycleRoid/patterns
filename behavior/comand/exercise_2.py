from abc import ABC, abstractmethod
from typing import List


class ReceiverA:
    @staticmethod
    def actionA():
        print("+A")

    @staticmethod
    def undoActionA():
        print("-A")


class ReceiverB:
    @staticmethod
    def actionB():
        print("+B")

    @staticmethod
    def undoActionB():
        print("-B")


class ReceiverC:
    @staticmethod
    def actionC():
        print("+C")

    @staticmethod
    def undoActionC():
        print("-C")


class AbstractCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unexecute(self):
        pass


class CommandA(AbstractCommand):
    def execute(self):
        ReceiverA().actionA()

    def unexecute(self):
        ReceiverA().undoActionA()


class CommandB(AbstractCommand):
    def execute(self):
        ReceiverB().actionB()

    def unexecute(self):
        ReceiverB().undoActionB()


class CommandC(AbstractCommand):
    def execute(self):
        ReceiverC().actionC()

    def unexecute(self):
        ReceiverC().undoActionC()


class MacroCommand(AbstractCommand):
    def __init__(self, cmds: List[AbstractCommand]):
        if len(cmds) > 5:
            raise ValueError("Too many commands")

        self.cmds = cmds

    def execute(self):
        for cmd in self.cmds:
            cmd.execute()

    def unexecute(self):
        for cmd in self.cmds[::-1]:
            cmd.unexecute()


class Menu:
    def __init__(
            self,
            cmd1: AbstractCommand,
            cmd2: AbstractCommand,
    ):
        macro = MacroCommand([cmd1, cmd2,])
        self.menuCmds = [cmd1, cmd2, macro]
        self.lastCmds = []

    def invoke(self, cmdIndex):
        curr_cmd = self.menuCmds[cmdIndex]
        curr_cmd.execute()
        self.lastCmds.append(curr_cmd)

    def undo(self, count):
        length = len(self.lastCmds)
        for cmd in self.lastCmds[length-count-1:]:
            cmd.undo()

    def redo(self, count):
        length = len(self.lastCmds)
        if length < count:
            redo_commands = self.lastCmds
        else:
            redo_commands = self.lastCmds[length - count - 1:]

        for cmd in redo_commands:
            cmd.execute()

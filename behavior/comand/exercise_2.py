class ReceiverA:
    @staticmethod
    def actionA():
        put("+A")

    @staticmethod
    def undoActionA():
        put("-A")


class ReceiverB:
    @staticmethod
    def actionB():
        put("+B")

    @staticmethod
    def undoActionB():
        put("-B")


class ReceiverC:
    @staticmethod
    def actionC():
        put("+C")

    @staticmethod
    def undoActionC():
        put("-C")

class CommandA:
    def execute(self):
        pass
        # Implement the method

    def unexecute(self):
        pass
        # Implement the method

# Implement the CommandB, CommandC
# and MacroCommand classes

class Menu:
    def __init__(self, cmd1, cmd2):
        pass
        # Implement the "constructor"

    def invoke(self, cmdIndex):
        pass
        # Implement the method

    def undo(self, count):
        pass
        # Implement the method

    def redo(self, count):
        pass
        # Implement the method
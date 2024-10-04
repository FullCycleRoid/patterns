from abc import abstractmethod


class AbstractButton:
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def getControl(self):
        pass


class Button1(AbstractButton):

    def getControl(self):
        return "[" + self.text.upper() + "]"


class Button2(AbstractButton):
    def getControl(self):
        return "<" + self.text.lower() + ">"


class AbstractLabel:
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def getControl(self):
        pass


class Label1(AbstractLabel):
    def getControl(self):
        return "=" + self.text.upper() + "="
        # Implement the method


class Label2(AbstractLabel):
    def getControl(self):
        return "\"" + self.text.lower() + "\""


class ControlFactory:
    @abstractmethod
    def createButton(self, text):
        return Button1(text)

    @abstractmethod
    def createLabel(self, text):
        return Label1(text)


class Factory1(ControlFactory):
    def createButton(self, text):
        return Button1(text)

    def createLabel(self, text):
        return Label1(text)


class Factory2(ControlFactory):
    def createButton(self, text):
        return Button2(text)

    def createLabel(self, text):
        return Label2(text)


class Client:
    def __init__(self, f: ControlFactory):
        self.factory = f
        self.controls = []
        self.result = []

    def addButton(self, text):
        b = self.factory.createButton(text)
        self.controls.append(b)

    def addLabel(self, text):
        l = self.factory.createLabel(text)
        self.controls.append(l)

    def getControls(self):
        for c in self.controls:
            r = c.getControl()
            self.result.append(r)

        return " ".join(self.result)

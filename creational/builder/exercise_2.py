class AbstractBuilder:
    def __init__(self):
        self._product = ''

    def buildStart(self, c):
        self._product += c.lower()

    def buildFirstChar(self, c):
        self._product += c.upper()

    def buildNextChar(self, c):
        self._product += c.lower()

    def buildDelim(self):
        pass

    def getResult(self):
        return self._product


class BuilderPascal(AbstractBuilder):

    def buildStart(self, c):
        self._product += c.lower()

    def buildFirstChar(self, c):
        self._product += c.upper()

    def buildNextChar(self, c):
        self._product += c.lower()

    def buildDelim(self):
        pass


class BuilderPython(AbstractBuilder):
    def buildStart(self, c):
        self._product += c.lower()

    def buildFirstChar(self, c):
        self._product += c.lower()

    def buildNextChar(self, c):
        self._product += c.lower()

    def buildDelim(self):
        self._product += '_'


class BuilderC(AbstractBuilder):
    def buildStart(self, c):
        self._product += c.lower()

    def buildFirstChar(self, c):
        self._product += c.lower()

    def buildNextChar(self, c):
        self._product += c.lower()

    def buildDelim(self):
        pass


class Director:
    def __init__(self, b):
        self.__b = b

    def getResult(self):
        return self.__b.getResult()

    def construct(self, template: str):
        template = [c for c in template.strip()]
        for i, c in enumerate(template):
            if i == 0:
                self.__b.buildStart(template[i])
            elif c == ' ':
                self.__b.buildDelim()
            elif c.isalpha() and template[i-1] == ' ':
                self.__b.buildFirstChar(template[i])
            else:
                self.__b.buildNextChar(template[i])

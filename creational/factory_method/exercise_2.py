class ConcreteProduct1:
    def __init__(self, info):
        self.info = info.lower()

    def getInfo(self):
        return self.info

    def transform(self) -> None:
        t = [c for c in self.info if c != '*' and c != ' ']
        self.info = '*'.join(t)


class ConcreteProduct2(ConcreteProduct1):
    def __init__(self, info):
        super().__init__(info)
        self.info = self.info.capitalize()

    def getInfo(self):
        return self.info

    def transform(self) -> None:
        if not self.info.startswith("=="):
            super().transform()
            self.info = "==" + self.info + "=="


class ConcreteCreator1:
    def factoryMethod(self, info) -> ConcreteProduct1:
        return ConcreteProduct1(info)

    def anOperation(self, info) -> str:
        p = self.factoryMethod(info)
        p.transform()
        p.transform()
        return p.getInfo()


class ConcreteCreator2(ConcreteCreator1):
    def factoryMethod(self, info) -> ConcreteProduct2:
        return ConcreteProduct2(info)

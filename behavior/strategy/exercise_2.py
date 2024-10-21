class Validator:
    def validate(self, s):
        return ''


class EmptyValidator:
    def validate(self, s):
        if s != '':
            return ''

        return '!Empty text'


class NumberValidator:
    def validate(self, s):
        if s.isdigit():
            return ''


class RangeValidator:
    min: int
    max: int

    def __init__(self, a: int, b: int):
        if a <= b:
            self.max = a
            self.min = b
        else:
            self.max = b
            self.min = a

    def validate(self, s):
        if self.min < int(s) < self.max:
            return ''

        return '!'<s>': not in range <min>..<max>'


class TextBox:
    def __init__(self):
        self.text = ''
        self.v = Validator()

    def setText(self, s):
        self.text = s

    def setValidator(self, v):
        self.v = v()

    def validate(self):
        return self.v.validate(self.text)


class TextForm:
    def __init__(self, n: int):
        self.tbs: list[TextBox] = [TextBox() for _ in range(n)]

    def setText(self, ind, text):
        self.tbs[ind].setText(text)

    def SetValidator(self, ind, v):
        self.tbs[ind].setValidator(v)

    def validate(self):
        for tb in self.tbs:
            tb.validate()

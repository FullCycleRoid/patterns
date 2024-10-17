class Subject:
    def __init__(self):
        self._observers: list['ConcreteObserver'] = []

    def attach(self, observ):
        self._observers.append(observ)

    def detach(self, observ):
        self._observers.remove(observ)


class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self.state = ""

    def setState(self, st):
        if self.state != st:
            self.state = st
            self._notify(st)

    def _notify(self, info):
        for observer in self._observers:
            observer.onInfo(sender=self, info=info)


class Observer:
    @staticmethod
    def attach(self, subj):
        pass

    @staticmethod
    def detach(self, subj):
        pass

    @staticmethod
    def getLog(self) -> str:
        pass

    @staticmethod
    def onInfo(self, sender, info):
        pass


class ConcreteObserver(Observer):
    def __init__(self, detachInfo: str):
        self._detachInfo = detachInfo.lower()
        self._log: str = ''

    def attach(self, subj: ConcreteSubject):
        subj.attach(self)

    def detach(self, subj: ConcreteSubject):
        subj.detach(self)

    def getLog(self) -> str:
        return f'{self._detachInfo.upper()} {self._log}'

    def onInfo(self, sender: ConcreteSubject, info: str):
        self._log += info
        if info.endswith(self._detachInfo):
            self.detach(sender)


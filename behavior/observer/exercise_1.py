from abc import ABC, abstractmethod


class Subject:
    def __init__(self):
        self._observers: list['AbstractObserver'] = []

    def attach(self, observ: 'AbstractObserver'):
        self._observers.append(observ)

    def detach(self, observ: 'AbstractObserver'):
        self._observers.remove(observ)

    def _notify(self):
        for observer in self._observers:
            observer.update()


class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self.state: str = ' '

    def setState(self, st: str):
        if self.state != st:
            self.state = st
            self._notify()

    def getState(self) -> str:
        return self.state


class AbstractObserver(ABC):

    @abstractmethod
    def attach(self):
        pass

    @abstractmethod
    def detach(self):
        pass

    @abstractmethod
    def getLog(self):
        pass

    @abstractmethod
    def update(self):
        pass


class ConcreteObserver(AbstractObserver):
    def __init__(self, subj: ConcreteSubject, detachInfo):
        self.subj: ConcreteSubject = subj
        self.detachInfo: str = detachInfo
        self.log: str = ''

    def attach(self):
        self.subj.attach(self)

    def detach(self):
        self.subj.detach(self)

    def getLog(self) -> str:
        return self.log

    def update(self) -> None:
        state = self.subj.getState()
        self.log += self.subj.getState()

        if state == self.detachInfo:
            self.detach()
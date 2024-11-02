from abc import abstractmethod


class State:
    @abstractmethod
    def insertCoin(self):
        pass

    @abstractmethod
    def getBall(self):
        pass

    @abstractmethod
    def returnCoin(self):
        pass

    @abstractmethod
    def addBall(self):
        pass


class ReadyState(State):
    def __init__(self, machine: 'BallMachine'):
        self.machine: BallMachine = machine

    def insertCoin(self):
        print("Coin is inserted")
        self.machine.setState(self.machine.GetHasPayedState())

    def getBall(self):
        print("You need to pay first»")

    def returnCoin(self):
        print("You need to pay first»")

    def addBall(self):
        pass


class HasPayedState(State):
    def __init__(self, machine: 'BallMachine'):
        self.machine: BallMachine = machine

    def insertCoin(self):
        print("You have already paid")

    def getBall(self):
        print("Take your ball")
        balls = self.machine.DecreaseBallCount()
        if balls:
            self.machine.setState(self.machine.GetReadyState())
        if not balls:
            self.machine.setState(self.machine.GetNoBallState())

    def returnCoin(self):
        print("Take your coin")
        self.machine.setState(self.machine.GetHasPayedState())

    def addBall(self):
        pass


class NoBallState(State):
    def __init__(self, machine: 'BallMachine'):
        self.machine: BallMachine = machine

    def insertCoin(self):
        print("Sorry, balls are over")

    def getBall(self):
        print("Sorry, balls are over")

    def returnCoin(self):
        print("Sorry, balls are over")

    def addBall(self):
        self.machine.setState(self.machine.GetReadyState())


class BallMachine:
    _state = None
    def __init__(self):
        self.ballCount = 3
        self._ready: ReadyState = ReadyState(self)
        self._hasPayed: HasPayedState = HasPayedState(self)
        self._noBall: NoBallState = NoBallState(self)
        self._currentState: State = self._ready

    def DecreaseBallCount(self) -> int:
        if self.ballCount > 0:
            self.ballCount -= 1

        return self.ballCount

    def setState(self, new_state: State) -> None:
        self._currentState = new_state

    def GetReadyState(self):
        return self._ready

    def GetHasPayedState(self):
        return self._hasPayed

    def GetNoBallState(self):
        return self._noBall

    def insertCoin(self):
        self._currentState.insertCoin()

    def getBall(self):
        self._currentState.getBall()

    def returnCoin(self):
        self._currentState.returnCoin()

    def addBall(self):
        print("Ball is added")
        self._currentState.getBall()

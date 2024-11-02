from __future__ import annotations
from abc import ABC, abstractmethod


class BallMachine:

    _state = None

    # def __init__(self, state: State) -> None:
    def __init__(self) -> None:
        self.ballCount = 3
        self.setState(ReadyState())

    def DecreaseBallCount(self) -> int:
        if self.ballCount > 0:
            self.ballCount -= 1

        return self.ballCount

    def setState(self, state: State):
        print(f'Ball count: {self.ballCount}')
        # print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def insertCoin(self):
        self._state.insertCoin()

    def getBall(self):
        self._state.getBall()

    def returnCoin(self):
        self._state.returnCoin()

    def addBall(self):
        self._state.addBall()


class State(ABC):
    @property
    def context(self) -> BallMachine:
        return self._context

    @context.setter
    def context(self, context: BallMachine) -> None:
        self._context = context

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
    def insertCoin(self):
        print("Coin is inserted")
        self.context.setState(HasPayedState())

    def getBall(self):
        if self.context.ballCount > 0:
            self.context.setState(HasPayedState())
        else:
            print('Ready state')
            print("You need to pay first»")

    def returnCoin(self):
        print("You need to pay first»")

    def addBall(self):
        pass


class NoBallState(State):
    def addBall(self) -> None:
        self.context.setState(ReadyState())

    def insertCoin(self) -> None:
        print("Coin is inserted")
        self.context.ballCount += 3
        self.context.setState(ReadyState())

    def getBall(self):
        print("Sorry, balls are over")

    def returnCoin(self):
        print("Sorry, balls are over")


class HasPayedState(State):
    def insertCoin(self):
        print("You have already paid")

    def addBall(self):
        print('You are Ready to Go!')

    def returnCoin(self):
        print('Coin is returned')
        self.context.ballCount -= 3
        self.context.setState(NoBallState())

    def getBall(self):
        print("Take your ball")
        balls = self.context.DecreaseBallCount()
        if balls:
            self.context.setState(ReadyState())
        if not balls:
            self.context.setState(NoBallState())


if __name__ == "__main__":
    context = BallMachine()
    context.insertCoin()
    context.getBall()

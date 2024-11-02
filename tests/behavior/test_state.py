import pytest

from behavior.state.exercise_2_guru import BallMachine


def test_state_guru():
    context = BallMachine()
    context.insertCoin()

    context.getBall()
    context.getBall()
    context.getBall()
    context.getBall()
    context.getBall()

    context.insertCoin()

    context.getBall()
    context.getBall()
    context.getBall()

    context.addBall()
    context.addBall()
    context.addBall()

    context.getBall()
    context.getBall()
    context.getBall()
    context.getBall()
    context.getBall()

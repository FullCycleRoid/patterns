import pytest

from behavior.observer.exercise_1 import ConcreteSubject, ConcreteObserver


@pytest.mark.parametrize(
    "input, result",
    [
        (
            "GYEWJFBBMMIRCCKKAPPPOZZDLLTXUUVV",
            [
                "GYEWJFBMIRCKA",
                "GYEWJFB",
                "GYEWJFBMIRC",
                "GYEWJFBMIRCAPOZD",
                "GYE",
                "GYEWJF",
                "G",
                "GYEWJFBMIRCKAPOZDLTXUV",
                "GYEWJFBMI"
            ]
        )
    ]
)
def test_abstract_factory_exc1(input, result):
    cs = ConcreteSubject()
    observers = []
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    while letters:
        letter = letters.pop(0)
        temp_obs = ConcreteObserver(cs, letter)
        temp_obs.attach()
        observers.append(temp_obs)

    for char in input:
        cs.setState(char)

    for obs in observers:
        print(obs.getLog())

import pytest

from behavior.observer.exercise_1 import ConcreteSubject, ConcreteObserver
from behavior.observer.exercise_2 import ConcreteSubject as ConcreteSubject2, ConcreteObserver as ConcreteObserver2


@pytest.mark.parametrize(
    "payload, result",
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
def test_abstract_factory_exc1(payload, result):
    cs = ConcreteSubject()
    observers = []
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    while letters:
        letter = letters.pop(0)
        temp_obs = ConcreteObserver(cs, letter)
        temp_obs.attach()
        observers.append(temp_obs)

    for char in payload:
        cs.setState(char)

    for ids, obs in enumerate(observers):
        assert obs.getLog() == result[ids]


@pytest.mark.parametrize(
    "payload, result",
    [
        (
            [
                "2b", "1a", "2b", "1p", "1m", "2a", "1m", "2a", "2o",
                "2o", "2s", "2y", "2y", "1q", "2y", "1q", "2i", "2h",
                "1s", "2h", "1s", "1s", "1r", "2p", "1f", "2f", "2f",
                "2m", "2m", "1u", "2u"
            ],
            [
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            ]
        )
    ]
)
def test_abstract_factory_exc1(payload, result):
    subj1 = ConcreteSubject2()
    subj2 = ConcreteSubject2()

    observers = [
        ConcreteObserver2("A"),
        ConcreteObserver2("B"),
        ConcreteObserver2("C"),
        ConcreteObserver2("D"),
        ConcreteObserver2("E"),
        ConcreteObserver2("F"),
        ConcreteObserver2("G")
    ]

    for obs in observers:
        obs.attach(subj1)
        obs.attach(subj2)

    for data in payload:
        if data.startswith("1"):
            subj1.setState(data)
        if data.startswith("2"):
            subj2.setState(data)

    for obs in observers:
        print(obs.getLog())


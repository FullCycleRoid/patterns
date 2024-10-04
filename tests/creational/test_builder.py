import pytest

from creational.builder.exercise_1 import Director, ConcreteBuilder1, ConcreteBuilder2


@pytest.mark.parametrize(
    "template, results",
    [
        ("ABC", ["-1--2--3-", "=1==2==3="]),
        ("CBA", ["-3--2--1-", "=3==2==1="]),
        ("AADC", ["-1--1--3-", "=1==1==3="]),
    ]
)
def test_builder_exc1(template, results):
    d1 = Director(ConcreteBuilder1())
    d2 = Director(ConcreteBuilder2())

    d1.construct(template)
    d2.construct(template)
    assert d1.getResult() == results[0]
    assert d2.getResult() == results[1]


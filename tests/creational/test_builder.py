import pytest

from creational.builder.exercise_1 import Director, ConcreteBuilder1, ConcreteBuilder2
from creational.builder.exercise_2 import BuilderPascal, BuilderC, BuilderPython, Director as Director2


@pytest.mark.parametrize(
    "template, results",
    [
        (" C AABB", ["-3--1--1--2--2-", "=***==*==*==**==**="]),
        ("B AABCCAC", ["-2--1--1--2--3--3--1--3-", "=**==*==*==**==***==***==*==***="]),
        ("CBCBCC", ["-3--2--3--2--3--3-", "=***==**==***==**==***==***="]),
        ("ABB   ", ["-1--2--2-", "=*==**==**="]),
        ("AC CCB", ["-1--3--3--3--2-", "=*==***==***==***==**="]),
    ]
)
def test_builder_exc1(template, results):
    d1 = Director(ConcreteBuilder1())
    d2 = Director(ConcreteBuilder2())

    d1.construct(template)
    d2.construct(template)
    assert d1.getResult() == results[0]
    assert d2.getResult() == results[1]


@pytest.mark.parametrize(
    "template, results",
    [
        ("Odd Minimum", ["oddMinimum", "odd_minimum", "oddminimum"]),
        ("positive MINIMUM", ["positiveMinimum", "positive_minimum", "positiveminimum"]),
        ("NEXT maximum", ["nextMaximum", "next_maximum", "nextmaximum"]),
        ("FIRST term", ["firstTerm", "first_term", "firstterm"]),
        ("MAXIMUM", ["maximum", "maximum", "maximum"]),
    ]
)
def test_builder_exc2(template, results):
    d1 = Director2(BuilderPascal())
    d2 = Director2(BuilderPython())
    d3 = Director2(BuilderC())

    d1.construct(template)
    d2.construct(template)
    d3.construct(template)
    assert d1.getResult() == results[0]
    assert d2.getResult() == results[1]
    assert d3.getResult() == results[2]


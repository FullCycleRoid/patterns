import pytest

from creational.prototype.exercise_1 import Client, ConcretePrototype1, ConcretePrototype2
from creational.prototype.exercise_2 import Rect, Line, Ellipse, GraphEditor


@pytest.mark.parametrize(
    "word, numbers, results",
    [
        ('WINDOW', [40, 17, 23, 13, 29], [
            "CP1=WINDOW=40 CP1=WINDOW=17 CP1=WINDOW=23 CP1=WINDOW=13 CP1=WINDOW=29",
            "CP2=WINDOW=40 CP2=WINDOW=17 CP2=WINDOW=23 CP2=WINDOW=13 CP2=WINDOW=29"
        ]
         ),
    ]
)
def test_prototype_1(word, numbers, results):
    client1 = Client(ConcretePrototype1(data=word, id=numbers[0]))
    client2 = Client(ConcretePrototype2(data=word, id=numbers[0]))

    for n in numbers:
        client1.operation(n)
        client2.operation(n)

    assert client1.getObjects() == results[0]
    assert client2.getObjects() == results[1]


@pytest.mark.parametrize(
    "p, objs, result",
    [
        (
            "RL",
            [
                (1, 1, 1, 3, 1),
                (0, 3, -2, 2, 3),
                (1, -2, 2, 4, -1),
                (0, 1, 2, 2, 4),
                (0, 2, 0, 4, 0)
            ],
             "Line(1,1,3,1) Rect(3,-2,2,3) Line(-2,2,4,-1) Rect(1,2,2,4) Rect(2,0,4,0)"
        )
    ]
)
def test_prototype_2(p, objs, result):
    types = {
        "R": Rect,
        "L": Line,
        "E": Ellipse
    }
    p0 = p[0]
    p1 = p[1]

    ge = GraphEditor(types[p0](), types[p1]())

    for obj in objs:
        ge.addGraphic(*obj)

    assert ge.drawAll() == result

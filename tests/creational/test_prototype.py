import pytest

from creational.prototype.exercise_1 import Client, ConcretePrototype1, ConcretePrototype2


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
def test_factory_method_exersice1_1(word, numbers, results):
    client1 = Client(ConcretePrototype1(data=word, id=numbers[0]))
    client2 = Client(ConcretePrototype2(data=word, id=numbers[0]))

    for n in numbers:
        client1.operation(n)
        client2.operation(n)

    assert client1.getObjects() == results[0]
    assert client2.getObjects() == results[1]

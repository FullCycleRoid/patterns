import pytest

from creational.abstract_factory.exercise_1 import AbstractFactory, ConcreteFactory1, AbstractProductA, AbstractProductB
from creational.abstract_factory.exercise_2 import Client, Factory2, Factory1


@pytest.mark.parametrize(
    "factory, Na, Nb, s, productAResult, productBResult",
    [
        (ConcreteFactory1, 11, 10, 'ABABB', '44', '120'),
        (ConcreteFactory1, 8, 2, 'ABBBA', '32', '50')
    ]
)
def test_abstract_factory_exc1(factory: AbstractFactory, Na, Nb, s, productAResult, productBResult):
    pa: AbstractProductA = factory.createProductA(Na)
    pb: AbstractProductB = factory.createProductB(Nb)
    for c in s:
        if c == 'A':
            pa.A()
        if c == 'B':
            pb.B(objA=pa)

    assert pa.getInfo() == productAResult
    assert pb.getInfo() == productBResult


@pytest.mark.parametrize(
    "N, sequence, results",
    [
        (3, ["L Message1", "B Caption1", "L Message2"], ["=MESSAGE1= [CAPTION1] =MESSAGE2=", '"message1" <caption1> "message2"']),
    ]
)
def test_abstract_factory_exc2(N, sequence, results):
    c1 = Client(f=Factory1())
    c2 = Client(f=Factory2())

    for s in sequence:
        type, text = s.split(' ')
        if type == 'B':
            c1.addButton(text)
            c2.addButton(text)

        if type == 'L':
            c1.addLabel(text)
            c2.addLabel(text)

    assert c1.getControls() == results[0]
    assert c2.getControls() == results[1]

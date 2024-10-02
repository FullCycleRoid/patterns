import pytest

from creational.factory_method.exercise_1 import ConcreteCreator1, ConcreteCreator2
from creational.factory_method.exercise_2 import ConcreteCreator1 as exs2_ConcreteCreator1, ConcreteCreator2 as exs2_ConcreteCreator2


@pytest.mark.parametrize(
    "payload, expected",
    [
        ('word', 'w o r d'),
        ('wOrD', 'w o r d'),
        ('two WORDS', 't w o w o r d s'),
        ('three WORDS here', 't h r e e w o r d s h e r e'),
    ]
)
def test_factory_method_exersice1_1(payload, expected):
    cc = ConcreteCreator1()
    assert cc.anOperation(payload) == expected


@pytest.mark.parametrize(
    "payload, expected",
    [
        ('word', 'W**O**R**D'),
        ('wOrD', 'W**O**R**D'),
        ('two WORDS', 'T**W**O**W**O**R**D**S'),
        ('three WORDS here', 'T**H**R**E**E**W**O**R**D**S**H**E**R**E'),
        ('sta*rs he**re', 'S**T**A**R**S**H**E**R**E'),
    ]
)
def test_factory_method_exersice1_2(payload, expected):
    cc = ConcreteCreator2()
    assert cc.anOperation(payload) == expected


@pytest.mark.parametrize(
    "payload, expected",
    [
        ('word', 'w*o*r*d'),
        ('wO*rD', 'w*o*r*d'),
        ('two WORDS', 't*w*o*w*o*r*d*s'),
        ('th*ree WOR*DS here', 't*h*r*e*e*w*o*r*d*s*h*e*r*e'),
    ]
)
def test_factory_method_exersice2_1(payload, expected):
    cc = exs2_ConcreteCreator1()
    res = cc.anOperation(payload)
    print(res, 'yhnghnghngh')
    assert cc.anOperation(payload) == expected


@pytest.mark.parametrize(
    "payload, expected",
    [
        ('word', '==W*o*r*d=='),
        ('wO*rD', '==W*o*r*d=='),
        ('two WO*RDS', '==T*w*o*w*o*r*d*s=='),
        ('three WO*RDS here', '==T*h*r*e*e*w*o*r*d*s*h*e*r*e=='),
    ]
)
def test_factory_method_exersice2_2(payload, expected):
    cc = exs2_ConcreteCreator2()
    assert cc.anOperation(payload) == expected

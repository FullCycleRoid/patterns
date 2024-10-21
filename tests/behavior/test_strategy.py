import pytest

from behavior.strategy.exercise_1 import Context1, Context2, ConcreteStrategyC, ConcreteStrategyA


@pytest.mark.parametrize(
    "payload, result",
    [
        (
            '12221122212121',
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
    contexts: list = []
    strategyC = ConcreteStrategyC()
    strategyA = ConcreteStrategyA()
    for i in range(len(payload)):
        if payload[i] == '1':
            ctx = Context1()
            ctx.setStrategy(strategyC)
            contexts.append(ctx)
        if payload[i] == '2':
            ctx = Context2()
            ctx.setStrategy(strategyA)
            contexts.append(ctx)

    for ctx in contexts:
        print(ctx.ContextInterface())

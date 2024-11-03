import pytest

from structural.composite.exercise_1 import Composite, Leaf


def test_composite_exc1():
    comp_a = Composite('A')
    comp_b = Composite('B')
    comp_c = Composite('C')
    comp_d = Composite('D')
    comp_e = Composite('E')
    comp_f = Composite('F')
    comp_g = Composite('G')

    leaf_1 = Leaf('1')
    leaf_2 = Leaf('2')
    leaf_3 = Leaf('3')
    leaf_4 = Leaf('4')
    leaf_5 = Leaf('5')

    comp_a.addComponent(comp_b)
    comp_a.addComponent(comp_c)
    comp_a.addComponent(comp_d)

    comp_d.addComponent(comp_e)
    comp_d.addComponent(comp_f)
    comp_d.addComponent(comp_g)

    comp_d.addComponent(leaf_1)
    comp_e.addComponent(leaf_2)
    comp_f.addComponent(leaf_3)
    comp_g.addComponent(leaf_4)
    comp_g.addComponent(leaf_5)

    print(comp_a.operation())

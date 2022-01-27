import firsttest
from temp import secondtest

def test_add():
    assert firsttest.add(3, 4) == 7
    assert firsttest.add(10, 1) == 11
    assert firsttest.add(2, 5) == 7

def test_divide():
    assert secondtest.divide(4, 2) == 2
    assert secondtest.divide(10, 1) == 10
    assert secondtest.divide(10, 5) == 2

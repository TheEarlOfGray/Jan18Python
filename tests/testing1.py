from applications.testing1 import func1

def test_func1_1():
    assert func1(5) == 10
    assert func1(5) == 10
    assert func1(5) == 10
    assert func1(5) == 10
    assert func1(15) == 30

def test_func1_2():
    assert func1(3) == 6
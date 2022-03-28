import calculator


def test_add():
    x = 10
    y = 25
    result = calculator.add(x, y)
    assert x + y == result


def test_substract():
    x = 20
    y = 10
    result = calculator.substract(x, y)
    assert x - y == result

def test_multiply():
    x = 20
    y =30
    result =calculator.multiply(x,y)
    assert  x * y ==result

def test_division():
    x = 900
    y = 30
    result = calculator.divisible(x, y)
    assert  x/y ==result
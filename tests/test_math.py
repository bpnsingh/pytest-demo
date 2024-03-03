import pytest
def test_plus():
    assert 1+1 == 2

def test_one_plus_two():
    a= 1
    b =2
    c = 3
    assert a+b == c

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert 'division by zero' in str(e.value)

#Test multiplication with differnt values
products = [
    (5,2,10),
    (5,0,0),
    (5,-2,-10),
    (-5,-2,10),
    (5.0,2,10.0)
]

@pytest.mark.parametrize('a,b,product',products)
def test_multiplication(a,b,product):
    assert a*b == product


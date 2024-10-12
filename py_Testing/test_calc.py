from calc import add,subtract
def test_add_both_positive():
    assert add(2,3)==5 
def test_add_both_negative():
    assert add(-2,-3)==-5 
def test_add_positive_negative():
    assert add(2,-3)==-1 
def test_add_zero():
    assert add(2,0)==2 


def test_subtract_both_positive():
    assert subtract(2,3)==-1
def test_subtract_both_negative():
    assert subtract(-2,-3)==1
def test_subtract_positive_negative():
    assert subtract(2,-3)==5
def test_subtract_zero():
    assert subtract(2,0)==2


def odd_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"
    
    
def test_odd_even():
    assert odd_even(2) == "even"
    assert odd_even(3) == "odd"
    assert odd_even(0) == "even"
    
def test_large_number():
    assert odd_even(100000000000) == "even"

odd_even("ten")

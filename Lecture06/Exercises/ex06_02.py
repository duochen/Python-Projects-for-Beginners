def odd_even(num):
    if not isinstance(num, int):
        return "Input must be an integer"
    return "even" if num % 2 == 0 else "odd"
    
def test_odd_even():
    assert odd_even(2) == "even"
    assert odd_even(3) == "odd"
    assert odd_even(0) == "even"
    
def test_large_number():
    assert odd_even(100000000000) == "even"

odd_even("ten")

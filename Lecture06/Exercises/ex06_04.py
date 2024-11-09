def is_palindrome(word):
    if not isinstance(word, str):
        return "Input must be a string"
    return word == word[::-1]

def test_palindrome():
    assert is_palindrome("abba") == True
    assert is_palindrome("hello") == False

def test_edge_cases():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_input_validation():
    assert is_palindrome(12321) == "Input must be a string"

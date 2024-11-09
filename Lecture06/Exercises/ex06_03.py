def is_palindrome(word):
    return word == word[::-1]

def test_palindrome():
    assert is_palindrome("abba") == True
    assert is_palindrome("hello") == False

def test_edge_cases():
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

is_palindrome(12321)

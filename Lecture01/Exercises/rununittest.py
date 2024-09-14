import unittest

def greet(name):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, World!"

class TestHello(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet(""), "Hello, World!")

if __name__ == '__main__':
    unittest.main()

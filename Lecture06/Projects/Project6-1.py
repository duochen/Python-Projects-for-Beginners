import random

def generate_test_cases(operation, num_cases=10):
    """Generates random test cases for basic math operations."""
    test_cases = []
    for _ in range(num_cases):
        a = random.randint(-100, 100)
        b = random.randint(-100, 100)
        
        if operation == "addition":
            expected = a + b
            test_cases.append((a, b, expected))
        elif operation == "subtraction":
            expected = a - b
            test_cases.append((a, b, expected))
        elif operation == "multiplication":
            expected = a * b
            test_cases.append((a, b, expected))
        elif operation == "division":
            if b == 0:  # Avoid division by zero
                b = random.randint(1, 100)
            expected = a / b
            test_cases.append((a, b, expected))
        else:
            raise ValueError("Unsupported operation")
    
    return test_cases

def test_operation(operation_func, test_cases):
    """Tests the given operation function with provided test cases."""
    for a, b, expected in test_cases:
        result = operation_func(a, b)
        assert result == expected, f"Test failed for input ({a}, {b}). Expected: {expected}, Got: {result}"
    print("All test cases passed!")

# Example operation functions
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

# Test the functions
if __name__ == "__main__":
    test_cases_add = generate_test_cases("addition", 5)
    test_operation(addition, test_cases_add)

    test_cases_sub = generate_test_cases("subtraction", 5)
    test_operation(subtraction, test_cases_sub)

    test_cases_mult = generate_test_cases("multiplication", 5)
    test_operation(multiplication, test_cases_mult)

    test_cases_div = generate_test_cases("division", 5)
    test_operation(division, test_cases_div)

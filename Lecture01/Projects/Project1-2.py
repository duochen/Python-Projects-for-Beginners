def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero."

def calculator():
    print("Welcome to the Basic Calculator!")
    
    while True:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))
        
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operator! Please try again.")
            continue
        
        print(f"The result is: {result}")
        
        again = input("Do you want to perform another calculation? (yes/no): ")
        if again.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()

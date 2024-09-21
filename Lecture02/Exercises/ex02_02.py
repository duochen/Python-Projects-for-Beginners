# python ex02_2.py 5 3
import argparse

# Create the ArgumentParser object
parser = argparse.ArgumentParser(description="Add two numbers together.")

# Add arguments for two numbers
parser.add_argument("num1", type=int, help="The first number to add")
parser.add_argument("num2", type=int, help="The second number to add")

# Parse the arguments from the command line
args = parser.parse_args()

# Add the two numbers
result = args.num1 + args.num2

# Print the result
print(f"The sum of {args.num1} and {args.num2} is {result}.")


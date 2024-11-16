import re

def validate_password(password):
    # (?=.*[A-Z]): At least one uppercase letter.
    # (?=.*[a-z]): At least one lowercase letter.
    # (?=.*\d): At least one digit.
    # .{8,}: At least 8 characters long.
    # Simple regex pattern: At least 8 chars, one uppercase, one lowercase, one digit
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
    
    # Check if password matches the pattern
    return bool(re.match(pattern, password))

# Test the function
password = input("Enter a password to validate: ")

if validate_password(password):
    print("Password is valid.")
else:
    print("Password is invalid. It must be at least 8 characters long, "
          "contain one uppercase letter, one lowercase letter, and one digit.")

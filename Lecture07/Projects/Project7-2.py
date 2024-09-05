import re

def validate_password(password):
    errors = []

    if len(password) < 8 or len(password) > 20:
        errors.append("Password must be between 8 and 20 characters long.")
    
    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain at least one uppercase letter.")
    
    if not re.search(r'[a-z]', password):
        errors.append("Password must contain at least one lowercase letter.")
    
    if not re.search(r'\d', password):
        errors.append("Password must contain at least one digit.")
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("Password must contain at least one special character.")
    
    if errors:
        return False, errors
    return True, ["Password is strong!"]

def main():
    password = input("Enter a password to validate: ")
    valid, messages = validate_password(password)
    
    if valid:
        print("Valid password!")
    else:
        print("Invalid password!")
    
    for message in messages:
        print(f"- {message}")

if __name__ == '__main__':
    main()

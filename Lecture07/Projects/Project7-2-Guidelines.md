### **Steps to Complete the Project: Regular Expression Password Validator**

### **Step 1: Understand the Project Requirements**
Before writing any code, understand what the password validator should do:
- The password must be **8 to 20 characters long**.
- It must contain **at least one uppercase letter** (A-Z).
- It must contain **at least one lowercase letter** (a-z).
- It must contain **at least one number** (0-9).
- It must contain **at least one special character** (`!@#$%^&*()-_+=<>?/`).

The program should:
1. Ask the user to input a password.
2. Check if the password meets all the criteria using **regular expressions**.
3. Provide feedback on what needs to be improved if the password is weak.

---

### **Step 2: Import the Required Module**
Python provides the `re` module for working with regular expressions. Start by importing it:

```python
import re
```

---

### **Step 3: Define the Regular Expression Pattern**
Create a pattern that enforces all the password rules.

```python
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$"
```

Explanation:
- `^` and `$` → Ensures the pattern applies to the entire password.
- `(?=.*[A-Z])` → Ensures **at least one uppercase letter**.
- `(?=.*[a-z])` → Ensures **at least one lowercase letter**.
- `(?=.*\d)` → Ensures **at least one number**.
- `(?=.*[@$!%*?&])` → Ensures **at least one special character**.
- `[A-Za-z\d@$!%*?&]{8,20}` → Limits the password length between **8 and 20** characters.

---

### **Step 4: Create a Function to Validate the Password**
Write a function that checks if the password meets the criteria:

```python
def validate_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,20}$"
    
    if re.match(pattern, password):
        return "✅ Strong password!"
    else:
        return "❌ Weak password! Make sure it contains:\n" \
               "- At least 8 characters and at most 20 characters.\n" \
               "- At least one uppercase letter.\n" \
               "- At least one lowercase letter.\n" \
               "- At least one number.\n" \
               "- At least one special character (@$!%*?&)."
```

---

### **Step 5: Get User Input and Test the Function**
Now, ask the user to enter a password and validate it:

```python
password = input("Enter a password to check its strength: ")
result = validate_password(password)
print(result)
```

---

### **Step 6: Enhance the Feedback System**
Instead of just saying the password is weak, provide **detailed feedback** on what is missing. Modify the function:

```python
def validate_password(password):
    errors = []

    if len(password) < 8 or len(password) > 20:
        errors.append("- Password must be between 8 and 20 characters long.")
    if not re.search(r"[A-Z]", password):
        errors.append("- At least one uppercase letter is required.")
    if not re.search(r"[a-z]", password):
        errors.append("- At least one lowercase letter is required.")
    if not re.search(r"\d", password):
        errors.append("- At least one number is required.")
    if not re.search(r"[@$!%*?&]", password):
        errors.append("- At least one special character (@$!%*?&) is required.")

    if errors:
        return "❌ Weak password! Here's what you need to fix:\n" + "\n".join(errors)
    else:
        return "✅ Strong password!"

# Test
password = input("Enter a password to check its strength: ")
print(validate_password(password))
```

---

### **Step 7: Test with Different Inputs**
Try running the program with different passwords and check the output.

#### Example Tests:
| Password        | Output |
|----------------|--------|
| `abc123`       | ❌ Weak password (Too short, missing uppercase & special char) |
| `Abc123`       | ❌ Weak password (Too short, missing special char) |
| `Abcdefgh1!`   | ✅ Strong password! |
| `ABCD1234!`    | ❌ Weak password (Missing lowercase letter) |

---

### **Step 8: Bonus - Improve User Experience**
To improve the program, consider:
- **Looping until a valid password is entered**:
  ```python
  while True:
      password = input("Enter a password to check its strength: ")
      feedback = validate_password(password)
      print(feedback)
      if "✅ Strong password!" in feedback:
          break
  ```
- **Hiding password input using `getpass` (for security)**:
  ```python
  import getpass
  password = getpass.getpass("Enter a password: ")
  ```
- **Saving passwords in a file** (for further exercises).

---

### **What Students Will Learn**
- **Regular expressions (`re` module)** for pattern matching.
- **String manipulation** and **pattern searching**.
- **Conditionals (`if-else`)** to provide feedback.
- **Loops (`while True`)** for continuous input validation.

---

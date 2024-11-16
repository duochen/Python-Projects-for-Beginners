import re

pattern = r"[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"
user_input = input()
if (re.search(pattern, user_input)):
    print("valid email")
else:
    print("invalid email")
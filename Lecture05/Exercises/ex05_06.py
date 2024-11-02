import re

text = "I like apples"
new_text = re.sub(r'[aeiou]', 'o', text)
print(new_text)

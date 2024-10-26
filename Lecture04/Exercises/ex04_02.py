import random

text = input("Enter your text: ")

ransom_text = ''.join(random.choice([char.upper(), char.lower()]) for char in text)
print(ransom_text)

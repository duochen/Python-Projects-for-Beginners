import re
pattern = r'\d{3}-\d{2,3}-\d{4}'
text = "Call 123-456-7890 or 123-45-6789."
matches = re.findall(pattern, text)
print(matches)

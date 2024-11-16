import re

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
text = "Contact us at support@example.com."
emails = re.findall(email_pattern, text)
print(emails)

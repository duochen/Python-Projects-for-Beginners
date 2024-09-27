import string

# Define the text variable
text = "Hello, world! This is a test: does it work? Yes, it does."

# Remove punctuation from the text
text = text.translate(str.maketrans('', '', string.punctuation))

# Print the result
print(text)

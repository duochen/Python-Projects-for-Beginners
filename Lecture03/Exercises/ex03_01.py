cipher = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
          '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

def jump_the_five(text):
    result = ""
    for char in text:
        if char in cipher:
            result += cipher[char]
        else:
            result += char
    return result

print(jump_the_five("12345"))  # Outputs: 98760
print(jump_the_five("Hello 123!"))  # Outputs: Hello 987!


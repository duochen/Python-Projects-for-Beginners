def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (ord(char) - start + shift_amount) % 26)
        else:
            result += char
    return result

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def atbash_cipher(text):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (25 - (ord(char) - start)))
        else:
            result += char
    return result

def vigenere_cipher(text, key):
    result = ''
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_as_int = [ord(i) for i in text]
    for i in range(len(text_as_int)):
        if text[i].isalpha():
            value = (text_as_int[i] + key_as_int[i % key_length]) % 26
            result += chr(value + ord('A') if text[i].isupper() else value + ord('a'))
        else:
            result += text[i]
    return result

def vigenere_decipher(text, key):
    result = ''
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    text_as_int = [ord(i) for i in text]
    for i in range(len(text_as_int)):
        if text[i].isalpha():
            value = (text_as_int[i] - key_as_int[i % key_length]) % 26
            result += chr(value + ord('A') if text[i].isupper() else value + ord('a'))
        else:
            result += text[i]
    return result

def play_game():
    print("Welcome to the Cipher Text Adventure!")
    print("You need to decode hidden messages to progress through the levels.")

    # Level 1: Caesar Cipher
    print("\nLevel 1: Caesar Cipher")
    encoded_message = caesar_cipher("MEET ME AT THE PARK", 3)
    print(f"Encoded message: {encoded_message}")
    user_input = input("Decode the message: ")
    if user_input.upper() == caesar_decipher(encoded_message, 3).upper():
        print("Correct! You've unlocked Level 2.")
    else:
        print("Incorrect! Try again.")

    # Level 2: Atbash Cipher
    print("\nLevel 2: Atbash Cipher")
    encoded_message = atbash_cipher("HELLO WORLD")
    print(f"Encoded message: {encoded_message}")
    user_input = input("Decode the message: ")
    if user_input.upper() == atbash_cipher(encoded_message).upper():
        print("Correct! You've unlocked Level 3.")
    else:
        print("Incorrect! Try again.")

    # Level 3: Vigenère Cipher
    print("\nLevel 3: Vigenère Cipher")
    key = "SECRET"
    encoded_message = vigenere_cipher("MEET ME AT THE LIBRARY", key)
    print(f"Encoded message: {encoded_message}")
    user_input = input("Decode the message: ")
    if user_input.upper() == vigenere_decipher(encoded_message, key).upper():
        print("Congratulations! You've completed the Cipher Text Adventure.")
    else:
        print("Incorrect! Try again.")

if __name__ == "__main__":
    play_game()

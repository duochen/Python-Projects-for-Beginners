Here’s a detailed explanation of the code for the Cipher Text Adventure project:

### 1. Caesar Cipher

**Caesar Cipher** is a substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.

**Caesar Cipher Encoding Function:**

```python
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
```

- **Parameters:**
  - `text`: The string to be encoded.
  - `shift`: The number of positions each letter should be shifted.
  
- **Process:**
  - **Loop Through Each Character:** Iterate through each character in the input text.
  - **Check If Character Is Alphabetic:** Use `char.isalpha()` to determine if the character is a letter.
  - **Determine Shift Amount:** Use modulo 26 to handle shifts greater than 26.
  - **Calculate Encoded Character:** Compute the new character position, ensuring it wraps around using modulo 26.
  - **Handle Non-Alphabetic Characters:** Leave non-alphabetic characters unchanged.
  
- **Return Value:** Returns the encoded text.

**Caesar Cipher Decoding Function:**

```python
def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)
```

- **Parameters:**
  - `text`: The string to be decoded.
  - `shift`: The number of positions each letter was shifted (negative for decoding).
  
- **Process:** Simply call `caesar_cipher` with a negative shift to reverse the encoding.
  
- **Return Value:** Returns the decoded text.

### 2. Atbash Cipher

**Atbash Cipher** is a substitution cipher where each letter in the alphabet is mapped to its reverse (A ↔ Z, B ↔ Y, etc.).

**Atbash Cipher Function:**

```python
def atbash_cipher(text):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (25 - (ord(char) - start)))
        else:
            result += char
    return result
```

- **Parameters:**
  - `text`: The string to be encoded/decoded.
  
- **Process:**
  - **Loop Through Each Character:** Iterate through each character in the input text.
  - **Check If Character Is Alphabetic:** Use `char.isalpha()` to determine if the character is a letter.
  - **Calculate Mapped Character:** The position of the character is reversed (A to Z, B to Y, etc.).
  - **Handle Non-Alphabetic Characters:** Leave non-alphabetic characters unchanged.
  
- **Return Value:** Returns the encoded/decoded text.

### 3. Vigenère Cipher

**Vigenère Cipher** is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword.

**Vigenère Cipher Encoding Function:**

```python
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
```

- **Parameters:**
  - `text`: The string to be encoded.
  - `key`: The keyword used to determine the shift values.
  
- **Process:**
  - **Convert Key and Text to Integer Lists:** Convert characters to their ASCII integer values.
  - **Iterate Through Text:** For each character in the text, apply a shift based on the corresponding key character.
  - **Handle Character Wrapping:** Ensure the new character wraps around if it exceeds 'Z' or 'z'.
  - **Handle Non-Alphabetic Characters:** Leave non-alphabetic characters unchanged.
  
- **Return Value:** Returns the encoded text.

**Vigenère Cipher Decoding Function:**

```python
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
```

- **Parameters:**
  - `text`: The string to be decoded.
  - `key`: The keyword used to reverse the encoding process.
  
- **Process:** Similar to encoding, but subtract the key values instead of adding them.
  
- **Return Value:** Returns the decoded text.

### 4. Text-Based Adventure Game

**Game Function:**

```python
def play_game():
    print("Welcome to the Cipher Text Adventure!")
    print("You need to decode hidden messages to progress through the levels.")
```

- **Introduction:** Print a welcome message explaining the game.

**Level 1: Caesar Cipher**

```python
    print("\nLevel 1: Caesar Cipher")
    encoded_message = caesar_cipher("MEET ME AT THE PARK", 3)
    print(f"Encoded message: {encoded_message}")
    user_input = input("Decode the message: ")
    if user_input.upper() == caesar_decipher(encoded_message, 3).upper():
        print("Correct! You've unlocked Level 2.")
    else:
        print("Incorrect! Try again.")
```

- **Encoded Message:** Use the Caesar cipher to encode a sample message.
- **User Input:** Prompt the user to decode the message.
- **Check Answer:** Compare the user's input to the decoded message.

**Level 2: Atbash Cipher**

```python
    print("\nLevel 2: Atbash Cipher")
    encoded_message = atbash_cipher("HELLO WORLD")
    print(f"Encoded message: {encoded_message}")
    user_input = input("Decode the message: ")
    if user_input.upper() == atbash_cipher(encoded_message).upper():
        print("Correct! You've unlocked Level 3.")
    else:
        print("Incorrect! Try again.")
```

- **Encoded Message:** Use the Atbash cipher to encode a sample message.
- **User Input:** Prompt the user to decode the message.
- **Check Answer:** Compare the user's input to the decoded message.

**Level 3: Vigenère Cipher**

```python
    print("\nLevel 3: Vigenère Cipher")
    key = "SECRET"
    encoded_message = vigenere_cipher("MEET ME AT THE LIBRARY", key)
    print(f"Encoded message: {encoded_message}")
    user_input = input("Decode the message: ")
    if user_input.upper() == vigenere_decipher(encoded_message, key).upper():
        print("Congratulations! You've completed the Cipher Text Adventure.")
    else:
        print("Incorrect! Try again.")
```

- **Encoded Message:** Use the Vigenère cipher to encode a sample message with a key.
- **User Input:** Prompt the user to decode the message.
- **Check Answer:** Compare the user's input to the decoded message.

**Main Execution:**

```python
if __name__ == "__main__":
    play_game()
```

- **Run Game:** Execute the `play_game()` function if the script is run directly.

This project introduces students to cipher techniques while integrating them into a fun and interactive text-based game, enhancing both their coding skills and understanding of cryptography.
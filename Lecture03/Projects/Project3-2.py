def vigenere_encrypt(text, key):
    encrypted_text = ""
    key = key.upper()
    key_length = len(key)

    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A') + 1  # Shift is 1-based index
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged

    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key = key.upper()
    key_length = len(key)

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A') + 1  # Shift is 1-based index
            decrypted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged

    return decrypted_text

# Verification
message = "HELLO"
key = "FUN"

# Encrypt the message
encrypted_message = vigenere_encrypt(message, key)
print("Encrypted message:", encrypted_message)

# Decrypt the message
decrypted_message = vigenere_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)

# Validation
assert encrypted_message == "NZZRJ", "Encryption failed!"
assert decrypted_message == "HELLO", "Decryption failed!"

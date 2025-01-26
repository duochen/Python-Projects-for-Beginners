def vigenere_cipher(text, keyword, mode='encrypt'):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = text.upper().replace(" ", "")
    keyword = keyword.upper()
    keyword_repeated = ''.join([keyword[i % len(keyword)] for i in range(len(text))])
    
    result = []
    
    for i, char in enumerate(text):
        if char in alphabet:
            text_index = alphabet.index(char)
            keyword_index = alphabet.index(keyword_repeated[i])
            
            if mode == 'encrypt':
                new_index = (text_index + keyword_index) % 26
            elif mode == 'decrypt':
                new_index = (text_index - keyword_index) % 26
            
            result.append(alphabet[new_index])
        else:
            result.append(char)  # Preserve non-alphabetic characters
    
    return ''.join(result)

# Input from user
text = input("Enter the message: ")
keyword = input("Enter the keyword: ")
mode = input("Encrypt or Decrypt? ").lower()

# Encrypt or decrypt the message
result = vigenere_cipher(text, keyword, mode)

# Display the result
if mode == 'encrypt':
    print(f"Encrypted message: {result}")
elif mode == 'decrypt':
    print(f"Decrypted message: {result}")

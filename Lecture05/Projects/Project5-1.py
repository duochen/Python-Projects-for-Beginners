import string

# Caesar cipher function
def caesar_cipher(text, shift, mode='encode'):
    result = []
    alphabet = string.ascii_lowercase
    shift = shift % 26

    for char in text.lower():
        if char in alphabet:
            new_pos = (alphabet.index(char) + shift) if mode == 'encode' else (alphabet.index(char) - shift)
            result.append(alphabet[new_pos % 26])
        else:
            result.append(char)

    return ''.join(result)

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ' ': '/'
}

def morse_encode(message):
    return ' '.join(MORSE_CODE_DICT[char.upper()] for char in message if char.upper() in MORSE_CODE_DICT)

def morse_decode(message):
    reverse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    return ''.join(reverse_dict[code] for code in message.split(' '))

# User interaction
def secret_message():
    print("Welcome to the Secret Message Encoder/Decoder!")
    message = input("Enter your message: ")
    choice = input("Choose an encoding method: Caesar (C) or Morse (M): ").upper()

    if choice == 'C':
        shift = int(input("Enter the Caesar cipher shift value: "))
        mode = input("Do you want to encode (E) or decode (D)? ").lower()
        print("Result:", caesar_cipher(message, shift, mode))

    elif choice == 'M':
        mode = input("Do you want to encode (E) or decode (D)? ").lower()
        if mode == 'e':
            print("Encoded message:", morse_encode(message))
        elif mode == 'd':
            print("Decoded message:", morse_decode(message))

secret_message()

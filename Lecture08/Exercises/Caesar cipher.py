def translate(message, key):
    translated = ''
    for char in message:
        index = ord(char)
        index = (index+key-32) % 96+32   
        translated += chr(index)
    return translated

message = input('what is your message to encrypt? ')
encrypted=translate(message, len(message))
print("encrypted: ",encrypted)
decrypted=translate(encrypted, -len(message))
print("decrypted: ",decrypted)
if decrypted== message:
    print('encrypt/decrypt successfully')

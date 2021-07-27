from secrets import token_bytes

def encrypt(original) :
    ob = original.encode()
    print('original_bytes: ',ob)
    ok = int.from_bytes(ob, "big")
    print('original_key: ',ok,'\n')
    db = token_bytes(len(ob))
    print('dummy_bytes: ',db)
    dk = int.from_bytes(db, "big")
    print('dummy_key: ',dk)
    enk = ok ^ dk
    print('encrypted_key: ',enk)
    return dk, enk

def decrypt(k1, k2):
    dek = k1 ^ k2
    print('decrypted_key: ',dek)
    deb = dek.to_bytes((dek.bit_length() + 7) // 8, "big")
    print('decrypted_bytes: ',deb)
    return deb.decode()

message=input('original_message: ')
key1, key2 = encrypt(message)
print()
result = decrypt(key1, key2)
print('decrypted_message: ',result)

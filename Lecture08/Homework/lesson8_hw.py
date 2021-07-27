from secrets import token_bytes

def translate(message, key):
    translated = ''
    for char in message:
        index = ord(char)
        index = (index+key-32) % 96+32   
        translated += chr(index)
    return translated

def encrypt(original) :
    ob = original.encode()
    ok = int.from_bytes(ob, "big")
    db = token_bytes(len(ob)) 
    dk = int.from_bytes(db, "big")
    enk = ok ^ dk
    return dk, enk

def decrypt(k1, k2):
    dek = k1 ^ k2 
    deb = dek.to_bytes((dek.bit_length() + 7) // 8, "big")
    return deb.decode()

def split(message):
    evens = message[::2] 
    odds = message[1::2]
    return  evens, odds

def combine(r1,r2):
    long=str(max(r1,r2)); short=str(min(r1,r2))
    for i in range(len(short)):
        long = long[:2*i+1]+short[i]+long[2*i+1:]
    return long

secret = input('secret? ')
caesar=translate(secret, len(secret))
print("Caesar encrypted: ",caesar)
k1,k2=encrypt(caesar)
print('XOR encrypted: ',k1,'\t',k2)
rail=combine(k1,k2)
print("rail encrypted: ",rail,'\n')
r1,r2=split(rail)
print('rail decrypted: ',r1,'\t',r2)
XOR = decrypt(int(r1), int(r2))
print('XOR decryped: ',XOR)
decrypted=translate(XOR, -len(XOR))
print("Caesar decrypted: ",decrypted)
if decrypted == secret:
    print('encrypt / decrypt successfully!')

def split(message):
    evens = message[::2]
    odds = message[1::2]
    return  evens, odds
def combine(m1,m2):
    for i in range(len(m2)):
        m1 = m1[:2*i+1]+m2[i]+m1[2*i+1:]
    return m1
message = input("What's your message to encrypt? ")
m1,m2=split(message)
print("encrypted =",m1,m2)
text=combine(m1,m2)
print("decrypted = ", text)
if text== message:
    print('encrypt/decrypt successfully')

'''c = n = 1
while c <= 1000:
    n = n+1
    prime = True
    for i in range(2,int(n/2)+1):
        if n % i==0:
            prime = False
            break
    if prime:
        c = c + 1
print(n,"is the 1000th prime number.")'''

c = n = 1
while c <= 1000:
    i = 2
    n = n+1
    while (n % i !=0) and (i <= int(n/2)):
        i = i + 1
    if i > int(n/2):
        c = c + 1
print(n,"is the 1000th prime number.")

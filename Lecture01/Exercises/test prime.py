x = int(input('giving a number: '))
for n in range(2,x+1):
    i = 2
    while (n % i != 0) and (i <= int(n/2)):
        i = i + 1
    if i > int(n/2):
        print(n, 'is a prime')
    else:
        print(n, 'is a composite')
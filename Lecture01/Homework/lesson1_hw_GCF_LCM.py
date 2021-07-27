def prime_numbers(n):
    numbers = []
    for i in range(2, n + 1):
        numbers.append(i)
    primes = []
    while len(numbers) > 0:
        prime = numbers[0]
        primes.append(prime)
        del numbers[0]
        for number in numbers:
            if number % prime == 0:
                numbers.remove(number)
    return primes

def prime_factorization(n, primes):
    prime_factors = []
    for prime in primes:
        while n % prime == 0:
            prime_factors.append(prime)
            n = n / prime
    return prime_factors

while True:
    numstr = input('What is the first integer you want? \
(Type quit if to stop) (Minimum number is 2): ')
    
    if numstr.lower() == 'quit':
        break
    if not numstr.isdigit():
        print('Input has to be an integer.')
        continue
    numint1 = int(numstr)
    if numint1 <= 1:
        print('Input has to be greater than 1.')
        continue

    numstr = input('What is the second integer you want? \
(Type quit if to stop) (Minimum number is 2): ')
    
    if numstr.lower() == 'quit':
        break
    if not numstr.isdigit():
        print('Input has to be an integer.')
        continue
    numint2 = int(numstr)
    if numint2 <= 1:
        print('Input has to be greater than 1.')
        continue

    primes1 = prime_numbers(numint1)
    prime_factors1 = prime_factorization(numint1, primes1)
    primes2 = prime_numbers(numint2)
    prime_factors2 = prime_factorization(numint2, primes2)

    if numint1 in primes1:
        print(f'{numint1} is a prime number.')       
    else:
        print(f'{numint1} is a composite number.')
        print(f'{numint1} = ', end = '')
        for i in range(len(prime_factors1)-1):
            print(f'{prime_factors1[i]} * ', end = '')
        print(prime_factors1[-1])

    if numint2 in primes2:
        print(f'{numint2} is a prime number.')        
    else:
        print(f'{numint2} is a composite number.')       
        print(f'{numint2} = ', end = '')
        for i in range(len(prime_factors2)-1):
            print(f'{prime_factors2[i]} * ', end = '')
        print(prime_factors2[-1])

    GCF = []
    for element in prime_factors1:
        if prime_factors2.count(element) > 0:
            GCF.append(element)
            prime_factors2.remove(element)
        
    gcf = 1
    for e in GCF:
        gcf = gcf * e

    lcm = 1
    for e in prime_factors1 + prime_factors2:
        lcm = lcm * e

    print(f"the Greatest Common Factor of {numint1} and {numint2} is: {gcf}")
    print(f"the Least Common Multiple of {numint1} and {numint2} is: {lcm}")


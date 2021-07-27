# finds all the primes up to n using sieve of eratosthenes
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

# finds prime factorization of n
def prime_factorization(n, primes):
    prime_factors = []
    for prime in primes:
        while n % prime == 0:
            prime_factors.append(prime)
            n = n / prime
    return prime_factors



while True:
    numstr = input('What is the integer you want? \
(Type quit if to stop) (Minimum number is 2): ')
    
    # check if user wants to quit
    if numstr.lower() == 'quit':
        break
    # check if input is a number
    if not numstr.isdigit():
        print('Input has to be an integer.')
        continue
    # check if input is greater than 1
    numint = int(numstr)
    if numint <= 1:
        print('Input has to be greater than 1.')
        continue

    # find all the primes up to numint
    primes1 = prime_numbers(numint)

    # check if numint is prime or composite
    if numint in primes1:
        print(f'{numint} is a prime number.')
    else:
        print(f'{numint} is a composite number.')
        # prime factorization of composite number
        prime_factors1 = prime_factorization(numint, primes1)
        # print prime factorization
        print(f'{numint} = ', end = '')
        for i in range(len(prime_factors1)-1):
            print(f'{prime_factors1[i]} * ', end = '')
        print(prime_factors1[-1])

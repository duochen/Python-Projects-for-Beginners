def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * i, n + 1, i):
                IsPrime[j] = False
    return [x for x in range(2, n + 1) if IsPrime[x]]

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

print(eratosthenes(120))
print(prime_numbers(120))

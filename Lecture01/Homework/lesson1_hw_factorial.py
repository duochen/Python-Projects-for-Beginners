def factorial (n):
    results = 1
    for i in range (1,n+1):
        results = results * i
    return results

while True:
    s = input('Factorial of what number? ')
    if s.isnumeric():
        fn = eval(s)
        if int(fn) == fn and fn > 0 and fn <= 10000:
            break
    print('Not valid input!')

print (factorial(fn))

def prime(n):
    i = 2
    while (n % i !=0) and (i < n):
        i = i + 1
    if i == n:
        return True
    else:
        return False



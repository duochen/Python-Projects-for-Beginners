import random
    
def linear_search(low,high,guess):
    i = 0
    for n in range(low,high+1):
        i += 1
        print(f'linear trial{i}: {n}')
        if n == guess:          
            break

def binaryi_search(low,high,guess):
    i = 0
    while low <= high: 
        mid = (low + high) // 2
        i += 1
        print(f'binary iterative trial{i}: {mid}')
        if mid < guess:
            low = mid+1
        elif mid > guess:
            high = mid-1
        else:
            break

def binaryr_search(low,high,guess):
    global j
    mid = (high + low) // 2
    j += 1
    print(f'binary recursive trial{j}: {mid}')
    if mid < guess:
        binaryr_search(mid+1, high, guess)
    elif mid > guess:
        binaryr_search(low, mid-1, guess)

j = 0
low = 10
high = 100
guess=random.randint(low,high)
print('guess: ',guess)
print()

linear_search(low,high,guess)
print()
binaryi_search(low,high,guess)
print()
binaryr_search(low,high,guess)

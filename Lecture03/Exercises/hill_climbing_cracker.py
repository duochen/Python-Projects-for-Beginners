import time
from random import randint, randrange

def fitness(combo, attempt):
    match = 0
    for i, j in zip(combo, attempt):
        if i == j:
            match += 1
    return match

passcode = '917643528'
combo = [int(i) for i in passcode]
best_try = [0] * len(combo)
best_try_match = fitness(combo, best_try)
count = 0

start_time = time.time()
while best_try != combo:  
    next_try = best_try[:]
    mutate_pos = randrange(0, len(combo))
    next_try[mutate_pos] = randint(0, 9)
    next_try_match = fitness(combo, next_try)
    if next_try_match > best_try_match:
        best_try = next_try[:]
        best_try_match = next_try_match
    count += 1
end_time = time.time()

print(f"passcode: {passcode}")
print(f"crack result: {best_try} in {count} tries!")
print(f"Runtime:  {end_time - start_time} seconds.")       

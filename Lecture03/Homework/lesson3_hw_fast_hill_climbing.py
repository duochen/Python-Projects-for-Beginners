import time
from random import randint, randrange, choice

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
fix_digit=[]
count = 0

start_time = time.time()    
while best_try != combo:  
    next_try = best_try[:]
    uncertain_digit=[i for i in range(0,len(combo)) if i not in fix_digit]
    mutate_pos = choice(uncertain_digit)
    next_try[mutate_pos] = randint(0, 9)
    next_try_match = fitness(combo, next_try)
    if next_try_match > best_try_match:
        best_try = next_try[:]
        best_try_match = next_try_match
        fix_digit.append(mutate_pos)
    count += 1
end_time = time.time()

print(f"passcode: {passcode}")
print(f"crack result: {best_try} in {count} tries!")
print(f"Runtime:  {end_time - start_time} seconds.")

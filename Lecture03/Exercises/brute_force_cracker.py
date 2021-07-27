import time
from itertools import product
passcode ="9176435"
ns = "0123456789"
combo = [i for i in passcode]

start_time = time.time()
for perm in product(ns, repeat=len(combo)):
    if perm == tuple(combo):
        break
end_time = time.time()

print(f"passcode: {passcode}")
print(f"crack result: {perm}")
print(f"Runtime:  {end_time - start_time} seconds.")   

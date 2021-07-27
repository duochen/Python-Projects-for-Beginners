import time
import random as r
passcode ="9176435"

start_time = time.time()
while True:
    trial = [r.randint(0,9) for i in range(len(passcode))]
    if trial == int(passcode):
        break
end_time = time.time()

print(f"passcode: {passcode}")
print(f"crack result: {trial}")
print(f"Runtime:  {end_time - start_time} seconds.")   

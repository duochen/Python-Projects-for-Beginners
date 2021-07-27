import time
passcode ="9176435"

start_time = time.time()
result=""
for p in passcode:
    for n in (0,1,2,3,4,5,6,7,8,9):
        if n==int(p):
            result+=str(n)
            break
end_time = time.time()

print(f"passcode: {passcode}")
print(f"crack result: {result}")
print(f"Runtime:  {end_time - start_time} seconds.")   

import time
passcode ="9176435"
ns = "0123456789"
def crack(passcode):
    for a in ns:
        for b in ns:
            for c in ns:
                for d in ns:
                    for e in ns:
                        for f in ns:
                            for g in ns:
                                if passcode==a+b+c+d+e+f+g:
                                    return(a+b+c+d+e+f+g)
start_time = time.time()
crack_result=crack(passcode)
end_time = time.time()
print(f"passcode: {passcode}")
print(f"crack result: {crack_result}")
print(f"Runtime:  {end_time - start_time} seconds.")   

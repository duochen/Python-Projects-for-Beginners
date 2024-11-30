def ladder(steps):
    direction = "up" if steps > 0 else "down"
    steps_abs = abs(steps)
    step_word = "step" if steps_abs == 1 else "steps"
    return f"{steps_abs} {step_word} {direction}"

print(ladder(3))  # Output: 3 steps up
print(ladder(-1))  # Output: 1 step down

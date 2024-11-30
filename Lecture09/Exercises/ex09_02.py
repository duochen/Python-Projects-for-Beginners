def ladder(steps):
    direction = "up" if steps > 0 else "down"
    return f"{abs(steps)} {'step' if abs(steps) == 1 else 'steps'} {direction}"


print(ladder(3))  # Output: 3 steps up
print(ladder(-1))  # Output: 1 step down

def test_ladder():
    assert ladder(3) == "3 steps up"
    assert ladder(-1) == "1 step down"
    assert ladder(0) == "0 steps down"
    
test_ladder()

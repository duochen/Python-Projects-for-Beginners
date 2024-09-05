def knapsack_greedy(weights, values, capacity):
    items = list(zip(weights, values))
    items = sorted(items, key=lambda x: x[1] / x[0], reverse=True)  # Sort by value/weight ratio
    
    total_value = 0
    total_weight = 0
    selected_items = []
    
    for weight, value in items:
        if total_weight + weight <= capacity:
            selected_items.append((weight, value))
            total_weight += weight
            total_value += value
    
    return selected_items, total_value

def print_knapsack_solution(selected_items, total_value):
    print("Selected items (weight, value):")
    for item in selected_items:
        print(item)
    print(f"Total value: {total_value}")

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

selected_items, total_value = knapsack_greedy(weights, values, capacity)
print_knapsack_solution(selected_items, total_value)

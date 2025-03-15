Here is a step-by-step guideline to complete **Project 2: Optimization - The Knapsack Problem** using the **Greedy Algorithm** in Python.

---

## **Step-by-Step Guide: Solving the Knapsack Problem Using the Greedy Algorithm**

### **Step 1: Understand the Knapsack Problem**
- The **Knapsack Problem** is a classic optimization problem where we aim to **maximize the value** of selected items while ensuring the total **weight does not exceed** the knapsack's capacity.
- Each item has:
  - **Weight**: How much space it takes in the knapsack.
  - **Value**: The benefit or worth of the item.

---

### **Step 2: Define the Greedy Approach**
- **Greedy Algorithm Strategy**:
  - Select items based on a certain **greedy criteria**.
  - Continue selecting items until we **run out of space** in the knapsack.
- **Common greedy criteria**:
  1. **Maximum value** first.
  2. **Minimum weight** first.
  3. **Maximum value-to-weight ratio** first (**most efficient**).

In this project, we will use **value-to-weight ratio** as the criteria.

---

### **Step 3: Define the Problem in Code**
- Given:
  - A list of items, each with a weight and a value.
  - A knapsack with a fixed capacity.
- Output:
  - The selected items.
  - The maximum value that can be carried.

---

### **Step 4: Implement the Solution**
#### **1. Define the Item Class**
Create a Python class to represent an item.

```python
class Item:
    def __init__(self, name, value, weight):
        self.name = name  # Item name
        self.value = value  # Item value
        self.weight = weight  # Item weight
        self.ratio = value / weight  # Value-to-weight ratio

    def __repr__(self):
        return f"{self.name} (Value: {self.value}, Weight: {self.weight})"
```

---

#### **2. Implement the Greedy Algorithm**
- Sort items **by value-to-weight ratio** in descending order.
- Add items **until the knapsack is full**.

```python
def knapsack_greedy(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item.ratio, reverse=True)

    total_value = 0
    knapsack = []

    for item in items:
        if capacity >= item.weight:
            knapsack.append(item)
            total_value += item.value
            capacity -= item.weight
        else:
            # If we can't fit the whole item, take a fraction of it
            fraction = capacity / item.weight
            total_value += item.value * fraction
            knapsack.append(f"{item.name} (Partial: {fraction*100:.2f}%)")
            break

    return knapsack, total_value
```

---

#### **3. Test the Program**
Define some items and test the function.

```python
# List of items (name, value, weight)
items = [
    Item("Gold", 100, 10),
    Item("Silver", 60, 6),
    Item("Bronze", 40, 4),
    Item("Diamond", 120, 12),
]

# Define the knapsack capacity
capacity = 15

# Run the greedy algorithm
selected_items, max_value = knapsack_greedy(items, capacity)

# Display the results
print("Selected items:")
for item in selected_items:
    print(item)

print(f"\nMaximum value in knapsack: {max_value}")
```


## 📌 **Insertion Sort Tutorial**

Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time. It’s very intuitive and easy to understand, making it ideal for beginners.

### ✅ **Step-by-Step Explanation**

1. Start with the first element and consider it sorted.
2. Take the next element, and compare it with the elements already sorted.
3. Move the new element leftward until you find the correct position.
4. Repeat until the entire array is sorted.

---

### 🔍 **Visual Example**

Consider sorting the array `[5, 3, 4, 1, 2]`.

**Step-by-step sorting:**

```
Initial Array: [5, 3, 4, 1, 2]

Pass 1:
[3, 5, 4, 1, 2] - (3 is inserted before 5)

Pass 2:
[3, 4, 5, 1, 2] - (4 is inserted between 3 and 5)

Pass 3:
[1, 3, 4, 5, 2] - (1 moves to the front)

Pass 4:
[1, 2, 3, 4, 5] - (2 inserted between 1 and 3)

Sorted Array: [1, 2, 3, 4, 5]
```

---

### 🐍 **Implementation in Python**

Here's how you implement insertion sort in Python:

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i

        # Shift larger values to the right
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1

        # Insert current_value at the correct position
        arr[position] = current_value

# Example usage:
arr = [5, 3, 4, 1, 2]
print("Original Array:", arr)
insertion_sort(arr)
print("Sorted Array:", arr)
```

**Output:**

```
Original Array: [5, 3, 4, 1, 2]
Sorted Array: [1, 2, 3, 4, 5]
```

---

### 🎯 **Time Complexity**

| Case | Time Complexity |
|------|-----------------|
| Best Case | O(n) |
| Average Case | O(n²) |
| Worst Case | O(n²) |

- **Best Case:** When the array is already sorted.
- **Worst Case:** When the array is sorted in reverse order.

Insertion Sort works efficiently with small arrays or nearly sorted arrays.

---

### 💡 **Practice Problems**

Encourage students to practice by sorting these arrays manually and then verifying their solutions with Python code.

1. `[7, 2, 9, 1, 6]`
2. `[10, 4, 6, 8, 2, 1]`
3. `[4, 3, 2, 1]`

---

### 🚩 **Summary**

Insertion Sort is easy to understand and implement, and it’s great for introducing sorting algorithms. Its efficiency decreases for larger lists, making it suitable mainly for small datasets or partially sorted data.

Encourage your students to write the algorithm themselves and experiment with different data sets to deepen their understanding.

Happy teaching! 🚀
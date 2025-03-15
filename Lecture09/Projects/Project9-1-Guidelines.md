### **Step-by-Step Guidelines**

#### **Objective:**
Students will implement and compare different sorting algorithms in Python. They will measure the execution time of each algorithm and visualize the results using a graph.

---
### **Step 1: Understand Sorting Algorithms**
Before writing any code, students should understand the three sorting algorithms:
1. **Bubble Sort** - Repeatedly swaps adjacent elements if they are in the wrong order.
2. **Insertion Sort** - Builds a sorted list one element at a time by inserting each item in its correct position.
3. **Merge Sort** - Recursively divides the list into halves, sorts them, and merges them back together.

Students should research how these algorithms work and their time complexities:
- Bubble Sort: O(n^2)
- Insertion Sort: O(n^2)
- Merge Sort: O(n log n)

---
### **Step 2: Set Up the Project**
1. Create a new Python script (e.g., `sorting_race.py`).
2. Import necessary libraries:
   ```python
   import time
   import random
   import matplotlib.pyplot as plt
   ```
3. Define a function to generate random lists of numbers:
   ```python
   def generate_random_list(size, min_val=1, max_val=1000):
       return [random.randint(min_val, max_val) for _ in range(size)]
   ```

---
### **Step 3: Implement the Sorting Algorithms**
#### **Bubble Sort**
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

#### **Insertion Sort**
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
```

#### **Merge Sort**
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
```

---
### **Step 4: Measure Execution Time**
Create a function to measure the time taken by each sorting algorithm:
```python
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time
```

---
### **Step 5: Compare Sorting Algorithms**
1. Generate random lists of different sizes (e.g., 100, 500, 1000, 5000 elements).
2. Measure and store execution times for each sorting algorithm.
3. Plot the results using Matplotlib.

#### **Code to Compare and Visualize Performance**
```python
def compare_sorting_algorithms():
    sizes = [100, 500, 1000, 5000]
    algorithms = {'Bubble Sort': bubble_sort, 'Insertion Sort': insertion_sort, 'Merge Sort': merge_sort}
    results = {alg: [] for alg in algorithms}
    
    for size in sizes:
        random_list = generate_random_list(size)
        for name, func in algorithms.items():
            temp_list = random_list.copy()
            results[name].append(measure_time(func, temp_list))
    
    for name, times in results.items():
        plt.plot(sizes, times, label=name)
    
    plt.xlabel('List Size')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.show()

compare_sorting_algorithms()
```

---
### **Step 6: Analyze and Discuss Results**
Students should answer the following questions:
- Which sorting algorithm was the fastest?
- Why do Bubble Sort and Insertion Sort perform poorly on large lists?
- How does Merge Sort handle larger lists more efficiently?
- What factors affect sorting time (e.g., initial order of elements, data size)?


---
### **Final Thoughts**
This project helps students:
- Develop a deeper understanding of sorting algorithms.
- Improve problem-solving skills by implementing and comparing different approaches.
- Learn to measure execution time and visualize data.

By following these steps, students will gain hands-on experience in algorithm analysis and performance comparison in Python!


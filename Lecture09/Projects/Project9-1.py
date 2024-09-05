import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

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

def measure_sort_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def print_sort_times(sort_times):
    for sort_name, time_taken in sort_times.items():
        print(f"{sort_name}: {time_taken:.6f} seconds")

# Generate random lists and measure sorting times
list_size = 1000
random_list = [random.randint(0, 10000) for _ in range(list_size)]

# Copy lists for each sorting algorithm
list_bubble = random_list.copy()
list_insertion = random_list.copy()
list_merge = random_list.copy()

sort_times = {}
sort_times['Bubble Sort'] = measure_sort_time(bubble_sort, list_bubble)
sort_times['Insertion Sort'] = measure_sort_time(insertion_sort, list_insertion)
sort_times['Merge Sort'] = measure_sort_time(merge_sort, list_merge)

print_sort_times(sort_times)

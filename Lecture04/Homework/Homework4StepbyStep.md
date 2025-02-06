Here’s a step-by-step guideline to complete the **Dice Rolling Simulation** project.

---

## **Step 1: Understand the Problem**
We need to simulate rolling a **six-sided die** multiple times, count how often each face appears, and visualize the results using a **bar chart**.

---

## **Step 2: Break Down the Project**
The project consists of three main parts:
1. **Simulating Dice Rolls** – Using Python’s `random` module to generate random numbers between 1 and 6.
2. **Counting the Results** – Keeping track of how often each number appears.
3. **Visualizing the Data** – Creating a bar chart using `matplotlib`.

---

## **Step 3: Write the Code Step by Step**

### **1. Import Necessary Libraries**
Python provides built-in libraries to help us:
```python
import random
import matplotlib.pyplot as plt
```

### **2. Ask the User How Many Rolls They Want**
```python
num_rolls = int(input("Enter the number of times to roll the die: "))
```

### **3. Simulate Rolling the Die**
Create a dictionary to store the count of each face (1-6) and roll the die `num_rolls` times.
```python
# Initialize count dictionary
roll_counts = {i: 0 for i in range(1, 7)}

# Roll the die num_rolls times
for _ in range(num_rolls):
    roll = random.randint(1, 6)  # Generate a number between 1 and 6
    roll_counts[roll] += 1  # Update the count for that face
```

### **4. Display the Frequency of Rolls**
After rolling, print the frequency of each die face:
```python
print("\nResults:")
for face, count in roll_counts.items():
    print(f"Face {face}: {count} times")
```

### **5. Create a Bar Chart**
Use `matplotlib` to visualize the results:
```python
# Extract data for plotting
faces = list(roll_counts.keys())
counts = list(roll_counts.values())

# Create the bar chart
plt.bar(faces, counts, color='blue', edgecolor='black')
plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title(f"Results of Rolling a Die {num_rolls} Times")
plt.xticks(faces)  # Ensure the x-axis labels are correct
plt.show()
```

---

## **Step 4: Test the Program**
1. **Run the script.**
2. **Input a number (e.g., 100 or 1000).**
3. **Observe the output and the bar chart.**

---

## **Step 5: Encourage Experimentation**
- Try rolling the die **10, 100, 1000, and 10000 times** and observe how the frequencies become closer to equal with more rolls.
- Modify the code to simulate a **20-sided die (D20) used in tabletop games**.
- Change the program to roll **two dice at once** and analyze the sum of both dice.



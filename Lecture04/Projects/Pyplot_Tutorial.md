# **Introduction to `matplotlib.pyplot`**
`matplotlib.pyplot` is a Python library used for creating graphs and charts. It helps us visualize data in a simple and fun way.

## **1. Installing `matplotlib`**
Before we start, ensure `matplotlib` is installed. If it's not installed, run:

```python
pip install matplotlib
```

## **2. Importing `matplotlib.pyplot`**
We need to import `matplotlib.pyplot` before using it:

```python
import matplotlib.pyplot as plt
```

---

## **3. Drawing a Simple Line Graph**
Let’s plot a simple line graph to show how it works.

```python
import matplotlib.pyplot as plt

# Data for the graph
x = [1, 2, 3, 4, 5]  # X-axis values
y = [2, 4, 6, 8, 10]  # Y-axis values

# Plotting the graph
plt.plot(x, y)

# Adding labels
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Graph")

# Show the graph
plt.show()
```

📌 **Explanation:**
- `plt.plot(x, y)`: Draws a line graph.
- `plt.xlabel()`, `plt.ylabel()`, `plt.title()`: Add labels and a title.
- `plt.show()`: Displays the graph.

---

## **4. Creating a Bar Chart**
Bar charts are useful for comparing values.

```python
import matplotlib.pyplot as plt

# Data for the bar chart
categories = ["Apple", "Banana", "Cherry", "Date"]
values = [10, 15, 7, 12]

# Creating the bar chart
plt.bar(categories, values, color="blue")

# Adding labels and title
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.title("Fruit Quantity Bar Chart")

# Show the bar chart
plt.show()
```

📌 **Explanation:**
- `plt.bar(categories, values)`: Creates a bar chart.
- `color="blue"`: Changes bar color.
- Labels and titles make it easy to understand.

---

## **5. Drawing a Pie Chart**
Pie charts help show parts of a whole.

```python
import matplotlib.pyplot as plt

# Data for the pie chart
labels = ["Math", "Science", "English", "History"]
sizes = [25, 35, 20, 20]

# Creating the pie chart
plt.pie(sizes, labels=labels, autopct="%1.1f%%")

# Adding a title
plt.title("Time Spent on Subjects")

# Show the pie chart
plt.show()
```

📌 **Explanation:**
- `plt.pie(sizes, labels=labels)`: Creates a pie chart.
- `autopct="%1.1f%%"`: Shows percentages on the chart.

---

## **6. Adding Multiple Lines to a Graph**
We can plot multiple lines on the same graph.

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

# Plotting both lines
plt.plot(x, y1, label="Line 1", color="red", linestyle="--")
plt.plot(x, y2, label="Line 2", color="blue", linestyle="-.")

# Adding labels, title, and legend
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Multiple Lines Graph")
plt.legend()

# Show the graph
plt.show()
```

📌 **Explanation:**
- `label="Line 1"`: Adds labels to differentiate lines.
- `color="red"`: Changes line color.
- `linestyle="--"`: Changes line style.
- `plt.legend()`: Shows the legend.

---

## **7. Customizing Graphs**
We can change marker styles, colors, and more.

```python
import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Customizing the plot
plt.plot(x, y, marker="o", color="green", linestyle="dashed", linewidth=2, markersize=8)

# Adding labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Customized Line Graph")

# Show the graph
plt.show()
```

📌 **Explanation:**
- `marker="o"`: Adds circle markers.
- `color="green"`: Sets the line color.
- `linestyle="dashed"`: Changes the line style.
- `linewidth=2`: Sets line thickness.
- `markersize=8`: Adjusts marker size.

---

## **Conclusion**
Now, you know how to:
✅ Draw **line graphs**  
✅ Create **bar charts**  
✅ Use **pie charts**  
✅ Plot **multiple lines**  
✅ Customize **graphs**  

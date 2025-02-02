Here's a **beginner-friendly tutorial** on using Python's `turtle` module, designed for **middle school students**.

---

# **Python Turtle Tutorial for Middle School Students**
**Objective:** Learn how to use Python's `turtle` module to draw shapes and create fun graphics.

## **1. Introduction to Turtle**
Python's `turtle` module lets us draw by controlling a virtual turtle on the screen. The turtle can move, turn, change colors, and draw lines.

### **Getting Started**
1. Open **Python IDLE** or any code editor (such as VS Code or Thonny).
2. Create a new Python file (`turtle_drawing.py`).

### **First Turtle Program**
Copy and run this code:
```python
import turtle

# Create a turtle object
t = turtle.Turtle()

# Move forward by 100 pixels
t.forward(100)

# Turn right by 90 degrees
t.right(90)

# Move forward by 100 pixels
t.forward(100)

# Stop the window from closing immediately
turtle.done()
```
🎯 **What Happens?**  
A window opens, and the turtle moves forward and turns right.

---

## **2. Changing Turtle's Appearance**
We can change the turtle’s shape, speed, and color.

```python
import turtle

t = turtle.Turtle()

# Change turtle shape and color
t.shape("turtle")
t.color("blue")

# Move forward
t.forward(100)

turtle.done()
```
🛠 **Try changing the shape**: `"turtle"`, `"arrow"`, `"circle"`, `"square"`  
🎨 **Try changing the color**: `"red"`, `"green"`, `"yellow"`

---

## **3. Drawing Basic Shapes**
### **Draw a Square**
```python
import turtle

t = turtle.Turtle()

for _ in range(4):
    t.forward(100)
    t.right(90)

turtle.done()
```

### **Draw a Triangle**
```python
import turtle

t = turtle.Turtle()

for _ in range(3):
    t.forward(100)
    t.left(120)

turtle.done()
```

### **Draw a Circle**
```python
import turtle

t = turtle.Turtle()
t.circle(50)  # 50 is the radius

turtle.done()
```

---

## **4. Adding Colors**
We can fill shapes with colors.

```python
import turtle

t = turtle.Turtle()
t.color("purple")
t.begin_fill()

for _ in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()

turtle.done()
```
🎨 **Change `"purple"` to another color** to try different effects.

---

## **5. Drawing a Star**
```python
import turtle

t = turtle.Turtle()
t.color("gold")

for _ in range(5):
    t.forward(100)
    t.right(144)

turtle.done()
```

---

## **6. Making the Turtle Draw Randomly**
Let's make the turtle **move randomly** and change colors!

```python
import turtle
import random

t = turtle.Turtle()
t.speed(0)  # Fastest speed
colors = ["red", "blue", "green", "purple", "orange"]

for _ in range(20):
    t.color(random.choice(colors))  # Choose a random color
    t.forward(random.randint(50, 150))  # Move a random distance
    t.right(random.randint(30, 180))  # Turn a random angle

turtle.done()
```
🎲 **What Happens?**  
The turtle draws **random** colorful lines every time you run the code!

---

## **7. Challenge: Draw a Rainbow Spiral**
```python
import turtle
import random

t = turtle.Turtle()
t.speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(100):
    t.color(colors[i % 6])  # Cycle through colors
    t.forward(i * 2)  # Increase step size
    t.right(59)  # Change turning angle

turtle.done()
```
🌈 **What Happens?**  
A colorful spiral pattern appears!

---

## **8. Bonus: Make the Turtle Follow Your Mouse**
```python
import turtle

t = turtle.Turtle()
t.speed(0)

def move_turtle(x, y):
    t.goto(x, y)

turtle.onscreenclick(move_turtle)  # Move the turtle when clicking

turtle.done()
```
🖱️ **Click anywhere on the screen**, and the turtle will follow your mouse!

---

### **Next Steps**
- Experiment with different shapes and angles.
- Combine loops (`for` and `while`) with turtle movements.
- Try making a **simple game** like a **drawing app** or **racing game**.
# Turtle Basics Tutorial for Middle School Students
# Let's learn how to draw shapes and patterns using Python's turtle library!

import turtle

# Step 1: Set up the screen and turtle
screen = turtle.Screen()
screen.title("Turtle Tutorial for Middle Schoolers")
screen.bgcolor("lightblue")  # Background color of the screen

# Create a turtle named "artist"
artist = turtle.Turtle()
artist.shape("turtle")  # Turtle shape
artist.color("green")   # Turtle color
artist.speed(2)         # Speed of drawing (1-10, 10 is fastest)

# Step 2: Draw a square
def draw_square():
    for _ in range(4):
        artist.forward(100)  # Move forward by 100 units
        artist.left(90)      # Turn left by 90 degrees

# Call the function to draw a square
draw_square()

# Step 3: Draw a triangle
def draw_triangle():
    artist.penup()
    artist.goto(-150, 0)  # Move to a new starting position
    artist.pendown()
    artist.color("blue")  # Change color for the triangle

    for _ in range(3):
        artist.forward(100)
        artist.left(120)   # Turn left by 120 degrees to form a triangle

# Call the function to draw a triangle
draw_triangle()

# Step 4: Draw a circle
def draw_circle():
    artist.penup()
    artist.goto(150, 0)   # Move to a new starting position
    artist.pendown()
    artist.color("red")   # Change color for the circle
    artist.circle(50)     # Radius of the circle is 50

# Call the function to draw a circle
draw_circle()

# Step 5: Experiment with colors and patterns
def draw_pattern():
    artist.penup()
    artist.goto(0, -150)
    artist.pendown()
    artist.color("purple")

    for i in range(36):       # Draw 36 times to make a circular pattern
        artist.forward(100)
        artist.left(170)      # Turn left by 170 degrees for the pattern

# Call the function to draw a pattern
draw_pattern()

# Finish up
turtle.done()

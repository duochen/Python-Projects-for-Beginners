import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set up the turtle
artist = turtle.Turtle()
artist.speed(0)
artist.hideturtle()

# Randomly generate shapes
def draw_random_shape():
    shape_type = random.choice(["circle", "rectangle", "line"])
    color = (random.random(), random.random(), random.random())
    artist.color(color)
    artist.penup()
    artist.goto(random.randint(-300, 300), random.randint(-300, 300))
    artist.pendown()
    
    if shape_type == "circle":
        radius = random.randint(10, 100)
        artist.begin_fill()
        artist.circle(radius)
        artist.end_fill()
    elif shape_type == "rectangle":
        width = random.randint(50, 200)
        height = random.randint(20, 100)
        artist.begin_fill()
        for _ in range(2):
            artist.forward(width)
            artist.right(90)
            artist.forward(height)
            artist.right(90)
        artist.end_fill()
    elif shape_type == "line":
        length = random.randint(50, 200)
        artist.pensize(random.randint(1, 10))
        artist.forward(length)
        
# Generate multiple shapes
for _ in range(20):
    draw_random_shape()

# End the drawing
turtle.done()

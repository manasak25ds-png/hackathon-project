import turtle
import math
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heartbeat Animation 💓")

# Create turtle
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(2)
pen.pensize(2)

# Function to draw a heart with a given scale
def draw_heart(scale=1.0, color="pink"):
    pen.clear()
    pen.penup()
    pen.goto(0, -100 * scale)  # Move to starting position
    pen.pendown()
    pen.color(color)
    pen.begin_fill()

    pen.left(140)
    pen.forward(111.65 * scale)
    for _ in range(200):
        pen.right(1)
        pen.forward(1.1 * scale)
    pen.left(120)
    for _ in range(200):
        pen.right(1)
        pen.forward(1.1 * scale)
    pen.forward(111.65 * scale)
    pen.end_fill()
    pen.setheading(0)  # Reset orientation

# Heartbeat animation loop
scale = 1.0
direction = 1
colors = ["#ff69b4", "#ff1493", "#ff85a2"]  # Pink shades

try:
    while True:
        draw_heart(scale, colors[int(time.time() * 5) % len(colors)])
        scale += 0.02 * direction
        if scale >= 1.1:
            direction = -1
        elif scale <= 1.0:
            direction = 1
        time.sleep(0.02)  # Control speed
except turtle.Terminator:
    pass  # Handle window close gracefully

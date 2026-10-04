import turtle
import time

def draw_heart(size, color):
    """Draws a heart shape with given size and color."""
    turtle.color(color)
    turtle.begin_fill()
    turtle.left(50)
    turtle.forward(size)
    turtle.circle(size / 2, 180)
    turtle.right(100)
    turtle.circle(size / 2, 180)
    turtle.forward(size)
    turtle.end_fill()

def heartbeat_animation():
    """Animates a heartbeat effect."""
    turtle.bgcolor("black")
    turtle.speed(0)  # Fastest drawing
    turtle.hideturtle()

    sizes = [100, 120, 140, 120, 100]  # Pulse sizes
    colors = ["red", "#ff4d4d", "#ff1a1a", "#ff4d4d", "red"]

    while True:
        turtle.clear()
        turtle.up()
        turtle.goto(0, -150)  # Position heart
        turtle.down()

        for size, color in zip(sizes, colors):
            turtle.clear()
            turtle.up()
            turtle.goto(0, -150)
            turtle.down()
            draw_heart(size, color)
            time.sleep(0.1)  # Delay for pulse effect

try:
    heartbeat_animation()
except turtle.Terminator:
    print("Heartbeat animation stopped.")
except Exception as e:
    print(f"Error: {e}")
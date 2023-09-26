import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

# Turtle setup
artist = turtle.Turtle()
artist.color("white")
artist.hideturtle()
artist.speed(0)

# Function to draw a building
def draw_building(x, y, width, height):
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.begin_fill()
    artist.color("grey")
    for _ in range(2):
        artist.forward(width)
        artist.left(90)
        artist.forward(height)
        artist.left(90)
    artist.end_fill()

# Function to draw windows
def draw_windows(x, y, width, height, rows, cols):
    window_width = width // cols
    window_height = height // rows
    artist.color("white")
    for r in range(rows):
        for c in range(cols):
            if random.random() > 0.95:  # Randomly decide whether to draw a window
                artist.penup()
                artist.goto(x + c * window_width, y + r * window_height)
                artist.pendown()
                artist.begin_fill()
                for _ in range(4):
                    artist.forward(window_width)
                    artist.left(90)
                artist.end_fill()

# Function to draw stars
def draw_stars(num_stars):
    artist.color("white")
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        if y > 0:  
            artist.penup()
            artist.goto(x, y)
            artist.pendown()
            artist.dot(random.randint(1, 3))

# Drawing buildings
building_specs = [
    (-150, -150, 80, 150),
    (-70, -150, 70, 100),
    (0, -150, 60, 200),
    (60, -150, 50, 170),
    (110, -150, 40, 140),
    (150, -150, 60, 180),
    (210, -150, 50, 160),
]

# First draw the buildings
for spec in building_specs:
    draw_building(*spec)

# Then add the windows
for spec in building_specs:
    draw_windows(*spec, rows=10, cols=4)

# Drawing stars
draw_stars(50)

# Hide turtle and close on click
artist.hideturtle()
screen.mainloop()
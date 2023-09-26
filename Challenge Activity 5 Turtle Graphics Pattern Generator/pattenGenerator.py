import turtle

# Initialize turtle instance
pen = turtle.Turtle()
screen = turtle.Screen()

# Set pen size to 3 for thicker lines
pen.pensize(3)
pen.speed(0)

# Move turtle to the starting position
pen.up()
pen.goto(-150, 0)
pen.down()

# Draw the first diamond
pen.goto(-50, 100)
pen.goto(50, 0)
pen.goto(-50, -100)
pen.goto(-150, 0)

# Move to the starting position for the second diamond
pen.up()
pen.goto(50, 0)
pen.down()

# Draw the second diamond
pen.goto(150, 100)
pen.goto(250, 0)
pen.goto(150, -100)
pen.goto(50, 0)

# Hide the turtle and close the drawing environment
pen.hideturtle()
screen.mainloop()
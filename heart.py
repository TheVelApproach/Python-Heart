import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.color("red")
pen.fillcolor("red")
pen.speed(3)  # Moderate speed, completes in a few seconds

# Draw heart shape
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

# Hide the turtle and keep the window open
pen.hideturtle()
screen.exitonclick()
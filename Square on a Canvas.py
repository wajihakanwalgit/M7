import turtle


screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Square with Turtle")

pen = turtle.Turtle()
pen.pensize(3)
pen.color("black", "orange")  

pen.begin_fill()
for _ in range(4):
    pen.forward(100)
    pen.left(90)
pen.end_fill()

turtle.done()

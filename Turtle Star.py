import turtle


screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Star with Turtle")


star = turtle.Turtle()
star.color("yellow")
star.pensize(2)
star.speed(5)


for _ in range(5):
    star.forward(200)
    star.right(144)  


star.hideturtle()
turtle.done()

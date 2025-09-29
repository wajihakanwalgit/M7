import turtle

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Polygons with Turtle")


pen = turtle.Turtle()
pen.pensize(3)
pen.speed(5)

def draw_polygon(sides, length, color, fill_color, start_pos):
    pen.penup()
    pen.goto(start_pos)   
    pen.color(color, fill_color)  
    pen.begin_fill()
    for _ in range(sides):
        pen.forward(length)
        pen.left(360 / sides)
    pen.end_fill()

draw_polygon(3, 100, "black", "yellow", (-200, 100))

pen.penup()
pen.goto(-50, 100)
pen.pendown()
pen.color("black", "green")
pen.begin_fill()
for _ in range(2):
    pen.forward(150)
    pen.left(90)
    pen.forward(80)
    pen.left(90)
pen.end_fill()


draw_polygon(6, 70, "black", "red", (200, 100))


pen.hideturtle()


turtle.done()

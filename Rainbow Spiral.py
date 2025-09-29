
import turtle
import colorsys


screen = turtle.Screen()
screen.bgcolor("black")


spiral = turtle.Turtle()
spiral.speed(0) 

num_colors = 36
colors = [colorsys.hsv_to_rgb(i/num_colors, 1, 1) for i in range(num_colors)]


turtle.colormode(1.0)  
for i in range(360):
    color = colors[i % num_colors]
    spiral.color(color)
    spiral.forward(i * 2)
    spiral.right(59)


turtle.done()

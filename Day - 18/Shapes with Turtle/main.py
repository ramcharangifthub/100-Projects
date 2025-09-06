import turtle as t
import random 
tim = t.Turtle()

colors = ["light cyan","ivory","medium slate blue","orchid"]

def draw_shape(num_of_sides):
    angle = 360/num_of_sides
    for x in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


for y in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(y)

screen = t.Screen()
screen.exitonclick()


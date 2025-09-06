import random 
import turtle as t

tim = t.Turtle()

tim.speed("slow")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
tim.speed("fastest")

def draw_spirograph(size_of_graph):
    for x in range(int(360/size_of_graph)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + 10)
        tim.circle(100)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
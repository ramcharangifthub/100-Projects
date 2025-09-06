import random 
import turtle as t

tim = t.Turtle()

direction = [0,90,120,180,270]
tim.pensize(15)
colors = ["blue","dark green","firebrick","black","red"]
tim.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

for  x in range(200):

    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

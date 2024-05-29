import turtle as t
import random as ran


carlos = t.Turtle()
t.colormode(255)
def random_color():
    r = ran.randint(0,255)
    g = ran.randint(0, 255)
    b = ran.randint(0, 255)
    tu_color = (r, g, b)
    return tu_color

carlos.speed(0)


def draw_spirograph(size):
    """draw a spirograph"""
    for i in range(int(360/size)):
        carlos.color(random_color())
        carlos.circle(120)
        #set the heading
        carlos.setheading(carlos.heading() + size)


draw_spirograph(5)


# for x in range(100):
#     carlos.speed(0)
#     carlos.color(random_color())
#     carlos.circle(120)
#     carlos.right(5)

screen =t.Screen()
screen.exitonclick()
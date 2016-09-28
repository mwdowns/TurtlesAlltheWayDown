from turtle import *
from shapes import *
import random

bgcolor("black")

# square(100, "red", "black")
#
# home()
# setheading(270)
# up()
# forward(200)
# down()
#
#
# triangle(100, "blue", "yellow")

# up()
# forward(300)
# down()
#


def starSky():
    ticks = 0
    starColor = ["yellow", "red", "lightblue", "pink", "lightgreen", "white", "orange", "magenta"]
    star(10, "black", "yellow")
    while ticks < 20:
        home()
        setheading(random.randrange(0, 360, 1))
        up()
        forward(random.randrange(10, 300, 1))
        down()
        ticks += 1
        star((random.randrange(5, 30, 1)), "black", starColor[random.randrange(0, len(starColor), 1)])
        up()
    if ticks == 20:
        home()
        mainloop()

starSky()


#
# up()
# right(90)
# forward(100)
# down()
#
# pentagon(100)
#
# up()
# right(160)
# forward(300)
# left(90)
# forward(50)
# down()
#
# octagon(100)
#
# up()
# right(170)
# forward(100)
# down()
#
# hexagon(100)
#
# up()
# right(90)
# forward(100)
# down()

# circle(.5)

from turtle import *

def triangle(size, color1, color2):
    setheading(60)
    color(color1, color2)
    begin_fill()
    for i in range(3):
        forward(size)
        right(120)
    end_fill()
    # mainloop()

# triangle()

def square(size, color1, color2):
    color(color1, color2)
    begin_fill()
    for i in range(4):
        forward(size)
        right(90)
    end_fill()
    # mainloop()
# square()

def pentagon(size, color1, color2):
    color(color1, color2)
    begin_fill()
    for i in range(5):
        forward(size)
        right(72)
    end_fill()
    # mainloop()
# pentagon()

def hexagon(size, color1, color2):
    color(color1, color2)
    begin_fill()
    for i in range(6):
        forward(size)
        right(60)
    end_fill()
    # mainloop()
# hexagon()

def octagon(size, color1, color2):
    color(color1, color2)
    begin_fill()
    for i in range(8):
        forward(size)
        right(45)
    end_fill()
    # mainloop()
# octagon()

def star(size, color1, color2):
    color(color1, color2)
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
        forward(size)
        left(72)
    end_fill()
    # mainloop()
# star()

def circle(size, color1, color2):
    color(color1, color2)
    begin_fill()
    for i in range(360):
        forward(size)
        right(1)
    end_fill()
    # mainloop()
# circle()

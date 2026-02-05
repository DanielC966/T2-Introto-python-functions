import turtle
from turtle import *
t = Turtle()
t.speed(0)

def square(angle, length):
    for i in range(4):
        t.forward(120)
        t.right(90)


for i in range(60):
    x=5
    y=5
    square(x, y)
    t.right(5)
    t.forward(5)
turtle.done()
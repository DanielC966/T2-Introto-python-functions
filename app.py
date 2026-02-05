import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed('fastest')

def square(x):
    for i in range(4):
        t.forward(x)
        t.left(90)
def invsquare(x):
    for i in range(4):
        t.forward(x)
        t.right(90)
def backsquare(x):
    for i in range(4):
        t.backward(x)
        t.right(90)  
def bottomleftsquare(x):
    for i in range(4):
        t.backward(x)
        t.left(90)


x=200
size=[5, 7, 8]

for i in range(4):
    square(x)
    invsquare(x)
    backsquare(x)
    bottomleftsquare(x)
    x+=30
    t.shapesize(size[0]+15, size[1]+15, size[2]+15)


turtle.done()
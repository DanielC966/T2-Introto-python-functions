import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

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
        t.forward(x)
        t.right(90)  

square(200)
invsquare(200)
t.shapesize(5, 7, 8)


turtle.done()
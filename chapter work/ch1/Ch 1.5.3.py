import turtle
turtle
gertrude = turtle.Turtle()
gertrude
gertrude.forward(100)
gertrude.right(90)
gertrude.forward(50)
gertrude.position()
gertrude.heading()

def drawSquare (myTurtle, sideLength) :
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    
from ds import *
import turtle
t= turtle.Turtle()
drawSquare(t,150)
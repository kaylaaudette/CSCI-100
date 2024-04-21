# Name: Kayla Audette
# HW 2

import turtle
import math

# put function definitions here

# modify this function
def drawSquare(myTurtle, sideLength, sideLength2):
    myTurtle.forward(sideLength2)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength2)
    myTurtle.right(90)
    myTurtle.forward(sideLength)

def drawRectangle(myTurtle, width, height):
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(height)
    myTurtle.right(90)
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(height)
    
def question3():
    for pos in range(-10, 11, 1): # (start, stop, step):
        print(pos)

def question4():
    for neg in range(10, -11, -1): # you go by a negtive if you want to start postive (math duh)
        print(neg)
    
# modify this function
def drawDoubleSpiral(firstTurtle, secondTurtle, maxSide):
    for sideLength in range(10, maxSide+1, 5):
        firstTurtle.forward(sideLength)
        firstTurtle.right(130)
        secondTurtle.forward(sideLength)
        secondTurtle.left(130)
   
def question6(myTurtle):
    startX = -100
    startY = startX/3 - 300
    myTurtle.up()
    myTurtle.goto(startX, startY) # moves turtle 
    
    myTurtle.down()
    endX = 100
    endY = endX/3 - 300
    myTurtle.goto(endX, endY)

# all function calls go under here
if __name__ == "__main__":
    # Comment out the function calls as you work through the homework
    ivy = turtle.Turtle()
    ivy.color('red')
    ivy.speed('fastest')
    ivy.begin_fill()
    
    ### Q1 [2 pts]
    ### Modify the drawSquare function to draw a rectangle whose horizontal width
    ### is twice the vertical width
    drawSquare(ivy, 100, 250)
    ivy.end_fill()


    ### Q2 [2 pts]
    ### Create a new function drawRectangle that takes three parameters:
    ### myTurtle, width, and height. Uncomment the line below to test it.
    width = 50
    height = 100
    ivy.color('black')
    drawRectangle(ivy, width, height) 

    ### Q3 [1 pts]
    ### Modify the function question3
    ### Use the range function to print out all numbers from -10 to 10.
    ### Uncomment the line below to test it
    question3()


    ### Q4 [1 pts]
    ### Modify the function question4
    ### Use the range function to print out all numbers from 10 to -10
    ### Uncomment the line below to test it
    question4()
    
    
    
    ### Q5 [2 pts]
    ### The drawDoubleSpiral function only takes one turtle and draws one spiral.
    ### Modify it to use a second turtle and create two spirals in opposite directions.
    ### Uncomment the line below to test it.
    turtle1 = turtle.Turtle()
    turtle2 = turtle.Turtle()
    turtle1.color('green')
    turtle2.color('blue')
    turtle1.speed('fastest')
    turtle2.speed('fastest')
    drawDoubleSpiral(turtle1, turtle2, 300) 

    
    ### Q6 [2 pts]
    ### Modify the function question6. Plot the function y = x/3 - 300
    ### Use x-coordinates from -100 to 100.
    ### Uncomment the line below to test it.
    bob = turtle.Turtle()
    question6(bob)

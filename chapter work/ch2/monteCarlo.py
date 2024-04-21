# Kayla Audette

import math
import random
import turtle 

def montePi(numDarts):
    inCircle = 0       
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)   
        if d <= 1:
            inCircle = inCircle + 1
    pi = inCircle/numDarts * 4
    return pi

#print(montePi(100))
#print(montePi(100))
#print(montePi(100))
#print(montePi(100))

# we got different numbers each time for the approximation for Pi
# this is beacuse we are using fucntions from the random moledule
# this will generate a random  number between 0 and 1. 

def showMontePi(numDarts):
    wn = turtle.Screen()
    #wn.bgcolor("light green")
    wn.bgcolor("light blue")
    #wn.setworldcoordinates(-2,-2,2,2)
    wn.setworldcoordinates(0,0,2,2) # makes it only upper-right quadrant


    drawingT = turtle.Turtle()

    drawingT.up()
    drawingT.goto(-1,0)
    drawingT.down()
    drawingT.goto(1,0)

    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(0,-1)

    circle = 0
    drawingT.up()
    turtle.tracer(2,1) # tell turtle module to update display quickly
    
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)
        drawingT.goto(x,y)
        if d <= 1:
            circle = circle + 1
            drawingT.color("blue")
        else:
            drawingT.color("red")            
        drawingT.dot()
        
    pi = circle/numDarts * 4
    return pi

#showMontePi(50)
#showMontePi(100)

#The wn.setworldcoordinates(-2,-2,2,2) changes the coordinates shown in the graphics window

#Finsih early

#1 The Monete carlo method is more accurate at large values 
# showMontePi(10000)
#2

def monteCircle(numDarts):
    wn = turtle.Screen()
    wn.bgcolor("light blue")
    wn.setworldcoordinates(-2,-2,2,2)


    drawingT = turtle.Turtle()

    drawingT.up()
    drawingT.goto(-1,0)
    drawingT.down()
    drawingT.goto(1,0)

    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(0,-1)

    circle = 0
    drawingT.up()
    turtle.tracer(2,1)     
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)
        drawingT.goto(x,y)
        if d <= 1:
            circle = circle + 1
            drawingT.color("blue")
            drawingT.dot()
            
        else:
            drawingT.color("red")
            
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)
        drawingT.goto(-x,y)
        if d <= 1:
            circle = circle + 1
            drawingT.color("blue")
            drawingT.dot()
            
        else:
            drawingT.color("red")
        
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)
        drawingT.goto(-x,-y)
        if d <= 1:
            circle = circle + 1
            drawingT.color("blue")
            drawingT.dot()
            
        else:
            drawingT.color("red")
            
    for i in range(numDarts):
        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)
        drawingT.goto(x,-y)
        if d <= 1:
            circle = circle + 1
            drawingT.color("blue")
            drawingT.dot()
            
        else:
            drawingT.color("red")
        
    pi = circle/numDarts * 4
    return pi

monteCircle(100)
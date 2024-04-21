# Kayla Audette

import turtle
import math
import random

## Option A: For loops are still hard.

# Q1: Write a for loop to compute the sum of the first 50 numbers (1+2+3+….+49+50).
def sum50():
    acc = 0
    for x in range(1, 50):
        acc = acc + x
    return acc

# Q2: Write a for loop to compute the n! (1∗2∗3∗...∗n)
def compute(n):
    acc = 0
    for x in range(1, n+1):
        acc = n * n-1 
    return acc

# Q3: Write a for loop that draws a square with a turtle.
def square(myTurtle, sideLength):
    for i in range(4): 
        myTurtle.forward(sideLength)
        myTurtle.left(90)

# Q4 Write a for loop that prints out the numbers -10, -9, -8, …., 9, 10.
def loop():
    for i in range(-10, 11, 1): #(start, stop, step)
        print(i)

## Option B: Turtles are still hard.

#Q1: Use a turtle to plot the function y = 10x + 18
def question1(myTurtle):
    startX = 0
    startY = startX*10 + 18
    myTurtle.up()
    myTurtle.goto(startX, startY) # moves turtle 
    
    myTurtle.down()
    endX = 10
    endY = endX*10 + 18
    myTurtle.goto(endX, endY)
    
#Q2: Use a turtle to draw a yellow triangle with a red background
def drawTriangle(sideLength):
    gwen = turtle.Turtle()
    gwen.shape("turtle") # makes cursor look like a turtle
    gwen.pencolor('yellow') # adds color to the line
    gwen.fillcolor('red') # adds fill (when it begins and ends 43 and 45) 
    gwen.begin_fill()
    for i in range(3): 
        gwen.forward(sideLength)
        gwen.left(120)
    gwen.end_fill()

#Q3: Use a turtle to draw a rectangle with width 300 and height 100
def drawRectangle(myTurtle, width, height):
    myTurtle.shape("turtle")
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(height)
    myTurtle.right(90)
    myTurtle.forward(width)
    myTurtle.right(90)
    myTurtle.forward(height)
    
## Option C: Functions are still hard.

# Q1: Write a function that uses a turtle to draw a polygon that has n sides.
def drawPolygon(myTurtle, sideLength, n):
    for i in range(n):
        myTurtle.shape("turtle")
        myTurtle.forward(sideLength)
        myTurtle.right(360/n)

# Q2: Write a function that takes one parameter for a person’s name and prints out “Hello” to that person.
def Hello(name):
    print("Hello", name)

# Q3: Write a function that returns the minimum of three numbers.
def minOfThree(a, b, c):
    if ((a < b) and (a < c)):
        return a
    if ((a > b) and (b < c)):
        return b
    if ((a > c) and (b > c)):
        return c

## Option D: If statements are booleans are still hard.

# Q1 Write a function that returns True if x is larger than 10 and returns False otherwise.
def function1(x):
    if x > 10:
        return True
    else:
        return False
    
# Q2 Write a function that returns True if and only if variable x is non-negative.
def function2(x):
    if x >= 0:
        return True
    else:
        return False

# Q3 Write a nested if statement that uses a variable snowFall and prints out:

def snow(snowFall):
    if snowFall >= 10:
        snow = "there was a hurricane today"
        return snow
    if 10 >= snowFall >= 7:
        snow = "there was some snow I guess"
        return snow
    if snowFall <= 3:
        snow = "not enough snow to matter"
        return snow
    else:
        snow = "??"
        return
    
## Option E: Random things are still hard. ##
import random

# Create a function called isItRaining which returns False with 90% probability.
def isItRaining():
    x = random.random()
    if x <= 0.9:
        return False
    else:
        return True

# Create a function called magicEightBallSays which randomly prints one of the following:
def magicEightBallSays():
     x = random.random()
"It is certain."
"Outlook good."
"Ask again later."
"Better not tell you now."
"Very doubtful"
    
#Create a variable called grade which randomly has the value A,B,C,D, or F.



#Create a variable called coinSide which randomly has the value 0 or 1.


print("------Option A--------")
# Q1
print ("Q1:", sum50())
# Q2
print ("Q2:", compute(10))
# Q3
bob = turtle.Turtle()
square(bob, 100)
# Q4
loop()
print("------Option B--------")
# Q1
bob = turtle.Turtle()
question1(bob)

#Q2
drawTriangle(200)

#Q3
bob.pencolor('green') # adds color to the line
bob.fillcolor('green') # adds fill (when it begins and ends 43 and 45) 
bob.begin_fill()
width = 300
height = 100
drawRectangle(bob, width, height)
bob.end_fill()

print("------Option C--------")
#Q1
liz = turtle.Turtle()
liz.pencolor('blue') # adds color to the line
liz.fillcolor('blue') # adds fill (when it begins and ends 43 and 45) 
liz.begin_fill()
drawPolygon(liz, 40, 10)
liz.end_fill()

#Q2
Hello("kylie")

#Q3
print("Q3:", minOfThree(3, 6, 1))

print("------Option D--------")

#Q1
print("Q1:", function1(10))

#Q2
print("Q2:", function2(-10))

#Q3
print("Q3:", snow(20))
print("Q3:",snow(7))
print("Q3:",snow(2))

print("------Option E--------")

print("Q1,", isItRaining())
print(magicEightBallSays())

print("----------------------")
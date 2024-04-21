# Kayla Audette

import turtle

# define your functions here (import statements than defintions and than all the call functions)
def printManyThings():
    for i in range(5, 101, 5): # 101 went over so you could see the final vaule (100)
        print(i) #prints the loop

def drawSpiral(myTurtle, maxSide):
    for sideLength in range(1, maxSide+1, 5):
        myTurtle.forward(sideLength)
        myTurtle.right(90)
       
def drawTriangle(myTurtle, sideLength1, sideLength2, angle):
    myTurtle.goto(90,0)
    myTurtle.forward(sideLength1)
    myTurtle.right(180-angle)

def drawOctagon(myTurtle, sideLength):
    for i in range(8):
        myTurtle.forward(sideLength)
        myTurtle.right(45)

def drawPolygon(myTurtle, sideLength, numSide):
   turnAngle = 360 / numSide
   for i in range(numSide):
      myTurtle.forward(sideLength)
      myTurtle.right(turnAngle)

def drawCircle(myTurtle, radius):
   circumference = 2*3.14*radius
   sideLen = circumference / 360 # note that 360 is the number of sides
   drawPolygon(myTurtle, sideLen, 360)
   
# call your functions here
printManyThings()

bob = turtle.Turtle()
bob.speed('fastest') # this makes bob run really fast

drawSpiral(bob,90) # makes a square sprial (maxSide is 90)
print("answer to question 3 is: 18")

drawTriangle(bob, 80, 480, 30) #this makes a triangle

drawOctagon(bob, 60) #this makes a octagon (8 sides)

drawPolygon(bob, 80, 3) # this makes a triangle 

drawPolygon(bob, 80, 6) # this makes an hexagon

bob.fillcolor('red') # doing this adds fill 
bob.begin_fill()
drawPolygon(bob, 80, 6)
bob.end_fill()
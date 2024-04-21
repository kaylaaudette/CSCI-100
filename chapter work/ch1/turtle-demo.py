# Kayla Audette
import turtle

# using these dashes ''' allows for this section to not be read by the program
'''
jane = turtle.Turtle()
print(jane)
print("Original Position:", jane.position())
jane.forward(100)
jane.right(90)
jane.shape("turtle") 
jane.forward(50)
print("current position:", jane.position())
print("Direction:", jane.heading())
'''

#drawing a square
def drawSquare(myTurtle,sideLength):
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)
    myTurtle.forward(sideLength)
    myTurtle.right(90)

bob = turtle.Turtle()
bob.shape("turtle") # makes cursor look like a turtle
# turtle.delay(50) slows down the turtle 
bob.pencolor('red') # adds color to the line
bob.fillcolor('blue') # adds fill (when it begins and ends 43 and 45) 
bob.begin_fill()
drawSquare(bob, 100)
bob.end_fill()

# drawing a triangle
def drawTriangle(myTurtle,sideLength):
    myTurtle.forward(sideLength)
    myTurtle.left(120)
    myTurtle.forward(sideLength)
    myTurtle.left(120)
    myTurtle.forward(sideLength)
    
# Add color and make a turtle (I changed to green and added turtle)
bob = turtle.Turtle()
bob.shape("turtle") # makes cursor look like a turtle
bob.pencolor('green') # adds color to the line
bob.fillcolor('green') # adds fill (when it begins and ends 43 and 45) 
bob.begin_fill()
drawTriangle(bob,200)
drawTriangle(bob, 400) #this is what changed the size 
bob.end_fill()
# Part 1: Turtles

# This loads the turtle module allowing for the use of its fuctions.
import turtle
   
# This creates a turtle object called ada.
ada = turtle.Turtle()
ada.shape("turtle") 
   
# These move ada around.
ada.goto(100,100)# move to the (x,y) coordinate given (two arguments).
ada.forward(200) # moves ada forward 200 pixels (one argument).
ada.right(90)    # directs ada 90 degrees to the right (one argument).
ada.forward(50)  # moves ada forward 50 pixels (one argument).
   
print("Where is ada? ", ada.position())       # prints the position of ada (two arguments, 1st names what is describing 2nd calls function).
print("Where is ada headed? ", ada.heading()) # counterclockwise degrees from right/east(two arguments, same thing).

# Can store function in a varible. 
'''
pos = ada.position()
print(pos) 
'''

# This allows for the lines to not happen behind the turtle (ada) until the pen is back down.
ada.right(90)
ada.up()         # pick up the pen (ada).
ada.forward(150) 
ada.down()       # put down the pen (ada).
ada.forward(50)
   
   
# Defining our own fuction with 'def' and the name of our function.
# Here we pass any number of parameters.
# All code part of this fuction must be indented by a tab character.
def skipForward(bob, hopCount): #two parameters (bob and hopCount)
    bob.up() # doesn't matter what we name it, it does not have to be named ada.
    bob.forward(hopCount) # we can use bob beacsue we are not intiallizing bob to be anything. 
    bob.down() # you can use any turtle with this fuction (whatever our frist argument is).
    bob.forward(hopCount)
   
# This code isn't indented. It is not par tof the function.
# Here, we call/invoke the fuction and give it arguments.
skipForward(ada, 20) # by calling the fuction (skipForward) we preform the action.  
skipForward(ada, 30) # they all have two arguments (ada and #).
skipForward(ada, 50)

# Define a drawpentagon fuction that takes one parameter (length)
def drawPentagon(length):
    kayla = turtle.Turtle()
    kayla.shape("turtle") 
    kayla.forward(length) #as long as it is the same parameter name you can call it anything
    kayla.right(360 / 5)
    kayla.forward(length) 
    kayla.right(360 / 5)
    kayla.forward(length) 
    kayla.right(360 / 5)
    kayla.forward(length) 
    kayla.right(360 / 5)
    kayla.forward(length) 
  
drawPentagon(50) #there is only one parameter so you just put length
drawPentagon(100)
drawPentagon(200)
    
# Part 2: Other functions

def add(x, y):
    result = x + y
    print(result) # this allows us to see the result in the shell
    
add(10, 30) #call/invoking fuction add(two argument)
add(524, 320) #call/invoking (two argument)

def subtract(x, y):
    result = x - y 
    print(result) # this allows us to see the result in the shell
    
subtract(10, 3) #call/invoking (two arguments)

    
def hello(name):
    print(name)
    
hello("Hello, Heather") #call/invoking 
hello("Welcome to CS 100") #call/invoking 
hello("Have an awesome day!") #call/invoking 

# Comment
# The fuctions we made add, subratact and hello are difference from position() and heading() 
# as you can store the functions position() and heading() in a varible than print that varible
pos = ada.position()
print(pos) 
# whereas for the functions we just made (add, subtract and hello) they cannot be stored in a varible 
# as it would be missing either one or two arguments (one for hello, two for subtract and add).

# Part 3: More Fuctions 

def circleArea(radius): #1 parameter
    area= pi * radius ** 2
    print(area)
    
circleArea(5) #call/invoking fuction (one argument)

def rectangleArea(width, height): #2 parameter
    area= width * height
    print(area)

rectangleArea(2, 7) #call/invoking (two arguments)

def squareArea(sideLength): #1 parameter
    area= sideLength ** 2
    print(area)

squareArea(8) #call/invoking (one argument)
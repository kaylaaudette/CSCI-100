import turtle 

# This makes a bunch of stars
'''
def drawShape1(bob):
    for i in range(50):
        bob.forward(i * 10)
        bob.right(144)

coolBob = turtle.Turtle()
coolBob.speed(100)
drawShape1(coolBob)
'''

# A werid skwiggily circle
'''
def drawShape2(bob):
    for i in range(180):
        bob.forward(100)
        bob.right(30)
        bob.forward(20)
        bob.left(60)
        bob.forward(50)
        bob.right(30)
        
        bob.penup()
        bob.setposition(0, 0)
        bob.pendown()
        bob.right(2)
  
coolBob = turtle.Turtle()
coolBob.speed(100)
drawShape2(coolBob)
'''

# Triangle circles (i guess)
'''
def drawShape3(bob):
    bob.pencolor("blue")
    for i in range(50):
        bob.forward(50)
        bob.left(123)
        
    bob.pencolor("red")
    for i in range(50):
        bob.forward(100)
        bob.left(123)
        
coolBob = turtle.Turtle()
coolBob.speed(100)
drawShape3(coolBob)
'''
# multicolor (rainbowish) swirl
'''
def drawShape4(bob):
    colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green']
    for x in range(360):
        bob.pencolor(colors[x % 6])
        bob.width(x / 5 + 1)
        bob.forward(x)
        bob.left(20)

coolBob = turtle.Turtle()
coolBob.speed(100)
'''
drawShape4(coolBob)
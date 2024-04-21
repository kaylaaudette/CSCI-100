#
    
    
x = 1
if (x > 3):
     print("A")
elif (x == 0):
     print("B")
else:
    print("C")
    
x= 10
y= 1
if (x > 15):
     print("A")
elif (x == 0):
     print("B")
elif (y < 2):
    print("C")
else:
    print("D")
    
print(9//2)


idx = 1
idx = idx * 2
idx = idx * 4
print(idx)

def myFunction(X,Y):
    if (X < 5):
        return True
    elif (X == 5):
        if (Y > 0):
            return True
        else:
            return False
    else:
        return False
    
print(myFunction(5, 1))

second = 60
minutes = 60
hour = 24
seconds = second * minutes* hour
print(seconds)

def sumOfEven():
    sum = 0
    for x in range (0, 101):
        if (x % 2 == 0):
            sum = sum + x
        else:
            sum = sum # do nothing
    return sum
sumOfEven()


def sum(Num):
    acc = 0
    for x in range(0, Num+1):
        acc = acc + x
    return acc
print( sum(2) )

#import turtle 
#ivy = turtle.Turtle()
#ivy.penup()
#ivy.goto(-100, (-100*5)+3)
#ivy.pendown()
#ivy.goto(100, (100*5)+3)


def calculateGrade(score):
    if (score >= 90):
        grade = "A"
    elif (score >= 80):
        grade = "B"
    elif (score >= 70):
        grade = "C"
    elif (score >= 60):
        grade = "D"
    grade = "F"
    print(grade)
    
calculateGrade(80)

def isOdd(n):
    if (n%2 == 0):
        return False
    else:
        return True
print ( isOdd(5))

def getMax(x,y,z):
    if (x >= y) and (x >= z):
        return x
    elif (y >= x) and (y >= z):
        return y
    else:
        return z
    
print ( getMax(1, 2, 3))
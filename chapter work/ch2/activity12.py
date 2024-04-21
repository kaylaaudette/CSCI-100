#Kayla Audette 

#Question 1
def factorial(n):
    acc = 1 ## this must be 1
    for num in range(1, n+1):
        acc = acc * num
        # when num is 1, acc = 1 * 1 = 1... ect
    return acc

# Question 2
def isEven(t):
    for x in range(0, t+1, 2):
        num = x
    if t == num:
        return True
    else:
        return False
# or
# if n%2 == 0
    #return True
    #else:
        #return False

# Question 3
def displayStudentInfo(v, c):
    print(v, "is a",c, "year old student")
    
    
# Question 4
def multiPrint(x, y):
    for num in range (y):
        print(x)

# Question 5
def getGrade(x):
    if x >= 90:
        myGrade = "A"
        return(myGrade)
    if x >= 80:
        myGrade = "B"
        return(myGrade)
    if x >= 70:
        myGrade = "C"
        return(myGrade)
    if x >= 60:
        myGrade = "D"
        return(myGrade)
    else:
        myGrade = "F"
        return(myGrade)
    
# Question 6
def positivity(n):
    if n >= 0:
        print("postive number")
    else:
        print("negative number")
        

print("----Question 1--------")
result = factorial(5)
print(result) # it should print 120
print("----Question 2--------")
isFiveEven = isEven(5)
print(isFiveEven) # it should print False
print("----Question 3--------")
displayStudentInfo("Emily", 20) # it should print "Emily is a 20 year old student"
displayStudentInfo("Bob", 24) # it should print "Bob is a 24 year old student"
print("----Question 4--------")
multiPrint("repeat", 4)
print("----Question 5--------")
myGrade = getGrade(89)
print(myGrade)
print("----Question 6--------")
positivity(5) # should print "positive number"
positivity(-10) # should print "negative number"
print("----------------------")
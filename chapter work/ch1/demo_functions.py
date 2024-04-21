# Kayla Audette

# Part 1
# - avg has 2 parameters: no1 & no2
# - avg returns

# Part 2

# Define functions at the top
def hello():
   print("Hello students")
   print("Oh hi")
   print("How are you?")
   print("I'm good thanks.")

def avg(no1, no2):
    s = no1+no2
    return s/2


if __name__ == "__main__":

    # Invoke your functions here
    hello() # prints "Hello students"
    print(hello())


    avg(4,8) #nothing outputs
    print( avg(4,10) ) # fuction call returns the avergae than THEN we print it
    result = avg(345, 6788)
    print(result)
    
# There would be nothing in the shell
avg(4,8)
# The average would be printed in the shell
print( avg(4,8) )
# The average would be printed in the shell
rez = avg(4,8)
print(rez)
# This is because the fucntions call is returned and then printed for the second two

# Part 3

print( avg(50, 75))

def prod(num1, num2):
    m = num1 * num2
    return m
print(int(prod(8,9)))
      
    
def mystery():
   print("A")
   print("B")
   return "123"
   print("C")
   print("D")
   
myResult = mystery()
print(myResult)
# the output in the shell will stop showing up after the return line 123 as the return stops it

# Part 4
def weirdSum(n1, n2, n3, n4):
    r = (n1 + n2) * (n3 + n4)

def secondsToday():
    s= 60*60824
    print("IN A DAY THERE ARE:", s)
    
secondsToday()

import math

def quadraticEx(a, b, c):
    d = b * b - 4 * a * c
    sqrt = math.sqrt(abs(d))
    print(- b / (2 * a), " + ", sqrt)  
    print(- b / (2 * a), " - ", sqrt)  
  
quadraticEx(4, 1, 3)

  
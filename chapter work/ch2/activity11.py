#Kayla Audette

import random
import math

#Question 1
def toCelsius(temperature):
    C = (temperature-32)*(5/9)
    return C

#Question 2
def toFahrenheit (temperature):
    F = (temperature * 9/5) + 32
    return F
# the fraction is inversted and instead of
#subtracting 32 you are adding it

# Question 3
def tossCoin():
    i = random.random()
    if (i > 0.5):
        return 1
    else:
        return 0
        
# Question 4
def tossCoinAcc(x):
    heads = 0
    tails = 0
    for i in range(x):
        c = random.random()
        if (c > 0.5):
            heads = (heads +1)
        else:
            tails = (tails +1)
    print(tails)
    print(heads)
    

#coin return 0 or 1 and call 1000 times
#accumluator varible

# Question 5
def getMax(a, b, c):
    if ((a >= b) and (a >= c)):
        return a
    if ((a <= b) and (b >= c)):
        return b
    if ((a <= c) and (b <= c)): #equal sign always goes after
        return c

#extra 
def Fib(N):
    if ((N == 1) or (N == 2)):
        return 1
    else:
        return Fib(N-1) + Fib(N-2)

    
print("----Question 1--------")
print("F = 32 -->", toCelsius(32))
print("F = 15 -->", toCelsius(15))
print("F = 85 -->", toCelsius(85))
print("----Question 2--------")
print("C = 32 -->", toFahrenheit(0))
print("C = 15 -->", toFahrenheit(-9.44))
print("C = 85 -->", toFahrenheit(29.44))
print("----Question 3--------")
for i in range(10):
    print( tossCoin() ) 
print("----Question 4--------")
(tossCoinAcc(1000))
print("----Question 5--------")
print( getMax(7, -4, 99) )
print( getMax(23, 5, 0) )
print( getMax(17, 74, 9) )
print( getMax(7, 7, -9) )
print( getMax(2, 2, 2) )
print( getMax(7, 9, 9) )
print( getMax(9, 7, 9) )
print("----------------------")
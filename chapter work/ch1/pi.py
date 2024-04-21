# Kayla Audette

# Approximate pi using Archimedes
# We know that c = 2pir
# Unit circle C= 2pi, pi = c/2 (we are going to approximate the c of the circle)
# Approximate by making a polygon inside the circle (length of side = c of polygon)
# using a triangle inside the polygon to find c (sin(360/n) = s/2, s = 2*sin(360/n)

import math

#Question 2
computeSum = 0
for x in range(51): #same as 0, 51 :)
    computeSum = computeSum + x
print("sum of the first 50 numbers is:", computeSum)

# using a function
def computeSumofFristFifty():
    computeSum = 0
    for x in range(51): #same as 0, 51 :)
        computeSum = computeSum + x
    return(computeSum)
y = computeSumofFristFifty
print("sum of the first 50 numbers is:", y)

# Question 3
def archimedesOctagon():
   side = 2 * math.sin(math.radians(45/2.0))
   polygonCircumference = 8 * side
   return (polygonCircumference / 2)

def archimedes(numSides):
    innerAngle = 360/ numSides # (B)
    side = 2 * math.sin(math.radians(innerAngle/2))
    polygonCircumference = numSides * side
    # circumference of circle .= polygon circumference
    return (polygonCircumference/ 2)

# computes an approximate Pi using the Leibniz formula (accumlate a product)
def leibniz(terms):
    # your code goes here
    approxPi =  0
    return approxPi
 
 # computes an approximate Pi using the Wallis formula (accumlate a sum) 
def wallis(numPairs):
    # your code goes here
    approxPi = 1
    return approxPi

#call it to compute vaule of Pi. Print the result 
result = archimedesOctagon()
print(result)

print("Octagon: ", archimedes(8))
print("Dodecadon: ", archimedes(12))

for sides in range(8, 100, 8):
   print(sides, archimedes(sides))
   
newSideLength = 10
for x in range(10):
    print(sides, archimedes(newSideLength))
    newSideLength = newSideLength * 10
    
       
print("Results for Leibniz formula:")
print(leibniz(200))
print(leibniz(500))
   
print("Results for Wallis formula:")
print(wallis(4))
print(wallis(20))
print(wallis(100))
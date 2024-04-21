

import math

def computeFactorial(n):
    productSoFar = 1
    for number in range(1, n+1):
        productSoFar = productSoFar * number
    return productSoFar

print(computeFactorial(5))
fivefactorical = computeFactorial(5)

def sumUpTo (n):
    sumSoFar = 0
    for number in range(1, n+1):
        sumSoFar = sumSoFar + number
    return sumSoFar

print("sum of first 10 numbers is:", sumUpTo(10))
print("factorial of 11 is: ", computeFactorial(11))
print("factorial of 11 is: ", math.factorial(11))
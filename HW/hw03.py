# Name: Kayla Audette
# HW 3

import math

## Q1. Finish/fix the following function so that it returns
## the sum of the first 100 even numbers (beginning with 2)
def q1_sum():
    sum = 0
    for x in range(0, 201, 2):
      sum = sum + x
    return sum

## Q2. Finish/fix the following function so that it returns
## the sum of the first 50 odd numbers.
def q2_sum():
    sum = 0
    for x in range(1, 100, 2):
        sum = sum + x
    return sum

## Q3. Finish/fix the following function so that it returns
## the average of the first 100 odd numbers.
def q3_avg():
    acc = 0
    for x in range(1, 201, 2):
        acc = acc + x
    avg = acc/100
    return avg

## Q4. Write a function called q4_avg which returns
## the average of the first N numbers, where N is a parameter
# your code here
def q4_avg(N):
    sum = 0
    for x in range(0, N+1):
        sum = sum + x
    avg = sum/N
    return avg

## Q5. Write a function called q5_factorial which returns
## the product of the first N numbers, where N is a parameter
# your code here
def q5_factorial(N):
    product = 1
    for number in range(1, N+1):
        product = product * number
    return product

## Q6. Finish/fix the following function so that it returns True
## if parameter X is strictly less than parameter Y, and
## it returns False otherwise
def q6_check(X, Y):
    if X < Y:
        return True
    else:
        return False

## Q7. Finish/fix the following function so that it returns True
## if parameter X is larger than 10. However, if X is smaller
## than or equal to 10, then it will evaluate parameter Y.
## In that case, if Y is smaller than 2, it will output True.
## Otherwise, it will output False.
def q7_check(X,Y):
    if X > 10:
        return True
    else:
        if Y<2:
            return True
        else:
            return False
   
    
    
## Q8. Finish/fix the following function so that it returns True
## if the value of the parameter count is between 1 and 10 inclusive
def q8_check(count):
    if ((count < 10) and (count > 1)):
        return True
    else:
        return False

## Q9. Finish/fix the following function so that it returns True
## if the parameter N is an odd number
def q9_is_odd(N):
    for x in range(1, N+1, 2):
        num = x
    if N == num:
        return True
    else:
        return False
    

## Q10. Finish/fix the following function so that it returns True
## if the parameter N is an even number
def q10_is_even(N):
    for x in range(0, N+1, 2):
        num = x
    if N == num:
        return True
    else:
        return False

if __name__ == "__main__":
    ## TODO: Uncomment each function call out as you work through the questions.
    ## When you're finished, all of them should be uncommented.
    ## Do not make any other changes here other than for uncommenting.
    print("Question 1 - test: ", q1_sum())
    print("------------------------------")
    print("Question 2 - test: ", q2_sum())
    print("------------------------------")
    print("Question 3 - test: ", q3_avg())
    print("------------------------------")
    print("Question 4 - testA: ", q4_avg(100))
    print("Question 4 - testB: ", q4_avg(200))
    print("------------------------------")
    print("Question 5 - testA: ", q5_factorial(5))
    print("Question 5 - testB: ", q5_factorial(10))
    print("------------------------------")
    print("Question 6 - testA: ", q6_check(5, 5))
    print("Question 6 - testB: ", q6_check(3, 5))
    print("------------------------------")
    print("Question 7 - testA: ", q7_check(10, 0))
    print("Question 7 - testB: ", q7_check(3, 0))
    print("Question 7 - testC: ", q7_check(3, 3))
    print("------------------------------")
    print("Question 8 - testA: ", q8_check(5))
    print("Question 8 - testB: ", q8_check(11))
    print("Question 8 - testC: ", q8_check(0))
    print("------------------------------")
    print("Question 9 - testA: ", q9_is_odd(5))
    print("Question 9 - testB: ", q9_is_odd(42))
    print("------------------------------")
    print("Question 10 - testA: ", q10_is_even(5))
    print("Question 10 - testB: ", q10_is_even(42))


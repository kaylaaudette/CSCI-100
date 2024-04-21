# Example 1 -- list of all numbers 0-19
# long form... too much code
numbersV2 = []
for x in range(0,20):
    numbersV2.append(x)
print("V2: ", numbersV2)

# list comprehensions -- a shorthand way to create a list
numbersV1 = [x for x in range(0,20) ]
print("V1:", numbersV1)

# manipulate x to say if it is even numbers 
numbersV1 = [x%2==0 for x in range(0,20) ]
print("V1:", numbersV1)

# EXAMPLE 2 --- A list of even numbers 0-18
# long form... SO MUCH CODE! :(
evenNumbersV2 = []
for num in range(0,20):
    if num % 2 == 0:
        evenNumbersV2.append(num)
print("V2:", evenNumbersV2)

# we can use if statements in list comprehension
evenNumbersV1 = [num for num in range(0,20) if num % 2 == 0]
print("V1:", evenNumbersV1)

# EXAMPLE 3 -- Loops
# for loop which loops 10 times
print("for loops:")
for number in range(0,10):
    print(number)
    
# while loop which loops 10 times
print("while loops:")
myNumber = 0
while (myNumber < 10):
    print(myNumber)
    myNumber = myNumber + 1

# Example 4-- why while loops are useful
# * any for loop can be written as a while loop,
# but not all while loops can be written as for loops!
# * important: we don't have to know how many times the while loop will execute
# * here we keep asking the person to enter in usernames & passwords. we only
# stop asking once they enter in a value "X" to stop.
givenUser = input("Let's build up a dictionary. What user you want to add (X to quit)")
accounts = {}
while (givenUser != "X"):
    givenPassword = input("What's the password for this user?")
    accounts[givenUser] = givenPassword
    
    # prepare for next iteration of while loop
    givenUser = input("What user do you want to add next? (X to quit)")
print(accounts)

#infitnite while loop
# num = 0
# while (num >=0): #condition will always be true 
#     print(num)
#     num = num + 1
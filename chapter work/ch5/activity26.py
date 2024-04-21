# Kayla Audette
# activity 26

# Question 1
a=["1", "2", "3", "4", "5"]
b = [int(x) for x in a]
print(b)

# Question 2
c = [x%3 == 0 for x in range(0,20)]
print(c)

# Question 3
d = [x/3 for x in range(0,100)]
print(d)

# Questions 4 & 5
User = int(input("Enter next number (negative number to stop):"))
accounts = {}
sum = 0
N = 0
while (User >= 0):
    sum = sum + User
    N = N + 1
    avg = sum/N
    
    User = int(input("Enter next number (negative number to stop):"))
print("Sum of all Positive Numbers:", sum)
print("Average of all Positive Numbers:", avg)
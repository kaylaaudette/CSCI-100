# Kayla Audette

# Question 1
cents = {
    'Nickel': 5,
    'Dime': 10,
    'Quarter': 25,
    'Dollar': 100
    }

print ( cents.keys() )
print ( cents.values() )
print ( cents.items())
print ( cents.get('Nickel'))
print (cents.get('Dime', 'none'))
for key in cents:
    print(cents[key])
print ( 'Dollar' in cents)
print ( 'cheese' not in cents)
print ( cents['Nickel'] )
del cents['Dime'] 
print(cents)

# Question 2 
personnel = {'Joe': 2000, 'Ana': 2500, 'Bob': 1800, 'Chris': 2100, 'Diana': 1900}
print(personnel)
bonus = input("What bonus do you want to give everybody?" )
bonus = int(bonus)
for key in personnel:
    personnel[key] = personnel[key] + bonus
print(personnel)

# Question 3
userPassword = {}
for a in range(5):
    userPassword[input('userName:')]=input('password:')
print(userPassword)
    
# Question 4
userPassword[input('Input Username:')]
print(userPassword)


    
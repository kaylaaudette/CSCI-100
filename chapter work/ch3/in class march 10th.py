mySting = "abc" # string
myList = [ 1, 2, 3] # list
myDictionary = {"michael": "A", "heather": "F"} # dictionary {key, vaule}

for ch in myString:
    print(ch)

for idx in range( len(myString) ):
    print(myString[idx])

print(myString[0])
print(myList[0])
print(myDictionary["heather"])

myList[0] = 100
print(myList)

myDictionary["heather"] = "C"
print(myDictionary)

myDictionary["bob"] = "A"
print(myDictionary)
    

nhl = {
    "Detroit": "Red Wings",
    "Pittsburgh", "Pennguins",
    "Philedelphia": "Flyrs"
    }

print( nhl["Pittsburgh"] )

for key in nhl:
    print( "keys:" + key + ", value: " + nhl[key] )
    

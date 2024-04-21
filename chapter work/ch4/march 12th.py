# in class


addressBook = {
    "Heather" : "330-555-5555",
    "Fareeda" : "330-123-4567",
    "Yazid"   : "215-555-1234"
    }
print( addressBook.keys() ) # keys (left of colon) -- names
print( addressBook.values() ) # vaules (right of colon) -- numbers

# accessing each item in a dictionary to print
for k in addressBook:
    print("the key is:", k)
    print("the value is", addressBook[k])
    print("----")
    
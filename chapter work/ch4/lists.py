myList = ['H', 'E', 'L', 'L', 'O', '!']
print(myList)

print("number of items:", len(myList))
print("number of 'L's:", myList.count('L'))

#lists can be heterogenous (i.e., contain different kinds of items)
myList[0] = "Y" # store "Y" at index 0 in myList
myList.insert(2, "words") # insert "words" at index 2, shift other items down
myList.pop() # remove last item of myList
myList.append("?") # add "?" to the end of myList
myList.pop(1) # remove item at index 1 of myList
print(myList)

# lists can store anything
words = ["cat", "rat", "dog", "emu", "brid"]
words.sort # sort in asecnding order
print("ordered:", words)
words.reverse()
print("reversed:", words)
words.remove("emu")
print(words)

# we can from lists from strings
myString = "here_is_some_longer_string"
splitList = myString.split("_") # create a list of strings using "_" as a delimiter
print(splitList)

#iterate through a string/list
for i in range (len(myString)):
    print(myString[i])
    
for ch in myString:
    print(ch)
    
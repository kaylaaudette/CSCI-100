# strings - immutable containers of characters accessible by index
course = "Scientific Computing"

# iterating over strings by character
for c in course:
    print("next character: ", c)

# iterating over strings by index
for i in range(len(course)):
    character = course[i]
    print( "next character at index: ", i, " is: ", character )

# functions on strings
l = len(course) # number of characters in the string
newString1 = "CS100 " + course # string concatenation operator (join two strings together)
newString2 = course * 6 # repetition operator (repeat the string)
newString3 = course.replace("Computing", "Programming") # replace all occurrences of "Computing" with "Programming"

# index operator -- return the character at that position
#   positive indices (start from the left)
#   negative indices (start from the right)
firstCharacter = course[0] # return first character
lastCharacter = course[-1] # return character at last index (-1)
someCharacter = course[5]  # return character at index 5

# slice operator
newString3 = course[:6]   # slice operator (start from beginning up to not including index 6)
newString4 = course[10:]  # slice operator (start from index 10 all the way to the end of string)
newString5 = course[6:10] # slice operator (start from index 6 up to not including index 10)

# containment operator
bool1 = "science" in course  # True/False whether the left string is in the right one
bool2 = "science" not in course # True/False whether the left string is NOT in the right one

# justification
print("-"*52) # to observe justification, print the "-" character 52 times
centeredStr = course.center(50) # return a new string of length 50, center justified
leftStr = course.ljust(50)      # return a new string of length 50, left justified
rightStr = course.rjust(50)     # return a new string of length 50, right justified
print( "-" + centeredStr + "-" )
print( "-" + leftStr + "-" )
print( "-" + rightStr + "-" )

# capitalization
lowerCase = course.lower() # return a new string with all letters in lowercase
upperCase = course.upper() # return a new string with all letters in uppercase

# finding and counting
occurrences1 = course.count("S") # number of occurrences of "s"
occurrences2 = course.count("Scienc") # number of occurrences of "Scienc"
idx1 = course.find("Scienc") # index where "Scienc" first occurs
idx2 = course.find("S") # index where "S" first occurs
idx3 = course.find("!") # returns -1 if item is not found
idx4 = course.index("Scienc") #index where "Scienc" first occurs
idx5 = course.index("S") # index where "S" first occurs
#idx6 = course.index("!") # throws an error if item is not found (commented out so it doesn't throw an error)

# functions relating numbers to strings/characters
num = ord('b') # ASCII value corresponding to 'b'
ch = chr(97)   # character corresponding to ASCII value 97
newString = str(32) # convert to a string


# lists - mutable containers of items accessible by index
courses = ["Scientific Computing", "Imperative Problem Solving", "Data Structures", "Operating Systems"]
grades = [90, 80, 75, 100, 88, 92, 74, 90]
randomStuff = ["word", 1, 'b', 3.14]

# iterating through lists by item
for item in courses:
    print("item is: ", item)

# iterating through lists by index position
for index in range(len(courses)):
    item = courses[index]
    print("item at index ", index, " is: " , item)

# other list functions
length = len(courses) # number of items in the list
newList1 = courses*3 # create a new list containing all items repeated 3 times
newList2 = courses + ["Algorithms", "Theory of Computing"] # concatenation -- put two lists together
occurrences = grades.count(90) # returns the number of times an item occurred in the list

# index
firstItem = courses[0] # access element at index 0
lastItem = courses[-1] # access element at last index
courses[0] = "CS 100" # change the element at index 0
itemIdx = courses.index("Imperative Problem Solving") # gives the index of where the item is located


# other mutations to list
courses.append("Programming Languages") # add to the end of the list
courses.insert(3, "Software Engineering") # add to index 3
lastItem = grades.pop() # remove and return last item of the list
firstItem = grades.pop(0) # remove item at index 0 and return it
grades.sort() # modify the given list so all items are in ascending order
grades.reverse() # modify the given list so all items are in order reverse to what they were
courses.remove("Data Structures")

# slice operator
subList1 = courses[:3] # list containing all items from the beginning up to but not including index 3
subList2 = courses[3:] # list containing all items from index 3 all the way to the end
subList3 = courses[2:4] # list containing all items from index 2 up to but not including 4
fullCopy = courses[:] # a copy of the list

# membership/containment operator
bool1 = "Data" in courses # return whether the entire item "Data" is in the list
bool2 = "Data" not in courses # return whether the entire item "Data" is NOT in the list

# other list functions (assuming list is of numbers)
mySum = sum(grades)
myMax = max(grades)
myMin = min(grades)

# getting a list from a string
myString = "Python is fun"
myList = myString.split(" ")

# dictionary -- mutable container of items (key/value pairs) accessible by key
funWords = {
    "defenestration": "the action of throwing someone out of a window",
    "amiable": "having or displaying a friendly and pleasant manner",
    "cockatiel": "a slender long-crested Australian parrot related to the cockatoos",
    "quixotic": "not sensible about practical matters",
    "absquatulate": "to leave somewhat abruptly",
    "floccinaucinihilipilification": "the action or habit of estimating something as worthless",
    "vomitous": "nauseauting or repulsive"
}

# iterating through the dictionary by key
for key in funWords:
    value = funWords[key]
    print("key is: ", key, "... and value is: ", value)

# getting elements as a list
allKeys = funWords.keys() # list of all keys
allValues = funWords.values() # list of all values
allItems = funWords.items() # list of all items as key/value pairs

# accessing items
definition0 = funWords["cockatiel"] # returns value associated with the key "cockatiel"
definition1 = funWords.get("cockatiel") # return value associated with the key "cockatiel"
definition2 = funWords.get("barbaric", "unknown definition") # return value associated with the key "barbaric", or returns "unknown definition" if not found

# modifying dictionary
# () -- anytime we call a function
# {} -- used to initialize a dictionary
# [] -- index operator and slice operator for strings/lists, index operator with dictionaries, used to initalize a list
funWords["vomitous"] = "inducing nausea" # change value associated with given key
funWords["alopecia"] = "hair loss" # add a new key/value pair

# containment/membership operator for KEYS (not values!)
bool1 = "amiable" in funWords # True, as "ambiable" is a key in the dictionary
bool2 = "hair loss" in funWords # False, as "hair loss" is not a KEY
bool3 = "hair loss" not in funWords # True

del funWords["alopecia"] # remove an item from the dictionary
length = len(funWords) # number of items in the dictionary

#Kayla Audette

myString = 'abc'
#myString[0] = 'd'
   
myList = ['a', 'b', 'c']
#myList[0] = 'd'

#TypeError: 'str' object does not support item assignment
# there was no d in either string so it couldn't ???

s = "I like apples"
k1 = s.split() # 'I' 'like' 'apples'
k2 = s.split('a') # 'I' 'like' 'pples'
k3 = s.split('e') # 'I' 'like' 'appl' 's'

m = "mississippi"
m1 = m.split('i')

# Write a function numWords(sentence) which takes a string as a parameter and returns the number of words in the given string. Call your function to test it works.
def numWords(sentence):
    #print("number of words:", sentence.count(' ')+1)
    List = sentence.split(' ')
    print(len(List))

# Q5 Write a function makeString(myList) that takes a list of words as a parameter and returns one big string consisting of all words in the list separated by spaces. 
def makeString(myList):
    acc = '' # empty string, length 0
    for item in myList: #string coming from myList
        acc = acc + item + ' '
    return acc

# Although Python provides many list methods, it’s good practice and instructive to think about how they are implemented. Write a function called checkIn(myList, key) that works similar to in, and call it to check that it works. It returns True if the given key exists is in list, and False otherwise. For example,
def checkIn(myList, key):
    for item in myList:
        if item == key:
            return True
    else:
        return False


print("----------Q1-----------")
print(myString)
print(myList)
print("----------Q3-----------")
print(m1)
print("----------Q4-----------")
numWords("the quick brown fox") 
print("----------Q5-----------")
print ( makeString(["the", "quick", "brown", "fox"])) # will print "the quick brown fox"
print("----------Q6-----------")
print( checkIn( ['a','b','c','d','e'], 'd') ) # will print True
print( checkIn( ['a','b','c','d','e'], 'f') ) # will print False

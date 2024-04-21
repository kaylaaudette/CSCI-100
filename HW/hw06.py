# Kayla Audette
# HW 6

# Q1: Make a function called createList which creates a list with following five items:
#      7, 9, 'a', 'cat', False
# Assign it to the variable theList and return it.
def createList():
    theList = [7, 9, 'a', 'cat', False]
    return theList

# Q2: Manipulate the parameter myList by performing
# the following actions to myList, in this order:
#   - Append 3.14
#   - Append 7
#   - Insert the value of 'dog' at position 3
#   - Remove the first 9
#   - Remove the item at index 5 by using pop
#   - Return myList when finished
def manipulate(myList):
    myList.append(3.14)
    myList.append(7)
    myList.insert(3, 'dog')
    myList.remove(9)
    myList.pop(5)
    return myList

# Q3: Create a function called listOfWords which takes a parameter
# called myPhrase and splits it into a list of words. Return the list of words.
def listOfWords(myPhrase):
    return myPhrase.split()


# Q4: Complete the following function that takes a string
# mySentence as a parameter and returns the number of words in
# the sentence.
def numWords(mySentence):
    List = mySentence.split(' ')
    return len(List)


# Although Python provides many list methods, it's good practice
# and instructive to think about how they are implemented. Implement
# a python function that works like the following
#   - Q5 [1pt]: count
#   - Q6 [1pt]: find
#   - Q7 [1pt]: insert
#   - Q8 [1pt]: inList (return True if item is in the list)
#   - Q9 [1pt]: reverse
#   - Q10 [1pt]: min

# Q5 (count equivalent)
# Return the number of times item appears in myList (don't use count)
def q5_count(myList, item):
    x = 0
    for i in myList:
        if i == item:
            x+= 1
    return x

# Q6 (find equivalent)
# Return the first index where the given item is found in myList, or if
# it cannot be found, return -1. (don't use find)
def q6_find(myList, item):
    acc = 0
    for i in myList:
        if item not in myList:
            return -1
        elif i != item:
            acc = acc + 1
        else:
            return acc

# Q7 (insert equivalent)
# Insert item into myList at the given index. Return modified list. (don't use insert)
def q7_insert(myList, index, item):
    return myList[:index]+[item]+myList[index:]
            

# Q8 (in equivalent)
# Return True if item is in myList, return False otherwise.
# (for ... in ... loop is OK, but don't use in just by itself)
def q8_inList(myList, item):
    if item in myList:
        return True 
    else:
        return False

# Q9 (reverse equivalent)
# Return a copy of myList such that the items are in reverse order (don't use reverse)
def q9_reverse(myList):
    newList=[]
    for x in myList:
        newList=[x]+newList
    return newList

# Q10 (min equivalent)
# Return the minimum element in the list
def q10_min(myList):
    minSoFar = myList[0]
    for i in range(1, len(myList)):
        if myList[i] < minSoFar:
            minSoFar = myList[i]
    return minSoFar


if __name__ == "__main__":
    ## TODO: Uncomment each function call out as you work through the questions.
    ## When you're finished, all of them should be uncommented.
    ## DO NOT make any other changes here other than to uncomment.
    print("Q1 - testA:", createList())
    print("----------------------")
    listA = [7, 'a', 'cat', 7, 9, False, 9]
    listB = ['e', 'c', 'b', 'bird', 9, 'd', 42]
    print("Q2 - testA:", manipulate(listA))
    print("Q2 - testB:", manipulate(listB))
    print("----------------------")
    print("Q3 - testA:", listOfWords("fun with python programming") )
    print("Q3 - testB:", listOfWords("if you like this class you might like CS110 too") )
    print("----------------------")
    print("Q4 - testA:", numWords("fun with python programming") )
    print("Q4 - testB:", numWords("if you like this class you might like CS110 too") )
    print("----------------------")
    list5A = [1, 5, 10, 23, 42, 9, 8, 15, 42, 3, 42]
    list5B = ['bat', 'rat', 'emu', 'bird', 'bird', 'bird', 'rat', 'bird']
    print("Q5 - testA:", q5_count(list5A, 42) )
    print("Q5 - testB:", q5_count(list5B, 'bird') )
    print("----------------------")
    brooklyn99 = ['jake', 'rosa', 'amy', 'gina', 'holt', 'terry', 'charles', 'scully', 'hitchcock']
    print("Q6 - testA:", q6_find(brooklyn99, 'pimento'))
    print("Q6 - testB:", q6_find(brooklyn99, 'terry'))
    print("----------------------")
    list7A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list7B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list7C = ['I', 'hope', "you're", 'having', 'a', 'good', 'day']
    print("Q7 - testA:", q7_insert(list7A, 0, 0))
    print("Q7 - testB:", q7_insert(list7B, 10, 11))
    print("Q7 - testC:", q7_insert(list7C, 5, "really"))
    print("----------------------")
    list8A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list8B = ['you', 'are', 'how', 'students', 'cs', 'hi']
    print("Q8 - testA:", q8_inList(list8A, 42))
    print("Q8 - testB:", q8_inList(list8B, 'hi'))
    print("----------------------")
    list9A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list9B = ['you', 'are', 'how', 'students', 'cs', 'hi']
    print("Q9 - testA:", q9_reverse(list9A))
    print("Q9 - testB:", q9_reverse(list9B))
    print("----------------------")
    list10A = [1, 10, 3, 5, -1, 2, -10, 0, 13]
    list10B = [300, 52, 5, 42, 13]
    print("Q10 - testA:", q10_min(list10A) )
    print("Q10 - testB:", q10_min(list10B) )  
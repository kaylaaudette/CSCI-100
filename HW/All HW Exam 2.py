print("---------HW 5---------")
# Q1 [0.5pt] Finish/fix this function so that it returns
# the first 6 characters from the string parameter myString.
# Use the slice operator.
def firstSix(myString):
    return myString[:6] 
print("Q1 - testA:", firstSix("Python's so cool") )
print("----------------------")
# Q2 [0.5pt] Finish/fix this function so that it returns
# the last 5 characters from the string parameter myString.
# Use the slice operator.
def lastFive(myString):
    return myString[-5:]
print("Q2 - testA:", lastFive("Ada worked with Charles Babbage") )
print("----------------------")
# Q3 [0.5pt] Finish/fix this function so that it returns
# a substring of myString consisting of
# first 8 characters followed by a single space followed
# by the last 8 characters.
def partialSubstring(myString):
    return myString[:8] + " " + myString[-8:]
print("Q3 - testA:", partialSubstring("She envisioned computers being more than calculators,") )
print("----------------------")
# Q4 [0.5pt] Finish/fix this function so that it returns
# the number of characters appearing in myString
def howManyCharacters(myString):
    return len (myString)
print("Q4 - testA:", howManyCharacters("Ada wrote the") )
print("----------------------")
# Q5 [0.5pt] Finish/fix this function so that it returns
# the number of occurrences of the character 'u' in myString
def numOccurrences(myString):
    return myString.count('u')
print("Q5 - testA:", numOccurrences("It computed") )
print("----------------------")
# Q6 [0.5pt] Finish/fix this function so it replaces all
# occurrences of the substring 'he' with 'vx'
def weirdReplace(myString):
    return myString.replace('he', 'vx')
print("Q6 - testA:", weirdReplace("here are some fun facts about her") )
print("----------------------")
# Q7 [0.5pt] Finish/fix this function so it returns the
# ASCII value of the single character
def toASCII(ch):
    return ord(ch)
print("Q7 - testA:", toASCII('a') )
print("----------------------")
# Q8 [1pt] Finish/fix this function so it returns the
# first index of where the character ch occurs in myString.
# If the character ch does not belong in the myString,
# then return "NOT FOUND"
def firstIndex(myString, ch):
    if ch in myString:
        return myString.index(ch)
    else:
        return "NOT FOUND"
print("Q8 - testA:", firstIndex("She was called the 'Princess of Parallelograms'", "w") )
print("Q8 - testB:", firstIndex("She conceptualised a flying machine", "z") )
print("----------------------")
# Q9 [1pt] Create a function named letterGrade which
# takes a single parameter that is an exam score from 0-100
# and returns the corresponding letter grade (A/B/C/D/F).
# Use the standard grading scale. A is [90, 100], B is [80, 90), etc.
def letterGrade(score):
    grade = "F"
    if (score >= 90):
        grade = "A"
    elif (score >= 80):
        grade = "B"
    elif (score >= 70):
        grade = "C"
    elif (score >= 60):
        grade = "D"
    return grade
print("Q9 - testA:", letterGrade(90) )# can do with all grades
print("----------------------")
# Q10 [1pt] Finish/fix the following function so that it
# converts a character from the alphabet to a number between 0-25
# in alphabetical order and returns it. If the input character
# is not A-Z or a-z, then return -1
def letterToIndex(c):
    c = c.lower()
    r = ord(c)- ord("a")
    if (0 <= r <= 25):
        return r
    else:
        return -1
print("Q10 - testA:", letterToIndex('a') )
print("Q10 - testB:", letterToIndex('z') )
print("Q10 - testC:", letterToIndex('Y') )
print("Q10 - testD:", letterToIndex('*') )
print("----------------------")
# Q11 [1pt] Finish/fix the following function so that it
# converts an index to a character and return it (0 --> a, 1 --> b, etc.)
# If the index is outside of the range [0,25], then return "?"
# Use the second parameter isCap to determine whether it
# should output a capital or a lowercase letter.
def indexToLetter(idx, isCap):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if (0<=idx<=25):
        place = alphabet[idx]
        if isCap==True:
            return place.upper()
        else:
            return place.lower()
    else:
        return "?"
print("Q11 - testA:", indexToLetter(0, True) )
print("Q11 - testB:", indexToLetter(0, False) )
print("Q11 - testC:", indexToLetter(25, True) )
print("Q11 - testD:", indexToLetter(24, False) )
print("Q11 - testE:", indexToLetter(-3, False) )
print("Q11 - testF:", indexToLetter(26, True) )
print("----------------------")
# Q12 [1pt] Write a function called stripSpaces which takes one
# parameter representing a phrase/paragraph, and return the
# same phrase/paragraph with the order of letters in tact but the
# spaces between each word removed
def stripSpaces(phrase):
    newPhrase = phrase.replace(' ','')
    return newPhrase
print("Q12 - testA:", stripSpaces("Hello CS100, what a beautiful day"))
print("----------------------")
# Q13 [1pt] Finish/fix the following function so that EACH of
# the characters in the parameter badSet are removed from
# the parameter myPhrase. Keep the original order of letters in tact.
def cleanUp(myPhrase, badSet):
    newPhrase= myPhrase
    for ch in badSet:
        newPhrase = newPhrase.replace(ch, '')
    return newPhrase
# newphrase = myPhrase.replace(badSet, '') you want to remove each on indivdually
print("Q13 - testA:", cleanUp("it's- a. great. day. punctuation, is! my: friend; said, e.e. cummings!", ",.-'!:;"))
print(" ")
print(" ")
print("---------HW 6---------")
# Q1: Make a function called createList which creates a list with following five items:
#      7, 9, 'a', 'cat', False
# Assign it to the variable theList and return it.
def createList():
    theList = [7, 9, 'a', 'cat', False]
    return theList
print("Q1 - testA:", createList())
print("----------------------")

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
listA = [7, 'a', 'cat', 7, 9, False, 9]
listB = ['e', 'c', 'b', 'bird', 9, 'd', 42]
print("Q2 - testA:", manipulate(listA))
print("Q2 - testB:", manipulate(listB))

# Q3: Create a function called listOfWords which takes a parameter
# called myPhrase and splits it into a list of words. Return the list of words.
def listOfWords(myPhrase):
    return myPhrase.split()
print("Q3 - testA:", listOfWords("fun with python programming") )
print("Q3 - testB:", listOfWords("if you like this class you might like CS110 too") )
print("----------------------")
# Q4: Complete the following function that takes a string
# mySentence as a parameter and returns the number of words in
# the sentence.
def numWords(mySentence):
    List = mySentence.split(' ')
    return len(List)
print("Q4 - testA:", numWords("fun with python programming") )
print("Q4 - testB:", numWords("if you like this class you might like CS110 too") )
print("----------------------")

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
list5A = [1, 5, 10, 23, 42, 9, 8, 15, 42, 3, 42]
list5B = ['bat', 'rat', 'emu', 'bird', 'bird', 'bird', 'rat', 'bird']
print("Q5 - testA:", q5_count(list5A, 42) )
print("Q5 - testB:", q5_count(list5B, 'bird') )
print("----------------------")
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
brooklyn99 = ['jake', 'rosa', 'amy', 'gina', 'holt', 'terry', 'charles', 'scully', 'hitchcock']
print("Q6 - testA:", q6_find(brooklyn99, 'pimento'))
print("Q6 - testB:", q6_find(brooklyn99, 'terry'))
print("----------------------")
# Q7 (insert equivalent)
# Insert item into myList at the given index. Return modified list. (don't use insert)
def q7_insert(myList, index, item):
    return myList[:index]+[item]+myList[index:]
list7A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list7B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list7C = ['I', 'hope', "you're", 'having', 'a', 'good', 'day']
print("Q7 - testA:", q7_insert(list7A, 0, 0))
print("Q7 - testB:", q7_insert(list7B, 10, 11))
print("Q7 - testC:", q7_insert(list7C, 5, "really"))
print("----------------------")         

# Q8 (in equivalent)
# Return True if item is in myList, return False otherwise.
# (for ... in ... loop is OK, but don't use in just by itself)
def q8_inList(myList, item):
    if item in myList:
        return True 
    else:
        return False
list8A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list8B = ['you', 'are', 'how', 'students', 'cs', 'hi']
print("Q8 - testA:", q8_inList(list8A, 42))
print("Q8 - testB:", q8_inList(list8B, 'hi'))
print("----------------------")
# Q9 (reverse equivalent)
# Return a copy of myList such that the items are in reverse order (don't use reverse)
def q9_reverse(myList):
    newList=[]
    for x in myList:
        newList=[x]+newList
    return newList
list9A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list9B = ['you', 'are', 'how', 'students', 'cs', 'hi']
print("Q9 - testA:", q9_reverse(list9A))
print("Q9 - testB:", q9_reverse(list9B))
print("----------------------")
# Q10 (min equivalent)
# Return the minimum element in the list
def q10_min(myList):
    minSoFar = myList[0]
    for i in range(1, len(myList)):
        if myList[i] < minSoFar:
            minSoFar = myList[i]
    return minSoFar
list10A = [1, 10, 3, 5, -1, 2, -10, 0, 13]
list10B = [300, 52, 5, 42, 13]
print("Q10 - testA:", q10_min(list10A) )
print("Q10 - testB:", q10_min(list10B) )

print(" ")
print(" ")
print("---------HW 7---------")
# Q1 [2pt]: Finish/fix the following function so that it takes the
# two lists and returns a dictionary with the names as the key
# and the scores as the values.
def makeDictionary(names, scores):
    newdict= dict(zip(names, scores))
    return newdict
names1 = ['joe', 'tom', 'barb', 'sue', 'sally']
scores1 = [10,     25,    10,     20,    5]
scoreDict1 = makeDictionary(names1, scores1)
    
names2 = ['joe', 'tom', 'barb', 'sue', 'sally', 'mary', 'jean']
scores2 = [25,     10,    40,     15,    10,      40,    10]
scoreDict2 = makeDictionary(names2, scores2)
print("Q1 - testA:", scoreDict1)
print("Q1 - testB:", scoreDict2)
    
print("----------------------")
# or
#   newdict = {}
#     for x in range (len(names)):
#         newdict[names[x]]=scores[x]
#     return newdict

# Q2 [2pt]: Update the given dictionary, scoreDict, in the following way.
# - Add score of 30 for 'john'.
# - Update the score for 'sally' to be 15.
# - Tom just dropped. Delete 'tom' and his score.
# - Return the modified dictionary.
def modifyDictionary(scoreDict):
    scoreDict['john']=30
    scoreDict["sally"] = 15
    del scoreDict["tom"]
    return scoreDict
scoreDict1 = modifyDictionary(scoreDict1)
scoreDict2 = modifyDictionary(scoreDict2)
print("Q2 - testA:", scoreDict1)
print("Q2 - testB:", scoreDict2)
    
print("----------------------")
# Q3 [1pt]: Create and return a sorted list of all the scores in scoreDict
def sortedScores(scoreDict):
    allValues = list(scoreDict.values())
    allValues.sort()
    return allValues
myScores1 = sortedScores(scoreDict1)
myScores2 = sortedScores(scoreDict2)
print("Q3 - testA:", myScores1)
print("Q3 - testB:", myScores2)
    
print("----------------------")
# Q4 [2pt]: Calculate average of all scores from the dictionary
def scoreAverage(scoreDict):
    allscores = list(scoreDict.values())
    average = sum(allscores)/len(allscores)
    return average

# Q5 [2pt]. Print out a table of students and their scores with the
# students listed in alphabetical order. See expected output.
# Hint: recall ljust for strings
def printTable(scoreDict):
    scores =list(scoreDict.keys())
    scores.sort()
    for name in scores:
        if name in scores:
            string = name.ljust(10) + " " + str(scoreDict[name])
            print(string)
# how do you format of table???

# Q6 [1pt]: Write a function getScore that takes a name and a dictionary as
# a parameter and returns the score for that name if
# it is in the dictionary. If the name is not in the dictionary,
# print an error message and return -1
def getScore(scoreDict, name):
    if name in scoreDict:
        score = scoreDict[name]
    elif name not in scoreDict:
        score = -1
        print("Error name not in dictionary")
    return score

if __name__ == "__main__":
    ## TODO: Uncomment each function call out as you work through the questions.
    ## When you're finished, all of them should be uncommented.
    ## DO NOT make any other changes here other than to uncomment.
   
    avgs1 = scoreAverage(scoreDict1)
    avgs2 = scoreAverage(scoreDict2)
    print("Q4 - testA:", avgs1)
    print("Q4 - testB:", avgs2)
    
    print("----------------------")
    print("Q5 - testA:")
    printTable(scoreDict1)
    print("Q5 - testB:")
    printTable(scoreDict2)
    
    print("----------------------")
    s1 = getScore(scoreDict1, 'mary')
    s2 = getScore(scoreDict2, 'mary')
    print("Q6 - testA:", s1)
    print("Q6 - testB:", s2)

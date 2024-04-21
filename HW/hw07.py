# Your Name
# HW 7

# Q1 [2pt]: Finish/fix the following function so that it takes the
# two lists and returns a dictionary with the names as the key
# and the scores as the values.
def makeDictionary(names, scores):
    newdict= dict(zip(names, scores))
    return newdict
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

# Q3 [1pt]: Create and return a sorted list of all the scores in scoreDict
def sortedScores(scoreDict):
    allValues = list(scoreDict.values())
    allValues.sort()
    return allValues

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
    names1 = ['joe', 'tom', 'barb', 'sue', 'sally']
    scores1 = [10,     25,    10,     20,    5]
    scoreDict1 = makeDictionary(names1, scores1)
    
    names2 = ['joe', 'tom', 'barb', 'sue', 'sally', 'mary', 'jean']
    scores2 = [25,     10,    40,     15,    10,      40,    10]
    scoreDict2 = makeDictionary(names2, scores2)
    print("Q1 - testA:", scoreDict1)
    print("Q1 - testB:", scoreDict2)
    
    print("----------------------")
    scoreDict1 = modifyDictionary(scoreDict1)
    scoreDict2 = modifyDictionary(scoreDict2)
    print("Q2 - testA:", scoreDict1)
    print("Q2 - testB:", scoreDict2)
    
    print("----------------------")
    myScores1 = sortedScores(scoreDict1)
    myScores2 = sortedScores(scoreDict2)
    print("Q3 - testA:", myScores1)
    print("Q3 - testB:", myScores2)
    
    print("----------------------")
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

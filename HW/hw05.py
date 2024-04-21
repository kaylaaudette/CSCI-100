# Your Name
# HW 5


# Q1 [0.5pt] Finish/fix this function so that it returns
# the first 6 characters from the string parameter myString.
# Use the slice operator.
def firstSix(myString):
    return myString[:6] 

# Q2 [0.5pt] Finish/fix this function so that it returns
# the last 5 characters from the string parameter myString.
# Use the slice operator.
def lastFive(myString):
    return myString[-5:] 

# Q3 [0.5pt] Finish/fix this function so that it returns
# a substring of myString consisting of
# first 8 characters followed by a single space followed
# by the last 8 characters.
def partialSubstring(myString):
    return myString[:8] + " " + myString[-8:]

# Q4 [0.5pt] Finish/fix this function so that it returns
# the number of characters appearing in myString
def howManyCharacters(myString):
    return len (myString)

# Q5 [0.5pt] Finish/fix this function so that it returns
# the number of occurrences of the character 'u' in myString
def numOccurrences(myString):
    return myString.count('u')

# Q6 [0.5pt] Finish/fix this function so it replaces all
# occurrences of the substring 'he' with 'vx'
def weirdReplace(myString):
    return myString.replace('he', 'vx')

# Q7 [0.5pt] Finish/fix this function so it returns the
# ASCII value of the single character
def toASCII(ch):
    return ord(ch)

# Q8 [1pt] Finish/fix this function so it returns the
# first index of where the character ch occurs in myString.
# If the character ch does not belong in the myString,
# then return "NOT FOUND"
def firstIndex(myString, ch):
    if ch in myString:
        return myString.index(ch)
    else:
        return "NOT FOUND"



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

# Q12 [1pt] Write a function called stripSpaces which takes one
# parameter representing a phrase/paragraph, and return the
# same phrase/paragraph with the order of letters in tact but the
# spaces between each word removed
def stripSpaces(phrase):
    newPhrase = phrase.replace(' ','')
    return newPhrase

# Q13 [1pt] Finish/fix the following function so that EACH of
# the characters in the parameter badSet are removed from
# the parameter myPhrase. Keep the original order of letters in tact.
def cleanUp(myPhrase, badSet):
    newPhrase= myPhrase
    for ch in badSet:
        newPhrase = newPhrase.replace(ch, '')
    return newPhrase
# newphrase = myPhrase.replace(badSet, '') you want to remove each on indivdually 
   

if __name__ == "__main__":
    ## TODO: Uncomment each function call out as you work through the questions.
    ## When you're finished, all of them should be uncommented.
    ## Do not make any other changes here other than for uncommenting.
    print("Q1 - testA:", firstSix("Python's so cool") )
    print("Q1 - testB:", firstSix("Ada Lovelace Day is in a few weeks") )
    print("----------------------")
    print("Q2 - testA:", lastFive("Ada worked with Charles Babbage") )
    print("Q2 - testB:", lastFive("in the 1800s on the Analytical Engine") )
    print("----------------------")
    print("Q3 - testA:", partialSubstring("She envisioned computers being more than calculators,") )
    print("Q3 - testB:", partialSubstring("coining the term 'poetical science'.") )
    print("----------------------")
    print("Q4 - testA:", howManyCharacters("Ada wrote the") )
    print("Q4 - testB:", howManyCharacters("first computer program") )
    print("----------------------")
    print("Q5 - testA:", numOccurrences("It computed") )
    print("Q5 - testB:", numOccurrences("Bernoulli numbers") )
    print("----------------------")
    print("Q6 - testA:", weirdReplace("here are some fun facts about her") )
    print("Q6 - testB:", weirdReplace("She was the daughter of the English poet Lord Byron") )
    print("----------------------")
    print("Q7 - testA:", toASCII('a') )
    print("Q7 - testB:", toASCII('A') )
    print("----------------------")
    print("Q8 - testA:", firstIndex("She was called the 'Princess of Parallelograms'", "w") )
    print("Q8 - testB:", firstIndex("She conceptualised a flying machine", "z") )
    print("----------------------")
    print("Q9 - testA:", letterGrade(90) )
    print("Q9 - testB:", letterGrade(85) )
    print("Q9 - testC:", letterGrade(71) )
    print("Q9 - testD:", letterGrade(68) )
    print("Q9 - testF:", letterGrade(57) )
    print("----------------------")
    print("Q10 - testA:", letterToIndex('a') )
    print("Q10 - testB:", letterToIndex('z') )
    print("Q10 - testC:", letterToIndex('Y') )
    print("Q10 - testD:", letterToIndex('*') )
    print("----------------------")
    print("Q11 - testA:", indexToLetter(0, True) )
    print("Q11 - testB:", indexToLetter(0, False) )
    print("Q11 - testC:", indexToLetter(25, True) )
    print("Q11 - testD:", indexToLetter(24, False) )
    print("Q11 - testE:", indexToLetter(-3, False) )
    print("Q11 - testF:", indexToLetter(26, True) )
    print("----------------------")
    print("Q12 - testA:", stripSpaces("Hello CS100, what a beautiful day"))
    print("Q12 - testB:", stripSpaces("computer science is awesome") )
    print("----------------------")
    print("Q13 - testA:", cleanUp("it's- a. great. day. punctuation, is! my: friend; said, e.e. cummings!", ",.-'!:;"))
    theRaven = "while i nodded, nearly napping, suddenly there came a tapping, as of some one gently rapping, rapping at my chamber door."
    print("Q13 - testB:", cleanUp(theRaven, "ipgn") )


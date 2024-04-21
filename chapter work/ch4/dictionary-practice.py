# Write a function, toPirate, that takesan English sentence in the form of a string as a parameter.
# The toPirate functionshould return a string containing the pirate translation of your sentence.
# Use thetable below to construct a translation dictionary.

def toPirate(str):
    # initialize a dictionary mapping regular words to pirate version words
    Piratedictionary = {
        "hello": "avast",
        "excuse": "arr",
        "sir": "matey",
        "boy": "matey",
        "man": "matey",
        "madam": "proud beauty",
        "officer": "foul blaggart",
        "the": "th`",
        "my": "me",
        "your": "yer",
        "is": "be",
        "are": "be",
        "restroom": "head",
        "restaurant": "galley",
        "hotel": "fleabag inn",
        }
    
    input_sentence= str(input("Enter a sentence:"))
    allWords = input_sentence.split()
    pirate = ""
    for word in allWords:
        if word in Piratedictionary:
            pirate = pirate + Piratedictionary[word] + " "
        else:
            pirate = pirate + word + " "
    return pirate
print( toPirate(str) )
# for every word in the string s we are given,
# - see if it has a pirate version assoicated with it
# - if it does, we can use the pirate-version word instead
# - if it doesn't, we can use what we are given




# strings and chars
x = "Good morning CS100"

# + concatenation - no space is added
print(x + "How are you?")

#repetition
print(x*3)

#hello_msg!
#0123456789...
# [] index operator (operator we can preform on string and will guve us exactly one character back.
print( x[0]) # index 0 (1st character)
print( x[3]) # index 3 (4th character)
print( x[-1]) # last
print( x[-5]) # 5th to last

# length (how many charcaters?)
print( len(x) )

# what is the last character?
#hello len("hello") = 5
#01234
lastIndex = len(x) - 1
print( x[lastIndex] )

# [:] slice operator
print( x[:4] )   # substring from [0, 4)
print( x[13:] )  # sunstring from [13, len(x)0
print( x[5:12] ) # substring from [5, 12)

# containmnt and other operations
print( "cs" in x)
print( "cs" in x.lower() )
print( x.count("n") ) # how many characters match
print( x.index("n") ) # where is forst occurence?
print( x.find("n") )  # same (but -1 if not found)



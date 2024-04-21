str = "python"
otherStr = str[:-1]
print(otherStr)





def mysteryFunction(myString, removeString):
    newStr = ""
    for ch in myString:
        if ch not in removeString:
            newStr = newStr + ch
    return newStr

print( mysteryFunction("hello!", "hi there") )
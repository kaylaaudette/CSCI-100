# Option D: Dictionaries

#See activity 20 (dictionaries)

#Create a dictionary containing the name and value of US denominations (penny, nickel, etc.)
denominations = {"dime": 0.10, "quarter": 0.25}
denominations["penny"] = 0.01 #[key] = value 
denominations["nickel"] = 0.05

print(denominations)

heathersCurrency = {
    "rupee": 1,
    "toaster": 100,
    "bird": 10000
    }

# merges two dictionaries
mergedDictionary = {}
for key in denominations:
    val = denominations[key]
    mergedDictionary[key] = val
print(mergedDictionary)

for key in heathersCurrency:
    val = heathersCurrency[key]
    mergedDictionary[key] = val
print(mergedDictionary)

#Use a while loop to add (key, value) pairs input from the user into a dictionary.
kaylaDictionary = {}
k = input("Enter in a key (Q to quit):")
while (k != "Q"): #not equal to
    v = input("Enter in a value: ")
    kaylaDictionary[k] = v
    k = input("Enter in a key (Q to quit):") # we will be checking if they added a Q
    
print(kaylaDictionary)
     
# Option E: Statistics – mean, median, mode, frequency distribution, correlation

# See activity 21 (Frequency distribution)
# See activity 23 (Correlation)
# Consider the list a=[1, 2, 3, 4, 1, 2, 3, 1, 3, 1, 2, 4, 5, 1, 2, 3, 6, 7, 3, 3, 1].
# Compute the mean, median, mode, and calculate the frequency distribution.
b =[1, 2, 3, 4, 1, 2, 3, 1, 3, 1, 2, 4, 5, 1, 2, 3, 6, 7, 3, 3, 1]
def mean(alist):
    mean = sum(alist) / len(alist)
    return mean
print("mean:", mean(b))

feq = {}
for item in b:
    item = str(item)
    if item in feq:
        feq[item] += 1
    else:
        feq[item] = 1
    print(feq)
    
feq = feq.values() #vaules number of occurances
maxcount = max(feq)
print("Max:", maxcount)



# Option F: Reading/writing to files
#See activity 23
#Save the rainfall.txt file locally.
#Count how many lines are in the file.
rainFile = open("rainfall.txt", 'r') #read file

numLines = 0
for line in rainFile: #go through each line in file
    lineWithoutLastCharacter = line[:-1]
    print(lineWithoutLastCharacter) #we can see all of our rainfall data (there was an extra line character)
    numLines += 1 # name whatever numLines and add lines each time you go through loop

print("Number of lines is:", numLines)
rainFile.close()

#Create a file called numbers.txt and write to it the
#first 100 numbers using a while loop

numberFile = open("number.txt", "w")#we are creating it "writing"

# using a for loop for first 100 numbers
for i in range(1, 101): #start at 1
    thingToWrite = str(i) + "\n" # makes i into string
    numberFile.write(thingToWrite) # i is a number but our function is a string
    # gives us numbers but not seperated so we add \n to make text go onto new line

# using a while loop for the next 100 numbers
nextNum = 101 #initilize to 101
while(nextNum <= 200):
    nextThingToWrite = str(nextNum) + "\n"
    numberFile.write(nextThingToWrite)
    nextNum += 1 # we have to increment it
    
numberFile.close()


#Option G: Reading from internet

#Read (but do not download) the file from http://csweb.wooster.edu/hguarnera/cs100/assignments/rainfall.txt.
#Output the contents of the page to the terminal decoded in UTF-8 format.
import urllib.request

url = urllib.request.urlopen("http://csweb.wooster.edu/hguarnera/cs100/assignments/rainfall.txt")

Table = url.readlines()

print(Table)

output = [line.decode("utf-8") for line in Table] #decoding every line in Table (gets rid of b)

print(output)

for item in output:
    print(item)


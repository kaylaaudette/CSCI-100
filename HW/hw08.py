# HW 8

# Finish the following function, which will take no parameters.
# It should read the rainfall.txt file and writes out to a new file called outRainfall.txt
# The new file should format each line so that the city is right-justified
# in a field that is 25 characters wide, and the rainfall data should be
# printed in a field that is 5 characters wide with 1 digit to the right
# of the decimal point.
def saveRainfallData():
    Rainfall = open('rainfall.txt', 'r')
    Rainfall2= open( 'outRainfall.txt', 'w')
    
    for line in Rainfall:
        split = line.split()
        
        city = split[0]
        inches = float(split[1])
        
        Rainfall2.write("%+25s %5.1f \n" % (city, inches))

    Rainfall.close()
    Rainfall2.close()
print("Running Q1: Rainfall data")

        
# Finish the following function, which will take no parameters.
# It should create and write to a file called outTemp.txt in order to create
# a temperature conversion table. The table should include temperatures from -300
# to 212 degrees Fahrenheit and their Celsius equivalents, presented in 2 columns
# with appropriate headings. Each column should be 10 characters wide, and each
# temperature should have 3 digits to the right of the decimal point.
def temperatureConversion():
    temperature = open("outTemp.txt", "w")
    temperature.write("%10s %10s \n" % ("Fahrenhiet", "Celcius"))
    
    for fahrenheit in range (-300, 213):
        
        celcius = 5/9*(fahrenheit - 32)
        temperature.write("%10.3f %10.3f \n" % (fahrenheit, celcius))
        
    temperature.close
print("Running Q2: Temperature conversion table")

# Finish the following function, which will take no parameters.
# It should read in the contents of the file loremipsum.txt and write out
# a new file called outLOREMIPSUM.txt where all the characters of the file are
# uppercase.
def contentsToUppercase():
    Uppercase = open('loremipsum.txt', 'r')
    Uppercase1 = open('outLOREMIPSUM.txt', 'w')
    
    for case in Uppercase:
        Uppercase1.write(case.upper())
    Uppercase.close()
    Uppercase1.close()
          
print("Running Q3: Uppercase file contents")

# alternate but don't really understadn the "a"
# def contentsToUppercase():
#     Uppercase = open('loremipsum.txt', 'r')
#     
#     for case in Uppercase.read():
#         newcase = case.upper()
#         Uppercase1 = open('outLOREMIPSUM.txt', 'a')
#         Uppercase1.write(newcase)
#           
#     print("Running Q3: Uppercase file contents")

# Finish the following function, which will take no parameters.
# It should read in the file 'loremipsum.txt' and print out
# the number of lines, words, and characters in the file.
def fileContentMetrics():
    file = open('loremipsum.txt', 'r')
    lines = 0
    word = 0
    characters = 0
    
    for line in file:
        lines = lines + 1
        wordslist = line.split()
        word += len(wordslist)
        characters += len(line)
        
    print("lines:", lines)
    print("words:", word)
    print("chars:", characters)
    file.close()

if __name__ == "__main__":
    # Q1
    saveRainfallData()
    
    # Q2
    temperatureConversion()
    
    # Q3
    contentsToUppercase()
    
    # Q4
    fileContentMetrics()
    
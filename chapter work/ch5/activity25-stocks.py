import math
import turtle
import urllib.request
   
# compute and return the mean of a given list
def mean(alist):
    mean = sum(alist) / len(alist)
    return mean
   
# compute and return the standard deviation of a given list
def standardDev(alist):
    theMean = mean(alist)    
    sum = 0
    for item in alist:
        difference = item - theMean
        diffsq = difference ** 2
        sum = sum + diffsq
           
    sdev = math.sqrt(sum/(len(alist)-1))
    return sdev
   
# compute and return the Pearson's correlation coefficient between two lists
def correlation(xlist, ylist):
    xbar = mean(xlist)
    ybar = mean(ylist)
    xstd = standardDev(xlist)
    ystd = standardDev(ylist)
    num = 0.0
    for i in range(len(xlist)):
        num = num + (xlist[i]-xbar) * (ylist[i]-ybar)
    corr = num / ((len(xlist)-1) * xstd * ystd) 
    return corr
   
# given two lists, plot the correlation between them
def plotCorrelation(xlist, ylist):
    wn = turtle.Screen()
    minX = min(xlist)
    minY = min(ylist)
    maxX = max(xlist)
    maxY = max(ylist)
    wn.setworldcoordinates(minX, minY, maxX, maxY)
       
    t = turtle.Turtle()
    t.speed('fastest')
    turtle.tracer(0, 0)
       
    for i in range(0, len(xlist)-1):
        t.up()
        t.goto(xlist[i], ylist[i])
        t.down()
        t.dot()
           
    wn.exitonclick()
  
# open two CSV files from the internet to read them (without downloading them locally)
url1 = urllib.request.urlopen("http://csweb.wooster.edu/hguarnera/cs100/assignments/AMZN.csv")
url2 = urllib.request.urlopen("http://csweb.wooster.edu/hguarnera/cs100/assignments/AAPL.csv")

# get rid of header rows from CSV files
amazonTable = url1.readlines()
appleTable = url2.readlines()
   
# use list comprehension to parse file from website as bytestring into a list of list of strings
amazonStocks = [line.decode("utf-8").split(',') for line in amazonTable[1:] ]
appleStocks = [line.decode("utf-8").split(',') for line in appleTable[1:] ]
   
# use list comprehension to form a list of just closing price as a floating point number
amazonClose = [ float(amazonStocks[i][4]) for i in range( len(amazonStocks) )]
appleClose = [ float(appleStocks[i][4]) for i in range( len(appleStocks) )]
   
# TODO: add code here to answer next questions (hint: you only need 2-3 lines total!)
for item in amazonClose:
    print(item)
    
print ("Correlation:", correlation(amazonClose, appleClose))

plotCorrelation(amazonClose, appleClose)
# This tell us that if Apple’s stock price goes up, is it likely that Amazon’s stock price will go up


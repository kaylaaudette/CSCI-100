import turtle
import math
   
# returning the average of alist
def mean(alist):
    mean = sum(alist) / len(alist)
    return mean
   
   
# displays a frecquncy chart for items in given list
def frequencyChart(alist):
       
    # initialize an empty dictionary 
    countdict = {}      
   
    # store the number of times each item appears in the given list
    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1         
       
    # list is : [3,3,5,7,1,2,5,2,3,4,6,3,4,6,3,4,5,6,6]
    # countdict is: { 3: 1,
    #                 5: 1,
    #                 7: 1,
    #                 1: 1,
    # itemList is a list of UNIQUE elements from alist
    itemlist = list(countdict.keys())
    minitem = 0
    maxitem = len(itemlist)-1
       
    # the max number of times the item occurs
    countlist = countdict.values() #vaules number of occurances
    maxcount = max(countlist)
       
    # calls a turtle 
    # sets the turtles coordinates
    wn = turtle.Screen()
    chartT = turtle.Turtle()
    wn.setworldcoordinates(-1,-1,maxitem+1,maxcount+1)
    chartT.hideturtle()
       
    # tells turtle where to go
    chartT.up()
    chartT.goto(0,0)
    chartT.down()
    chartT.goto(maxitem,0)
    chartT.up()
       
    # draws the chart
    chartT.goto(-1,0)
    chartT.write("0",font=("Helvetica",16,"bold"))
    chartT.goto(-1,maxcount)
    chartT.write(str(maxcount),font=("Helvetica",16,"bold"))
       
    # plots the points on the chart
    for index in range(len(itemlist)):
        print("Index: ", index) # printing the index of each vaule that occurs in the item list in the shell
        chartT.goto(index,-1) # making tutrle go to the horizontial position of where the value will be on the chart
        chartT.write(str(itemlist[index]),font=("Helvetica",16,"bold")) # labels the x axis
           
        chartT.goto(index,0)
        chartT.down()
        chartT.goto(index,countdict[itemlist[index]])
        chartT.up()
                   
    # add code to plot mean of occurrences in red
    m = mean(countlist)
    chartT.goto(0, m)
    chartT.pencolor('Red')
    chartT.down()
    chartT.goto(maxitem, m)
   
    wn.exitonclick()
   
   
#lst = [7, 11, 9, 18,15, 12]
lst = [3,3,5,7,1,2,5,2,3,4,6,3,4,6,3,4,5,6,6]
#lst = [2,3,4,2,3,3]
#lst = ['a', 'b', 'c', 'd', 'f', 'c', 'b', 'c', 'a', 'd', 'a', 'b', 'b', 'c', 'b', 'a', 'c', 'd']
   
#
frequencyChart(lst)
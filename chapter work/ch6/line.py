# Kayla Audette 
from image import *
import random 

myWindow = ImageWin(600, 400, "My Awesome Window")
img = FileImage("wooster-img.jpg")
img.draw(myWindow)
   
# Activity 
from image import *
   
myWin = ImageWin(300, 300, "Class image")
   
# create a new image which we modify
img = EmptyImage(300,300)
   
blackPixel = Pixel(0,0,0) # change number change color 
   
# diagonal pixels are colored black
for i in range(300):
    img.setPixel(i,i,blackPixel)
       
# YOUR CODE HERE (change image before it is displayed & saved)
for x in range(100):
    for y in range(100):
        Pixelcolor = Pixel(250,0,0)
        img.setPixel(x,y,Pixelcolor)
        
for x in range(100,300):
    for y in range(101):
        randomred = random.randrange(250)
        randomgreen = random.randrange(250)
        randomblue = random.randrange(250)
        img.setPixel(x,y, Pixel(randomblue,randomgreen,randomred) )
        
# displays the image
img.draw(myWin)
   
# saves image to the given file name
img.save("classImg.gif")
   
# when you click anywhere on the window, it closes
myWin.exitOnClick()
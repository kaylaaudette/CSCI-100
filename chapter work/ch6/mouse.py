from image import *
   
# get image
img = FileImage("mickey.jpg")
width = img.getWidth()
height = img.getHeight()
   
# create window
myWin = ImageWin(width, height, "Awesome Image")
   
#Number three nested for loop

# go through each pixel
for row in range(height):
    for col in range(width):
        oldPixel = img.getPixel(col, row)
        
        #get red, green, blue vaules
        r = oldPixel.getRed()
        g = oldPixel.getGreen()
        b = oldPixel.getBlue()
        
        # check if this color is close to yellow
        if (r >= 215) and (g >= 185) and (b <=160):
            bluePixel = Pixel(0,0,255)
            img.setPixel(col,row,bluePixel)
            
def negative(p):
    newRed = 255 - p.getRed()
    newGreen = 255 - p.getGreen()
    newBlue = 255 - p.getBlue()
    newPixels = Pixel(newRed, newGreen, newBlue)
    return newPixels

def pixelMapper(img, rgbFunction):    
    width = img.getWidth()
    height = img.getHeight()
    newImg = EmptyImage(width, height)
       
    for row in range(height):
        for col in range(width):
            originalPixel = img.getPixel(col, row)
            newPixel = rgbFunction(originalPixel)
            newImg.setPixel(col, row, newPixel)
       
    return newImg


            
# display image on window
img = pixelMapper(img, negative)
img.draw(myWin)

# print out RGB values of pixel based on where mouse clicks
x,y = myWin.getMouse()
p = img.getPixel(x,y)
print("Pixel values: ", p.getRed(), p.getGreen(), p.getBlue())
   
# exit window when user clicks on any part of it
myWin.exitOnClick()

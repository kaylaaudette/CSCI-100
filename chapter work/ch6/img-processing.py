from image import *

# takes a pixel and negates it
def negativePixel(oldPixel):
    newRed = 255 - oldPixel.getRed()
    newGreen = 255 - oldPixel.getGreen()
    newBlue = 255 - oldPixel.getBlue()
    return Pixel(newRed, newGreen, newBlue)
   
# take a pixel and make it sepia
def sepiaPixel(oldPixel):
    newR = (oldPixel.getRed() * 0.393) + (oldPixel.getGreen() * 0.769) + (oldPixel.getBlue() * 0.189) 
    newG = (oldPixel.getRed() * 0.349) + (oldPixel.getGreen() * 0.686) + (oldPixel.getBlue() * 0.168) 
    newB = (oldPixel.getRed() * 0.272) + (oldPixel.getGreen() * 0.534) + (oldPixel.getBlue() * 0.131) 
    newR = int(newR)
    newG = int(newG)
    newB = int(newB)
    if newR >255:
        newR = 255
    if newG >255:
        newG = 255
    if newB >255:
        newB = 255
    return Pixel(newR, newG, newB)
   
   
# take a pixel and remove all red from it
def noBluePixel(oldPixel):
    newRed1 = oldPixel.getRed()
    newGreen1 = oldPixel.getGreen()
    newBlue1 = 0
    return Pixel(newRed1, newGreen1, newBlue1)

   
   
# go through each pixel using the provided rgbFunction to modify it
def pixelMapper(oldImage, rgbFunction):    
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    newImg = EmptyImage(width, height)
       
    for row in range(height):
        for col in range(width):
            originalPixel = oldImage.getPixel(col, row)
            newPixel = rgbFunction(originalPixel)
            newImg.setPixel(col, row, newPixel)
       
    return newImg
   
   
# open an image to draw it on the screen
oldImage = FileImage("bird.jpg")
w = oldImage.getWidth()
h = oldImage.getHeight()
myImageWindow = ImageWin(w*2, h*2, "Image Processing")
oldImage.draw(myImageWindow)
   
# process image and display result on other half of the screen
print("Processing image....")
newImage = pixelMapper(oldImage, negativePixel) # using the negativePixel function!
newImage.setPosition(oldImage.getWidth() + 1, 0)
newImage.draw(myImageWindow)

# calling pixelMapper function, and we get something back (newImage)
newImage2 = pixelMapper(oldImage, sepiaPixel) 
newImage2.setPosition(0, oldImage.getHeight() + 1)
newImage2.draw(myImageWindow)
   
newImage3 = pixelMapper(oldImage, noBluePixel)
newImage3.setPosition(oldImage.getWidth() + 1, oldImage.getHeight() + 1)
newImage3.draw(myImageWindow)
   
print("Done!")
   
myImageWindow.exitOnClick()

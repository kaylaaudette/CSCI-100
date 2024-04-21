def negativePixel(oldPixel):
    newRed = 255 - oldPixel.getRed()
    newGreen = 255 - oldPixel.getGreen()
    newBlue = 255 - oldPixel.getBlue()
    return Pixel(newRed, newGreen, newBlue)
   
# take a pixel and make it sepia
def sepiaPixel(oldPixel):
    # FIX
    return oldPixel
   
   
# take a pixel and remove all red from it
def noBluePixel(oldPixel):
    # FIX
    return oldPixel
   
   
   
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
   
newImage2 = pixelMapper(oldImage, sepiaPixel) 
newImage2.setPosition(0, oldImage.getHeight() + 1)
newImage2.draw(myImageWindow)
   
newImage3 = pixelMapper(oldImage, noBluePixel)
newImage3.setPosition(oldImage.getWidth() + 1, oldImage.getHeight() + 1)
newImage3.draw(myImageWindow)
   
print("Done!")
   
myImageWindow.exitOnClick()

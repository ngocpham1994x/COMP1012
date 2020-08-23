"Ngoc Pham 7891063"

#%matplotlib inline
import numpy as np
import matplotlib.pylab as plt  
from scipy import misc

#this function blacks out everything outside a circle whose radius the minimum
#of the height and width of image
#origImg - the image to be manipulated
#returns the altered image
def circle(origImg):
    img = np.array(origImg)  #make a copy of image to manipulate and return
    xSize,ySize,zSize = np.shape(img)

    centerX = xSize/2
    centerY = ySize/2
    radius = min(centerX,centerY)
    
    for x in range(xSize):
        for y in range(ySize):
            if (x - centerX)**2 + (y - centerY)**2 > radius**2:
                img[x,y,:] = 0

    return img


#this function blurs out everything inside a circle whose radius the minimum
#of the height and width of image
#origImg - the image to be manipulated
#returns the altered image
def circleBlur(origImg):
    img = np.array(origImg)
    xSize,ySize,zSize = np.shape(img)

    centerX = xSize/2
    centerY = ySize/2
    radius = min(centerX,centerY)
    
    for x in range(1,xSize-1):
        for y in range(1,ySize-1):
            for z in range(zSize):
                if (x - centerX)**2 + (y - centerY)**2 < radius**2:
                    img[x,y,z] = ((int(img[x-1,y-1,z])+ int(img[x-1,y,z])
                                          + int(img[x-1,y+1,z]) + int(img[x,y-1,z])
                                          + int(img[x,y,z]) + int(img[x,y+1,z])
                                          + int(img[x+1,y-1,z]) + int(img[x+1,y,z])
                                          + int(img[x+1,y+1,z]))/9)

     
    # You have to int each value then divide by 9
    # if no int each value, just int(sum/9) will not work 

    return img


    
#this function blurs in the input image and returns a copy
#of the height and width of image
#origImg - the image to be manipulated
#returns the altered image        
def blur(origImg):
    
    img = np.copy(origImg)  #make a copy of image to manipulate and return
    xSize,ySize,zSize = np.shape(img)
    
    for x in range(1,xSize-1):
        for y in range(1,ySize-1):
            for z in range(zSize):    
                img[x,y,z] = ((int(img[x-1,y-1,z])+ int(img[x-1,y,z])
                                          + int(img[x-1,y+1,z]) + int(img[x,y-1,z])
                                          + int(img[x,y,z]) + int(img[x,y+1,z])
                                          + int(img[x+1,y-1,z]) + int(img[x+1,y,z])
                                          + int(img[x+1,y+1,z]))/9)
    
    # You have to int each value then divide by 9
    # if no int each value, just int(sum/9) will not work 
                
    return img            

#display the image img
def displayImage(img):
    plt.imshow(img)
    plt.show()    

    
#main
f = misc.face()

img = np.array(f[200:400,600:800,:]) # take a part of the picture to work with (for speed issues)
displayImage(img) #display original picture

image = circle(img) 
displayImage(image)

N = 5 #number of times to apply blur function
M = 10 #number of times to apply circleBlur function


#apply blur N times
for i in range(N):
    img = blur(img)
    
displayImage(img) #display blurred image

img = np.array(f[200:400,600:800,:])

#apply circleBlur M times
for i in range(M):
    img = circleBlur(img)
    
displayImage(img) #display image with inside of circle blurred.



import cv2 as cv

img = cv.imread('cat.jpg')
height, width, channel = img.shape

for y in range (height):
    for x in range (width):
        pass
#        print (img[y,x])

print (img[0,0])



import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')
height, width, channel = img.shape

for y in range (height):
    for x in range (width):
        if y < 10:
            img[y,x] = [0,0,255]

cv.imshow('image',img)
cv.waitKey()



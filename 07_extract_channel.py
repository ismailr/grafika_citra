import cv2 as cv
import numpy as np

image = cv.imread('cat.jpg')
(height, width, channel) = image.shape

red = image * [0,0,1]
green = image * [0,1,0]
blue = image * [1,0,0]

red = np.uint8 (red)
green = np.uint8 (green)
blue = np.uint8 (blue)

cv.imshow('red', red)
cv.imshow('green', green)
cv.imshow('blue', blue)
cv.waitKey()


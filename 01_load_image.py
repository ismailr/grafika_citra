import cv2 as cv

img = cv.imread('cat.jpg')
cv.imshow('image',img)
cv.waitKey()

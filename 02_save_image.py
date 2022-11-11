import cv2 as cv

img = cv.imread('cat.jpg')
cv.imwrite('cat_copy.jpg',img)

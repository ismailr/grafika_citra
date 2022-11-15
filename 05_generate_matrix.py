import cv2 as cv
import numpy as np

height, width, channel = (400,400,3)

black = np.zeros ((height, width, channel), dtype='uint8')
cv.imshow('black', black)
cv.waitKey()

white = np.ones ((height, width, channel), dtype='uint8') * 255
cv.imshow('white', white)
cv.waitKey()

red = np.full ((height, width, channel), [0,0,255], dtype='uint8')
cv.imshow('red', red)
cv.waitKey()

grey = np.ones ((height, width, channel), dtype='uint8') * 128
cv.imshow('grey', grey)
cv.waitKey()

random = np.random.rand (height, width, channel) * 255
random = np.uint8(random)
cv.imshow('random', random)
cv.waitKey()


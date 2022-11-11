import cv2 as cv
import numpy as np

image = cv.imread('cat.jpg')
(height, width, channel) = image.shape

add = np.ones((height,width,channel), dtype='uint8') * 100

# tambah intensitas setiap piksel (setiap channel) dengan 100
image_tambah = cv.add (image,add)
image_kurang = cv.subtract (image,add)
cv.imshow('image_lama',image)
cv.imshow('image_tambah',image_tambah)
cv.imshow('image_kurang',image_kurang)
cv.waitKey()

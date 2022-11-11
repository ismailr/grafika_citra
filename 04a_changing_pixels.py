import cv2 as cv

img = cv.imread('cat.jpg')
height, width, channel = img.shape

for y in range (height):
    for x in range (width):
        if y < 10:
            img[y,x] = [0,0,255]

cv.imshow('image',img)
cv.waitKey()

# Ubahlah piksel baris ke 20 - 50
# menjadi warna biru


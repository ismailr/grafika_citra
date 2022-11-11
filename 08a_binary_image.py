import cv2 as cv

img = cv.imread('cat.jpg')
height, width, channel = img.shape

for y in range (height):
    for x in range (width):
        avg = img[y,x].mean()
        if avg > 128:
            img[y,x] = [255,255,255]
        else:
            img[y,x] = [0,0,0]
            
cv.imshow('image',img)
cv.waitKey()

# Ubahlah sehingga warna putih menjadi hitam
# dan warna hitam menjadi putih

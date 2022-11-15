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

# Ubahlah menjadi 3 warna
# jika rata-rata < 85, warna piksel jadi hitam
# jika rata-rata >= 85 dan < 170, warna piksel jadi abu-abu [128,128,128] 
# dan jika rata-rata >= 170, warna piksel jadi putih

import cv2 as cv
import numpy as np
import time

image = cv.imread ("cat.jpg", cv.IMREAD_GRAYSCALE)
height, width = image.shape

result = np.zeros (image.shape, image.dtype)

t = time.time()
for y in range (height - 1):
    for x in range (width - 1):
        value = 5 * image[y,x] - image[y+1,x] - image[y-1,x] - image[y,x-1] - image[y,x+1]
        if value > 255: value = 255
        if value < 0: value = 0

        result[y,x] = value

t = time.time() - t

cv.imshow ("original", image)
cv.imshow ("result", result)
print ("Menajamkan gambar dalam waktu  ", t, "detik")
cv.waitKey()

import cv2 as cv
import numpy as np
import time

image = cv.imread ("cat.jpg")
height, width, channel = image.shape

result = np.zeros (image.shape, image.dtype)

t = time.time()
for y in range (height - 1):
    for x in range (width - 1):
        for c in range(channel):
            value = 5 * image[y,x,c] - image[y+1,x,c] - image[y-1,x,c] - image[y,x-1,c] - image[y,x+1,c]
            if value > 255: value = 255
            if value < 0: value = 0

            result[y,x,c] = value

t = time.time() - t

cv.imshow ("original", image)
cv.imshow ("result", result)
print ("Menajamkan gambar dalam waktu  ", t, "detik")
cv.waitKey()

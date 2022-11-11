import cv2 as cv
import numpy as np
import time

image = cv.imread ("cat.jpg")

t = time.time()
kernel = np.array ([[0,-1,0],
                    [-1,5,-1],
                    [0,-1,0]], np.float32)

result = cv.filter2D (image, -1, kernel)
t = time.time() - t

cv.imshow ("original", image)
cv.imshow ("result", result)
print ("Menajamkan gambar dalam waktu  ", t, "detik")
cv.waitKey()

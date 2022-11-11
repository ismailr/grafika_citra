import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('cat.jpg')
plt.hist(img.ravel(), 256, [0,256])
plt.show()


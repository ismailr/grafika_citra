import numpy as np
import cv2 as cv

img = cv.imread('cat.jpg')

red = img[:,:,2].ravel()
npixels = len(red)

# bin 1 = 0-9, bin 2 = 10-19, bin 3 = 20-29, ..., bin 26 = 250-259
# index bin 1 = 0, index bin 2 = 1, ..., index bin 26 = 25
nbin = 26
imgbin = np.zeros((nbin), dtype=int)

for i in range (npixels):
    index = np.floor (red[i]/10) 
    index = int (index)
    imgbin[index] += 1

print (imgbin)

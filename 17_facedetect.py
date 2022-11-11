import numpy as np
import cv2 as cv

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) == 0: return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

cascade = cv.CascadeClassifier("haarcascade_frontalface_alt.xml")

video = cv.VideoCapture(0)
if not video.isOpened():
    print ("Can not open camera")
    exit()

while True:
    _ret, img = video.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    rects = detect(gray, cascade)
    draw_rects(img, rects, (0, 255, 0))

    cv.imshow('facedetect', img)

    if cv.waitKey(1) == ord('q'):
        break


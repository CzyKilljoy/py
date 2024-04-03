import math

import cv2
import numpy as np


def picshow(name, file):
    cv2.imshow(name, file)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('C:/Users/ASUS/anaconda3/Library/include/boost/compute/interop/opencv/task/src/f2.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# kernal = np.ones((3, 3), dtype=np.uint8)
# img1 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, kernal)
# img1 = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernal)
'''cv2.imshow('cc', img1)
cv2.waitKey(0)'''
a, img2 = cv2.threshold(img1, 180, 255, cv2.THRESH_BINARY)
b, p = cv2.findContours(img2, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
c = len(b)
for i in range(c):
    t = cv2.contourArea(b[i])
    s = cv2.minAreaRect(b[i])
    o = cv2.boxPoints(s)
    o = np.int64(o)
    if 5000 <= t <= 8000:
        cv2.drawContours(img, b, i, (0, 255, 255), 1)
        for j in range(4):
            cv2.line(img, o[j], o[(j + 1) % 4], (0, 0, 255), 3)
picshow('ab', img)
cv2.imwrite('C:/Users/ASUS/anaconda3/Library/include/boost/compute/interop/opencv/picture/t2.png', img)

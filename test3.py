import cv2
import numpy as np


def picshow(name, file):
    cv2.imshow(name, file)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('C:/Users/ASUS/anaconda3/Library/include/boost/compute/interop/opencv/task/src/f3.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
low = np.array([0, 90, 90])
high = np.array([10, 255, 255])
kernal = np.ones((8, 8), dtype=np.uint8)
img2 = cv2.inRange(img1, low, high)
img2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernal)
count, labels, stats, center = cv2.connectedComponentsWithStats(img2, 8, ltype=cv2.CV_16U)
for i in range(0, count):
    if 300 < stats[i, -1] < 10000:
        cv2.rectangle(img, (stats[i, 0], stats[i, 1]), (stats[i, 0]+stats[i, 2], stats[i, 1]+stats[i, 3]), (255, 255, 0), 2)
picshow('kj', img)
cv2.imwrite('C:/Users/ASUS/anaconda3/Library/include/boost/compute/interop/opencv/picture/t3.png', img)

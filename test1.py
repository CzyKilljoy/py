import cv2
import numpy as np


def picshow(name, file):
    cv2.imshow(name, file)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img = cv2.imread('C:/Users/ASUS/anaconda3/Library/include/boost/compute/interop/opencv/task/src/f1.jpg')
img1 = cv2.GaussianBlur(img, (7, 7), 0)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
circle = cv2.HoughCircles(img2, cv2.HOUGH_GRADIENT, 1, 10, param1=100, param2=30, minRadius=0, maxRadius=100)
if circle is not None:
    circles = np.uint16(np.around(circle))
    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 255), -1)
picshow('kj', img)
cv2.imwrite('C:/Users/ASUS/anaconda3/Library/include/boost/compute/interop/opencv/picture/t1.png', img)

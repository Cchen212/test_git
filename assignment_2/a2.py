##### 分段线性变换
import cv2
import numpy as np

img = cv2.imread('D:\DIP4E Book Images Global Edition\lena.tif')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = img.shape[:2]

def divided_liner_transform(imgGray, x1, x2):
    r1, s1 = x1
    r2, s2 = x2

    k1 = s1 / r1
    k2 = (s2 - s1)/(r2 - r1)
    k3 = (255 - s2)/(255 - r2)

    imgTransform = np.empty((width, height), np.uint8)
    for i in range(height):
        for j in range(width):
            r = imgGray[i, j]
            if r <= r1:
                imgTransform[i, j] = k1 * r
            elif r1 < r <= r2:
                imgTransform[i, j] = k2 * (r - r1) + s1
            elif r2 < r:
                imgTransform[i, j] = k3 * (r - r2) + s2
    return imgTransform

imgTransform = divided_liner_transform(imgGray, [96, 30], [182, 220])
cv2.imshow('img', img)
cv2.imshow('imgTransform', imgTransform)
cv2.waitKey(0)
##### 几何变换

import cv2
import numpy as np
import math

img = cv2.imread('D:\DIP4E Book Images Global Edition\lena.tif')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = img.shape[:2]

def geometryTransform(imgGray, a11, a12, a13, a21, a22, a23):
    height, width = imgGray.shape[:2]
    imgGeo = np.empty((height, width), np.uint8)
    #构造变换矩阵A
    A = np.float32([[a11, a12, a13], [a21, a22, a23], [0, 0, 1]])
    for x in range(height):
        for y in range(width):
            x1 = int(np.dot(A, (np.array([x, y, 1])).reshape((-1, 1)))[0])
            y1 = int(np.dot(A, (np.array([x, y, 1])).reshape((-1, 1)))[1])
            if (x1 < 0) | (x1 > height - 1) | (y1 < 0) | (y1 > width - 1):
                continue
            imgGeo[x1, y1] = imgGray[x, y]

    return imgGeo

imgEqual = geometryTransform(imgGray, 1, 0, 0, 0, 1, 0) #恒等变换
imgShrink = geometryTransform(imgGray, 0.5, 0, 0, 0, 0.5, 0) #缩小一半
imgRotate = geometryTransform(imgGray, math.cos(math.pi/4), -math.sin(math.pi/4), 0, math.sin(math.pi/4), math.cos(math.pi/4), 0)#转45度
imgTranslation = geometryTransform(imgGray, 1, 0, 100, 0, 1, 100)#平移
imgVerticalCut = geometryTransform(imgGray, 1, 1, 0, 0, 1, 0)#垂直剪切
imgHorizontalCut = geometryTransform(imgGray, 1, 0, 0, 1, 1, 0)#水平剪切

cv2.imshow('imgGray',imgGray)
cv2.imshow('imgEqual', imgEqual)
cv2.imshow('imgShrink', imgShrink)
cv2.imshow('imgRotate', imgRotate)
cv2.imshow('imgTranslation', imgTranslation)
cv2.imshow('imgVerticalCut', imgVerticalCut)
cv2.imshow('imgHorizontalCut', imgHorizontalCut)
cv2.waitKey(0)
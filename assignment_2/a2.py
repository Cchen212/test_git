##### 分段线性变换
import cv2
import numpy as np

img = cv2.imread('D:\DIP4E Book Images Global Edition\lena.tif')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = img.shape[:2]

### 对比度拉伸
def constrastStretch(imgGray, x1, x2):
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

### 灰度级分层
def grayLevelLayered(imgGray, a, b, type):
    imgLayer = imgGray.copy()

    if type == 0: # type0 保持其他灰度值不变
        # 突出灰度级[a, b]间的亮度
        imgLayer[(imgLayer[: , :] >= a) & (imgLayer[: , :] <= b)] = 255
    else:  # 将不感兴趣的灰度级区域置零
        imgLayer[(imgLayer[: , :] < a) | (imgLayer[: , :] > b)] = 0
        # 突出灰度级[a, b]间的亮度
        imgLayer[(imgLayer[: , :] >= a) & (imgLayer[: , :] <= b)] = 255
    return imgLayer

### 比特平面分层, r为当前比特平面
def bitePlaneLayered(imgGray, r):
    imgBit = imgGray.copy()
    imgBit[: , :] = 255 * (imgBit[: , :] // (2 ** (r - 1)) % 2)
    return imgBit

imgSTretch = constrastStretch(imgGray, [96, 30], [182, 220])
imgLayer0 = grayLevelLayered(imgGray, 155, 225, 0)
imgLayer1 = grayLevelLayered(imgGray, 155, 225, None)
imgBit1 = bitePlaneLayered(imgGray, 1)
imgBit2 = bitePlaneLayered(imgGray, 2)
imgBit4 = bitePlaneLayered(imgGray, 4)
imgBit6 = bitePlaneLayered(imgGray, 6)
imgBit8 = bitePlaneLayered(imgGray, 8)

cv2.imshow('img', img)
cv2.imshow('imgTransform', imgSTretch)
cv2.imshow('imgLayer0', imgLayer0)
cv2.imshow('imgLayer1', imgLayer1)
cv2.imshow('imgBit1', imgBit1)
cv2.imshow('imgBit2', imgBit2)
cv2.imshow('imgBit4', imgBit4)
cv2.imshow('imgBit6', imgBit6)
cv2.imshow('imgBit8', imgBit8)
cv2.waitKey(0)
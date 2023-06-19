##### 非线性变换
import cv2
import numpy as np

img = cv2.imread('D:\DIP4E Book Images Global Edition\lena.tif')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#归一化到[0, 255]
normImg = lambda x: 255. * (x - x.min()) / (x.max() - x.min())

### 对数变换：常用在傅里叶频谱处理中压缩其动态范围，这里只做点运算的例子
def logTransform(imgGray, a):
    imgLog = imgGray.copy()
    imgLog[: , :] = a * np.log(1 + imgLog[: , :])
    imgLog = np.uint8(normImg(imgLog))
    return imgLog

### 伽马变换:常用在对遵循幂律响应的设备进行伽马校正得到输入图像的忠实显示
def gamaTransform(imgGray, c, r):
    imgGama = imgGray.copy()
    imgGama[: , :] = c * pow(imgGama[: , :], r)
    imgGama = np.uint8(normImg(imgGama))
    return imgGama

imgLog = logTransform(imgGray, 3)
imgGama = gamaTransform(imgGray, 2, 2)
cv2.imshow('imgLog', imgLog)
cv2.imshow('imgGama', imgGama)
cv2.waitKey(0)
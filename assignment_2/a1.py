#对随机一张灰度图片进行线性、分段线性、非线性的点运算
#####  线性变换
import cv2
import numpy as np

img = cv2.imread('D:\DIP4E Book Images Global Edition\lena.tif')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = img.shape[:2]

#创建空白数组
img1 = np.empty((height, width), np.uint8)
img2 = np.empty((height, width), np.uint8)
img3 = np.empty((height, width), np.uint8)
img4 = np.empty((height, width), np.uint8)
img5 = np.empty((height, width), np.uint8)
img6 = np.empty((height, width), np.uint8)

#线性变换：Dt[i, j] = a * D[i, j] + b
a1, b1 = 1, 50     #a = 1, b = 50，灰度值上移
a2, b2 = 1, -50    #a = 1, b = -50，灰度值下移
a3, b3 = 1.5, 0    #a > 1, b = 0，对比度增强
a4, b4 = 0.75, 0   #0 < a < 1, b = 0，对比度减小
a5, b5 = -0.5, 255 #a < 0, b = 255，暗区域变亮，亮区域变暗
a6, b6 = -1, 255   #a = -1, b = 255，灰度值反转

for i in range(height):
    for j in range(width):
        img1[i][j] = min(255, max((a1 * imgGray[i][j]) + b1, 0))
        img2[i][j] = min(255, max((a2 * imgGray[i][j]) + b2, 0))
        img3[i][j] = min(255, max((a3 * imgGray[i][j]) + b3, 0))
        img4[i][j] = min(255, max((a4 * imgGray[i][j]) + b4, 0))
        img5[i][j] = min(255, max((a5 * imgGray[i][j]) + b5, 0))
        img6[i][j] = min(255, max((a6 * imgGray[i][j]) + b6, 0))

titleList = ["0.imgGray", "1.b = 50", "2.b = -50", "3.a = 1.5", "4.a = 0.75", "5.a = -0.5", "a = -1"]
imgList = [imgGray, img1, img2, img3, img4, img5, img6]
for i in range(7):
    cv2.imshow(titleList[i], imgList[i])
cv2.waitKey(0)
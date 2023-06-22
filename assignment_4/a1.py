##### 何恺明博士去雾算法复现

import cv2
import numpy as np
from PIL import Image

img = cv2.imread('C:\\Users\\M\\image_processing\\assignment_4\\75.jpg')

### 双端队列
class Deque:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    # 往双端队列前端添加元素
    def addFront(self, item):
        self.items.insert(0, item)
    # 往双端队列后端添加元素
    def addRear(self, item):
        self.items.append(item)
    # 从前端移除双端队列元素：
    def removeFront(self):
        return self.items.pop(0)
    # 从后端移除双端队列元素：
    def removeRear(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def look(self):
        print(self.items)
    def peekleft(self):
        return self.items[0]
    def peek(self):
        return self.items[-1]
    
### 最小滤波器
def minFilter(a, r):
    L = Deque()
    minval = np.zeros(len(a))
    L.addRear(0)
    for i in range(1, len(a), 1):
        while a[i] < a[L.peek()]:
            L.removeRear()
            if L.size() == 0:
                break
        L.addRear(i)
        if i >= r:
            minval[i - r] = a[L.peekleft()]
        if i == 2 * r + L.peekleft():
            L.removeFront()

    for j in range(len(a) - r, len(a), 1):
            if j > r + L.peekleft():
                L.removeFront()
            minval[j] = a[L.peekleft()]
    return minval

### 暗通道图像 r为滤波窗口半径
def darkChannel(img, r):
    height, width = img.shape[:2]
    ###得到每个像素点RGB通道上的最小值
    minRGB = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            minRGB[i][j] = img[i][j][0]
            if minRGB[i][j] > img[i][j][1]:
                minRGB[i][j] = img[i][j][1]
            if minRGB[i][j] > img[i][j][2]:
                minRGB[i][j] = img[i][j][2]

    ### 先对每行进行最小滤波，再通过转置，对每列进行最小滤波，最后再转置回原来的格式
    minDarkChannelRow = np.zeros((height, width))
    for x in range(height):
        minDarkChannelRow[x] = minFilter(minRGB[x], r)
    Transposed = [[row[i] for row in minDarkChannelRow] for i in range(width)]
    minDarkChannelcol = np.zeros((width, height))
    for y in range(width):
        minDarkChannelcol[y] = minFilter(Transposed[y], r)

    minDarkChannel2 = [[row[i] for row in minDarkChannelcol] for i in range(height)]
    minDarkChannel2 = np.array(minDarkChannel2)### 得到二维数组信息

    ### 将二维数组转成图片显示
    minDarkChannel3 = Image.fromarray(minDarkChannel2)
    minDarkChannel3 = minDarkChannel3.convert('L')
    minDarkChannel3 = cv2.cvtColor(np.asarray(minDarkChannel3), cv2.COLOR_RGB2BGR)
    return minDarkChannel3

cv2.imshow('img', img)
minDarkChannel = darkChannel(img, 7)
cv2.imshow('minDarkChannel', minDarkChannel)
cv2.waitKey(0)
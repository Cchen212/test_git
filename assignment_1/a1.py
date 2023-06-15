#生成图像lena不同空间分辨率、不同灰度分辨率的图片
import cv2

img = cv2.imread('D:\DIP4E Book Images Global Edition\lena.tif')
##### 空间分辨率
### 第一种缩放方法，用resize()，在第二个参数给定尺寸大小，这里长和宽放大两倍
# img.shape:查看图像的形状，即图像栅格的行数（高度）、列数（宽度）和通道数，这里将高度和宽度读出赋值
height, width = img.shape[:2]
print("原图分辨率：", img.shape[:2])
enlarge = cv2.resize(img, (2 * width, 2 * height))
print("缩放：放大后：", enlarge.shape[:2])

### 第二种缩放方法，用resize()，在第四、五个参数给定缩放比例。这里长和宽缩小到0.5倍，好处是不用读取长宽
shrink = cv2.resize(img, None, fx = 0.5, fy = 0.5)
print("缩放：缩小后：", shrink.shape[:2])
cv2.imshow('img', img)
cv2.imshow('enlarge', enlarge)
cv2.imshow('shrink', shrink)
cv2.waitKey(0)


##### 灰度分辨率
# 下面函数先将图形量化到level+1级，再量化到256级显示图形
def reduce_intensity_levels(img, level):
    img = cv2.copyTo(img, None)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            si = img[x, y]
            ni = int(level * si / 255 + 0.5) * (255 / level)
            img[x, y] = ni
    return img
# cv2.COLOR_BGR2GRAY 将BGR格式转换成灰度图片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
level8 = reduce_intensity_levels(gray, 7)
level2 = reduce_intensity_levels(gray, 1)
cv2.imshow('gray', gray)
cv2.imshow('level8', level8)
cv2.imshow('level2', level2)
cv2.waitKey(0)
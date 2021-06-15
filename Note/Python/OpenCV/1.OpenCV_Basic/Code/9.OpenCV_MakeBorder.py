import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('RedDotSight.jpg')

#色彩對調
img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#處理範圍
top=200
bottom=200
left=200
right=200

BLUE = [0, 0, 255]  #藍色

#邊界處理
replicate = cv2.copyMakeBorder(img1, top=top, bottom=bottom, left=left, right=right, borderType=cv2.BORDER_REPLICATE)   #重複最後一個像素
reflect = cv2.copyMakeBorder(img1, top, bottom, left, right, cv2.BORDER_REFLECT)    #畫面倒影重複
reflect101 = cv2.copyMakeBorder(img1, top, bottom, left, right, cv2.BORDER_REFLECT_101) #與上相似
wrap = cv2.copyMakeBorder(img1, top, bottom, left, right,cv2.BORDER_WRAP)   #重複圖片
constant = cv2.copyMakeBorder(img1, top, bottom, left, right, cv2.BORDER_CONSTANT, value=BLUE)  #指定顏色
"""
cv2.imshow('replicate', replicate)
cv2.imshow('reflect', reflect)
cv2.imshow('reflect101', reflect101)
cv2.imshow('wrap', wrap)
cv2.imshow('constant', constant)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

plt.subplot(231), plt.imshow(img1), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant), plt.title('CONSTANT')

plt.show()

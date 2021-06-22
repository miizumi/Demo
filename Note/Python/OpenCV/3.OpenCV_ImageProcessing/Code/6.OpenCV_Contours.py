import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('Coin.jpg')  #讀取照片，一定要保留原圖。

img_New=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       #轉灰階
img_New = cv2.medianBlur(img_New,5)                 #中值模糊，為了降噪。
ret , img_New = cv2.threshold(img_New,100,255,0)    #二值化

#找輪廓
contours, hierarchy = cv2.findContours(img_New, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#將輪廓畫至原圖上。
#img = cv2.drawContours(img, contours, -1, (0,0,255))  #畫出所有輪廓
img = cv2.drawContours(img, contours, -1, (0,0,255),3)  #線條粗度=3
#img = cv2.drawContours(img, contours, -1, (0,0,255),-1)  #輪廓填滿

cv2.imshow('Original',img)  #原圖
cv2.imshow('Contours',img_New)  #處理後

cv2.waitKey(0)
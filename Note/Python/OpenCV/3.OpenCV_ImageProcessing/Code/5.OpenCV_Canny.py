import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Coin.jpg', 0)  #讀取灰階照片。

cv2.imshow('Original',img)  #原圖

img= cv2.GaussianBlur(img , (9,9),0)    #高斯模糊
edges = cv2.Canny(img, 100, 200)    #邊緣檢測

cv2.imshow('Edges',edges)   #結果
cv2.waitKey(0)
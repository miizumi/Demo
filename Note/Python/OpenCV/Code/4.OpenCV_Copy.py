import cv2
import numpy as np

img=cv2.imread('1.jpg')#讀取圖片，會讀成ndarray型態。

#取圖片某段
img2=img[100:200,10:50].copy()
cv2.imshow('img2',img2) #備註一下，如果顯示圖片視窗用一樣的名稱，後來者會把前者蓋過，等於只會出現一個視窗。

cv2.imshow('img',img) #顯示圖片，一定要有顯示視窗的名稱。

#複製貼上局部照片，利用numpy的技巧!
img[0:100,0:40]=img2
cv2.imshow('img3',img) #顯示圖片，一定要有顯示視窗的名稱。


cv2.waitKey(0)

cv2.destroyAllWindows()


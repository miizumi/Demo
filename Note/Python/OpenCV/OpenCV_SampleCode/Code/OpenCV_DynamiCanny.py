import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass;

img = cv2.imread('Coin.jpg', 0)  #讀取灰階照片。

cv2.imshow('Original',img)  #原圖

#動態改變視窗
form_Name='DynamicEdge'     #視窗名稱
cv2.imshow(form_Name,img)   #先建立視窗

# TrackBar
cv2.createTrackbar('GaussianBlur',form_Name,0,100,nothing)   #高斯模糊
cv2.createTrackbar('threshold1',form_Name,0,255,nothing)   #threshold1
cv2.createTrackbar('threshold2',form_Name,0,255,nothing)   #threshold2

while True:
    blur_Bar=cv2.getTrackbarPos('GaussianBlur',form_Name)
    t1      =cv2.getTrackbarPos('threshold1',form_Name)   #threshold1
    t2      =cv2.getTrackbarPos('threshold2',form_Name)   #threshold2

    #避免高斯Ksize偶數會出錯。
    if blur_Bar%2 ==0:
        blur_Bar=blur_Bar+1

    edge_Img=cv2.GaussianBlur(img,(int(blur_Bar),int(blur_Bar)),0)
    edge_Img=cv2.Canny(edge_Img,t1,t2)

    cv2.imshow(form_Name,edge_Img)

    key=cv2.waitKey(1)  #每1ms更新

    if key ==27:
        break;


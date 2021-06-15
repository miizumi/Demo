import cv2
import numpy as np
img=cv2.imread('1.jpg')#讀取圖片，會讀成ndarray型態。

#區塊上色。
img[:10,-10:]=[0,255,255]     #右上角
img[-10:,-10:]=[0,255,0]    #右下角

cv2.imshow('image',img) #顯示圖片，一定要有顯示視窗的名稱。
#這次把按鍵記錄起來。
key=cv2.waitKey(0)
if key==27:   #ASCII code27=ESC
    cv2.destroyAllWindows() #關閉
elif key==ord('s'):   #如果是s
    cv2.imwrite('2_new.png', img)   #存檔





import cv2
import numpy as np

img=cv2.imread('ContoursObject.jpg')            #讀取圖片
cv2.imshow('Image',img)

img_Gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #轉灰階
img_New = cv2.medianBlur(img_Gray,5)             #中值模糊

# 二值化，這裡的二值化要將物體變黑，其他區域變白。
ret, img_New = cv2.threshold(img_New, 45 , 255 ,cv2.THRESH_BINARY )

#找輪廓
contours_List , hierarchy = cv2.findContours(img_New,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#避免輪廓取得一些小雜點，可以先做一次篩選

contours_List=[contour for contour in contours_List if cv2.contourArea(contour)>100]

print('物件數量：',len(contours_List))

count=1

for contour in contours_List :

    #取外接矩形
    x,y,w,h =cv2.boundingRect(contour)

    #設定物件在圖片中的範圍
    img_Object = img[y:y+h,x:x+w]
    img_Name= 'Image'+str(count)    #視窗名稱

    cv2.imshow(img_Name,img_Object)

    count+=1

cv2.waitKey(0)
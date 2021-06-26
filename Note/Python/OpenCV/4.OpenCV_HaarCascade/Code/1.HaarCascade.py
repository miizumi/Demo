import cv2
import numpy as np


#先確認cascade文件位置，可以替換不同的訓練檔案，去測試出最好的結果。
#臉部偵測
face_Cascade= cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

#眼睛偵測
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#讀取圖片
img = cv2.imread('izumi.jpg')
img_Gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #轉灰階

#眼睛一定長在臉上，所以先偵測臉，再從臉中偵測眼睛較省效能，也不容易出差錯。
#Cascade偵測 (臉部)
faces=face_Cascade.detectMultiScale(img_Gray,
    scaleFactor=1.1,    #縮放比，可以隨著想要偵測的物體大小調整，必須大於1 (>1)
    minNeighbors=3,
    minSize=(20,30),
    flags=cv2.CASCADE_SCALE_IMAGE)

print("偵測臉部數量：",len(faces))
print(faces)

#框列臉部
for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    eye= eye_cascade.detectMultiScale(img_Gray)
    print("偵測眼睛數量：", len(eye))
    for(eye_X,eye_Y,eye_W,eye_H) in eye:
        cv2.rectangle(img,(eye_X,eye_Y),(eye_X+eye_W,eye_Y+eye_H),(255,0,0),2)


cv2.imshow('image',img)
cv2.waitKey(0)


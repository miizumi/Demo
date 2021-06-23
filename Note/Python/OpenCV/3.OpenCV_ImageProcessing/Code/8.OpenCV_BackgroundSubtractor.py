import cv2
import numpy as np

# pip install opencv-contrib-python

#讀取影像
cap = cv2.VideoCapture('video1.avi')

#宣告主體，有四種可以使用。
mog = cv2.bgsegm.createBackgroundSubtractorMOG()
mog2 = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
gmg= cv2.bgsegm.createBackgroundSubtractorGMG()
knn = cv2.createBackgroundSubtractorKNN(detectShadows=True)

while True:
    ret,frame = cap.read()

    if frame is not None:
        frame_Mask  = mog.apply(frame) #去除背景，會得到一個灰階的遮罩

        cv2.imshow('Mask',frame_Mask)

        frame_New = cv2.bitwise_and(frame,frame,mask=frame_Mask)    #用遮罩做AND運算
        cv2.imshow('Video',frame_New)


        key= cv2.waitKey(20)
        if key == 27: #ESC
            break;
cap.release()
cv2.destroyAllWindows()
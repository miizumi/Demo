import numpy as np
import cv2

def nothing(x):
    pass;


#建立圖底
img=np.zeros((512,512,3),np.uint8)

#建立視窗

window_Name='Image'
#cv2.namedWindow(window_Name)    #正確做法
cv2.imshow(window_Name,0)      #相同效果

##建立滑動桿 TrackBar

#建立三色TrackBar
cv2.createTrackbar('R',window_Name,0,255,nothing)
cv2.createTrackbar('G',window_Name,0,255,nothing)
cv2.createTrackbar('B',window_Name,0,255,nothing)

#開關功能
switch='0(Off / 1(On)'
cv2.createTrackbar(switch,window_Name,0,1,nothing)

while True:

    #取得滑桿位置
    r=cv2.getTrackbarPos('R',window_Name)
    g=cv2.getTrackbarPos('G',window_Name)
    b=cv2.getTrackbarPos('B',window_Name)
    s=cv2.getTrackbarPos(switch,window_Name)

    if s == 0:      #功能關閉
        img[:]=0    #畫布還原成黑色
    else:               #功能開啟
        img[:]=[b,g,r]  #設定顏色


    cv2.imshow(window_Name,img)
    key=cv2.waitKey(1)  #每1ms更新

    if key == 27:
        break;


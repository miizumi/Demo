import cv2
import numpy as np

#畫一張280*280大小的圖，3byte=256色，資料型態是 8bit=1byte=0~255，用0填滿資料所以會是黑色。
img =np.full(shape=(280,280,3),fill_value=0,dtype=np.uint8)

#先佔好視窗
cv2.namedWindow('image')

#做個布林，表示左鍵狀態。
drawing=False

def draw(event,x,y,flags,param):
    global img,drawing;

    if event ==cv2.EVENT_LBUTTONDOWN:   #按下滑鼠左鍵
        drawing=True    #表示左鍵被按下。
        #畫圓圈，座標以事件發生時滑鼠的位置。
        cv2.circle(img,(x,y),2,(255,0,0),-1)    #畫個藍色

    elif (event==cv2.EVENT_MOUSEMOVE) and (drawing == True):    #當左鍵被按下且滑鼠移動
        cv2.circle(img, (x, y), 2, (255, 255, 255), -1) #畫個白色

    elif event ==cv2.EVENT_LBUTTONUP:   #左鍵放開
        drawing=False
        cv2.circle(img,(x,y),2,(0,0,255),-1)    #畫個紅色


#偵測滑鼠動作
cv2.setMouseCallback('image',draw)



#死迴圈，更新圖片
while True:
    cv2.imshow('image',img)
    key=cv2.waitKey(1)

    if key==ord('c'):   #還原成乾淨的畫布
        img=np.full(shape=(280,280,3),fill_value=0,dtype=np.uint8)
    elif key==27:   #ESC
        break;

cv2.destroyAllWindows()
import cv2
import numpy as np

#畫一張280*280大小的圖，3byte=256色，資料型態是 8bit=1byte=0~255，用0填滿資料所以會是黑色。
img =np.full(shape=(280,280,3),fill_value=0,dtype=np.uint8)

#先佔好視窗
cv2.namedWindow('image')

#做個布林，表示左鍵狀態。
drawing=False

#要做連續畫線的功能，所以在加兩個紀錄頭尾X,Y的變數。
last_X=0
last_Y=0

#紀錄畫線前的畫面。
imgbk=img.copy()

def draw(event,x,y,flags,param):
    #全域變數
    global img,drawing,last_X,last_Y,imgbk;

    # 按下滑鼠左鍵
    if event ==cv2.EVENT_LBUTTONDOWN:
        if drawing==False:  #當前狀態不在畫圖中
            #先把畫線前的畫面記起來
            imgbk=img.copy()
            #紀錄當前位置
            last_X=x
            last_Y=y

        drawing=True    #表示左鍵被按下。

    elif event == cv2.EVENT_MOUSEMOVE:    #滑鼠移動
        if drawing == True: #確定左鍵被按下
            #下面兩行要一起看
            #當滑鼠在移動的時候不斷的畫線到目前滑鼠位置、還原畫面。
            img=imgbk.copy()
            cv2.line(img,pt1=(last_X,last_Y),pt2=(x,y),color=(255,255,255),thickness=2)

    elif event ==cv2.EVENT_LBUTTONUP:   #左鍵放開
        drawing=False   #改變按下狀態

        img=imgbk.copy()    #還原畫面
        cv2.line(img,pt1=(last_X,last_Y),pt2=(x,y),color=(255,0,0),thickness=5) #畫出正式要的線。


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
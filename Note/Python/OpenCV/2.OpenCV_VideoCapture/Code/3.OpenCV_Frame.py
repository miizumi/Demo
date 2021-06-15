import numpy as np
import cv2

video = cv2.VideoCapture('VideoForTest.mp4')

#取影片FPS
fps=video.get(cv2.CAP_PROP_FPS)
print("FPS : ",fps)
#倒帶使用，先跳到十秒後(fps*10)。
#video.set(1,fps*10)

while video.isOpened():
    ret , frame = video.read()
    if ret == True: #有取得畫面。

        #目前張數位置
        frame_Now = video.get(cv2.CAP_PROP_POS_FRAMES)
        print("目前張數位置 : ",frame_Now)

        #快轉(跳過張數)
        video.set(1,frame_Now+1)    #2倍速
        #video.set(1,frame_Now+2)   #3倍速
        #video.set(1,frame_Now+4)   #5倍速
        #video.set(1,frame_Now-2)   #倒帶




        #顯示畫面
        cv2.imshow('video',frame)
        key=cv2.waitKey(int(1000/fps))
        #ESC 離開
        if key == 27:
            break;

    else:
        break;

cap.release()
cv2.destroyAllWindows()
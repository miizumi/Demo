import numpy as np
import cv2

"""
即時影像資料來源:
https://tw.live/
"""
cap = cv2.VideoCapture("https://cctvn.freeway.gov.tw/abs2mjpg/bmjpg?camera=15690")



fps = cap.get(cv2.CAP_PROP_FPS)  # FPS
print("fps",fps)

frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 寬
print('H*W：', frame_height ," * ",frame_width)

while cap.isOpened():
    ret, frame = cap.read()                 #取得回應、畫面
    if ret==True:                           #若有取得畫面
        cv2.imshow('frame', frame)          #顯示畫面
        key = cv2.waitKey(int(1000/fps))    #設定更新時間
        if key == 27:  # ESC
          break
    else:
        print("Waiting for connection")


cap.release()
cv2.destroyAllWindows()

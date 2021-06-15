import cv2
import numpy as np

#取得畫面
#cap = cv2.VideoCapture(0)             #鏡頭
cap = cv2.VideoCapture("videoTest.avi") #影片


#畫面尺寸
frame_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 高
frame_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # 寬
print('H：', frame_height )
print('w：', frame_width)


"""
#畫面尺寸   (設定)
frame_width = cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)  # 寬
frame_height = cap.set(cv2.CAP_PROP_FRAME_HEIGHT,200)  # 高
"""



# FPS
fps = cap.get(cv2.CAP_PROP_FPS)  # 25.0  FPS
print("fps", fps)

# 影片長度
num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 總張數
print('Total:', num_frames)  # 影片張數
print('during time sec:', num_frames / fps)  # 影片時長

# 目前畫面位置(第幾張)
FRAME_NOW = cap.get(cv2.CAP_PROP_POS_FRAMES)  # 現在位置 在第幾張
print('frame:', FRAME_NOW)


while(True):
    ret, img = cap.read()
    if img is not None:
         cv2.imshow('img',img)
    k=cv2.waitKey(66)      # 15 FPS   # FPS frame per sec 1000/80
    if k== 27:         # ESC
        break



cap.release()
cv2.destroyAllWindows()


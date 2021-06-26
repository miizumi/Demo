import cv2
import numpy as np
import time


#會返回電腦從某一時間經過Tick的次數
tick1 = cv2.getTickCount()  #記得放在迴圈外，也就是影片讀取前。
print('tick_Last',tick1)

time.sleep(0.01)   #間隔10ms

tick2 = cv2.getTickCount()
print('tick1',tick2)

#計算差異
tick_diff = tick2-tick1
print('tick_diff',tick_diff)

#取得每秒Tick次數
tick_Count=cv2.getTickFrequency()
print('tickCount',tick_Count)

# 實際經過時間
time_Sec =tick_diff /tick_Count  #秒
print('time_Real_Sec',time_Sec)

time_ms =time_Sec*1000  #毫秒
print('time_Real_ms',time_ms)


#算出waitkey
FPS = 30
wait_ms = 1000/FPS

wait_ms=wait_ms-time_ms
print('wait_ms',wait_ms)

#避免出現0或是負數。
if wait_ms<=0:
    wait_ms =1

#最後waitkey的值
print('wait_ms', wait_ms)



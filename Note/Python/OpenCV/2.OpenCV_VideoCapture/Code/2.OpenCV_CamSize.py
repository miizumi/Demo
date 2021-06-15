# https://www.learnpythonwithrune.org/find-all-possible-webcam-resolutions-with-opencv-in-python/
import cv2
import numpy as np
import pandas as pd

cap = cv2.VideoCapture(0)


#取得常見解析度列表
url = "https://en.wikipedia.org/wiki/List_of_common_resolutions"    #維基百科：List of common resolutions
dpi_Df = pd.read_html(url)[0]   #讀取成DataFrame
dpi_Df.columns = dpi_Df.columns.droplevel() #去除多重index

#設定鏡頭
cap = cv2.VideoCapture(0)

#用以儲存已確定的解析度
resolutions = {}

for index, row in dpi_Df[["W", "H"]].iterrows(): #取寬高欄位，並逐行讀取

        #當前嘗試的解析度
        print(row["W"],row["H"])

        #設定解析度
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, row["W"])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, row["H"])

        #取得當前解析度
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

        #存入dict
        resolutions[str(width)+"x"+str(height)] = "OK"
        print(str(width)+" x "+str(height)+"= OK")
print("--------------------")
print(resolutions)
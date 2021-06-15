import cv2
import numpy as np
from ffpyplayer.player import MediaPlayer

#用numpy做出一個全黑的圖
img=np.zeros((512,512,3),np.uint8)

#畫線
cv2.line(img,pt1=(0,511),pt2=(511,0),color=(255,0,0),thickness=5)

#折線、多邊形
points=np.array([[[10,5],[20,30],[70,20],[50,10]]],np.int32)
cv2.polylines(img,points,True,(0,122,122))  #True，最後一筆是否連回第一筆
"""
#老師版本(1,4,1,2)
pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
print(pts.shape)            # (4, 2)
pts = pts.reshape((-1,1,2))  #  4,1,2
print(pts.shape)          # (4, 1, 2)     [[[10,5]] , [[20,30]] , [[70 20]] , [[50 10]]]
t1=np.array([pts])
print(t1.shape)   # (1, 4, 1, 2)
"""


#箭頭，跟畫線方法一樣。
cv2.arrowedLine(img,pt1=(0,250),pt2=(400,370),color=(0,168,0),thickness=4)

#方形，最常出現!(底圖，左上，右下，顏色，粗細)
cv2.rectangle(img,(50,70),(350,150),(118, 247, 228),5)


#空心圓
cv2.circle(img,center=(400,370),radius=90,color=(118, 202, 228),thickness=3)    #radius=圓圈半徑

#實心圓
cv2.circle(img,center=(440,380),radius=40,color=(180, 86, 228),thickness=-1)    #thickness粗細度改成負號，就會填滿圓圈


#扇形
#angle=扇形起始位置,startAngle=從起始位置開始畫圓的起始位置,endAngle=終點位置。
cv2.ellipse(img,center=(256,256),axes=(100,100),angle=30,startAngle=60,endAngle=135,color=(136, 251, 228),thickness=-1)
#所以會畫出 在angle位置開始，從startAngle順時針畫到endAngle的扇形，扇形角度=endAngle-startAngle。


#文字

#先建立字型
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,text='Izumi Github note',org=(60,120),fontFace=font,fontScale=1,color=(219, 186, 195),thickness=2)


from PIL import ImageFont, ImageDraw, Image

# 載入字體
fontPath = "KAIU.TTF" #標楷體
font = ImageFont.truetype(fontPath, 48) #(字體檔案,字體大小)

#將底圖轉換成PIL影像
imgPil = Image.fromarray(img)

#在PIL圖片上繪製文字
draw = ImageDraw.Draw(imgPil)
draw.text((80,450),'育全的GitHub筆記', font = font, fill = (255,255,255))

#在轉回Numpy陣列
img = np.array(imgPil)


#註：所有繪圖的函式返回值都是None，所以不能用指定給變數。

form_Name='image'
#建立空視窗，可以在尚未有圖之前先呼叫出來
cv2.namedWindow(form_Name,0)
cv2.imshow(form_Name,img)

cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
from matplotlib import pyplot as plt


from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['SimSun'] # 替換sans-serif字型
plt.rcParams['axes.unicode_minus'] = False  #解決座標軸負數的負號顯示問題

#讀取後轉灰階
img = cv2.imread('RedDotSight.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#img = cv2.imread('RedDotSight.jpg',0)   #相同讀取+灰階效果

#一般二值化

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)  # <127    0  else 255
#ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
#ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
#ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
#ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

#自適應二值化
img=cv2.medianBlur(img,5)    #5*5中值模糊

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2) #算素平均
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)  #高斯平均

titles = ['原圖', '一般二值化',
          '自適應二值化：算數平均', '自適應二值化：高斯平均']
images = [img, th1, th2, th3]

#分割顯示
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray') #顯示圖片位置
    plt.title(titles[i])            #圖片標題
    plt.xticks([]), plt.yticks([])  #去除座標值

plt.show()


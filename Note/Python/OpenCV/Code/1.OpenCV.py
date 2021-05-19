import cv2

img=cv2.imread('1.jpg')#讀取圖片，會讀成ndarray型態。

cv2.imshow('image',img) #顯示圖片，一定要有顯示視窗的名稱。
#顯示圖片時會因為程式結束，所以圖片視窗也隨之關閉。

#等待按鍵，隨便按都會關閉圖片視窗。(也可以直接關閉視窗)
cv2.waitKey(0)

#使用完關閉，良好習慣。
cv2.destroyAllWindows()
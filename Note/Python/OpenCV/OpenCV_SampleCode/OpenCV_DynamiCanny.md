# Canny邊緣檢測動態調整

_參照code：OpenCV_DynamiCanny.py_

影像處理時要每次調整參數實在累人，可以使用滑動桿動態調整，能省去很多時間。

## 讀取圖片

先將圖片以灰階讀取，方便處理。
```python
img = cv2.imread('Coin.jpg', 0)  #讀取灰階照片。
cv2.imshow('Original',img)  #原圖
```

## 建立滑動桿。

記得一定要先建立視窗，才能建立滑動桿。

```python
#動態改變視窗
form_Name='DynamicEdge'     #視窗名稱
cv2.imshow(form_Name,img)   #先建立視窗

# TrackBar
cv2.createTrackbar('GaussianBlur',form_Name,0,100,nothing)   #高斯模糊
cv2.createTrackbar('threshold1',form_Name,0,255,nothing)   #threshold1
cv2.createTrackbar('threshold2',form_Name,0,255,nothing)   #threshold2
```

## 動態處理

用迴圈做出動態效果，要注意模糊的Ksize只能奇數，所以要做一個避免出錯的部分。
```python
while True:
    blur_Bar=cv2.getTrackbarPos('GaussianBlur',form_Name)
    t1      =cv2.getTrackbarPos('threshold1',form_Name)   #threshold1
    t2      =cv2.getTrackbarPos('threshold2',form_Name)   #threshold2

    #避免高斯Ksize偶數會出錯。
    if blur_Bar%2 ==0:
        blur_Bar=blur_Bar+1

    edge_Img=cv2.GaussianBlur(img,(int(blur_Bar),int(blur_Bar)),0)
    edge_Img=cv2.Canny(edge_Img,t1,t2)

    cv2.imshow(form_Name,edge_Img)

    key=cv2.waitKey(1)  #每1ms更新

    if key ==27:
        break;
```
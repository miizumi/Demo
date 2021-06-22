# 尋找物件

此範例主要透過輪廓找出圖片上的物件，並獨立視窗顯示。

## 預處理

預處理技巧不贅述。

```python
img=cv2.imread('ContoursObject.jpg')            #讀取圖片
cv2.imshow('Image',img)

img_Gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #轉灰階
img_New = cv2.medianBlur(img_Gray,5)             #中值模糊

# 二值化，這裡的二值化要將物體變黑，其他區域變白。
ret, img_New = cv2.threshold(img_New, 45 , 255 ,cv2.THRESH_BINARY )
```


## 找輪廓

找輪廓有時會找到一些奇怪的小點，除了預處理將其清除以外，也可以利用計算面積的小技巧。

```python
contours_List=[contour for contour in contours_List if cv2.contourArea(contour)>100]
```

## 取外接矩形，並獨立顯示。

取得外接矩形，也就等同於找到獨立視窗需要的座標與寬高。

```python
#取外接矩形
x,y,w,h =cv2.boundingRect(contour)

#設定物件在圖片中的範圍
img_Object = img[y:y+h,x:x+w]
img_Name= 'Image'+str(count)    #視窗名稱

cv2.imshow(img_Name,img_Object)
```


執行結果

![find_Object](./Img/find_Obiect.jpg)
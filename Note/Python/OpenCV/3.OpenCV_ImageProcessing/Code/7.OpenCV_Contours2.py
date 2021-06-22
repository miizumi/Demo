import cv2
import numpy as np

img=cv2.imread('ContoursObject.jpg')            #讀取圖片
img_Gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #轉灰階
img_New = cv2.medianBlur(img_Gray,5)             #中值模糊
ret, img_New = cv2.threshold(img_New, 45 , 255 ,cv2.THRESH_BINARY ) #二值化

#找輪廓
contours_List , hierarchy = cv2.findContours(img_New,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

con_Count = 1
for contour in contours_List:

    print("物件編號：",con_Count)

    # 取出物件
    mask = np.zeros(img_Gray.shape,np.uint8)    #與底圖相同規格的單色圖片。
    cv2.drawContours(mask,[contour],-1,255,-1)  #畫出輪廓並以白色填滿。

    mask_Name = "Mask."+str(con_Count)  #分別顯示物件
    img_Mask=cv2.bitwise_and(img, img, mask=mask)   #AND運算
    cv2.imshow(mask_Name,img_Mask)  #顯示圖片
    con_Count+=1

    #cv2.moment 計算動能
    con_Moment=cv2.moments(contour)

    # 分行顯示，可以讓dict跳行不會擠在一起。
    from pprint import pprint
    pprint(con_Moment)

    #計算重心
    con_X=int(con_Moment['m10']/con_Moment['m00'])  #重心的X座標
    con_Y=int(con_Moment['m01']/con_Moment['m00'])  #重心的Y座標

    # 在重心的位置畫出黃色圓點
    cv2.circle(img,(con_X,con_Y),10,(0,255,255),-1)

    #計算面積
    con_Area = cv2.contourArea(contour)
    print("物體面積：",con_Area)

    #計算周長
    con_Perimeter = cv2.arcLength(contour,True)
    print("物體周長：",con_Perimeter)


    #外接矩形(匡列物體)

    x,y,w,h = cv2.boundingRect(contour) #回傳左上角座標x,y 方形的寬高 w,h。
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)  #繪製矩形

    #最小外接矩形(順著物體角度旋轉)

    box = cv2.minAreaRect(contour)  #會返回三個值  座標,寬高,旋轉角度
    """
    a,b,c = cv2.minAreaRect(contour)  #三個值分開承接
    print('a:',a)   #座標(x,y)    #a: (286.4943542480469, 348.7501525878906)
    print('b:',b)   #寬高(w,h)    #b: (151.21095275878906, 280.33673095703125)
    print('c:',c)   #旋轉角度      #c: 88.69805145263672

    (x,y),(w,h),c = cv2.minAreaRect(contour)  #個別承接
    print('x:',x)   #座標X   #x: 286.4943542480469
    print('y:',y)   #座標Y   #y: 348.7501525878906
    print('w:',w)   #寬      #w: 151.21095275878906
    print('h:',h)   #高      #h: 280.33673095703125
    print('c:',c)   #旋轉角度 #c: 88.69805145263672
    """
    box = np.int0(cv2.boxPoints(box))   #去小數點
    cv2.drawContours(img , [box] , -1 , (0,255,0),2)    #繪製輪廓

    #外接正圓
    center,radius=cv2.minEnclosingCircle(contour)   #回傳圓心、半徑

    center=np.int0(center)  #去除小數點
    radius=int(radius)      #去除小數點

    cv2.circle(img,center,radius,(255,0,0),2)   #繪製圓形

    #外接橢圓
    ellipse= cv2.fitEllipse(contour)        #回傳值((座標),(軸長),角度)
    cv2.ellipse(img,ellipse,(255,255,0),2)  #繪製橢圓

    #擬合線
    rows, cols = img.shape[:2]
    [vx, vy, x, y] = cv2.fitLine(contour, cv2.DIST_L2, 0, 0.01, 0.01)
    lefty = int((-x * vy / vx) + y)
    righty = int(((cols - x) * vy / vx) + y)
    cv2.line(img, (cols - 1, righty), (0, lefty), (255, 0, 255), 2)

#形狀匹配

cnt_a, cnt_b, cnt_c = contours_List[0], contours_List[1], contours_List[2]
print(cv2.matchShapes(cnt_a, cnt_a, 1, 0.0))  # 0.0
print(cv2.matchShapes(cnt_a, cnt_b, 1, 0.0))  # 0.4335000641805755
print(cv2.matchShapes(cnt_a, cnt_c, 1, 0.0))  # 0.10646901442163553
print(cv2.matchShapes(cnt_b, cnt_c, 1, 0.0))  # 0.32703104975893993

cv2.imshow('Img',img)
cv2.imshow('contours',img_New)

cv2.waitKey(0)
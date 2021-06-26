import cv2
import numpy as np

# pip install opencv-contrib-python

#宣告兩種，可以比較效果
mog2 = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
gmg= cv2.bgsegm.createBackgroundSubtractorGMG()

#Cascade
person_Cascade=cv2.CascadeClassifier('haarcascade_fullbody.xml')

#讀取影像
cap = cv2.VideoCapture('TownCentreXVID.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
print('FPS : ',fps )

#先計算好，不要放到迴圈內浪費效能。
fps_ms =1000/fps

#計算張數
frame_Count= 0
person_Count = 1
while True:
    ret,frame = cap.read()

    if frame is not None:

        tick1 = cv2.getTickCount()

        #每十張做一次比對
        if frame_Count % 10 == 0:



            frame_New = frame.copy()  # 避免截圖出現線條，複製一個做處理。
            frame=cv2.resize(frame,(640,480))

            frame_Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            frame_mog2  = mog2.apply(frame_Gray) #去除背景，會得到一個灰階的遮罩
            frame_gmg =gmg.apply(frame_Gray)

            #AND運算
            #frame_mog2 = cv2.bitwise_and(frame,frame,mask=frame_mog2)
            #frame_gmg = cv2.bitwise_and(frame,frame,mask=frame_gmg)


            #Haar
            person =person_Cascade.detectMultiScale(
                frame_Gray,
                scaleFactor=1.1,
                minNeighbors=3,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE)

            for (x,y,w,h) in person:
                #儲存照片
                #person_Image = frame[y:y+h,x:x+w]
                #cv2.imwrite('Person_'+str(person_Count)+'.jpg',person_Image)
                #person_Count+=1

                #匡列物體
                cv2.rectangle(frame_New,(x,y),(x+w,y+h),(0,0,255),2)

            cv2.imshow('Video',frame_New)


        # 動態waitkey
        tick_diff=cv2.getTickCount()-tick1

        time_diff=(tick_diff/cv2.getTickFrequency())*1000

        print('time_diff : ',time_diff)

        wait_ms =fps_ms-time_diff

        #當處理時間超過waitkey時
        if wait_ms < 1:
            frame_Jump=(wait_ms/fps_ms)*-1  #計算超過幾個影格。

            frame_Now = cap.get(cv2.CAP_PROP_POS_FRAMES)    #取當前影格位置。
            cap.set(1,frame_Now+frame_Jump) #跳過影格，減緩畫面延遲感。

            wait_ms=1   #讓waitKey不要小於1。

        print('wait_ms :',wait_ms)
        key= cv2.waitKey(int(wait_ms))
        if key == 27: #ESC
            break;
cap.release()
cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread('izumi.png', 0)  # 灰階
cv2.imshow('izumi.png', img)
print(img.shape)

#溶解
kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow('erode', erosion)


#擴充
kernel = np.ones((3, 3), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('dilation', dilation)

kernel = np.ones((3, 3), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=5)
cv2.imshow('dilation2', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()
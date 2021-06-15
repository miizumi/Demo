import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('RedDotSight.jpg', 0)  #讀取灰階照片。

#Laplacian
laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian=cv2.convertScaleAbs(laplacian)

# X方向求導數
sobelx = cv2.Sobel(img, cv2.CV_64F,1, 0, ksize=5)
sobelx=cv2.convertScaleAbs(sobelx)  #絕對值

# Y方向求導數
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
sobely=cv2.convertScaleAbs(sobely)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('RedDotSight.jpg')


blur= cv2.blur(img,(5,5))   #平均模糊
gaussian = cv2.GaussianBlur(img, (7, 7), 0)   #高斯模糊
median=cv2.medianBlur(img,5)    #中值模糊
bilateral=cv2.bilateralFilter(img,5,21,21)    #雙向模糊


cv2.imshow('image',img)
cv2.imshow('blur', blur)
cv2.imshow('gaussian',gaussian)
cv2.imshow('median', median)
cv2.imshow('bilateral', bilateral)

cv2.waitKey(0)
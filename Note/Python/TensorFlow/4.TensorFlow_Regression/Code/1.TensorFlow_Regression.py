import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split



#準備資料----------------------------------------------------

X = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
Y = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

#切割
X_Train,X_Test,Y_Train,Y_Test=train_test_split(X,Y,test_size=0.1)

#建立模組
model=tf.keras.models.Sequential()
import tensorflow as tf
import numpy as np
import pandas as pd

from sklearn import datasets
from sklearn.model_selection import train_test_split

#準備資料----------------------------------------------------

iris_dataframe=datasets.load_iris()

category=3
dim=4


X_Train,X_Test,Y_Train,Y_Test=train_test_split(iris_dataframe.data,iris_dataframe.target,test_size=0.1)

#獨熱編碼
Y_Train2=tf.keras.utils.to_categorical(Y_Train,num_classes=category)
Y_Test2=tf.keras.utils.to_categorical(Y_Test,num_classes=category)


#建立模型
model=tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.relu,input_dim=dim))
model.add(tf.keras.layers.Dense(units=10,activation=tf.nn.relu ))
model.add(tf.keras.layers.Dense(units=category,activation=tf.nn.softmax))

#編譯
model.compile(optimizer='adam',
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=['accuracy'])

#用變數承載會把訓練過程記錄下來，用Debug可以查看可以用的參數。
history=model.fit(X_Train, Y_Train2,
          epochs=200,
          batch_size=128)


#測試
score=model.evaluate(X_Test,Y_Test2,batch_size=128)
print("score:",score)


#畫圖

import matplotlib.pyplot as plt

plt.plot(history.history['accuracy'])
plt.plot(history.history['loss'])
plt.title('model accuracy')
plt.ylabel('acc & loss')
plt.xlabel('epoch')
plt.legend(['acc', 'loss'], loc='upper left')
plt.show()
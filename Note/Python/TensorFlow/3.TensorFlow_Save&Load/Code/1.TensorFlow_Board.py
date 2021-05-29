import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow.keras.callbacks import TensorBoard
from sklearn.model_selection import train_test_split
from sklearn import datasets

#資料準備_鳶尾花----------------------------

iris=datasets.load_iris()

X=iris.data
Y=iris.target

X_Train,X_Test,Y_Train,Y_Test=train_test_split(X,Y,test_size=0.1)

Y_Train2=tf.keras.utils.to_categorical(Y_Train)
Y_Test2=tf.keras.utils.to_categorical(Y_Test)

dim=4
category=len(Y_Train2[0])


model=tf.keras.models.Sequential([
    tf.keras.layers.Dense(units=20,activation=tf.nn.relu,input_dim=dim),
    tf.keras.layers.Dense(units=40,activation=tf.nn.relu),
    tf.keras.layers.Dense(units=category,activation=tf.nn.softmax)
])

#編譯
opt=tf.keras.optimizers.Adam(lr=0.001)
model.compile(optimizer=opt,
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=['accuracy'])

#宣告TensorBoard
tensorboard=TensorBoard(log_dir="logs") #把los檔案存在當前檔案路徑下。

#訓練
history=model.fit(X_Train,Y_Train2,
                  epochs=100,
                  batch_size=20,
                  callbacks=[tensorboard],  #每次訓練儲存log
                  verbose=1)    #處理時的資訊顯示

#測試
score=model.evaluate(X_Test,Y_Test2,batch_size=20)
print("score:",score)
pass;
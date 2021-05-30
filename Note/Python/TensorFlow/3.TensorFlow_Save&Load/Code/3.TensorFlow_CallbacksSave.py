import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn import datasets
from tensorflow.keras.models import model_from_json

#資料準備_鳶尾花----------------------------

iris=datasets.load_iris()

X=iris.data
Y=iris.target

X_Train,X_Test,Y_Train,Y_Test=train_test_split(X,Y,test_size=0.1)

Y_Train2=tf.keras.utils.to_categorical(Y_Train)
Y_Test2=tf.keras.utils.to_categorical(Y_Test)

dim=4
category=len(Y_Train2[0])


#讀取模型與權重-------------------------------

try:    #用Try包裝，讀取失敗就改成建立新模型。
    #讀取架構
    with open('model_callbacksSave.json', 'r') as f:
        model = model_from_json(f.read())
    #讀取權重
    model.load_weights('model_callbacksSave.h5')

    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
                  loss=tf.keras.losses.categorical_crossentropy,
                  metrics=['accuracy'])

except IOError: #在發生讀取失敗才進到此處。
    #建立新模型
    model=tf.keras.models.Sequential([
        tf.keras.layers.Dense(units=20,activation=tf.nn.relu,input_dim=dim),
        tf.keras.layers.Dense(units=40,activation=tf.nn.relu),
        tf.keras.layers.Dense(units=category,activation=tf.nn.softmax)
    ])

    #編譯
    model.compile(optimizer=tf.keras.optimizers.Adam(lr=0.001),
                  loss=tf.keras.losses.categorical_crossentropy,
                  metrics=['accuracy'])
    # 儲存模型架構
    with open('model_callbacksSave.json', 'w') as f:
        f.write(model.to_json())



#儲存模型權重

check_Point=tf.keras.callbacks.ModelCheckpoint(
    "model_callbacksSave.h5",monitor='loss',
    save_best_only=True,mode='auto',period=1)


#訓練
history=model.fit(X_Train,Y_Train2,
                  epochs=1000,
                  batch_size=20,
                  callbacks=[check_Point,])

#測試
score=model.evaluate(X_Test,Y_Test2,batch_size=20)
print("score:",score)
pass;
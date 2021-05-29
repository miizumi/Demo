import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn import datasets
import tensorflow as tf


#資料準備_鳶尾花----------------------------

iris=datasets.load_iris()

X=iris.data
Y=iris.target

X_Train,X_Test,Y_Train,Y_Test=train_test_split(X,Y,test_size=0.1)

Y_Train2=tf.keras.utils.to_categorical(Y_Train)
Y_Test2=tf.keras.utils.to_categorical(Y_Test)

dim=4
category=len(Y_Train2[0])


#用函式建立模組

def mlp_Model(opt):
    # 建立模組
    model=tf.keras.models.Sequential([
        tf.keras.layers.Dense(units=20,activation=tf.nn.relu,input_dim=dim),
        tf.keras.layers.Dense(units=40,activation=tf.nn.relu),
        tf.keras.layers.Dense(units=category,activation=tf.nn.softmax)
    ])

    #編譯
    model.compile(optimizer=opt,
                  loss=tf.keras.losses.categorical_crossentropy,
                  metrics=['accuracy'])

    #訓練
    history=model.fit(X_Train,Y_Train2,epochs=100,batch_size=20)

    return history


#各種優化器訓練---------------------------------------

learning_Rate=0.01

adam_History=mlp_Model(tf.keras.optimizers.Adam(lr=learning_Rate))    #lr=學習效率
sgd_History=mlp_Model(tf.keras.optimizers.SGD(lr=learning_Rate))
rms_History=mlp_Model(tf.keras.optimizers.RMSprop(lr=learning_Rate))
adagrad_History=mlp_Model(tf.keras.optimizers.Adagrad(lr=learning_Rate))
adadelta_History=mlp_Model(tf.keras.optimizers.Adadelta(lr=learning_Rate))
Nadam_History=mlp_Model(tf.keras.optimizers.Adagrad(lr=learning_Rate))
#動量調整
mom_History=mlp_Model(tf.keras.optimizers.SGD(lr=learning_Rate,momentum=0.9))

#繪製成圖-------------------------------------------

import  matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['SimSun'] # 替換sans-serif字型
plt.rcParams['axes.unicode_minus'] = False  #解決座標軸負數的負號顯示問題

#畫線
plt.plot(adam_History.history['accuracy'])
plt.plot(sgd_History.history['accuracy'])
plt.plot(rms_History.history['accuracy'])
plt.plot(adagrad_History.history['accuracy'])
plt.plot(adadelta_History.history['accuracy'])
plt.plot(Nadam_History.history['accuracy'])
plt.plot(mom_History.history['accuracy'])

#圖表設定
plt.title('優化器準確率訓練過程')
plt.ylabel('準確率')
plt.xlabel('訓練次數')
plt.legend(['Adam','SGD','RMSprop','Adagrad','Adadelta','Nadam','Momentum'],loc='lower right')

plt.show()

print(adam_History)

pass;
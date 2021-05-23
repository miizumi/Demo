from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf

import pandas as pd



#資料準備---------------------------------------------------------------------------
data=pd.read_excel('weather.xlsx',0) #備註一下，可能需要openpyxl

#取特徵值的欄位，順便轉Numpy，會形成二維資料。
featrues_list=['MinTemp','MaxTemp','Sunshine','WindGustSpeed','WindSpeed9am','WindSpeed3pm',
               'Humidity9am','Humidity3pm','Pressure9am','Pressure3pm',
               'Cloud9am','Cloud3pm','Temp9am','Temp3pm']
featrues=data[featrues_list].to_numpy()

#標籤答案，讀取時順便轉numpy，還會轉成一維。
today_Label=data['TodayLabel'].to_numpy()
tomorrow_Label=data['TomorrowLabel'].to_numpy()

#特徵數與答案種類
category=2
dim= len(featrues_list)

#這裡示範預測隔天天氣。
x_train,x_test,y_train,y_test=train_test_split(featrues,tomorrow_Label,test_size=0.1)  #切割

#向量化
y_train2=tf.keras.utils.to_categorical(y_train,num_classes=category)
y_test2=tf.keras.utils.to_categorical(y_test,num_classes=category)
#建立模組----------------------------------------------------------------------------

model=tf.keras.models.Sequential([
    tf.keras.layers.Dense(units=50,activation=tf.nn.relu,input_dim=dim),
    tf.keras.layers.Dense(units=100,activation=tf.nn.relu),
    tf.keras.layers.Dense(units=category,activation=tf.nn.softmax)
])

#編譯-------------------------------------------------------------------------------
model.compile(optimizer='adam',
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=['accuracy'])

#訓練-------------------------------------------------------------------------------
epochs_Base=2000
batch_Base=20
model.fit(x_train,y_train2,epochs=epochs_Base,batch_size=batch_Base)

#測試-------------------------------------------------------------------------------
score=model.evaluate(x_test,y_test2,batch_size=batch_Base)
print("權重：",score)

#預測-------------------------------------------------------------------------------

predict=model.predict_classes(x_test)
print('測試資料預測')
print('實際答案：',y_test)
print('預測答案：',predict)

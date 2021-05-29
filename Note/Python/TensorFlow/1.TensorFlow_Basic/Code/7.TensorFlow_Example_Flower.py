from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf


#資料準備-----------------------------------------------------------
iris=datasets.load_iris()

dim=len(iris.feature_names) #取得特徵數
print('特徵數：',dim)   #特徵數： 4
category=len(iris.target_names) #取得答案種類
print('答案數：',category)  #答案數： 3

#資料切割
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.1)
#順手向量化
y_train2=tf.keras.utils.to_categorical(y_train,num_classes=category)
y_test2=tf.keras.utils.to_categorical(y_test,num_classes=category)

#建立模型-----------------------------------------------------------------

model=tf.keras.models.Sequential([
    tf.keras.layers.Dense(6,activation=tf.nn.relu,input_dim=dim),
    tf.keras.layers.Dense(9,activation=tf.nn.relu),
    tf.keras.layers.Dense(14,activation=tf.nn.relu),
    tf.keras.layers.Dense(category,activation=tf.nn.softmax)
])

#編譯--------------------------------------------------------------------

model.compile(optimizer='adam',
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=['accuracy'])

#訓練--------------------------------------------------------------------
model.fit(x_train,y_train2,epochs=100,batch_size=20)

#測試--------------------------------------------------------------------
score=model.evaluate(x_test,y_test2,batch_size=20)
print("權重：",score)

#權重： [0.11891574412584305, 1.0]
#權重： [0.1936449110507965, 1.0]
#權重： [0.06030178442597389, 1.0]

#預測--------------------------------------------------------------------
predict_class=model.predict_classes(x_test)
print('前十筆測試答案：',y_test[:10])           #前十筆測試答案： [1 2 2 1 2 0 0 1 1 2]
print('前十筆預測答案：',predict_class[:10])    #前十筆預測答案： [1 2 2 1 2 0 0 1 1 2]

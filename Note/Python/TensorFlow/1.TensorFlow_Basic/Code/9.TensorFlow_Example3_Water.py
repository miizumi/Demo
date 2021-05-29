import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


#準備資料----------------------------------------------------
dataframe=pd.read_csv('water_potability.csv')

##方法一 刪掉該筆
#dataframe=dataframe.dropna()    #刪除空值

##方法二 放特殊值-1
#dataframe=dataframe.fillna(-1)  #填滿空值為-1

##方法三 放平均值
dataframe=dataframe.fillna(dataframe.mean())  #填滿空值為平均值


#均一化
dataframe=((dataframe-dataframe.min())/(dataframe.max()-dataframe.min()))

#特徵值
features_List=['ph','Hardness','Solids','Chloramines',
             'Sulfate','Conductivity','Organic_carbon',
             'Trihalomethanes','Turbidity']
x=dataframe[features_List]

#答案
y=dataframe['Potability']

#要轉成numpy的陣列。
x=x.to_numpy()
y=y.to_numpy()

category= len(np.unique(y))
dim= len(features_List)

print(category)

#資料切割
X_Train,X_Test,Y_Train,Y_Test=train_test_split(x,y,test_size=0.1)

#向量化
Y_Train2=tf.keras.utils.to_categorical(Y_Train,num_classes=category)
Y_Test2=tf.keras.utils.to_categorical(Y_Test,num_classes=category)
#KNN-------------------------------------------------------------
knn=KNeighborsClassifier()
knn.fit(X_Train,Y_Train)

print('預測：',knn.predict(X_Test)[:10])
print('實際：',Y_Test[:10])
print('準確率： %.2f' % knn.score(X_Test,Y_Test))

#MLP--------------------------------------------------------------

#建立模型
model=tf.keras.models.Sequential([
    tf.keras.layers.Dense(units=dim*2,activation=tf.nn.relu,input_dim=dim),
    tf.keras.layers.Dense(units=dim*3,activation=tf.nn.relu),
    tf.keras.layers.Dense(units=dim*4,activation=tf.nn.relu),
    tf.keras.layers.Dense(units=category,activation=tf.nn.softmax),
])


#編譯
model.compile(optimizer='adam',
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=['accuracy'])

#訓練
model.fit(X_Train, Y_Train2,
          epochs=50,
          batch_size=20)


#測試
model.summary()
score = model.evaluate(X_Test, Y_Test2 )
print("score:",score)

predict2 = model.predict_classes(X_Test)
print("predict_classes:",predict2[:10])
print("y_test",Y_Test[:10])

import numpy as np
import tensorflow as tf
#產生資料集
def CreateDatasets(Category,Amount,Dimension):
    #測試特徵
    x_list = np.random.random((Amount, Dimension)) * Category    #建立好維度，乘上分類大小。

    #測試標籤
    y_list = ((x_list[:,0]+x_list[:,1])/2).astype(int)       #將兩個特徵值平均後，取整數(轉int取整)。

    #測試答案-向量化
    y_list2=tf.keras.utils.to_categorical(y_list, num_classes=(Category)) #記得最後一個建構子不要亂填。

    #回傳
    return x_list, y_list,y_list2

#資料設定
category=4  #答案的種類數，也會決定特徵的最大數值
dimension=2 #特徵數

#呼叫函式
x_train,y_train,y_train2=CreateDatasets(category,2000,dimension)


#-------------------------------------------------------------------

units_Base=3
#建立模型
model=tf.keras.models.Sequential([
    tf.keras.layers.Dense(units=10*units_Base,activation=tf.nn.relu,input_dim=dimension),
    tf.keras.layers.Dense(units=10*units_Base,activation=tf.nn.relu),
    tf.keras.layers.Dense(units=10*units_Base,activation=tf.nn.relu),
    tf.keras.layers.Dense(units=category,activation=tf.nn.relu),
])

#編譯
model.compile(optimizer='adam',
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=['accuracy'])

#訓練
epochs_Base=10
model.fit(x_train,y_train2,epochs=10*epochs_Base,batch_size=30)

#測試
x_test,y_test,y_test2=CreateDatasets(category,10,dimension) #產生測試用資料集
score= model.evaluate(x_test,y_test2,batch_size=50)
print('權重：',score)



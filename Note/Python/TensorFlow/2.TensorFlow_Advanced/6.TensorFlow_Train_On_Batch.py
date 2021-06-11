from sklearn.model_selection import train_test_split
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


#資料準備
num=50  #資料數量
X=np.linspace(-4,4,num) #產生-4~4的連續數字
np.random.shuffle(X)    #隨機打亂資料

Y = 0.1*np.sin(X)   #sin波形答案

x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.2) #切割

# 建立模型
model = tf.keras.models.Sequential([
   tf.keras.layers.Dense(units=100, activation=tf.nn.tanh, input_dim=1),
   tf.keras.layers.Dense(units=100, activation=tf.nn.tanh),
   tf.keras.layers.Dense(units=1),
])
#編譯
model.compile(loss='mse', optimizer='sgd', metrics=['acc'])


#基本用法
"""
for step in range(2000):
    cost = model.train_on_batch(x_train, y_train)  
    print("[loss,acc]",cost)    #顯示訓練結果
"""

#存檔
"""
for step in range(2000):
    cost = model.train_on_batch(x_train, y_train2,)
    if step % 20 == 0:  #20次訓練分段        
        #保存模型架構
        with open("model.json", "w") as json_file:
           json_file.write(model.to_json())
        #保存模型權重
        model.save_weights("model.h5")
"""


#畫圖觀察
for step in range(8001):    #進行8001次訓練
    cost = model.train_on_batch(x_train, y_train)  #指定變數，會得到[loss,acc]
    if step % 100 == 0: #每一百次更新圖表
        W, b = model.layers[0].get_weights()    #取得參數 權重、閾值

        print("step{} Weights = {}, bias = {} train cost{}".format(step,W, b, cost))

        plt.cla()           #清空plt
        plt.scatter(X, Y)   # 化新的散佈圖

        #預測
        Y_pred2 = model.predict(X)
        plt.scatter(X, Y_pred2,color="yellow") #當前預測散佈圖

        #在圖上寫字
        plt.text(0, -0.05, 'epoch:%d  ,loss=%.4f ' % (step,cost[0]),
                 fontdict={'size': 10, 'color': 'red'})

        plt.pause(0.1)


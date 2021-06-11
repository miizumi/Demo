import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split

#資料準備
X = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
Y = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
X_Train,X_Test,Y_Train,Y_Test=train_test_split(X,Y,test_size=0.1,random_state=42)   #資料切割

#建立模型
model=tf.keras.models.Sequential([
       tf.keras.layers.Dense(units=1,input_dim=1)
])
model.summary() #顯示模型資訊

#編譯
model.compile(loss='mse',optimizer='sgd',metrics=['accuracy']) #適合用回歸

#訓練
history = model.fit(X_Train,Y_Train,
                    epochs=3000,
                    batch_size=len(Y_Test))

#測試
cost = model.evaluate(X_Test,Y_Test)      #評估
print(cost)

weights , biases =model.layers[0].get_weights() #取得權重 (權重，閾值)
print('weights',weights)
print('biases',biases)

Y_Predict=model.predict(X_Test)

#畫圖
plt.scatter(X,Y)            #X,Y散佈圖
plt.scatter(X_Test,Y_Test)  #測試集散佈圖
plt.plot(X_Test,Y_Predict)  #預測線圖

x2 = np.linspace(0,1,100)   #產生0~1之間，連續100個數字。
y2 = (x2 * weights[0] + biases[0])
plt.plot(x2,y2,'-r',label='weights')
plt.legend()
plt.show()

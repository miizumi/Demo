import tensorflow as tf
import numpy as np


#亂數產生訓練資料
x1=np.random.random((500,1))  #產生五百筆 0~1的資料。
x2=np.random.random((500,1))+1  #同上，產生完後全部+1，所以會是1~2。
x_train=np.concatenate((x1, x2))  #資料串起來。

y1=np.zeros((500,), dtype=int)  #產生五百筆 0 的資料
y2=np.ones((500,), dtype=int)   #產生五百筆 1
y_train=np.concatenate((y1, y2))  #也是把資料串起來


#建立模型
model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(10, activation=tf.nn.relu, input_dim=1), #input_dim=特徵數
  tf.keras.layers.Dense(10, activation=tf.nn.relu),
  tf.keras.layers.Dense(2, activation=tf.nn.softmax)  #第一個參數2=答案類別數。
])
"""

# 用像list增加的方式，一個一個加上去。
model.add(tf.keras.layers.Dense(units=10,
                 activation=tf.nn.relu,    #tf.nn.relu
                 input_dim=1))
model.add(tf.keras.layers.Dense(units=10,
                 activation=tf.nn.relu ))  # tf.nn.relu
model.add(tf.keras.layers.Dense(units=2,
                 activation=tf.nn.softmax ))  #tf.nn.softmax


"""
#編譯
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#訓練
model.fit(x_train, y_train,
          epochs=10,
          batch_size=50)  #batch_size 如果不塞 他就是自動預設

#不用加上print，直接print過程。
model.summary()

#測試
x_test=np.array([[0.22],[0.31],[1.22],[1.33]])  #準備測試資料
y_test=np.array([0,0,1,1])

score = model.evaluate(x_test, y_test, batch_size=128)  #測試特徵、測試答案、單次評估數量。
print("score:",score)   #score: [0.26251232624053955, 1.0]

predict = model.predict(x_test)

print("predict:",predict)   #預測答案機率


predict_class=model.predict_classes(x_test)
print("prdict_classes：\r\n",predict_class)  #預測答案

#預測答案 np.argmax(predict[0])
print("Ans:",np.argmax(predict[0]),np.argmax(predict[1]),np.argmax(predict[2]),np.argmax(predict[3]))

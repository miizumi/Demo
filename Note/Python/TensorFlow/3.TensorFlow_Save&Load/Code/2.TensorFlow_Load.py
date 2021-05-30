import numpy as np
import pandas as pd
import tensorflow as tf

#讀取模型架構
#引用
from tensorflow.keras.models import model_from_json
with open('model.json','r') as f:
    model=model_from_json(f.read())


#儲存模型權重
model.load_weights("model.h5")

#編譯
opt=tf.keras.optimizers.Adam(lr=0.001)
model.compile(optimizer=opt,
              loss=tf.keras.losses.categorical_crossentropy,
              metrics=['accuracy'])



#預測

X_Test=[[5.9,3,5.1,1.8],[6.2,2.8,4.8,1.8]]
Y_Test=[2,2]


predict=model.predict_classes(X_Test)

print('實際結果',Y_Test)
print('預測結果',predict)
pass;
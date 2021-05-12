import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd
import numpy as np

#準備訓練與測試用的資料
x_values=pd.DataFrame([0,1,2]) #訓練用特徵
y_values=pd.DataFrame([0,0.3,0.6])  #訓練用答案
x_test=pd.DataFrame([-1,3,5])   #測試用特徵

#宣告線性迴歸模組
body_reg=linear_model.LinearRegression()

#對模組進行訓練
body_reg.fit(x_values,y_values)

#進行結果預測
y_test_predict=body_reg.predict(x_test)
print('預測結果：',y_test_predict)

#繪製圖表
plt.scatter(x_values,y_values)  #畫出訓練用資料
plt.scatter(x_test,y_test_predict,color='red') #畫出預測的資料

plt.plot(x_test.values,y_test_predict,'b-')    #畫出預測線，迴歸分析線

plt.show()
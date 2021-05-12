#引用
from sklearn import tree
import numpy as np

#資料準備------------------------------------------------------

#樣本
X=np.array([[180, 85],[174, 80],[170, 75],  #樣本-男
            [167, 45],[158, 52],[155, 44]]) #樣本-女
#答案
Y=np.array(['man','man','man','woman','woman','woman'])

#使用演算法----------------------------------------------------
#宣告
decision_Tree=tree.DecisionTreeClassifier()

#訓練
decision_Tree.fit(X,Y)

#預測
predict=decision_Tree.predict([[173,76]])
print(predict)

#繪成圖表，更容易理解-------------------------------------------
import matplotlib.pyplot as plt

#男生
plt.plot(X[:3,0],X[:3,1],'yx') #(前三筆身高，前三筆體重)

#女生
plt.plot(X[3:,0],X[3:,1],'g.')

#畫出一個要預測的點
plt.plot([173],[76],'r^')

#其他設定
plt.ylabel('Weight')
plt.xlabel('Height')
plt.legend(('man','woman'),loc='upper left')
plt.show()

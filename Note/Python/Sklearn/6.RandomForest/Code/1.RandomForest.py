from sklearn.ensemble import RandomForestClassifier
import numpy as np

#樣本
X=np.array([[180, 85],[174, 80],[170, 75],  #樣本-男
            [167, 45],[158, 52],[155, 44]]) #樣本-女
#答案
Y=np.array(['man','man','man','woman','woman','woman'])

#宣告
randomForest=RandomForestClassifier(n_estimators=100,max_depth=10,random_state=2)   #一百棵樹，10層深度

#訓練
randomForest.fit(X,Y)

#預測
print(randomForest.predict([[180,85]]))
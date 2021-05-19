from sklearn.naive_bayes import GaussianNB
import numpy as np

#資料-----------------------------------

X=np.array([[9,9],[9.2,9.2],[9.6,9.2],[9.2,9.2],[6.7,7.1],[7,7.4],[7.6,7.5],    #柳丁
            [7.2,10.3], [7.3,10.5], [7.2,9.2], [7.3,10.2], [7.2,9.7], [7.3,10.1],[7.3,10.1]])   #檸檬

Y=np.array([1,1,1,1,1,1,1,
            2,2,2,2,2,2,2]) # 訓練答案

#--------------------------------------

#宣告
bayes=GaussianNB()

#訓練
bayes.fit(X,Y)

#每個分類的概率
print('每個分類的概率',bayes.class_prior_) #[0.5 0.5]

#取估算工具的參數
print('估算工具的參數',bayes.get_params())

#預測
X_test=np.array([[8,8],[8.3,8.3]])
bayes_Predict=bayes.predict(X_test)
print(bayes_Predict)    #[1 1]，兩個都是1(柳丁)

#各分類機率
print(bayes.predict_proba(X_test))



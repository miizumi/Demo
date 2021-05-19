import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn import metrics

from sklearn.model_selection import train_test_split

#讀資料---------------------------------------------
star_df=pd.read_excel("Stars.xls",0)

star_df["ColorNo"]=star_df.Color.astype("category").cat.codes   # 資料轉成數字
star_df["Spectral_ClassNo"]=star_df.Spectral_Class.astype("category").cat.codes   # 資料轉成數字

XList=["Temperature","L","R","A_M","ColorNo","Spectral_ClassNo","Spectral_Number"]
YList=["Type"]


#Split-------------------------------------------

X=star_df[XList].to_numpy()
Y=star_df["Type"].to_numpy()
X_train ,X_test ,Y_train ,Y_test = train_test_split(X,Y,test_size=0.1)

print("Regression-------------------------------------------")

from sklearn import linear_model
#宣告
star_Reg=linear_model.LinearRegression()

#訓練
star_Reg.fit(X_train,Y_train)

#預測
Y_test_Predict=star_Reg.predict(X_test)

print("coef 係數：",star_Reg.coef_)
print("singular 單數：",star_Reg.singular_)
print('正確答案：',Y_test)
print('預測答案：',Y_test_Predict)


print("KNN-----------------------------------------------")

from sklearn.neighbors import KNeighborsClassifier

star_Knn=KNeighborsClassifier()
star_Knn.fit(X_train,Y_train)
Knn_Predict=star_Knn.predict(X_test)

print('正確答案：',Y_test)
print('預測答案：',Knn_Predict)
print("準確率： %.2f" % metrics.accuracy_score(Y_test,Knn_Predict))


print("K-means------------------------------------------")
from sklearn.cluster import KMeans

star_Kmeans=KMeans(n_clusters=6)
star_Kmeans.fit(X_train)
star_Predict=star_Kmeans.predict(X_test)

print('正確答案：',Y_test)
print('預測答案：',Knn_Predict)
print("準確率： %.2f" % metrics.accuracy_score(Y_test,star_Predict))


print("決策樹-------------------------------------------")
from sklearn import tree
decisionTree=tree.DecisionTreeClassifier()
decisionTree.fit(X_train,Y_train)
decisionTree_Predict=decisionTree.predict(X_test)
#輸出樹狀圖
tree.export_graphviz(decisionTree,out_file='tree.dot')

print('正確答案：',Y_test)
print('預測答案：',Knn_Predict)
print("準確率： %.2f" % metrics.accuracy_score(Y_test,star_Predict))


print("隨機森林-------------------------------------------")
from sklearn.ensemble import RandomForestClassifier
rForest=RandomForestClassifier()
rForest.fit(X_train,Y_train)
rForest_Predict=rForest.predict(X_test)

#輸出樹狀圖
from sklearn.tree import export_graphviz

estimator=rForest.estimators_[0]    #取得第0棵樹
export_graphviz(estimator,out_file='rForest.dot')   #輸出成dot

print('正確答案：',Y_test)
print('預測答案：',rForest_Predict)
print("準確率： %.2f" % metrics.accuracy_score(Y_test,rForest_Predict))


print("貝氏分類-------------------------------------------")
from sklearn.naive_bayes import GaussianNB
bayes=GaussianNB()
bayes.fit(X_train,Y_train)
bayes_Predict=bayes.predict(X_test)


print('正確答案：',Y_test)
print('預測答案：',rForest_Predict)
print("準確率： %.2f" % metrics.accuracy_score(Y_test,rForest_Predict))

print("Lasso-------------------------------------------")
#用來算數值的
from sklearn import linear_model

lasso=linear_model.Lasso(alpha=0.1)
lasso.fit(X_train,Y_train)
lasso_Predict=lasso.predict(X_test)

print('正確答案：',Y_test)
print('預測答案：',lasso_Predict)


print("SGD---------------------------------------------")
#分類
from sklearn.linear_model import SGDClassifier
sgd=SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
sgd.fit(X_train,Y_train)
sgd_Predict=sgd.predict(X_test)

print('正確答案：',Y_test)
print('預測答案：',lasso_Predict)
print("準確率： %.2f" % metrics.accuracy_score(Y_test,lasso_Predict))

print("高斯---------------------------------------------")
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct,WhiteKernel

kernel=DotProduct()+WhiteKernel()

gaussian=GaussianProcessRegressor(kernel=kernel,random_state=0)

gaussian.fit(X_train,Y_train)
gaussian_Predict=gaussian.predict(X_test)

print('正確答案：',Y_test)
print('預測答案：',gaussian_Predict)

print("svm.SVR-----------------------------------------")
from sklearn import svm
svr=svm.SVR()
svr.fit(X_train,Y_train)
svr_Predict=svr.predict(X_test)


print('正確答案：',Y_test)
print('預測答案：',svr_Predict)

print("svm.SVC-----------------------------------------")
svc=svm.SVC()
svc.fit(X_train,Y_train)
svc_Predict=svc.predict(X_test)


print('正確答案：',Y_test)
print('預測答案：',svc_Predict)

"""
#Seaborn------------------------------------------
import seaborn as sns

star_Seaborn=star_df[["Temperature","L","R","A_M","ColorNo","Spectral_ClassNo","Spectral_Number","Type"]]
sns.set_theme(style="whitegrid")
sns.pairplot(star_Seaborn,hue="Type")

plt.show()
"""
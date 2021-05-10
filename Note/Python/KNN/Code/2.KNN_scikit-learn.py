#匯入KNN函式庫
from sklearn.neighbors import KNeighborsClassifier

#---------------------------------------------

featrues=[[9, 9.0], [9.2, 9.2], [9.6, 9.2], [9.2, 9.2], [6.7, 7.1], [7, 7.4], [7.6, 7.5],   #這裡是橘子的特徵值
          [7.2, 10.3], [7.3, 10.5], [7.2, 9.2], [7.3, 10.2], [7.2, 9.7], [7.3, 10.1], [7.3, 10.1]]  #這裡是雷夢

label=[1,1,1,1,1,1,1,   #橘子
       2,2,2,2,2,2,2]   #雷夢

#宣告演算法主體
neigh=KNeighborsClassifier(n_neighbors=3)   #K=3

#訓練
neigh.fit(featrues,label)

#預測
predict=neigh.predict([[7,9]])
print(predict)  #[2]

#預測時的概率估計
proda=neigh.predict_proba([[7,9]])
print(proda)    #[[0. 1.]]


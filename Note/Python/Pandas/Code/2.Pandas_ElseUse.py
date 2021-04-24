import pandas as pd

df=pd.read_csv('交通事故代號對照表.csv')

#二維大小，輸出為(列,行)
print(df.shape)

#DataFrame的詳細資訊，注意這是個方法所以要加括號，沒加會輸出表單內容。
print(df.info())

#各數值的描述統計。
print(df.describe())

#計算數量
print(df.count())

#最小值
print(df.min())

#最大值
print(df.max())

#最小值的位置
print(df.idxmin())

#最大值的位置
print(df.idxmax())

#10%分位數
print(df.quantile(0.1))

#數值加總
print(df.sum())

#均值
print(df.mean())

#中位數
print(df.median())

#眾數
print(df.mode())

#方差
print(df.var())

#標準差
print(df.std())

#平均絕對偏差
print(df.std())

#偏度
print(df.skew())

#峰度
print(df.kurt())
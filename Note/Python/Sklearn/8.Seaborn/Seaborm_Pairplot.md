# 散佈圖矩陣

引用
```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```

資料讀取
```python
#資料讀取
dataframe = pd.read_excel ('weather.xlsx',0)
#比較欄位
df=dataframe[['Sunshine','WindSpeed9am','Humidity9am','Pressure9am','Cloud9am','Temp9am','TodayLabel']]
```

```python
#繪製圖形
sns.pairplot(df, hue="TodayLabel")  #hue=標籤答案欄位
plt.show()  #顯示圖形

```
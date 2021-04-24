# 其他方法、屬性
_參照code：2.Pandas_ElseUsed.py_

_此範例與說明未完善，日後補上_

### 二維大小，輸出為(列,行)
```python
print(df.shape)
```
### DataFrame的詳細資訊
注意這是個方法所以要加括號，沒加會輸出表單內容。
```python
print(df.info())
```

### 各數值的描述統計
```python
print(df.describe())
```

### 計算數量
```python
print(df.count())
```

### 最小值
```python
print(df.min())
```

### 最大值
```python
print(df.max())
```

### 最小值的位置
```python
print(df.idxmin())
```

### 最大值的位置
```python
print(df.idxmax())
```

### 10%分位數
```python
print(df.quantile(0.1))
```

### 數值加總
```python
print(df.sum())
```

### 均值
```python
print(df.mean())
```

### 中位數
```python
print(df.median())
```

### 眾數
```python
print(df.mode())
```

### 方差
```python
print(df.var())
```

### 標準差
```python
print(df.std())
```

### 平均絕對偏差
```python
print(df.std())
```

### 偏度
```python
print(df.skew())
```

### 峰度
```python
print(df.kurt())
```
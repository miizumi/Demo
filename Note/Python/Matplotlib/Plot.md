# Plot 基本線圖
引用函式庫
```python
import matplotlib.pyplot as plt
```
畫線語法(x軸,Y軸,線條樣式,標籤)
```python
plt.plot(labels,list_male,'b.-',label='Men')
#x軸可以不用宣告，會自動從1開始填入。
plt.plot(list_female,'r.-',label='Women')

#線條樣式元素 例:'b.-',藍色線條附圓點
#基本色：r=red,b=blue,g=green,y=yellow,k=black
#線條樣式：(-)線條,(.)圓點,(*)星號點,,,,
```
如果字太擠可以自訂X,Y軸刻度
```python
plt.xticks(['93','95','97','99','101','103','105','107'])   #x軸刻度
plt.yticks([45,50,55,60,65,70,75])  #y軸刻度
```

在畫布上出現網格，方便辨識。
```python
plt.grid()
```

賦予表抬頭
```python
plt.title('這是抬頭')
```

線條說明
```python
plt.legend()
```
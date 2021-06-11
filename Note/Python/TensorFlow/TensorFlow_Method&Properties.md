# TensorFlow 方法

<br/>
<br/>

## 評估模型

用於評估訓練後的模型，會返回一個List，損失值&指標值 (loss,metric)。

```python
#取值(list)
cost = model.evaluate(X_Test,Y_Test)
#不取值
model.evaluate(X_Test,Y_Test)
```

<br/>
<br/>

## 取得權重(參數)

返回參數 (權重，閾值)，一定要指定第幾層，否則出錯。

```python
#取值，需用兩個變數裝。
weights , biases =model.layers.get_weights()
```

<br/>
<br/>

# TensorFlow 屬性

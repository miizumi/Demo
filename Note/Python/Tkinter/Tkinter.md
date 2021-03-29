# Tkinter

<br/><br/><br/>

# 視窗呼叫
```python
import tkinter as tk

#宣告視窗物件
win=tk.TK() 

#給予視窗名稱 (非必要)
win.wm.title('title_Name')

#設定視窗最大、最小
win.minsize(weight=100,height=100) #最小
win.maxsize(weight=999,height=999) #最大

#是否讓使用者更改大小(視窗拉伸，未設定預設為True)
win.resize(width=True,Height=False)

#呼叫出視窗
win.mainloop()
```

<br/><br/><br/>

# Label 標籤

## 可以套用的元素
  |元素|語法|補充說明|
  |----|----|---|
  |文字|text="文字"|
  |背景顏色|bg='red' |顏色的部分可以使用#RRGGBB|
  |文字顏色|fg='white'|
  _如有星號為較難理解且未實作_

```python
    #宣告標籤物件，win=視窗物件。所有物件第一個參數必定為父視窗。
    label1=tk.Label(win,text="標籤顯示文字")
    #套用其他元素    
    labeㄠ2=tk.Label(win,text="套用元素",bg='blue',fg='green')
```
<br/><br/><br/>

# 顯示元件
<br/>

## 可以套用的元素

  |元素|語法|補充說明|
  |----|----|---|
  |位置對齊|anchor="nw"|以東西南北縮寫'n,s,w,e,center'混和共可達9個方向，預設為置中(center)|
  |*是否填充父元件的額外空間|expand=True'|預設False|
  |*指定填充 pack 分配的空間|fill='none'|預設值為none，表示保持原始尺寸。還可以使用的值有："x"（水平填充），"y"（垂直填充）和 "both"（水平和垂直填充）
  |*將該元件放到該選項指定的元件中|in_=|指定的元件必須是該元件的父元件|
  |X軸內間距|ipadx=10||
  |Y軸內間距|ipadx=10||
  |X軸外間距|padx=10||
  |Y軸外間距|padx=10||
  |指定元件放置位置|side='top'|預設值為'top',能賦予'left','bottom','right'

<br/>

## 顯示元件有三個函式能使用
+ ### Pack()
  不指定位置，以新增順序排序元件。
  <br/>不算好用，不是很推薦。
  <br/>_能套用的元素_：anchor, expand, fill, in_, ipadx(...), side  
  
```python
    #直接操作
    label1.pack()   

    #移除顯示
    label1.pack_forget() #

    #
    label1.place(x=100,y=50) #指定座標位置。
    lablel1.grid()  #按照行/列形式排序元件。
    #註：不要在同一個父元件底下混合使用grid跟pack。
```
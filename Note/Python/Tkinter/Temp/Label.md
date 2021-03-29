# Label 標籤
```python
    #宣告標籤物件，win=視窗物件。
    label1=tk.Label(win,text="標籤顯示文字")
```

# 顯示元件
    label1.pack()   #不指定位置，以新增順序排列元件
    label1.place(x=100,y=50) #指定座標位置。
    lablel1.grid()  #按照行/列形式排序元件。
    #註：不要在同一個父元件底下混合使用grid跟pack。
```
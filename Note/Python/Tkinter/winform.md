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
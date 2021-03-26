# Function   函式、函數
善用函式能減少重複撰寫、易於維護
當有程式碼以相同方式執行多次時可以將其包裝成函式。

```python
    #宣告
    def fun_name():
        print('執行區')
    
    #叫用
    fun_name()
```

 可以使用參數與回傳值
```python
    def f_name(num,multiple=10):    #參數可以加上預設值。
        a=num*10
        return a    #可以有回傳值

    x=f_name(100)   # x=1000 #有預設值的參數可以不用給予
    y=f_name(10,30) # y=300  #也可以給唷
```

 Python可以有多回傳值
```python
    def f_name(value):
        a=value*10
        b=value*20
        return a,b
    x,y=f_name(10) #也要用兩個變數接
```

# Global & Local 全域變數&區域變數
 如果想在函式裡使用全域變數，需要加上global關鍵字。
 </br>範例一 使用全域變數

```python
    def f_name():
        global x    #指定函式內的x皆為全域變數的x
        x=4         #這裡的x會操作全域變數
    
    x=2
    f_name()
    print(x) #x:4
```

範例二 未使用全域關鍵字
```python
    def f_name():
        x=4      #未使用全域關鍵字，所以是宣告全新的區域變數
        print(x) #x:4

    x=2
    f_name()
    print(x)    #x:2    
```

通常不用使用global關鍵字，看起來不專業且外行!
<br/>以下為好的範例

```python
    def fun(x):
        x=x+1
        return(x)

    x=3
    x=fun(x)    #將變數帶入，接取新的值回來
    print(x)    #x:4
```

---
<br/>

# 引用函式庫
引用函式庫要把函式庫放進相同路徑，或是路徑下的資料夾。
<br/>切記函式庫PY檔名稱不要以數字開頭。

```python
    #引用語法
    import Myfunction       #相同路徑下的函式庫引用。
    import Function1 as F1  #可以給引用的函式庫暱稱，方便使用。
    from sub import Function2 #相同路徑下資料夾引用方式。

    #叫用函式庫
    Myfunction.fun()
    F1.fun()
```


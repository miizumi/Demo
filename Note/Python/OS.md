# OS 函式庫
os函式庫主要提供跟目錄/檔案有關的函式。
```python
    import os 
```

讀取目錄下的所有檔名。
```python
    List=os.listdir()   #不給參數會預設為PY檔目錄下。

    dirPath=r"C:\Users"     #如有許多逸出字元，可以前方加上r，等同C#(@)。
    List=os.listdir(dirPath)    #可以指定目錄。
```

找尋指定副檔名

第一種方式，雖然看起來比較笨。
```python
index=len(fileName)-1       #必須從LIST最後往前進行檢查
while index>=0:
    if(fileName[index][-3:]!='csv'):
        del fileName[index]     #如果從頭檢查，可能會出現錯位，導致刪除資料不正確。亦或是使用remove()，也能達到效果。
    index=index-1               #倒序刪除不會影響未檢查的值。
```

第二種，因為檔名是可以允許存在( . )，所以寫起來比較麻煩，看起來費效能。
```python
index=len(fileName)-1
while index>=0:
    if(fileName[index].split('.')[-1]!='csv'):
        del fileName[index]
    index=index-1
```
# CSV 檔案讀取
CSV格式跟DataTable概念很相似，可以用EXCEL開啟。
<br/>CSV是一種純文字的類型，工控領域很常使用。常見以逗號(,)分隔，(\n)換行。
<br/>閱讀CSV檔建議使用LibreOffice

### 指定開啟檔案
```python
    fw=open('fileName.csv','w') #'w'為寫入，'r'是讀取。
    #用完記得關閉資料流
    fw.close()

    #另一種的using寫法
    with open ('fileName.csv','r') as fr:
        #這裡面擺執行式
        #此方式好處是最後不用關閉，縮排離開即關。
        #缺點是使用都要在縮排內。
```

### 讀取方式
```python
    #讀取一行  
    fr.readline()
    
    #一行一行讀取至結束
    for row in fr:
        #取得的資料會是一個字串，例row:'"時間","姓名","上下班"\n'
        rowList=row.split(",")  #以逗號分隔取成List
        print(rowlist[0])       # rowlist[0]:"時間"
        print(rowlist[1])       # rowlist[1]:"姓名"
        print(rowlist[2])       # rowlist[2]:"上下班"\n 

        #每行的最後一排都會有\n，並不會被刪除，而且每個資料都會有雙引號(")。
        #這不是能好好取用的資料，必須手動做整理！

        #正確整理
        print(rowlist[0].replace('"','')))       # 時間
        print(rowlist[1].replace('"','')))       # 姓名
        #最後一行必須替換兩次
        x=rowlist[2].replace('"',''))
        x=x.replace('\n',''))
        print(x)       # 上下班        

        #備註
        #如果資料為數字組成的字串(ex:'123')，也可以直接轉型成int，會使引號(')消失。
        x='123'     # x:'123'
        x=int(x)    # x:123


```

### 寫入 (這不常使用，先看過就好)
```py    
    fr.write('"時間","姓名","上下班"\n')    #就這樣，很簡單，沒了。
```

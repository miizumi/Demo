# LIST 清單

將LIST轉型成String，可以使所有內容連接起來。
```python
    list=[a,b,c,d,e]
    newList=str(list)[1,-1] #把頭尾去掉，才不會出現中括號[]
    print(newList)  #print：abcde
```


---

## SORT 排序

### 字串前方有數字1~10以上
因為如果有1~10以上字串排序，會形成尷尬的排列結果。<br/>
例如：<br/>
+  排列前=[1,2,3,4,5,6,7,8,9,10]
+  排列後=[1,10,2,3,4,5,6,7,8,9]

<br/>可以使用split切成LIST，再將切出的數字做排序。

借用黏巴達的方式排序。(不需要引用)
```python
    #數字在開頭
    #a:
    list.sort(key = lambda x:int(x.split(a)[0]))

    #如果數字夾在字源中間
    list.sort(key = lambda x:int(x.split(a)[0].split(b)[1]))
    #b:數字的前一個字元
    #a:數字的後一個字元    
```
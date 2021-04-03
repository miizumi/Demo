# Dictionary 字典
基本架構為一個KEY(鍵)對應一個VALUE(值)。<br/>
KEY具有唯一性，不得有重複(Primary Key)。

## 宣告方式
主要架構以大括號包裝，KEY:VALUE，給予鍵值，以逗號區別(,)。
```python
dic={'a':1,'b':2,'c':3} #宣告三個鍵值
```
新增建值
```python
dic['d']=4  #定義不存在的鍵，即可新增。
```
使用方法
```python
#一般叫用
print(dic['a']) #叫用方式類似於List，只是輸入的是Key

#也可以套用For...in
for x in dic:   #這裡的x會等於Key，等同於Foreach每個Key。
    print(dic[x])    #print：1 2 3 4
    
```

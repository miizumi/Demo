# List 陣列
python的陣列主要分三種
1. 一維
2. 二維
3. 多維
<br/>***馬的廢話***

### 基本認知
 + 矩陣內不要混和不同的資料型態，不好看且容易有問題。
 + list2=list1 
      <br/>會將list2導向list1的記憶體位置，若list2有更動，會影響list1。
      <br/>正確方式：list2=list1.copy


---
## 基本應用
```python
animals=['Dog','Cat','Frog']    #基本的一維陣列

print(animals[0])            #叫用方式 # print:Dog

print(animals[-1])            #會取得最後的值 #print：Frog

num=animals.index['Cat']     #尋找值的位置，以最先遇到為主 # num=1

length=len(animals)          #取陣列長度。# length=3

del animals[0]               #可以刪除指定位置的值,刪除第一項好用



room=[['1F-1','1F-2','1F-3'],#二維陣列寫法，多維依此列推。
      ['2F-1','2F-2','2F-3'],
      ['3F-1','3F-2','3F-3']]

print(room[1][2])            #多維的叫用方式，如果有更多就繼續接下去 # print:2F-2
```

將LIST轉型成String，可以使所有內容連接起來。
```python
list = ['a', 'b', 'c', 'd', 'e']
newList=str(list)[1:-1] #把頭尾去掉，才不會出現中括號[]
print(newList)  #print：abcde
```

## 資料切割
```python
list=[1,2,3,4,5,6,7,8,9]
#LIST[x:y] 以x開頭,y的前一值結束。
list=list[2:5] #x可不填,預設從頭開始、y同理，不填則取至結束。
print(list)     #print：[3, 4, 5]
```

## 較為特別的應用方式
```python
list=[3,1]

list=list*2 #重複兩次，串接起來

print(list) #[3, 1, 3, 1]

list=list+[3,4,5] #直接與陣列串接

print(list) #[3, 1, 3, 1, 3, 4, 5]

print( 1 in list) #檢查是否含值，回傳值為bool

#可以在list裡寫出條件式(判別、迴圈)

#想要將全部的值做變動
list=[1,2,3,4]
list=[x*2 for x in list]    #將list裡的值全部乘2
print(list) #[2, 4, 6, 8]

#還可以套上if
list=[1,2,3,4]
list=[x for x in list if x>=3]  #把不符合條件的值拋棄，只取要的值。
print(list) #[3, 4]

```

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

## 題外話
早期電腦效能較差，有些寫法會影響效能。
```python
while x<len(array) #每當迴圈進入條件時，都會執行一次取長度。

y=len(array)       #此方式效率較佳
while x<y          
```
---
# Range 範圍
Range函式會產生一維的整數陣列
```python
# list=range(start,stop,step) 開頭,結束,數列差
a=range(5)        #a=[0,1,2,3,4]
                  #只給予Stop參數，預設會從0開始每個差為+1 

b=range(2,6)      #b=[2,3,4,5]
                  #只給開頭到結束，預設差為+1        
                  #注意，Stop會在達到參數之前停止!

c=range(6,0,-2)   #c=[6,4,2]
                  #也可以使其負成長

#指定參數的宣告方式
d=range(start=0,stop=6,step=2)      #d=[0,2,4]

print(list(a)) #產生的陣列跟LIST一樣，但變數指標不同，若要以LIST顯示仍要轉型。
```


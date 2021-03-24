# List 陣列
python的陣列主要分三種
1. 一維
2. 二維
3. 多維
<br/>***馬的廢話***
```python
animals=['Dog','Cat','Frog']    #基本的一維陣列

print(animals[0])            #叫用方式 # print:Dog

num=animals.index['Cat']     #尋找值的位置，以最先遇到為主 # num=1

length=len(animals)          #取陣列長度。# length=3

del animals[0]               #可以刪除指定位置的值,刪除第一項好用



room=[['1F-1','1F-2','1F-3'],#二維陣列寫法，多維依此列推。
      ['2F-1','2F-2','2F-3'],
      ['3F-1','3F-2','3F-3']]

print(room[1][2])            #多維的叫用方式，如果有更多就繼續接下去 # print:2F-2
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
import numpy as np

#Numpy的陣列宣告方式(一維陣列)
list_a=np.array([1,2,3])

#顯示list_a的資料型態
print(type(list_a)) #<class 'numpy.ndarray'>

#顯示陣列維度
print(list_a.shape) #(3,)

#呼叫數值
print(list_a[0],list_a[1],list_a[2])    #1 2 3

#更改數值
list_a[0]=5

print(list_a)   #[5 2 3]


##二維陣列

#宣告
list_b=np.array([[1,2,3],[4,5,6]])
print(list_b)   #[[1 2 3]
                # [4 5 6]]

#顯示維度
print(list_b.shape) #(2, 3)

#呼叫數值
print(list_b[0,0],list_b[1,0],list_b[0,1])  #1 4 2
#也可以用原先的LIST呼叫方式
print(list_b[0][1])


##題外話
#可以透過轉型將原先的LIST轉成Numpy的資料型態
list_a=[1,2,3]
print(type(np.array(list_a)))

list_c=np.array([[[1,2,3],[4,5,6],[1,2,3]],[[1,2,3],[4,5,6],[1,2,3]]])
print(list_c.shape)

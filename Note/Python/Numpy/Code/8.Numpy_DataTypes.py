import numpy as np

#一般宣告
list_a=np.array([1, 2])
print(list_a.dtype) #int32

list_b=np.array([1.0,2.0])  #有小數點就會變成浮點數。
print(list_b.dtype) #float64

#指定資料型態
list_c=np.array([1,2],dtype=np.int64)
print(list_c.dtype) #int64
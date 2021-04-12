import numpy as np

#一維陣列的資料對應。
list1=np.array([5,4,3,2,1]) #被索引的陣列
list2=[0,2,4]   #存放索引值的陣列，此陣列可以為一般的list資料型態。
list3=list1[list2]
print(list3) #[5 3 1]

# #索引出來的資料型態是Numpy的Array
print(type(list3))  #<class 'numpy.ndarray'>

#如果不想開宣告索引陣列，可以使用這個寫法。
list3=list1[[0,1,3]]    #索引值內的陣列必須再加上一層中括號[]。
print(list3)    #[5 4 2]


#以二維陣列當索引值。
list1=np.array([0,1,2,3,4,5,6,7,8,9]) #被索引的陣列
list2=np.array([[0,3],[5,6]])   #以二維陣列當索引時，資料型別必須為Numpy的Array。
list3=list1[list2]
print(list3)

print('------------')

#如果想寫一起的話，只能以這樣的寫法，較不美觀。
list3=list1[np.array([[0,3],[5,6]])]
print(list3)

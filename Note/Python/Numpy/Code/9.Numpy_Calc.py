import numpy as np

#定義兩個二維陣列
list_a=np.array([[1,2],[3,4]],dtype=np.float64) #指定為雙精度浮點數
list_b=np.array([[5,6],[7,8]],dtype=np.float64)

##np.add(x,y) 加法
print('加法')
#簡單粗暴，也適用於其他四則運算。
print(list_a+list_b)    #[[ 6.  8.]
                        # [10. 12.]]

#使用函式
print(np.add(list_a,list_b))    #[[ 6.  8.]
                                # [10. 12.]]

#不一定要陣列相加，可以使某一陣列內的資料加上一個指定的值。
print(list_a+10)    #[[11. 12.]
                    # [13. 14.]]

##np.subtract(x,y) 減法
print('減法')
#一樣可以簡單粗暴。
print(list_a-list_b)    #[[-4. -4.]
                        # [-4. -4.]]

#使用函式
print(np.subtract(list_a,list_b))   #[[-4. -4.]
                                    # [-4. -4.]]

#如果減數是一維陣列，則會將二維陣列的每個陣列都做減法，一樣可以套用其他四則運算。
print(list_a-[1,2]) #[[0. 0.]
                    # [2. 2.]]

##np.multiply(x,y)  乘法
print('乘法')

print(np.multiply(list_a,list_b))   #[[ 5. 12.]
                                    # [21. 32.]]

##np.divide(x,y) 除法
print("除法")

print(np.divide(list_a,list_b)) #[[0.2        0.33333333]
                                # [0.42857143 0.5       ]]

##np.square(x) 平方
print('平方')
#平方取法為x**2
print(np.square(list_a))    #[[ 1.  4.]
                            # [ 9. 16.]]


##np.sqrt(x) 平方根
print('平方根')

#平方根取法為x//2
print(np.sqrt(list_a))  #[[1.         1.41421356]
                        # [1.73205081 2.        ]]

##矩陣乘法，有兩種寫法。
print('矩陣乘法')
#1.x.dot(y)
print(list_a.dot(list_b))   #[[19. 22.]
                            # [43. 50.]]

#2.np.dot(x,y)
print(np.dot(list_a,list_b))    #[[19. 22.]
                                # [43. 50.]]
import matplotlib.pyplot as plt

#資料
x_List=[1,2,3,4]    #油價
y_List=[0,0.3,0.6,0.9]  #增加人數比例

#畫點
plt.plot(x_List,y_List,'gx')
#畫線
plt.plot(x_List,y_List,'r--')

#圖表顯示範圍
plt.axis([0,5,0,1])

plt.show()
import matplotlib.pyplot as plt
import  numpy as np

#---------------------------------------------

#柳丁數據
orange_X=[9,9.2,9.6,9.2,6.7,7,7.6]
orange_Y=[9.0,9.2,9.2,9.2,7.1,7.4,7.5]
plt.plot(orange_X,orange_Y,'yx')    #畫線

#檸檬數據
lemon_X=[7.2,7.3,7.2,7.3,7.2,7.3,7.3]
lemon_Y=[10.3,10.5,9.2,10.2,9.7,10.1,10.1]
plt.plot(lemon_X,lemon_Y,'g.')  #畫線

#繪製未知數據
plt.plot([7],[9],'r^')

#繪製未知數據的範圍
circle=plt.Circle((7,9),1.2,color='#eeeeee')
plt.gcf().gca().add_artist(circle)

#設定圖表大小
plt.axis([6,11,6,11])

#圖表其他設定
plt.ylabel('H cm')
plt.xlabel('W cm')
plt.legend(('Orange','Lemons'),loc='upper right')

plt.show()
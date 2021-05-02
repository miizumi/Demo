import matplotlib.pyplot as plt

#--------------------------------------------------------------


#柳丁
orange_Width=[9,9.2,9.6,7.5,6.7,7]
orange_Length=[9.4,9.2,9.2,9.2,7.1,7.4]

plt.plot(orange_Width,orange_Length,'yx')

#檸檬
lemon_Width=[7.2,7.3,7.2,7.3,7.2,7.3,7.3]
lemon_Length=[10.,10.5,9.2,10.2,9.7,10.1,10.1]

plt.plot(lemon_Width,lemon_Length,'gx')

#繪製
plt.plot([6.5,9.0],[7.8,12.5],'k--')

#圖表相關
plt.ylabel('Length(cm)')
plt.xlabel('Width(cm)')
plt.legend(('Orange','Lemon'),loc='upper right')
plt.show()

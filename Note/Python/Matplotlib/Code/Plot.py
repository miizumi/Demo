import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
plt.rcParams['font.sans-serif'] = ['SimSun']
plt.rcParams['axes.unicode_minus'] = False

labels=[1,2,3,4,5,6,7]

line1=[5,3,9,4,2,4,5,]
line2=[4,1,2,1,4,7,9,]

plt.plot(labels,line1,'b.-',label='線1')
plt.plot(labels,line2,'r.-',label='線2')
plt.grid()  #網格
plt.title('This is Title')
plt.legend()
plt.show()
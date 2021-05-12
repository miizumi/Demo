import matplotlib.pyplot as plt
import numpy as np

#產生1~3.9，30個float的陣列。
x=np.arange(30)/10+1

#產生30個-0.1~0.1之間的亂數
delta=np.random.uniform(low=-0.1,high=0.1,size=(30,))

#產生30個點，y為list。
y=0.3*x-0.3+delta

#以藍點表示隨機生成的點
plt.plot(x,y,'bo')

#線性回歸
plt.plot(x,0.3*x-0.3,'k--')

#計算殘差
sum=0.0
i=0
for x1 in x :
    y1=0.3*x1-0.3           #線上的位置
    y2=0.3*x1-0.3+delta[i]  #實際的位置

    plt.plot((x1,x1), (y1,y2), 'r-')#繪製距離

    sum=sum+abs(y1-y2)  #abs=絕對值
    i=i+1
print('殘差=',sum/30)

plt.show()
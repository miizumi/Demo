import pandas as pd


data = {'名字':['王曉明','周星星','吳猛達'],
       '外號':['小明','阿星',None]}
df = pd.DataFrame(data,columns=['名字','外號'])

replace_dict={'小明':'阿明',"阿星":"小星",None:'阿達'}   #替換答案用的Dictionary

#替換至新欄位
df['外號']=df['外號'].map(replace_dict)
#套用函式
df['打招呼']=df['外號'].map('你好，我的外號叫做{}'.format)
import pandas as pd

#讀取資料

#讀取excel(檔案路徑要加副檔名,sheet)
dataFrame=pd.read_excel('交通事故代號對照表.xls','sheet')
#CSV

#dataFrame=pd.read_csv('交通事故代號對照表.csv')
#所有欄位名稱
print(dataFrame.columns)

#第3位置上的欄位名稱。
print(dataFrame.columns[3])

print('----------------------------------')

#顯示前3列的資料，不給參數預設是5。
print(dataFrame.head(3))
#顯示前5列的資料
print(dataFrame[:5])

print('----------------------------------')


##取某欄位的資料

#取一個欄位，輸出會有兩排資料，首排為index。
#輸出欄位名稱'光線'的資料
print('取一個欄位的資料')
print(dataFrame.光線)
print(dataFrame['光線'])


##找出指定位置資料的方法
print('取資料')
#在dataFrame的'事故位置'欄位找位置 2 的資料
print(dataFrame['事故位置'][2])
#找位置5
print(dataFrame['事故位置'][5])
#範圍資料切割，輸出2,3,4位置的資料。
print(dataFrame["事故位置"][2:5])
#value 會單純取值，並輸出成list，也就是不會出現index。
print(dataFrame['事故位置'].values)

print('----------------------------------')

#取兩個欄位，要用兩層中括號包裝。
print('取兩個欄位的資料。')
t2=dataFrame[['路面鋪裝','路面狀態']]
print(t2)


#兩個以上欄位要取範圍比較麻煩
#t2[4] 這樣是沒辦法的，這是錯誤的方式！
print('方法一')
print(t2[4:5])  #必須指定範圍，即使只取一列。
print('方法二')
print(t2.loc[4])    #使用函式，但排版會有點奇怪。

print('----------------------------------')
#顯示DataFrame中row的資訊(start,stop,step)，回傳值可以當Range使用。
a=dataFrame.index
print(a)
for x in a:
    print(x)

print('----------------------------------')

from pandas import ExcelWriter

#建立檔案的時候，要用一個變數包裝後續才有辦法使用。
writer = ExcelWriter('test.xlsx', engine='xlsxwriter')#建立檔案(新檔案名稱,借用引擎)
dataFrame.to_excel(writer, sheet_name='sheet2')#只會對記憶體進行操作。
writer.save()#這裡才會真正寫入到檔案。
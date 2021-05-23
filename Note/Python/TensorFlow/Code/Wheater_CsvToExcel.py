import pandas as pd
from pandas import ExcelWriter

csv_Dataframe=pd.read_csv('weather.csv')    #讀取CSV

csv_Dataframe.dropna(axis=0, how='any', inplace=True)   #刪除有空值的列

replace_dict={'Yes':'1',"No":"0"}   #替換答案用的Dictionary

#替換至新欄位
csv_Dataframe['TodayLabel']=csv_Dataframe['RainToday'].map(replace_dict)
csv_Dataframe['TomorrowLabel']=csv_Dataframe['RainTomorrow'].map(replace_dict)

#存成xls
writer = ExcelWriter('weather.xlsx', engine='xlsxwriter')   #塞檔案用的變數
csv_Dataframe.to_excel(writer, sheet_name='weather',index=False) #寫入變數，index刪掉，他很煩。
writer.save()   #存檔

print('Save OK')
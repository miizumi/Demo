# coding=gbk
import requests
import xlwt
import json


#台灣證交所-各類指數日成交量值
url = 'https://www.twse.com.tw/exchangeReport/BFIAMU?response=json&date=&_=1618685303771'

#模擬瀏覽器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
#請求資料
req = requests.get(url, headers=headers)


#讀取JSON格式檔
try:
    json_Data=json.loads(req.text)
    print('\033[1;42;30m資料讀取成功')
except:
    print('\033[1;41;30m 資料讀取失敗!')
    print('\033[0;31m   請檢查檔案是否為Json格式')

try:
    print('\033[0m   資料寫入中...')
    #取得標題作為檔案名稱
    xml_Name=json_Data['title']


    #宣告excel檔
    xml_Wb=xlwt.Workbook()
    #建立新表
    sheet=xml_Wb.add_sheet(xml_Name)

    #寫入位置的欄列索引
    col_index=0
    row_index=0

    # 欄位名稱寫入第一行
    for col in json_Data['fields']:
        sheet.write(row_index,col_index,col)
        col_index=col_index+1   #每一格寫完都要跳下一格索引

    # 寫完記得索引至下一行
    row_index=row_index+1

    #開始寫入資料
    for row in json_Data['data']:

        col_index=0 #每一行寫完索引歸0

        for value in row:
            sheet.write(row_index,col_index,value)
            col_index=col_index+1

        row_index = row_index + 1

    #該資料最後有一個NOTE區塊，雖然看不懂，但也加上去較為完整。
    row_index=row_index+2   #區隔兩行，排版較好看
    for note in json_Data['notes']:
        sheet.write(row_index,0,note)
        row_index = row_index + 1

    #檔案名稱加上副檔名
    xml_Name = xml_Name + ".xls"

    #Excel存檔
    xml_Wb.save(xml_Name)
    print('   存檔完成')
    print('   檔案名稱：' + xml_Name)
except:
    print('\033[1;41;30m 資料寫入失敗!')
    print('\033[0;31m   請檢查資料')



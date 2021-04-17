# coding=gbk
import requests
import xlwt
import json


#̨���C����-���ָ���ճɽ���ֵ
url = 'https://www.twse.com.tw/exchangeReport/BFIAMU?response=json&date=&_=1618685303771'

#ģ�M�g�[��
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
#Ո���Y��
req = requests.get(url, headers=headers)


#�xȡJSON��ʽ�n
try:
    json_Data=json.loads(req.text)
    print('\033[1;42;30m�Y���xȡ�ɹ�')
except:
    print('\033[1;41;30m �Y���xȡʧ��!')
    print('\033[0;31m   Ո�z��n���Ƿ��Json��ʽ')

try:
    print('\033[0m   �Y�ό�����...')
    #ȡ�Ø��}����n�����Q
    xml_Name=json_Data['title']


    #����excel�n
    xml_Wb=xlwt.Workbook()
    #�����±�
    sheet=xml_Wb.add_sheet(xml_Name)

    #����λ�õę�������
    col_index=0
    row_index=0

    # ��λ���Q�����һ��
    for col in json_Data['fields']:
        sheet.write(row_index,col_index,col)
        col_index=col_index+1   #ÿһ���궼Ҫ����һ������

    # ����ӛ����������һ��
    row_index=row_index+1

    #�_ʼ�����Y��
    for row in json_Data['data']:

        col_index=0 #ÿһ�Ќ��������w0

        for value in row:
            sheet.write(row_index,col_index,value)
            col_index=col_index+1

        row_index = row_index + 1

    #ԓ�Y��������һ��NOTE�^�K���mȻ����������Ҳ����ȥ�^��������
    row_index=row_index+2   #�^����У��Ű��^�ÿ�
    for note in json_Data['notes']:
        sheet.write(row_index,0,note)
        row_index = row_index + 1

    #�n�����Q���ϸ��n��
    xml_Name = xml_Name + ".xls"

    #Excel��n
    xml_Wb.save(xml_Name)
    print('   ��n���')
    print('   �n�����Q��' + xml_Name)
except:
    print('\033[1;41;30m �Y�ό���ʧ��!')
    print('\033[0;31m   Ո�z���Y��')



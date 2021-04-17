# Excel寫入
PIP 安裝
> pip install xlwt

引用
```python
import xlwt
```

宣告，並不會直接建立檔案。
```python
book = xlwt.Workbook()
```

建立表單(sheet)
```python
#name = 表單名稱
sheet = book.add_sheet('name')
```

寫入資料
```python
#sheet.write(row,col,value)
sheet.write(0,1,'資料') #在第0行，第一欄，寫入 "資料" 。
```

存檔，通常在資料都寫完畢後再作執行。
```python
#檔案名稱順手加上副檔名
book.save('Excel_Name.xls')
```



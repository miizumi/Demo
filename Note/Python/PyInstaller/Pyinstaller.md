# Pyinstaller
Pyinstaller函式庫可以把Py檔打包成exe檔，在不同的作業系統上使用，就會打包成該作業系統的執行檔。

Pyinstaller會將需要的PIP連同打包，給予使用者檔案時不需要另外安裝PIP的函式庫以及Python主程式。

安裝函式庫
> pip install pyinstaller

使用起來非常簡單。

1. 先開啟指令視窗(cmd、Terminal)

2. 移動到程式碼路徑

3. 執行指令
> pyinstaller 檔案名稱.py

使用成功會在該路徑下發現一個dist資料夾，裡面就是包裝好的程式碼，如果有其他相關的檔案(如:excel,csv,jpg)記得順手丟進去。
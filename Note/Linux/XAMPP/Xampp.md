# Xampp 安裝方式

一樣必須去官網下載到XAMPP的安裝檔。

有兩種方式，一是先在其他地方下載完成再使用Filezila上傳，二是先找好下載的網址然後在Linux上使用wget指令。

取得檔案後，可以使用兩個指令。

第一個是設定使用權限，775簡單說就是所有人可讀可寫可執行。

> chmod 755 xampp-linux-x64-7.1.27-1-installer.run

第二個是執行檔案。

>sudo ./xampp-linux-x64-7.1.27-1-installer.run

如果安裝過程被Killed掉，可以試試看重新開機。

# 執行XAMPP

啟動

>sudo /opt/lampp/lampp start

停止

>sudo /opt/lampp/lampp stop

查看狀態

>sudo /opt/lampp/lampp status



# 錯誤問題

ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)

可能是沒有安裝mysql伺服器端。

> sudo apt-get install mysql-server
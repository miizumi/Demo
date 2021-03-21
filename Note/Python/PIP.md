# 何謂PIP
全名   Python Package
<br/>PIP是Pyhon的套件管理程式，可以用來安裝和管理第三方函式庫。
<br/>python的擴充套件副檔名為.egg
<br/>egg就是一個zip檔。

在新的Python版本中，已經都包含了PIP安裝工具，Windows可以透過CMD安裝。
<br/>*如果是在面試之類的場合遇到面試官問：請問你怎麼安裝PIP，請回答：我都使用CMD安裝PIP。*

PIP存放位置
+ python//Lib
+ Python//Lib//site-packages

## PyPi 
https://pypi.org/
<br/>第三方函式庫的官方網站，內有詳細說明

<br/><br/>

# pip指令   
_以下皆為老師課本內的範例_

## 安裝套件
安裝套件預設會安裝最新版本的套件
```c#
pip install numpy //pip install "套件名稱"
```
也可以指定版本
```c#
pip install virtualenv==1.6.3 //pip install "套件名稱==版本""
```
 也可以指定一個範圍的版本
```
pip install virtualenv>=1.6.3 
pip install virtualenv<1.6.3 
```
 也可以指定一個網路連結來安裝
```
pip install install http://example.com/virtualenv-1.6.4.zip

```

## 移除套件
相較於easy_install，pip支援較多自動化清理的工作，後續不用人工清理殘留檔案
```C#
pip uninstall numpy //pip uninstall ‘套件名稱’ 
```

## 更新套件版本
```C#
    pip install -U "numpy" //pip install -U "套件名稱"
```
## 升級PIP
    python -m pip install --upgrade pip
    或者
    pip install --upgrade pip

## 列出已安裝PIP
    pip list

## 搜尋套件
    pip search numpy

## 列出範例
    pip help

<br/><br/>

# 推薦安裝的pip
pip install Pillow # 顯示圖片
<br/>pip install Pillow-PIL # 顯示圖片
<br/>pip install PyInster # 把.py 包成.exe
<br/>pip install XlsxWriter # Excel 函式庫
<br/>pip install beautifulsoup4 # 爬蟲等函式庫
<br/>pip install MySQL-python # 資料庫 Python 2.x
<br/>pip install pymysql # 資料庫 Python
<br/>pip install TensorFlow # TensorFlow 類神經
<br/>pip install h5py # TensorFlow 類神經的權重函式庫
<br/>pip install jeiba # 中文語意處理
<br/>pip install lxml # XML 處理
<br/>pip install matplotlib # 畫圖表函式庫
<br/>pip install opencv-python # OpenCV 函式庫
<br/>pip install opencv-contrib-python # OpenCV 函式庫
<br/>pip install pandas # 表單資料函式庫
<br/>pip install pandas-datareader # 表單資料函式庫
<br/>pip install requests # 網路函式庫
<br/>pip install scipy # 機器學習函式庫
<br/>pip install xlrd # XML 處理函式庫
<br/>pip install xlwt # XML 處理函式庫
import requests
#美人湯的引用方法較為不一樣
from bs4 import BeautifulSoup

#取得網頁回應
req=requests.get('https://www.gamer.com.tw/index2.php')

#宣告美人湯主體
#取得的回應內容(req.text)依照情況轉編碼。
soup=BeautifulSoup(req.text.encode('utf-8'),'html.parser')


#取得網頁標題
print('取得網頁標題')
print(soup.title)   #<title>巴哈姆特電玩資訊站 -- 系統忙碌中</title>

#取得標題內的文字
print('文字')
print(soup.title.string)    #巴哈姆特電玩資訊站 -- 系統忙碌中


#取得目前節點的父類，即上一層的意思。
print('取得目前節點的父類')
print(soup.title.parent)    #<head>....省略....</head>

#取得標籤名稱
print('取得標籤名稱')
print(soup.title.parent.name)   #head

#取得HTML中第一個p的內容
print('取得HTML中第一個p的內容')
print(soup.p)   #<p data-translate="turn_on_cookies" style="color:#bd2426;">....省略....</p>


#取得HTML中第一個a的內容
print('取得HTML中第一個a標籤')
print(soup.a)   #<a href="mailto:webmaster@gamer.com.tw">webmaster@gamer.com.tw</a>


# get('x')
print('取得該標籤內的x屬性')
print(soup.p.get('data-translate'))   #turn_on_cookies

# p['x']
print('取得標籤內x屬性的值，x為標籤的屬性名稱。使用與GET一樣')
print(soup.p['style'])          #color:#bd2426;

# a['x']
print('其他標籤也能這樣使用')
print(soup.a['href'])   #mailto:webmaster@gamer.com.tw


#取得HTML中所有的a
print('取得所有的a標籤')
print(soup.find_all('a'))   #回傳值為list。

#找所有x標籤，輸出為list，跟find_all有異曲同工之妙。
print('取得所有的p標籤')
print(soup.select('p')) #回傳list

## contents
print('取得目前節點中，依照HTML標籤所切割的內容，回傳為list')
print(soup.a.contents)  #['webmaster@gamer.com.tw']
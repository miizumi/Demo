import requests
from bs4 import BeautifulSoup

#目標
url = 'https://www.ptt.cc/bbs/hotboards.html'

#模擬瀏覽器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
req = requests.get(url, headers=headers)

#美人湯

soup=BeautifulSoup(req.text.encode('utf-8'),'html.parser')

#取得網頁標題
print(soup.title.string)

#取得每個文章的標題
for row in soup.select('.board-title'):
    print(row.string)
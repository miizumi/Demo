from bs4 import BeautifulSoup
exam_Html="""
<head>
    <title>爬蟲練習</title>
</head>
<body>
    <p class="title"><b>The test</b></p>
    <a class="redcolor" href="https://www.ptt.cc/index.html" id="link1">PTT介紹首頁</a>
    <a class="bluecolor" href="https://www.youtube.com/" id="link2">Youtube</a>
    <a class="redcolor"  href="https://www.gamer.com.tw/index2.php" id="link3">巴哈姆特電玩資訊站</a>
    <div id="data1">
        品牌
    	<ul class="data2">
        	<li> Sony </li>
        	<li> MicroSoft </li>            
        </ul>
    </div>
    <div>
        電玩主機
        <h1 class="data3"> PlayStation</h1>
    	<ul class="data4">
        	<li> PS5 </li>
        	<li> PS4 </li>
        </ul>
    </div>
</body>
"""
soup=BeautifulSoup(exam_Html,'html.parser')

#第一題:
print('顯示 [PlayStation]')
print(soup.select('.data3')[0].string)


#第二題:
print('顯示 [PS5]  和  [PS4]')
print(soup.select('.data4')[0].text)

# print(soup.select('.data4')[0].contents)

#第三題:
print('顯示 [Sony]和 [MicroSoft]  和 [PS5]  和  [PS4]')
print('方法一')    #分開顯示
for x in soup.select('li'):
    print(x.text)

#如果以LIST直接顯示，會出現LI標籤。
print(soup.select('li'))    #[<li> Sony </li>, <li> MicroSoft </li>, <li> PS5 </li>, <li> PS4 </li>]

#可以用這種寫法，一行搞定，輸出為list。
print([x.text for x in soup.select('li')])  #[' Sony ', ' MicroSoft ', ' PS5 ', ' PS4 ']


#第4題:
print('顯示 [品牌]')
print(soup.select('#data1')[0].contents[0].string)

#第5題:
print('顯示 [電玩主機]')
print(soup.select('div')[1].contents[0].string)

#第6題:
print('顯示 [data2]')
a = soup.select('#data1')[0]
print(a.contents[1].get("class"))



#第7題:
#顯示 [data3]
a = soup.select('div')[1].contents[1].get('class')
print(a)
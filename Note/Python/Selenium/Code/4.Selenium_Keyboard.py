from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#啟動模擬器
driver=webdriver.Chrome('chromedriver.exe',chrome_options=webdriver.ChromeOptions())

#目標為Google搜尋引擎
driver.get('https://www.google.com/')

#輸入框的name='q'，故以此搜尋。
search_Bar=driver.find_element_by_name('q')

##模擬鍵盤輸入
#清空輸入框
search_Bar.clear()
#對該元素做輸入字串的動作
search_Bar.send_keys('Python')
#Keys可以做出鍵盤上的多種輸入操作
#以逗號分隔可以做多次操作
search_Bar.send_keys(' selenium',Keys.ARROW_LEFT)
#模擬方向鍵左
search_Bar.send_keys(Keys.ARROW_LEFT)
#按下Enter
search_Bar.send_keys(Keys.RETURN)


"""
資料來源:

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

#取用chrome的設定值
option = webdriver.ChromeOptions()

#宣告模擬器主體，這裡會直接開啟模擬器
driver = webdriver.Chrome('chromedriver.exe',chrome_options=option)

#模擬器指向網址
driver.get('http://www.python.org')

#assert 確認條件，條件成立程式才會繼續走，否則出錯。
assert "Python" in driver.title #檢查網站Title是否含有"Python"

#assert 相似於if
#與這行效果相同
# if driver.title.find("Python")>0:

#查找第一個name=q的元素     #其他查找元素可以上參考網站查詢。
elem = driver.find_element_by_name("q")
#清空textbox
elem.clear()

#輸入"pycon"
elem.send_keys("pycon")

#按下Enter
elem.send_keys(Keys.RETURN)


#意指有搜尋出東西
assert "No results found." not in driver.page_source

#顯示搜尋出的東西
print(driver.page_source)
#停滯五秒
time.sleep(5)
#關閉模擬器
driver.close()

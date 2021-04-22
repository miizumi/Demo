from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import os

#宣告模擬器主體，這裡會直接開啟模擬器
driver = webdriver.Chrome()

#如果指向本地檔案，可以用絕對位置，相對位置會出錯。
driver.get('file:///'+os.path.abspath('./3.Selenium_FindMethod2.html'))

#搜尋超連結標籤
#針對超連結的文字搜尋
continue_link1=driver.find_element_by_link_text('Continue')
print(continue_link1.text)
#搜尋部分含有文字的超連結。
continue_link2=driver.find_element_by_partial_link_text('Conti')
print(continue_link2.text)

#搜尋對應名稱的標籤
tag_Name=driver.find_element_by_tag_name('h1')
print(tag_Name.text)

#針對Class名稱搜尋
class_Name=driver.find_element_by_class_name('content')
print(class_Name.text)

#針對Css選擇器搜尋
css_Selector=driver.find_element_by_css_selector('p.content')
print(css_Selector.text)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time
import os

#宣告模擬器主體，這裡會直接開啟模擬器
driver = webdriver.Chrome()

#如果指向本地檔案，可以用絕對位置，相對位置會出錯。
driver.get('file:///'+os.path.abspath('./Selenium_FindMethod.html'))

#查找ID=loginForm
login_Form=driver.find_element_by_id('loginForm')
#查找Name=username
userName=driver.find_element_by_name('username')
userName.send_keys('admin')
#查找Name=password
passWord=driver.find_element_by_name('password')
passWord.send_keys('password')
#因為會指定找到的第一個元素，所以這段會找到'Login'而不會找到'Clear'按鈕。
login_Btn=driver.find_element_by_name('continue')
login_Btn.click()

#Xpath示範
print('Xpath示範-form')
#1.絕對位置
form_1=driver.find_element_by_xpath('/html/body/form[1]')
print(form_1)
#2.指定頁面中的第一個Form
form_2=driver.find_element_by_xpath('//form[1]')
print(form_2)
#3.ID=loginForm的form元素
form_3=driver.find_element_by_xpath("//form[@id='loginForm']")
print(form_3)
#尋找第一個含有input元素且name=username的form元素，
form_4=driver.find_element_by_xpath("//form[input/@name='username']")
print(form_4)

print('Xpath示範-username')

#id=loginForm的元素中第一個input子元素。
userName_1=driver.find_element_by_xpath("//form[@id='loginForm']/input[1]")
print(userName_1)
#指定節點之中，第一個name='username'的input元素。
userName_2=driver.find_element_by_xpath("//input[@name='username']")
print(userName_2)

print('Xpath示範-Clear')
#尋找name='continue'、type='button'的input元素。
clear_Btn1=driver.find_element_by_xpath("//input[@name='continue'][@type='button']")
print(clear_Btn1)
#尋找id='loginForm'的form元素，再往下尋找第四個input。
clear_Btn2=driver.find_element_by_xpath("//form[@id='loginForm']/input[4]")
print(clear_Btn2)



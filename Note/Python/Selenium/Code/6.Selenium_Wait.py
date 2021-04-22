from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#引用
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#啟動模擬器
driver=webdriver.Chrome('chromedriver.exe',chrome_options=webdriver.ChromeOptions())
driver.get('https://www.google.com')

##顯性等待
#先設定等待時間(模擬器,時間(秒))
wait=WebDriverWait(driver,10)
#尋找等待目標
ec=EC.presence_of_element_located((By.NAME,'q'))

#這個寫法也是可以的
#EC.element_to_be_clickable((By.NAME,'q'))

#執行等待
element=wait.until(ec)
print('already')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#啟動模擬器
driver=webdriver.Chrome('chromedriver.exe',chrome_options=webdriver.ChromeOptions())
driver.get('https://www.fooish.com/html/select-option-optgroup-tag.html')

"""
<select name="pets">
<option value="">請選擇你最愛的寵物</option><option value="dog">Dog</option><option value="cat" selected="selected">Cat</option><option value="hamster">Hamster</option><option value="parrot">Parrot</option><option value="spider" disabled="disabled">Spider</option><option value="goldfish">Goldfish</option></select>
"""

#每段程式執行都做一點延遲，比較像人工處理。
time.sleep(2)

#尋找下拉式選單
pets_ComboBox=driver.find_element_by_name('pets')

#要取得下拉式選單內的所有元素，所以要用elements。
pets_option=pets_ComboBox.find_elements_by_tag_name('option')
#跑一圈所有的值
for row in pets_option:
    print('選項：',row.text)   #順便顯示出所有的值

    if(row.text=='Cat'):    #比較出自己想要的選項
        row.click() #點擊

time.sleep(2)
#-------------------------------------------------

#使用函式庫更加方便快速且準確。
from selenium.webdriver.support.ui import Select

#宣告主體。
cars_Select=Select(driver.find_element_by_name('cars'))

#確認此選單是否可以多選。
print('多選：',cars_Select.is_multiple)


#Select提供了三種選擇的方法
#方法一，根據排序。
cars_Select.select_by_index(0)  #選第一個
time.sleep(1)

#方法二，根據顯示文字。
cars_Select.select_by_visible_text('BMW')   #選擇BMW
time.sleep(1)

#方法三，根據元素內的Value。
cars_Select.select_by_value('saab')   #選擇value='Saab'
time.sleep(1)

## 顯示已被選取的選項
for value in cars_Select.all_selected_options:
    print(value.text)

##取消選項的方式。
#方法一，根據排序。
cars_Select.deselect_by_index(0)  #取消第一個
time.sleep(1)
#方法二，根據顯示文字。
cars_Select.deselect_by_visible_text('BMW') #取消BMW
time.sleep(1)
#方法三，根據元素內的Value。
cars_Select.deselect_by_value('saab')   #取消value='Saab'
time.sleep(1)
#取消所有選項
cars_Select.deselect_all()
time.sleep(1)
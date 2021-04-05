# Arduino 簡介
## 特色
+ OPEN SOURCE
  + 不僅程式碼開源，硬體也是開放的。可以免費下載開發用IDE、電路設計圖。
+ 簡單好用資源多
  + 網路上很多作品可供參考使用。
+ 物美價廉
  + 就便宜阿
  
<br/>

# 開發環境

## Sketch
官方提供的免費IDE，程式語法類似於C/C++，跨平台。

![Sketch](./ArduinoIMG/Sketch.png)

<br/>

每支Arduino程式都會用到Setup()、loop() 兩個函式，為求方便可以直接抓範例 BarMinimun。

![Sketch-2](./ArduinoIMG/Sketch-2.png)

<br/>

# 環境測試
可以利用範例中的Blink進行測試

「上傳」按鈕可以先將程式碼驗證再寫入板子。
(我買的便宜大陸版偶爾會出錯，多試幾次總會成功一次...)
![upload](./ArduinoIMG/Sketch-3.png)

如果出現下圖情況，可以先去裝置管理員找設定接口，如沒有可能是驅動未安裝。

![error](./ArduinoIMG/Sketch-4.png)

官方IDE內已經含有驅動程式，可以指定位置安裝。
![driver](./ArduinoIMG/Sketch-5.png)

如果是非官方版本Arduino，可能會出現USB2.0-Ser!

![errorDriver](./ArduinoIMG/Sketch-6.png)

這時候只需要去GOOGLE找CH340晶片驅動安裝程式即可。

![CH340](./ArduinoIMG/Sketch-7.png)


# 參考引用網站

傑森創工
<br/>https://blog.jmaker.com.tw/
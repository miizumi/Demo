# Bluetooth
相較於WiFi來說，藍芽連接傳遞資料更為簡單，程式碼也是如此。

ESP32本身自帶藍芽功能，不用接線、設定ATCommand、宣告通訊協定，省去很多繁雜的步驟，且使用的是低功率藍芽，其耗電量較少，傳輸距離理論值為300公尺，實際使用30公尺是沒問題的。

本身自帶的藍芽無法使用於IOS系統

ESP32

+ 藍芽 v4.2 完整標準，包含傳統藍芽 (BR/EDR) 和低功耗藍芽 (BLE)
+ 支持標準 Class-1、Class-2 和 Class-3，且無需外部功率放大器
+ 增強型功率控制 (Enhanced Power Control)
+ 輸出功率高達 +12 dBm
+ NZIF 接收器具有–97 dBm 的 BLE 接收靈敏度
+ 自適應跳頻 (AFH)
+ 基於 SDIO/SPI/UART 接口的標準 HCI
+ 高速 UART HCI，最高可達 4 Mbps
+ 支持藍芽 4.2 BR/EDR 和 BLE 雙模 controller
+ 同步面向連接/擴展同步面向連接 (SCO/eSCO)
+ CVSD 和 SBC 音頻編解碼算法
+ 藍芽微微網 (Piconet) 和散射網(Scatternet)
+ 支持傳統藍芽和低功耗藍芽的多設備連接
+ 支持同時廣播和掃描
+ 傳送接收（SPP）

<br/>
<br/>
<br/>

# 簡單單向傳輸

使用ESP32傳遞資料給其他藍芽裝置，
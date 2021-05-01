import serial  # 引用pySerial模組

com_Port = 'COM5'    # 指定通訊埠名稱
baud_Rates = 9600    # 設定傳輸速率

# 初始化序列通訊埠(指定通訊埠名稱，鮑率)
ser = serial.Serial(com_Port, baud_Rates)

try:
    #以無限迴圈方式不停收資料。
    while True:
        while ser.in_waiting:          # 若收到資料
            data = ser.readline()  # 讀取一行
            print('接收到的原始資料：', data)    #這裡輸出會是Byte編碼
            print('解碼後的資料：', data.decode()) # 用預設的UTF-8解碼

except KeyboardInterrupt:
    ser.close()    # 跟資料庫一樣用完要關閉的概念。
    print('序列阜關閉')
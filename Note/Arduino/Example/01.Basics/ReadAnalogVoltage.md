# ReadAnalogVoltage 讀取類比電壓

## CODE

```ino
void setup() {
  //要讀取甚麼資訊，就記得要建立序列傳輸。
  Serial.begin(9600);
}

void loop() {
  // 這裡讀取數值存入變數。
  int sensorValue = analogRead(A0);
  
  // 類比訊號收到的值範圍是0~1023，是由0~5V變化。
  // 故這裡做轉換的計算 值*比率(5/1023)
  float voltage = sensorValue * (5.0 / 1023.0);
  // 顯示數值。
  Serial.println(voltage);
}
```
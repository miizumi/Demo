# Blink
以下簡單解析這個範例的用處
<br/>程式碼：
```arduino
void setup() {
    //pin腳模式(指定PIN位置,模式)
  pinMode(LED_BUILTIN, OUTPUT);
    //此處意指，把LED_BUILTIN設定為輸出模式，把電向外送才能控制LED燈點亮或息滅。

}
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   //信號輸出(腳位，電位) HIGH(高電位)在UNO版上代表5V電
  delay(3000) //程式停駐不動(毫秒);                       
  digitalWrite(LED_BUILTIN, LOW);    //LOW(低電位)，代表不給腳位供電
  delay(1000);                       
}
```

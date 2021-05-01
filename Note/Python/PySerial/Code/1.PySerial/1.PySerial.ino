//引用
#include "DHT.h"
//設定
#define DHTPIN 9
#define DHTTYPE DHT11
//宣告主體
DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(9600);
  dht.begin();  //初始化DHT
  
}

void loop()
{
  delay(1000);
  float h = dht.readHumidity();   //取得濕度
  float t = dht.readTemperature();  //取得溫度C

  //顯示在監控視窗裡
  Serial.println(String(h)+","+String(t));
}

void setup() {
  //設定腳位
  pinMode(7,OUTPUT);
}

void loop() {
  //高電位，通電。
  digitalWrite(7,HIGH);
  delay(2000);

  //低店位，斷電。
  digitalWrite(7,LOW);
  delay(1000);
}

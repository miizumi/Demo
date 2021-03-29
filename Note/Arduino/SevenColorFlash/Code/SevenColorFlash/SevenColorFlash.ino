//設定腳位
const int PIN = 13;
void setup() {
  //設定腳位模式
  pinMode(PIN,OUTPUT);

}

void loop() {
  //給予高電位，使其亮燈。
  digitalWrite(PIN,HIGH);
  delay (10000); 

  //熄燈
  digitalWrite (PIN, LOW); 
  delay (2000); 

}

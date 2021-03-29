const int color1_PIN = 9;
const int color2_PIN = 10;

void setup() {
  // put your setup code here, to run once:
  pinMode(color1_PIN,OUTPUT);
  pinMode(color2_PIN,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  //熄燈
  digitalWrite(color1_PIN,LOW);
  digitalWrite(color2_PIN,LOW);
  delay(2000);

  //顏色1亮  紅色
  digitalWrite(color1_PIN,HIGH);
  digitalWrite(color2_PIN,LOW);
  delay(2000);
  
  //顏色2亮  綠色
  digitalWrite(color1_PIN,LOW);
  digitalWrite(color2_PIN,HIGH);
  delay(2000);


  //顏色1+2混合 黃色
  digitalWrite(color1_PIN,HIGH);
  digitalWrite(color2_PIN,HIGH);
  delay(2000);

}

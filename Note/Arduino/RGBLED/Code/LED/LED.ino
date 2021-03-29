//把針腳位置放入變數，以名稱代替方便記憶使用。
const int Red=9;
const int Green=10;
const int Blue=11;

void setup() {
  //設定腳位模式
  pinMode(Red,OUTPUT);
  pinMode(Green,OUTPUT);
  pinMode(Blue,OUTPUT);

}

void loop() {
  
  //基本三色變換
  analogWrite(Red,255);
  analogWrite(Green,0);
  analogWrite(Blue,0);
  delay(1000);
  
  analogWrite(Red,0);
  analogWrite(Green,255);
  analogWrite(Blue,0);
  delay(1000);
  
  analogWrite(Red,0);
  analogWrite(Green,0);
  analogWrite(Blue,255);  
  delay(1000);
  

  /*
  //基本三色變換，偷懶寫法。
  analogWrite(Red,255);
  analogWrite(Blue,0);
  delay(1000);
  
  analogWrite(Red,0);
  analogWrite(Green,255);
  delay(1000);
  
  analogWrite(Green,0);
  analogWrite(Blue,255);  
  delay(1000);
  */

  
}

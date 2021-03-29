//把針腳位置放入變數，以名稱代替方便記憶使用。
const int Red=9;
const int Green=10;
const int Blue=11;

//將變數設置在外，才不會影響每次迴圈
int r,g,b=0;

#define speed 20

void setup() {
  //設定腳位模式
  pinMode(Red,OUTPUT);
  pinMode(Green,OUTPUT);
  pinMode(Blue,OUTPUT);

}

void loop() {
  //循序變色

  //1.先升紅色    無>紅  (6.再次升紅色=>紫)
  for(;r<255;r++)
  {
    analogWrite(Red,r);
    delay(speed);
    }

  //7.藍色降低    紫>紅
  for(;b>0;b--)
  {
    analogWrite(Blue,b);
    delay(speed);
    }  

  //2.綠色升高    紅>黃
  for(;g<255;g++)
  {
    analogWrite(Green,g);
    delay(speed);
    }

  //3.紅色降低    黃>綠
  for(;r>0;r--)
  {
    analogWrite(Red,r);
    delay(speed);
    }

  //4.藍色升高    綠>青
  for(;b<255;b++)
  {
    analogWrite(Blue,b);
    delay(speed);
    }

  //5.綠色降低    青>藍
  for(;g>0;g--)
  {
    analogWrite(Green,g);
    delay(speed);
    }
  //6.接下來要升紅色 於是返回迴圈開頭

  
}

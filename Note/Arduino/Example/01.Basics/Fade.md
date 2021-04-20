# Fade 用類比訊號輸出做呼吸燈LED
Fade 退色，可表達淡入淡出的意思。

## 官方文件：

This example demonstrates the use of the analogWrite() function in fading an LED off and on. AnalogWrite uses pulse width modulation (PWM), turning a digital pin on and off very quickly with different ratio between on and off, to create a fading effect.

## 單字解釋：
+ demonstrates 展示
  

## 本人的不負責翻譯： 

此範例展示如何使用 analogWrite() 函式 製作出呼吸燈LED，AnalogWrite使用PWM(模擬類比運號)功能讓LED快速的更換頻率達到呼吸燈的效果。


## 範例接版：

![Circuit](./../IMG/fade_Circuit.png)

## 圖解：

![Schematic](./../IMG/fade_Schematic.png)

## CODE

```ino
int led = 9;           // 設定LED腳位
int brightness = 0;    // 存放目前亮度
int fadeAmount = 5;    // 每次更改亮度的浮動值


void setup() {
  //設定腳位為輸出
  pinMode(led, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // 對腳位進行亮度改變
  analogWrite(led, brightness);

  //每完成一個迴圈，做一次亮度更改
  brightness = brightness + fadeAmount;

  // 當亮度小於0或是達到255，就把浮動加上負數，超過最大就會變負數，減到0則又會變回正數。
  if (brightness <= 0 || brightness >= 255) {
    fadeAmount = -fadeAmount;
  }
  //延遲30毫秒
  delay(30);
}
```
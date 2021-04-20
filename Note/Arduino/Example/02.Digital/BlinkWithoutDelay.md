# Blink Without Delay 不使用Delay函式做出燈光閃爍

此範例不依靠Delay作為頻率的依據使燈光閃爍，用意單純練習Millis函數。

經由取得主機上的時間，以目前時間減去前次更改LED狀態時間，若達到原設好的頻率時間，就改變LED狀態。

```ino
 unsigned long currentMillis = millis();
```
## unsigned
 關鍵字代表此變數為無符號數，也就是只有正數(自然數)，等於有兩倍的最大值。最大值為4294967295。

## millis()
這個函數會傳回從開機到目前的毫秒數，傳回值是unsigned long。大約50天才會歸零

## CODE
```ino
// const(constants) 是指此變數宣告後不能做改變。
const int ledPin =  LED_BUILTIN;//  LED_BUILTIN 此變數是板子上的LED腳位預設是13。

// 宣告變數改變led的狀態
int ledState = LOW;            

//儲存LED最後改變狀態的時間
unsigned long previousMillis = 0;        // will store last time LED was updated

//設定多久改變時間的變數
const long interval = 1000; 

void setup() {
  // 設置腳位為輸出模式
  pinMode(ledPin, OUTPUT);
}

void loop() {


  //unsigned 是無符號數的意思。
  unsigned long currentMillis = millis();
  //當 目前時間 減掉 前次改變時間 超過改變頻率的變數時
  if (currentMillis - previousMillis >= interval) {
    // 先把目前時間存起來，作為下一次改變的頻率依據。
    previousMillis = currentMillis;

    // 改變LED狀態，若燈熄滅，則開啟，反之亦然。
    if (ledState == LOW) {
      ledState = HIGH;
    } else {
      ledState = LOW;
    }

    // 套用變數，讓燈作動!
    digitalWrite(ledPin, ledState);
  }
}
```
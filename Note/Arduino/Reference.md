# 常見關鍵字參考

## const 使變數唯獨
常數(Constant)的意思，亦為變數。宣告變數前加上關鍵字會使其變數唯獨，如果更改值就會出錯。
```arduino
const int Red=9;
```

## #define 在程式執行前設定
也就是在程式執行之前宣告變數的意思

舉例：宣告變數VALUE=ABC
```ino
#define VALUE ABC
```

## 轉型
轉文字 String()

舉例
```ino
float a=10.1
String(a)
```
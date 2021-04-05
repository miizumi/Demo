
//載入音調、頻率的對照檔。
#include "pitches.h"

//旋律
int melody[] = {
  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
};

// 每個音的拍子。4:4分音符、8:8分音符。
int noteDurations[] = {
  4, 8, 8, 4, 4, 4, 4, 4
};


void setup() {
  // iterate over the notes of the melody:
  for (int thisNote = 0; thisNote < 8; thisNote++) {

    //計算音符長度。4分音符：1000/4
    //            8分音符：1000/8
    int noteDuration = 1000 / noteDurations[thisNote];

    //tone(Pin,音調,拍子)
    tone(7, melody[thisNote], noteDuration);

    //每個音之間要停一小段，範例上建議為拍子長度+30%
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);

    //停止撥放
    noTone(7);
  }
}

void loop() {
  //不需要重複撥放，所以這裡不寫。
}

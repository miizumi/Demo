const int digitalPin = 2;
const int analogPin = A0;
int digitalValue, analogValue;

void setup() {

  pinMode(digitalPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalValue = digitalRead(digitalPin);

  analogValue = analogRead(analogPin);
  Serial.println(analogValue);
  delay(500);

}

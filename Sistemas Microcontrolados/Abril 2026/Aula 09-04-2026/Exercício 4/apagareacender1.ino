// C++ code
//
void setup()
{
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);
  pinMode(4, INPUT);
}

void loop()
{
  if(digitalRead(2) == HIGH){
    digitalWrite(3, HIGH);
    delay(1000);
  }else if (digitalRead(4) == HIGH){
    digitalWrite(3, LOW);
    digitalWrite(2, LOW);
    delay(1000);
  }
}
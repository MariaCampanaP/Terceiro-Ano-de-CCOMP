// C++ code
void setup()
{
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);
}

void loop()
{
  if(digitalRead(2) == HIGH){
    if(digitalRead(3) == LOW){
      digitalWrite(3, HIGH);
  }else{
    digitalWrite(3, LOW);
  }
 delay(200);
  }
}
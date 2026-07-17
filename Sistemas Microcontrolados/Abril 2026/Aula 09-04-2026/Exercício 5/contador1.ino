// C++ code
//

int i = 0;

void setup()
{
  pinMode(2, INPUT);
  pinMode(3, OUTPUT);
  pinMode(4, INPUT);
  pinMode(5, OUTPUT);
}

void loop()
{
  if(digitalRead(2) == HIGH){
    i++;
    delay(200);
  }
  
  if(i == 1){
    digitalWrite(3, HIGH);
  } else if (i == 2){
    digitalWrite(4, HIGH);
  }else if (i == 3){
    digitalWrite(5, HIGH);
  }else if(i == 4){
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
    i == 0;
  }
}
  
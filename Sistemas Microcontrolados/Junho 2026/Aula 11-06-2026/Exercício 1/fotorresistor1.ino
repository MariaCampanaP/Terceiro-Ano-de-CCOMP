int ledPin = 10;
int ldrPin = 0;
int ldrValor = 0;

void setup(){
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  ldrValor = analogRead(ldrPin);
  if(ldrValor >= 800){ //800 lux
    digitalWrite(ledPin, HIGH);
  }else{
    digitalWrite(ledPin, LOW);
  }
  Serial.println(ldrValor);
  delay(10);
}
  
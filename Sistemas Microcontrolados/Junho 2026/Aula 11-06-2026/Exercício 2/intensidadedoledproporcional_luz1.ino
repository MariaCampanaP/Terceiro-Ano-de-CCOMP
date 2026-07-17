int ledPin = 10;
int ldrPin = 0;
int ldrValor = 0;

void setup(){
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  ldrValor = analogRead(ldrPin);
  int brilho = map(ldrValor, 1022, 713, 0, 255);
  
  analogWrite(ledPin, brilho);
  
  //Serial.println(ldrValor);
  delay(10);
}
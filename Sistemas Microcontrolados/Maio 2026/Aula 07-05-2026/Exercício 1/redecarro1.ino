int trig = 2;
int echo = 3;
int buzzer = 4;

double tempo, cm;

void setup() {
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(buzzer, OUTPUT);

  Serial.begin(9600);
}

void loop() {

  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  tempo = pulseIn(echo, HIGH);

  cm = tempo / 58;

  Serial.println(cm);

  if (cm < 25) {
    tone(buzzer, 1500);
  }

  else if (cm < 50) {
    tone(buzzer, 1500);
    delay(150);
    noTone(buzzer);
    delay(150);
  }

  else if (cm < 100) {
    tone(buzzer, 1500);
    delay(500);
    noTone(buzzer);
    delay(500);
  }

  else {
    noTone(buzzer);
  }
}
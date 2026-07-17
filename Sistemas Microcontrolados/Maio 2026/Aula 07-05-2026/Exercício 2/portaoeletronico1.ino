#include <Servo.h>

int trig = 2;
int echo = 3;
int buzzer = 4;
int servoPin = 9;

double tempo, cm;

Servo portao;

enum Estado {
  FECHADO,
  ABERTO
};

Estado estadoAtual = FECHADO;

void setup() {

  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(buzzer, OUTPUT);

  Serial.begin(9600);

  portao.attach(servoPin);

  portao.write(0);
}

void loop() {


  digitalWrite(trig, LOW);
  delayMicroseconds(2);

  digitalWrite(trig, HIGH);
  delayMicroseconds(10);

  digitalWrite(trig, LOW);

  tempo = pulseIn(echo, HIGH);

  cm = tempo / 58;

  Serial.print("Distancia: ");
  Serial.print(cm);
  Serial.print(" cm | Estado: ");


  switch (estadoAtual) {

    case FECHADO:

      Serial.println("FECHADO");

      portao.write(0);

      if (cm < 25) {
        estadoAtual = ABERTO;
      }

      break;

    case ABERTO:

      Serial.println("ABERTO");

      portao.write(90);

      if (cm > 50) {
        estadoAtual = FECHADO;
      }

      break;
  }


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
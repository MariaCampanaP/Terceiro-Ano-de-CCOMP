#include <Servo.h>

Servo servoMotor;

void setup(){
  servoMotor.attach(2);

  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
}

void loop(){
  //Estado: VERMELHO (cancela fechada)
  digitalWrite(3, HIGH);
  digitalWrite(4, LOW);
  servoMotor.write(0); // cancela fechada

  delay(3000);

  //Estado: VERDE (cancela aberta)
  digitalWrite(3, LOW);
  digitalWrite(4, HIGH);
  servoMotor.write(90); // cancela aberta

  delay(3000);
}
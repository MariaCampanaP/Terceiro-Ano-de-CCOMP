// C++ code
//

#include <Servo.h>

Servo servoMotor;
int pos, potencia;

void setup(){
  servoMotor.attach(2);
  servoMotor.write(0);
  Serial.begin(9600);
}

void loop(){
  
  potencia = analogRead(A0);
  
  pos = map(potencia, 0, 1023, 0, 179);
  
  servoMotor.write(pos);
  
  delay(15);
  
}
 
  
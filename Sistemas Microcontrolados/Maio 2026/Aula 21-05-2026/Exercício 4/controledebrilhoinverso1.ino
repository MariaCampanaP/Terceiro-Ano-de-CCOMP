const int led1 = 9;
const int led2 = 10;
const int potenciometro = A0;

int valorPot = 0;
int brilhoLed1 = 0;
int brilhoLed2 = 0;

enum Estado{
  LER_POT,
  AJUSTAR_LEDS
};

Estado estadoAtual = LER_POT;

void setup(){
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  
  Serial.begin(9600);
}

void loop(){
  switch(estadoAtual){
    case LER_POT:
     valorPot = analogRead(potenciometro);
     brilhoLed1 = map(valorPot, 0, 1023, 0, 255);
     brilhoLed2 = map(valorPot, 0, 1023, 255, 0);
     estadoAtual = AJUSTAR_LEDS;
     break;
    
    case AJUSTAR_LEDS:
     analogWrite(led1, brilhoLed1);
     analogWrite(led2, brilhoLed2);
     
     Serial.print("Pot: ");
     Serial.print(valorPot);
    
     Serial.print(" | LED1: ");
     Serial.print(brilhoLed1);
     
     Serial.print(" | LED2: ");
     Serial.println(brilhoLed2);
     
     estadoAtual = LER_POT;
     break;
    
  }
  
  delay(20);
  
}
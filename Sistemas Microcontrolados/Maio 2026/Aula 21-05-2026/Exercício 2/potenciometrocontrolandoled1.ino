const int led = 9;
const int potenciometro = A0;

int valorPot = 0;
int brilho = 0;

enum Estado{
  LER_POT,
  AJUSTAR_LED
};

Estado estadoAtual = LER_POT;

void setup(){
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  switch(estadoAtual){
    case LER_POT:
     valorPot = analogRead(potenciometro);
     brilho = map(valorPot, 0, 1023, 0, 255);
     estadoAtual = AJUSTAR_LED;
     break;
    
    case AJUSTAR_LED:
     analogWrite(led, brilho);
     Serial.print("Potenciometro: ");
     Serial.print(valorPot);
     Serial.print(" | Brilho: ");
     Serial.println(brilho);
    
     estadoAtual = LER_POT;
     break;
    
  }
  
  delay(20);
  
}
const int buzzer = 8;
const int potenciometro = A0;

int valorPot = 0;
int frequencia = 0;

enum Estado{
  LER_POT,
  TOCAR_BUZZER
};

Estado estadoAtual = LER_POT;

void setup(){
  pinMode(buzzer, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  switch(estadoAtual){
    case LER_POT:
     valorPot = analogRead(potenciometro);
     frequencia = map(valorPot, 0, 1023, 100, 2000);
     estadoAtual = TOCAR_BUZZER;
     break;
    
    case TOCAR_BUZZER:
     tone(buzzer, frequencia);
    
     Serial.print("Potenciometro: ");
     Serial.print(valorPot);
     
     Serial.print(" | Frequencia: ");
     Serial.print(frequencia);
     Serial.println(" Hz");
    
     estadoAtual = LER_POT;
     break;
    
  }
  
  delay(20);
  
}
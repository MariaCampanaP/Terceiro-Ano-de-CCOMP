int ledPin = 10;
int ldrPin = A0;
int ldrValor = 0;

int contador = 0;
bool estavaEscuro = false;

void setup(){
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  ldrValor = analogRead(ldrPin);
  
  if(ldrValor < 800){ //Ambiente escuro
    digitalWrite(ledPin, LOW); //Apaga o LED
    
    if(!estavaEscuro){
      contador++;
      Serial.print("O ambiente ficou escuro ");
      Serial.print(contador);
      Serial.println(" vez(es). ");
      
      estavaEscuro = true;
    }
    
  }else{ //Ambiente claro
    
    digitalWrite(ledPin, HIGH); //Acende o LED
    estavaEscuro = false;
  }
  
  delay(10);
  
}
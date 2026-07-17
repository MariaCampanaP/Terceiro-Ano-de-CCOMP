int ledPin = 10;
int buzzerPin = 8;
int ldrPin = A0;
int ldrValor = 0;

unsigned long tempoInicioEscuro = 0;

enum Estado{
  CLARO,
  ESCURO,
  ALARME
};

Estado estado = CLARO;

void setup(){
  pinMode(ledPin, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  
  ldrValor = analogRead(ldrPin);
  
  switch(estado){
    
    case CLARO:
    
    	digitalWrite(ledPin, HIGH); //Ambiente claro
    	noTone(buzzerPin);
    
    if(ldrValor < 800){
      tempoInicioEscuro = millis();
      estado = ESCURO;
      Serial.println("Ambiente escuro.");
    }
    break;
    
    case ESCURO:
    
    digitalWrite(ledPin, LOW);
    
    if(ldrValor >= 800){
      estado = CLARO;
    }else if (millis() - tempoInicioEscuro >= 3000){
      estado = ALARME;
      Serial.println("ALARME! Ambiente escuro por mais de 3 segundos.");
    }
    break;
    
    case ALARME:
    
    digitalWrite(ledPin, LOW);
    tone(buzzerPin, 1000); //Buzzer toca em 100 Hz
    
    if(ldrValor >= 800){
      noTone(buzzerPin);
      estado = CLARO;
      Serial.println("Ambiente voltou a ficar claro.");
    }
    break;
  }
  
  delay(10);
  
}
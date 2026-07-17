const int led = 9;

int brilho = 0;

int passo = 5;

enum Estado{
  AUMENTANDO,
  DIMINUINDO
};

Estado estadoAtual = AUMENTANDO;

void setup(){
  pinMode(led, OUTPUT);
}

void loop(){
  switch(estadoAtual){
    case AUMENTANDO:
     brilho += passo;
     analogWrite(led, brilho);
    
    if(brilho >= 255){
      brilho = 255;
      estadoAtual = DIMINUINDO;
    }
    break;
    
    case DIMINUINDO:
     brilho -= passo;
     analogWrite(led, brilho);
    
    if(brilho <= 0){
      brilho = 0;
      estadoAtual = AUMENTANDO;
    }
    break;
  }
  
  delay(30);
}
int a = 3, b = 2, c = 8, d = 7, e = 6, f = 4, g = 5;

int numeros[10][7] = {
  //a b c d e f g
  {1,1,1,1,1,1,0}, //0
  {0,1,1,0,0,0,0}, //1
  {1,1,0,1,1,0,1}, //2
  {1,1,1,1,0,0,1}, //3
  {0,1,1,0,0,1,1}, //4
  {1,0,1,1,0,1,1}, //5
  {1,0,1,1,1,1,1}, //6
  {1,1,1,0,0,0,0}, //7
  {1,1,1,1,1,1,1}, //8
  {1,1,1,1,0,1,1}  //9
};

int pinos[6] = {a,b,c,d,e,f};
int pinosnum[7] = {a,b,c,d,e,f,g};

int botao = 10;

void setup() {

  for(int i = 0; i < 6; i++){
    pinMode(pinos[i], OUTPUT);
  }

  pinMode(botao, INPUT);

  randomSeed(analogRead(0));
}

void mostrarNumero(int num){

  for(int i = 0; i < 7; i++){
    digitalWrite(pinosnum[i], numeros[num][i]);
  }

}

void apagarTudo(){

  for(int i = 0; i < 7; i++){
    digitalWrite(pinos[i], LOW);
    digitalWrite(pinosnum[i], LOW);
  }

}

void loop() {

  // animação girando
  for(int i = 0; i < 7; i++){
    

    apagarTudo();

    digitalWrite(pinos[i], HIGH);

    delay(200);

    // botão apertado
    if(digitalRead(botao) == HIGH){

      int randNum = random(0,9);

      mostrarNumero(randNum);

      delay(2000);
    }
  }
}
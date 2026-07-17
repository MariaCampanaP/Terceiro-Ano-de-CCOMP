int a = 3, b = 2, c = 8, d = 7, e = 6, f = 4, g = 5, h = 9;
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

int pinos[7] = {a,b,c,d,e,f,g};

void setup() {
  for(int i = 0; i < 7; i++){
    pinMode(pinos[i], OUTPUT);
  }
}

void mostrarNumero(int num){

  for(int i = 0; i < 7; i++){
    digitalWrite(pinos[i], numeros[num][i]);
  }

}

void loop() {

  for(int i = 0; i < 10; i++){

    mostrarNumero(i);

    delay(1000);
  }

}
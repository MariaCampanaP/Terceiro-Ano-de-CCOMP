void setup()
{
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
}

void loop()
{
  for(int n=0; n<32; n++){//percorre o número
    for(int bit=0; bit < 5; bit++){//percorre a posição dos bits
      if(bitRead(n, bit) == 1){//acende/apaga o let da posição dependedo se o bitRead for 1 ou 0
      	digitalWrite(bit+2, HIGH);
      }else{
      	digitalWrite(bit+2, LOW);
      }
    }
    delay(500);
  }

}
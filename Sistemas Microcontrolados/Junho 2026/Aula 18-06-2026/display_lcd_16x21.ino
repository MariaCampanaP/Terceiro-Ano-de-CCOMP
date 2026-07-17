//Escrever uma mensagem no display LCD 16x2
#include <LiquidCrystal.h> //Inclusão da Biblioteca
LiquidCrystal lcd(12, 11, 10, 5, 4, 3, 2);

int backLight = 13; //Pino 13 responsável pelo controle do LED

void setup(){
  pinMode(backLight, OUTPUT);
  digitalWrite(backLight, HIGH); //Liga backlight
  
  lcd.begin(16, 2); //Colunas, linhas. Use 16,2 para display LCD 16x2
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Testando LCD");
  
  lcd.setCursor(0, 1); //Posiciona o cursos para a coluna 0, linha 1 (segunda linha)
  lcd.print("Boa tarde.");
  //Serial.begin(9600);
}

void loop(){
  delay(1000);
  lcd.noDisplay(); //Desliga Display
  delay(500);
  lcd.display(); //Liga Display
}

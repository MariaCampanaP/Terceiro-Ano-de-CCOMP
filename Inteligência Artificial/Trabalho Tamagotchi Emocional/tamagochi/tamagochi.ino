//Escrever uma mensagem no display LCD 16 x 2
#include <LiquidCrystal.h> //Inclusão da Biblioteca
LiquidCrystal lcd(12, 11, 10, 5, 4, 3, 2);

int backLight = 13;// pino 13 responsável pelo controle do LED
int botaoComida = 9, botaoDormir = 8, botaoBrincar = 7;
bool menuAberto = false;
int fome = 100;
int energia = 100;
int felicidade = 100;
int tempo = 0, tempoComida = 0, tempoDormir = 0, tempoBrincar = 0;
int py=0, px=0;//posição do pet
int menu = 0;
int alerta = 0;
int i = 0;
String pet = "(0w0)";

void setup(){
  pinMode(backLight, OUTPUT);
  digitalWrite(backLight, HIGH);// Liga backlight.

  lcd.begin(16, 2);//Colunas, linhas. Use 16,2 para display LCD 16x2
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(pet);
  
  pinMode(botaoComida, INPUT);
  pinMode(botaoDormir, INPUT);
  pinMode(botaoBrincar, INPUT);

  Serial.begin(9600);
}
void loop(){
  if (menu != 9){
    //lcd.noDisplay();// Desliga Display:
    //lcd.display();// Liga Display:
    lcd.setCursor(px, py);
    lcd.print(pet);
    //delay(1000);

    //Alerta caso alguns dos status estejam baixos
    if (alerta == 1){
      delay(2000);
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("(>_<)");
      lcd.setCursor(0,1);
      lcd.print("Estou com fome!!");
      pet = "(-_-)";
      delay(3000);
      lcd.clear();
      alerta = 0;

    } else if (alerta == 2){
      delay(2000);
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("(=_=)");
      lcd.setCursor(0,1);
      lcd.print("Ai que sono...");
      pet = "(-_-)";
      delay(3000);
      lcd.clear();
      alerta = 0;

    }else if (alerta == 3){
      delay(2000);
      lcd.clear();
      lcd.setCursor(0,0);
      lcd.print("(;-;)");
      lcd.setCursor(0,1);
      lcd.print("Estou triste...");
      pet = "(-_-)";
      delay(3000);
      lcd.clear();
      alerta = 0;
    }

    //verificação caso um botão seja pressionado
    if (menuAberto == false){
      if (digitalRead(botaoComida) == HIGH){
        menuAberto = true;
        menu = 1;
      }
      if (digitalRead(botaoDormir) == HIGH){
        menuAberto = true;
        menu = 2;
      }
      if (digitalRead(botaoBrincar) == HIGH){
        menuAberto = true;
        menu = 3;
      }
    }

    //Implementar cada menu de alimentação, dormir, e a brincadeira (Reconhecimento de expressão por IA)
    if (menu == 1){//Alimentação
      delay(2000);
      lcd.clear();

      if(fome < 100){
        for (i = 0; i < 3; i++){
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("(^o^)");
          lcd.setCursor(0,1);
          lcd.print("Nham!");
          delay(500);
          lcd.setCursor(0,0);
          lcd.print("(^-^)");
          lcd.setCursor(0,1);
          lcd.print("Nham! Nham!");
          delay(500);
        }
        fome += 25;
      }else{
        lcd.setCursor(0,0);
        lcd.print("(>_<)");
        lcd.setCursor(0,1);
        lcd.print("Num quero!");
        felicidade -= 5;
        delay(500);
      }
      menu = 0;
      menuAberto = false;
      delay(3000);
      lcd.clear();

    }else if (menu == 2){//Dormir
      delay(2000);
      lcd.clear();

      if(energia < 100){
        for (i = 0; i < 3; i++){
          lcd.clear();
          lcd.setCursor(0,0);
          lcd.print("(=v=).");
          lcd.setCursor(0,1);
          lcd.print("z");
          delay(333);
          lcd.setCursor(0,0);
          lcd.print("(=v=)..");
          lcd.setCursor(0,1);
          lcd.print("zz");
          delay(333);
          lcd.setCursor(0,0);
          lcd.print("(=v=)...");
          lcd.setCursor(0,1);
          lcd.print("zzz...");
          delay(333);
        }
        energia += 25;
      }else{
        lcd.setCursor(0,0);
        lcd.print("(>_<)");
        lcd.setCursor(0,1);
        lcd.print("Num quero!");
        felicidade -= 5;
        delay(500);
      }
      menu = 0;
      menuAberto = false;
      delay(3000);
      lcd.clear();

    }else if (menu == 3){//Brincadeira
      delay(2000);
      lcd.clear();

      if(felicidade < 100){
        char emocao = Serial.read();

        //Verifição da emocão
        if (emocao == '0'){//Neutro
          lcd.setCursor(0,0);
          lcd.print("(0_0)");
          lcd.setCursor(0,1);
          lcd.print(".");
          delay(1000);
          lcd.print("..");
          delay(1000);
          lcd.print("...");
          delay(1000);

      } else if (emocao == '1'){//Feliz
          lcd.setCursor(0,0);
          lcd.print("(^w^)");
          lcd.setCursor(0,1);
          lcd.print("Ebaaaa!");
          delay(1000);
          lcd.print("Ebaaaa!!");
          delay(1000);
          lcd.print("Ebaaaa!!!");
          delay(1000);
          felicidade += 25;

      }else if (emocao == '2'){//Raiva
          lcd.setCursor(0,0);
          lcd.print("(@A@)");
          lcd.setCursor(0,1);
          lcd.print("AAAAAAAAAHHH!");
          delay(1000);
          lcd.print("AAAAAAAAAHHH!!");
          delay(1000);
          lcd.print("AAAAAAAAAHHH!!!");
          delay(1000);
          felicidade -= 25;

      }else if (emocao == '3'){//Triste
          lcd.setCursor(0,0);
          lcd.print("(0^0)");
          lcd.setCursor(0,1);
          lcd.print("O que foi?");
          delay(1000);
          lcd.print("O que foi??");
          delay(1000);
          lcd.print("O que foi???");
          delay(1000);
          felicidade -= 10;      
      }

      }else{
        lcd.setCursor(0,0);
        lcd.print("(>_<)");
        lcd.setCursor(0,1);
        lcd.print("Num quero!");
        felicidade -=5;
        delay(500);
      }
      menu = 0;
      menuAberto = false;
      delay(3000);
      lcd.clear();
    }

    //deixa o pet normal se os status estiverem bons
    if(fome == 100 && energia == 100 && felicidade == 100){
      pet = "(0_0)";
    }

    //Menu padrão onde o pet se movimenta
    if (tempo % 500 == 0 && tempo > 1 && menu == 0){
      if (px == 11){
        if (py == 0){
          px = 0;
          py = 1;
          lcd.clear();
        }else{
          px = 0;
          py = 0;
          lcd.clear();
        }
      }else{
        px++;
        lcd.clear();
      }
    }
    tempo++;
    if (tempo == 10000){
      //"Tick" onde um dos status do pet será reduzido
      int status = random(0, 4);
      if (status == 1){
          fome -= 25;
      }else if (status == 2){
          energia -= 25;
      }else if (status == 3){
          felicidade -= 25;
      }

      if (status == 1 && fome <= 75){
          alerta = 1;
      } else if (status == 2 && energia <= 75){
          alerta = 2;
      }else if (status == 3 && felicidade <= 75){
          alerta = 3;
      }
      
      if (fome <= 0 || energia <= 0 || felicidade <= 0){
      	menu = 9;
        menuAberto = true;
      }

      tempo = 0;
    }
  } else {
    lcd.clear();
  	lcd.setCursor(0,0);
    lcd.print("+");
    lcd.setCursor(0,1);
    lcd.print("O  R.I.P");
    delay(10000);
    lcd.noDisplay();
  }
}

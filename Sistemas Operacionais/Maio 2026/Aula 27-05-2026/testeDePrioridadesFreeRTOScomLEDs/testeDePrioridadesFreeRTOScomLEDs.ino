#define N 7

const int ledA = 18;
const int ledB = 19;

void TarefaA(void *p){
  for(int i = 0; i < N; i++){
    digitalWrite(ledA, HIGH);
    Serial.print("A ");

    //LED ligado por 500 ms
    vTaskDelay(pdMS_TO_TICKS(500));

    digitalWrite(ledA, LOW);

    vTaskDelay(pdMS_TO_TICKS(500));

  }

  Serial.println("\nTarefa A finalizada");
  vTaskDelete(NULL);
}

void TarefaB(void *p){
  for(int i = 0; i < N; i++){
    digitalWrite(ledB, HIGH);
    Serial.print("B ");

    //LED ligado por 500 ms
    vTaskDelay(pdMS_TO_TICKS(500));

    digitalWrite(ledB, LOW);

    //LED apagado por 1000 ms
    vTaskDelay(pdMS_TO_Ticks(1000));
  }

  Serial.println("\nTarefa B finalizada");
  vTaskDelete(NULL);
}

void setup(){
  Serial.begin(115200);

  pinMode(ledA, OUTPUT);
  pinMode(ledB, OUTPUT);

  delay(1000);

  //Limpa o monitor serial
  for(int i = 0; i < 20; i++){
    Serial.println();
  }

  Serial.println("=== Teste Controlado ===");

  //Tarefa A - prioridade 1
  xTaskCreate(
    TarefaA,
    "A",
    2048,
    NULL,
    3,
    NULL
  );

  //Tarefa B - prioridade 3
  xTaskCreate(
    TarefaB,
    "B",
    2048,
    NULL,
    1,
    NULL
  );
}

void loop(){
  vTaskDelay(pdMS_TO_TICKS(1000));
}
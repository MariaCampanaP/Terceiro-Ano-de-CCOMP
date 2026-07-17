#define N 7

const int ledA = 18;
const int ledB = 19;

void TarefaA(void *p){
  for(int i = 0; i < N; i++){
    digitalWrite(ledA, HIGH);
    Serial.print("A ");

    //Sem vTaskDelay()
    //vTaskDelay(pdMS_TO_TICKS(500));

    digitalWrite(ledA, LOW);
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

  Serial.println("=== TESTE SEM vTaskDelay Na Tarefa A ===");

  xTaskCreate(
    TarefaA,
    "A",
    2048,
    NULL,
    3, //maior prioridade
    NULL
  );

  xTaskCreate(
    TarefaB,
    "B",
    2048,
    NULL,
    1, //menor prioridade
    NULL
  );
}

void loop(){
  vTaskDelay(pdMS_TO_TICKS(1000));
}
#define N 7 

void TarefaA(void *p){ 
  for(int i = 0; i < N; i++){ 
    Serial.print("A "); 
    vTaskDelay(pdMS_TO_TICKS(1000)); 
  } 
  Serial.println("\nTarefa A finalizada"); 
  vTaskDelete(NULL); 
} 

void TarefaB(void *p){ 
  for(int i = 0; i < N; i++){ 
    Serial.print("B "); 
    vTaskDelay(pdMS_TO_TICKS(1000)); 
  } 
  Serial.println("\nTarefa B finalizada"); 
  vTaskDelete(NULL); 
} 

void setup(){ 
  Serial.begin(115200); 
  delay(1000); 

  //limpar monitor 
  for(int i = 0; i < 20; i++) Serial.println(); 
  Serial.println("=== Teste Controlado ==="); 
  xTaskCreate(TarefaA, "A", 2048, NULL, 1, NULL); 
  xTaskCreate(TarefaB, "B", 2048, NULL, 1, NULL); 
  } 

void loop(){ 
  vTaskDelay(pdMS_TO_TICKS(1000)); 
}
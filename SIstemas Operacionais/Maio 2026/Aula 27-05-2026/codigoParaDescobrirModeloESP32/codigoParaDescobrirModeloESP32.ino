void setup(){
  Serial.begin(11520);
  delay(1000);

  Serial.println("\n=== Diagnóstico do ESP32 ==="); //Retorna o modelo exato do chip (Ex: ESP32, ESP32-S3, ESP32-C3)
  Serial.printf("Modelo do Chip: %s\n", ESP.getChipModel()); //Mostra e revisão do silício do chip
  Serial.printf("Revisão do Chip: %d\n", ESP.getChipRevision()); //Retorna a quantidade de núcleos ativos (1 ou 2)
  Serial.printf("Núcleos (Cores): %d\n", ESP.getChipCores()); //Retorna o tamanho da memória Flash interna/externa integrada em Bytes
  Serial.printf("Tamanho da Flash: %d MB\n", ESP.getFlashChipSize() / (1024 * 1024)); //Retorna o endereço MAC único do chip (usado frequentemente como ID única)
  uint64_t chipId = ESP.getEfuseMac();
  Serial.printf("ID Único (MAC): %04X%08X\n", (uint16_t)(chipId >> 32), (uint32_t)chipId);
  Serial.println("============================\n");
}

void loop(){
  //Nada a fazer aqui
}
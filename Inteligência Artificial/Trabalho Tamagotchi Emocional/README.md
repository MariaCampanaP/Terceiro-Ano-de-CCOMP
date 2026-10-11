<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&color=FFDE21&reversal=false"/>

## ☕︎︎ Projeto - Tamagotchi Emocional

Projeto acadêmico que une a matéria de **Inteligência Artificial** e **Sistemas Microcontrolados**: uma CNN reconhece a expressão facial do usuário pela webcam (feliz, bravo ou triste) e envia o resultado por comunicação serial para um Tamagotchi rodando em um display LCD 16x2, que reage à emoção detectada. 

---

## ☕︎︎ Breve História do Contexto

O **Tamagotchi** foi lançado em 23 de novembro de 1996 no Japão pela empresa Bandai, criado em parceria com Akihiro Yokoi e Aki Maita. O nome vem da junção de *tamago* ("ovo" em japonês) e *uotchi* (adaptação de "watch"/relógio em inglês), pois a ideia inicial era um relógio de pulso.
O pequeno aparelho em formato de ovo (ou chaveiro) simulava a criação de um bichinho virtual que pedia comida, banho, carinho e atenção. Se fosse ignorado, o pet "morria". Virou uma febre global em 1997, levando até a proibições em escolas por distrair os alunos.
O brinquedo desembarcou no Brasil (popularizando-se também com versões similares e concorrentes como os bichinhos virtuais de feira), marcando a infância dos anos 90.
Ganhou novas versões com conexão infravermelho (*Connection* em 2004) e, mais recentemente, telas coloridas e conexão Wi-Fi (*Tamagotchi Uni* em 2023).
O fenômeno já ultrapassou a marca de **90 milhões de unidades vendidas** em todo o mundo.

---

## ☕︎︎ Como Funciona

```
Webcam → Python (OpenCV + CNN) → Serial USB (9600 bps) → Arduino → LCD 16x2
```
 
1. A webcam captura o rosto do usuário.
2. O frame é convertido para cinza, redimensionado para 48x48 e normalizado.
3. A CNN classifica a emoção (`happy`, `angry`, `sad`).
4. O Python envia um código ao Arduino via PySerial.
5. No modo **Brincar**, o Tamagotchi reage de acordo com a emoção recebida.

| Emoção | Classe (Python) | Código enviado ao Arduino |
|--------|-----------------|---------------------------|
| Happy  | 0               | `1`                       |
| Angry  | 1               | `2`                       |
| Sad    | 2               | `3`                       |
 
---
 
## ☕︎︎ Estrutura do repositório
 
| Arquivo        | Função                                                                 |
|----------------|------------------------------------------------------------------------|
| `machine.py`   | Baixa o dataset, pré-processa, treina a CNN, avalia e salva `modelo.keras` |
| `cnn.py`       | Teste do modelo com webcam + detecção de rosto (Haar Cascade), sem Arduino |
| `teste.py`     | Execução final: classifica a webcam e envia a emoção ao Arduino        |
| `tamagochi.ino`| Código do Tamagotchi (display, botões, status do pet, leitura serial)  |
 
---
 
## ☕︎︎ Datasets
 
- **FER-2013** (principal): baixado automaticamente pelo `machine.py` via `gdown` para a pasta `emotions/`.
- **CK+ (Extended)** (secundário): deve estar na pasta `ckextended/`, com subpastas `happy`, `anger` e `sadness`. Se a pasta não existir, o treino usa só o FER-2013.
Imagens de 48x48 pixels em tons de cinza. Apenas 3 classes foram usadas.
 
| Classe | Imagens |
|--------|---------|
| Felicidade | 1843 |
| Raiva      | 1003 |
| Tristeza   | 1275 |
 
O desbalanceamento é tratado com `compute_class_weight`.
 
---
 
## ☕︎︎ Modelo
 
CNN com três blocos convolucionais e camadas densas finais:
 
- 3x `Conv2D` (32, 64 e 128 filtros, 3x3, ReLU) + `BatchNormalization` + `MaxPooling2D` + `Dropout` (0,25 / 0,25 / 0,35)
- `Flatten` → `Dense(128, ReLU)` → `Dropout(0,5)` → `Dense` softmax
**Treinamento:** Adam (lr = 0,0005), `sparse_categorical_crossentropy`, até 40 épocas, batch 64, validação interna de 10%, `EarlyStopping` (paciência 6, monitorando `val_loss`). Divisão treino/teste 80/20 estratificada, `random_state=25`.
 
---
 
## ☕︎︎ Resultados
 
Acurácia geral no conjunto de teste: **71,20%** (2160 imagens).
 
| Classe | Precisão | Recall | F1-score | Suporte |
|--------|----------|--------|----------|---------|
| happy  | 77,05%   | 87,64% | 82,00%   | 720     |
| angry  | 67,97%   | 65,42% | 66,67%   | 720     |
| sad    | 67,28%   | 60,56% | 63,74%   | 720     |
 
A emoção *happy* é a mais bem reconhecida. *Angry* e *sad* são as mais confundidas entre si. O treino gera `matriz_confusao.png` e `historico_treinamento.png`.
 
---
 
## ☕︎︎ Hardware
 
- Arduino Uno
- Display LCD 16x2
- Protoboard, jumpers
- 3 botões (Comida, Dormir, Brincar)
- Webcam
**Pinagem usada em `tamagochi.ino`:**
 
| Componente        | Pino(s)                     |
|-------------------|-----------------------------|
| LCD (RS, E, D4–D7)| 12, 11, 10, 5, 4, 3, 2      |
| Backlight         | 13                          |
| Botão Comida      | 9                           |
| Botão Dormir      | 8                           |
| Botão Brincar     | 7                           |
 
---

## ☕︎︎ Como executar
 
### 1. Instalar dependências
 
```bash
pip install numpy opencv-python tensorflow scikit-learn matplotlib seaborn gdown pyserial pandas
```
 
### 2. Treinar o modelo
 
```bash
python machine.py
```
 
Gera o arquivo `modelo.keras`.
 
### 3. (Opcional) Testar só com a webcam
 
```bash
python cnn.py
```
 
Mostra a emoção detectada na tela. Pressione **ESC** para sair.
 
### 4. Rodar com o Arduino
 
1. Envie `tamagochi.ino` para o Arduino pela Arduino IDE.
2. Em `teste.py`, ajuste a porta serial para a do seu computador (no código está `COM13`):
```python
   arduino = serial.Serial('COM13', 9600, timeout=1)
```
3. Feche o Monitor Serial da Arduino IDE (ele ocupa a porta).
4. Execute:
```bash
   python teste.py
```
 
Pressione **ESC** para encerrar.
 
---

## ☕︎︎ Como jogar
 
| Botão   | Ação                                                              |
|---------|-------------------------------------------------------------------|
| Comida  | Aumenta a fome em 25 (se já estiver cheio, o pet recusa)          |
| Dormir  | Aumenta a energia em 25 (se já estiver descansado, o pet recusa)  |
| Brincar | Lê a emoção enviada pelo Python e o pet reage                     |
 
Reações no modo Brincar:
 
| Emoção | Reação do pet | Felicidade |
|--------|---------------|------------|
| Happy  | `(^w^)` "Ebaaaa!" | +25 |
| Angry  | `(@A@)` "AAAAAAAAAHHH!" | −25 |
| Sad    | `(0^0)` "O que foi?" | −10 |
 
Fome, energia e felicidade começam em 100 e caem aos poucos de forma aleatória. O pet avisa quando algum status fica baixo. Se algum chegar a 0, o pet morre (`R.I.P`).
 
---

## ☕︎︎ Limitações
 
- O desempenho depende de iluminação, posição da câmera e ângulo do rosto.
- Raiva e tristeza têm expressões parecidas e são frequentemente confundidas.
- Apenas três emoções são reconhecidas.

---

## ☕︎︎ Equipe

**Luna**
- GitHub: [Luna-Osti](https://github.com/Luna-Osti)
- LinkedIn: [Luna Osti de França](https://www.linkedin.com/in/luna-osti-de-frança-23961b321/)

**Maria Rita**
- GitHub: [MariaCampanaP](https://github.com/MariaCampanaP)
- LinkedIn: [Maria Rita Campana Peixoto](https://www.linkedin.com/in/maria-rita-campana/)

**Vallentina**
- GitHub: [Vallentinanina](https://github.com/Vallentinanina)
- LinkedIn: [Vallentina Rodrigues Costa Groetaers Sousa](https://www.linkedin.com/in/vallentina-rodrigues-costa-groetaers-sousa-435b85319/)
  
## ☕︎︎ Como Usar

## Como clonar apenas esta pasta

Este repositório contém todas as disciplinas do 3° ano. Se quiser baixar **somente** a pasta "Trabalho Tamagotchi Emocional" (dentro de Inteligência Artificial), use o sparse-checkout do Git:

```bash
git clone --no-checkout https://github.com/MariaCampanaP/Terceiro-Ano-de-CCOMP.git
cd Terceiro-Ano-de-CCOMP
git sparse-checkout init --cone
git sparse-checkout set "Inteligência Artificial/Trabalho Tamagotchi Emocional"
git checkout main
```
   
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&color=FFDE21&reversal=false&section=footer"/>

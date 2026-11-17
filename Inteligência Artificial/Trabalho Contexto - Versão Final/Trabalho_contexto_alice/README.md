<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&color=FFDE21&reversal=false"/>

## ☕︎︎ Projeto - Contexto: Alice no País das Maravilhas - Versão Final

Jogo de adivinhação de palavras inspirado no jogo online [Contexto](https://contexto.me/), desenvolvido para as disciplinas de **Inteligência Artificial** e **Redes de Computadores e Sistemas Distribuídos** do curso de Bacharelado em Ciência da Computação da Universidade Estadual do Paraná (UNESPAR).

O projeto utiliza como referência a obra **Alice no País das Maravilhas**, de Lewis Carroll, tanto na identidade visual da interface quanto na construção do vocabulário utilizado pelo algoritmo de similaridade semântica.

A aplicação combina **Processamento de Linguagem Natural (NLP)**, vetores de palavras (world embeddings) e similaridade de cosseno para criar uma experiência de adivinhação baseada na proximidade de significado entre palavras.

## ☕︎︎ Sobre o projeto

O Contexto é um jogo de adivinhação no qual o objetivo é descobrir uma palavra secreta por meio de tentativas ilimitadas.

Inspirado no jogo original, o projeto utiliza um sistema de classificação semântica: cada palavra digitada recebe uma posição em um ranking, indicando sua proximidade em relação à palavra secreta.

Nesta versão, o vocabulário é extraído do livro Alice no País das Maravilhas, permitindo explorar técnicas de Inteligência Artificial em um conjunto de palavras delimitado por uma obra literária.

## ☕︎︎ Como o jogo funciona

1. O servidor sorteia uma palavra secreta a partir do vocabulário extraído do livro.
2. Um ranking é calculado considerando a similaridade semântica entre todas as palavras do vocabulário e a palavra secreta.
3. O jogador realiza tentativas por meio da interface gráfica.
4. Cada tentativa retorna uma posição real no ranking.
5. Quanto menor o número da posição, maior a proximidade semântica com a palavra secreta

A palavra secreta ocupa sempre a posição 1.

O jogo também oferece dicas, validação de palavras, identificação de tentativas repetidas e indicadores visuais de proximidade.

## ☕︎︎ Funcionalidades implementadas

## Interface gráfica
- Menu principal com navegação entre as telas.
- Tela de ajuda com explicação das regras.
- Tela sobre com informações da equipe e do projete.
- Interface de jogo com campo de entrada de palavras.
- Elementos ilustrativos inspirados no universo de Alice no País das Maravilhas.
- Menu de opções com acesso às funcionalidades adicionais.

## Mecânica do jogo
- Sorteio de palavra secreta.
- Ranking calculado por similaridade semântica.
- Classificação real das palavras enviadas.
- Histórico de tentativas ordenado por proximidade.
- Contador de tentativas.
- Validação de palavras fora do vocabulário.
- Identificação de palavras já utilizadas.
- Sistema de dicas com palavras mais próximas da resposta.
- Barra de proximidade com escala logarítmica:
  - 🟩 Verde: muito perto.
  - 🟨 Amarelo: perto.
  - 🟥 Vermelho: longe.
  - Sem barra: muito longe.

## Mecânica do jogo
- Tela de vitória ao encontrar a palavra secreta.
- Tela de desistência com revelação da palavra.
- Exibição do número de tentativas realizadas.
- Bloqueio de novas tentativas após o encerramento da partida.

## ☕︎︎ Arquitetura do sistema
 
O projeto utiliza uma arquitetura cliente-servidor, separando a interface gráfica da lógica responsável pelo processamento das palavras e pelo funcionamento do jogo.
 
A comunicação entre os componentes é realizada por meio de **XML-RPC**, utilizando a biblioteca padrão do Python.
 
```text
┌──────────────────────────────────┐
│ CLIENTE                          │
│ cliente_interface_contexto.py    │
│                                  │
│ CustomTkinter                    │
│ Interface gráfica                │
│ Navegação e interação            │
└────────────────┬─────────────────┘
                 │
                 │ XML-RPC
                 │ localhost:9876
                 │
┌────────────────▼─────────────────┐
│ SERVIDOR                         │
│ servidor_integrador_cosseno.py   │
│                                  │
│ Processamento NLP                │
│ Ranking semântico                │
│ Lógica do jogo                   │
└────────────────┬─────────────────┘
                 │
                 ▼
             livro.txt
```
 
### Responsabilidades dos componentes
 
**Cliente — `cliente_interface_contexto.py`**
 
Responsável pela interface gráfica, navegação entre telas, interação com o jogador e apresentação dos resultados. As operações relacionadas à lógica do jogo são solicitadas remotamente ao servidor por meio de um `ServerProxy`.
 
**Servidor — `servidor_integrador_cosseno.py`**
 
Responsável pelo processamento do livro, construção do vocabulário, sorteio da palavra secreta, cálculo do ranking semântico, validação das tentativas e disponibilização das funções remotas.
 
Por padrão, a comunicação ocorre em `localhost`, utilizando a porta `9876`.
 
### Funções remotas disponibilizadas
 
| Função                     | Responsabilidade                                                                                                |
| -------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `iniciarJogo()`            | Sorteia a palavra secreta, gera o ranking e reinicia o histórico de tentativas.                                 |
| `calcularPosicao(palavra)` | Retorna a posição da palavra no ranking. Retorna `-1` para palavras inválidas e `-2` para tentativas repetidas. |
| `solicitarDica()`          | Retorna uma palavra mais próxima da secreta do que a melhor tentativa atual.                                    |
| `revelarPalavraSecreta()`  | Retorna a palavra secreta, utilizada no encerramento por desistência.                                           |
 
---

## ☕︎︎ Processamento de Linguagem Natural (NLP)
 
O processamento do livro é realizado utilizando a biblioteca spaCy, com o modelo de português `pt_core_news_lg`.
 
### Pipeline de processamento
 
1. **Leitura:** carregamento do arquivo `livro.txt`, contendo o texto de Alice no País das Maravilhas em português.
2. **Extração de substantivos:** identificação gramatical e lematização das palavras utilizando o spaCy.
3. **Normalização:** conversão para letras minúsculas, remoção de acentos com Unidecode e eliminação de caracteres não alfabéticos.
4. **Filtragem:** remoção de palavras irrelevantes por meio de listas de stopwords, incluindo pronomes, verbos auxiliares, advérbios e termos estruturais do livro.
5. **Construção do vocabulário:** seleção das palavras que aparecem pelo menos cinco vezes na obra (`freq_min=5`).
6. **Representação vetorial:** utilização dos vetores semânticos (*word embeddings*) disponibilizados pelo modelo.
7. **Cálculo de similaridade:** comparação dos vetores por meio da similaridade de cosseno.
8. **Ordenação:** construção do ranking, da palavra semanticamente mais próxima à mais distante da palavra secreta.
### Similaridade de cosseno
 
A similaridade de cosseno permite comparar a orientação de dois vetores, indicando o quanto suas representações semânticas são próximas.
 
Sua fórmula é:
 
$$
\text{similaridade}(A,B) = \frac{A \cdot B}{\|A\| \, \|B\|}
$$
 
Quanto maior a similaridade, maior a proximidade entre as representações vetoriais das palavras.
 
---

## ☕︎︎ Tecnologias utilizadas
 
| Tecnologia        | Aplicação                                                                    |
| ----------------- | ---------------------------------------------------------------------------- |
| Python 3          | Linguagem principal do projeto.                                              |
| CustomTkinter     | Construção da interface gráfica.                                             |
| Tkinter (Canvas)  | Criação de elementos ilustrativos e componentes gráficos personalizados.     |
| spaCy             | Processamento de Linguagem Natural, análise gramatical e vetores semânticos. |
| `pt_core_news_lg` | Modelo de linguagem em português.                                            |
| NumPy             | Operações vetoriais e cálculo de similaridade de cosseno.                    |
| Unidecode         | Normalização e remoção de acentos.                                           |
| XML-RPC           | Comunicação entre cliente e servidor.                                        |
| JSON              | Configuração do tema visual.                                                 |
 
---
 
## ☕︎︎ Como executar o projeto
 
### Pré-requisitos
 
- Python 3.10 ou superior.
- pip.
- Arquivos do projeto disponíveis localmente.
### 1. Instalação das dependências
 
No terminal, dentro da pasta do projeto, execute:
 
```bash
pip install customtkinter spacy numpy unidecode
```
 
Em seguida, instale o modelo de português do spaCy:
 
```bash
python -m spacy download pt_core_news_lg
```
 
### 2. Verificação dos arquivos
 
Certifique-se de que os seguintes arquivos estejam disponíveis na pasta do projeto:
 
- `cliente_interface_contexto.py`
- `servidor_integrador_cosseno.py`
- `livro.txt`
- `tema_contexto.json` (opcional)
Caso o arquivo `tema_contexto.json` não seja encontrado, o cliente utiliza automaticamente o tema padrão `blue` do CustomTkinter.
 
### 3. Inicialização do servidor
 
Abra um terminal na pasta do projeto e execute:
 
```bash
python servidor_integrador_cosseno.py
```
 
Aguarde a mensagem:
 
```text
Servidor Contexto - Alice Iniciado
```
 
O carregamento do modelo de linguagem e do livro pode levar alguns instantes.
 
### 4. Inicialização do cliente
 
Abra um segundo terminal e execute:
 
```bash
python cliente_interface_contexto.py
```
 
Após a abertura da interface, clique em **Entrar** para iniciar uma partida.
 
> **Observação:** a cada nova partida, o servidor realiza o sorteio da palavra secreta e o cálculo do ranking. Para fins de teste, a palavra secreta também é apresentada no terminal do servidor.
 
### 5. Comunicação entre máquinas diferentes
 
Por padrão, o sistema utiliza `localhost`, na porta `9876`.
 
Para executar o cliente e o servidor em máquinas diferentes, é necessário alterar o endereço de conexão no `ServerProxy` do cliente e configurar o servidor para escutar no endereço de rede apropriado.
 
---
 
## ☕︎︎ Evolução e entregas do projeto
 
O desenvolvimento foi dividido em duas etapas acadêmicas, permitindo a evolução gradual da interface gráfica para uma aplicação completa com processamento semântico e arquitetura distribuída.
 
### 3º Bimestre — Estrutura inicial
 
- Definição das tecnologias utilizadas.
- Escolha da obra literária e da identidade visual.
- Desenvolvimento das telas iniciais: Menu, Ajuda, Sobre e Jogo.
- Implementação da navegação entre telas.
- Construção dos elementos gráficos inspirados em Alice no País das Maravilhas.
### 4º Bimestre — Implementação final
 
- Separação da aplicação em cliente e servidor.
- Implementação da comunicação por XML-RPC.
- Processamento do livro utilizando NLP.
- Extração e normalização do vocabulário.
- Cálculo do ranking por similaridade de cosseno.
- Implementação da posição real das palavras.
- Sistema de dicas funcional.
- Validação de palavras inválidas e repetidas.
- Barra visual de proximidade e tabela ordenada.
- Implementação das telas de vitória e desistência.
---
 
## ☕︎︎ Equipe
 
### Luna Osti de França
 
- GitHub: [Luna-Osti](https://github.com/Luna-Osti)
- LinkedIn: [Luna Osti de França](https://www.linkedin.com/in/luna-osti-de-frança-23961b321/)
### Maria Rita Campana Peixoto
 
- GitHub: [MariaCampanaP](https://github.com/MariaCampanaP)
- LinkedIn: [Maria Rita Campana Peixoto](https://www.linkedin.com/in/maria-rita-campana/)
### Vallentina Rodrigues Costa Groetaers Sousa
 
- GitHub: [Vallentinanina](https://github.com/Vallentinanina)
- LinkedIn: [Vallentina Rodrigues Costa Groetaers Sousa](https://www.linkedin.com/in/vallentina-rodrigues-costa-groetaers-sousa-435b85319/)
---

## ☕︎︎ Como Usar

## Como clonar apenas esta pasta

Este repositório contém todas as disciplinas do 3° ano. Se quiser baixar **somente** a pasta "Trabalho Contexto" (dentro de Inteligência Artificial), use o sparse-checkout do Git:

```bash
git clone --no-checkout https://github.com/MariaCampanaP/Terceiro-Ano-de-CCOMP.git
cd Terceiro-Ano-de-CCOMP
git sparse-checkout init --cone
git sparse-checkout set "Inteligência Artificial/Trabalho Contexto - Versão Final"
git checkout main
```
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&color=FFDE21&reversal=false&section=footer"/>

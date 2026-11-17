# Contexto - Alice no País das Maravilhas

Jogo de adivinhação de palavras inspirado no jogo online [Contexto](https://contexto.me/), desenvolvido para as disciplinas de **Inteligência Artificial** e **Redes de Computadores e Sistemas Distribuídos** do curso de Bacharelado em Ciência da Computação da Universidade Estadual do Paraná (UNESPAR).

O jogo utiliza como base o livro **Alice no País das Maravilhas** de Lewis Carroll, tanto para a identidade visual da interface quanto para o vocabulário que será usado no cálculo de similaridade semântica entre as palavras.

## Equipe

- Luna Osti de França
- Maria Rita Campana Peixoto
- Vallentina Rodrigues Costa Groetaers Sousa

## Como o jogo funciona 

O servido sorteia uma **palavra secreta** a partir do vocabulário do livro e calcula um **ranking** de todas as outras palavras por proximidade semântica com ela. A cada tentativa, o jogador descobre em que posição do ranking sua palavra está: a palavra secreta é a posição **1**, e quanto menor o número, mais perto o jogador está da resposta.

## Entregas

### 3° Bimestre 

- Definição das tecnologias utilizadas
- Definição do livro escolhido e do visual do jogo
- Implementação das telas iniciais (Menu, Ajuda, Sobre e Jogo), com navegação funcional entre elas

### 4° Bimestre

- Separação do projeto em **cliente** (interface) e **servidor** (lógica do jogo), comunicando-se via **XML-RPC**
- Processamento do livro com NLP e cálculo real do ranking por **similaridade de cosseno**
- Posição real de cada palavra no ranking
- Dicas funcionando
- Validação de palavras (inválidas e repetidas)
- Barra de proximidade colorida e tabela ordenada por proximidade
- Telas de resultado (vitória e desistência), com revelação da palavra secreta

## Arquitetura
 
```
┌──────────────────────────────┐   XML-RPC    ┌─────────────────────────────────┐
│ cliente_interface_contexto.py│ ───────────► │ servidor_integrador_cosseno.py  │
│ (customtkinter)              │ ◄─────────── │ (spaCy + NumPy)                 │
└──────────────────────────────┘ localhost:   └─────────────────────────────────┘
                                   9876                      │
                                                             ▼
                                                        livro.txt
```
 
- O **servidor** (`servidor_integrador_cosseno.py`) carrega o livro, monta o vocabulário, sorteia a palavra secreta e responde às requisições do cliente.
- O **cliente** (`cliente_interface_contexto.py`) exibe a interface e chama as funções remotas do servidor por meio de um `ServerProxy`.
- Por padrão a comunicação é feita em `localhost`, porta `9876`. Para jogar em máquinas diferentes, altere o endereço no `ServerProxy` do cliente (e o endereço em que o servidor escuta) para o IP da máquina do servidor.

### Funções remotas expostas pelo servidor
 
| Função | Descrição |
|---|---|
| `iniciarJogo()` | Sorteia a palavra secreta, gera o ranking e zera o histórico de tentativas |
| `calcularPosicao(palavra)` | Retorna a posição da palavra no ranking. Retorna `-1` se a palavra não está no vocabulário e `-2` se já foi tentada |
| `solicitarDica()` | Retorna uma palavra aleatória que está mais perto da secreta do que a melhor tentativa até o momento |
| `revelarPalavraSecreta()` | Retorna a palavra secreta (usada ao desistir) |

### Pipeline de processamento do livro
 
1. **Leitura** do `livro.txt` (texto de *Alice no País das Maravilhas* em português).
2. **Extração de substantivos** com o spaCy (modelo `pt_core_news_lg`), usando o **lema** de cada palavra.
3. **Normalização**: minúsculas, remoção de acentos (`unidecode`) e de caracteres não alfabéticos.
4. **Filtragem** por listas de *stopwords* (estruturais, pronomes, verbos auxiliares, advérbios e termos próprios do livro, como "capítulo" e "gutenberg").
5. **Vocabulário**: apenas palavras que aparecem pelo menos **5 vezes** no livro (`freq_min=5`).
6. **Ranking**: o vetor (*word embedding*) de cada palavra do vocabulário é comparado ao da palavra secreta por **similaridade de cosseno**, e as palavras são ordenadas da mais para a menos similar.
## Tecnologias Utilizadas
 
- **Python 3**
- **[customtkinter](https://github.com/TomSchimansky/CustomTkinter)** - construção da interface gráfica, com tema visual customizado (`tema_contexto.json`)
- **Tkinter (Canvas)** - elementos ilustrados (relógio do Coelho Branco, cartas de baralho, Absolem/cogumelo) e linhas da tabela de tentativas
- **[spaCy](https://spacy.io/)** (`pt_core_news_lg`) - análise gramatical, lematização e vetores de palavras
- **NumPy** - cálculo da similaridade de cosseno
- **Unidecode** - normalização de acentos
- **XML-RPC** (`xmlrpc.server` / `xmlrpc.client`, biblioteca padrão) - comunicação entre cliente e servidor
## Como executar
 
### Pré-requisitos
 
- Python 3.10 ou superior instalado
- pip (gerenciador de pacotes do Python)
### Instalação das dependências
 
No terminal, dentro da pasta do projeto, execute:
 
```bash
pip install customtkinter spacy numpy unidecode
python -m spacy download pt_core_news_lg
```
 
### Arquivos necessários
 
Na mesma pasta devem estar:
 
- `servidor_integrador_cosseno.py`
- `cliente_interface_contexto.py`
- `livro.txt` (obrigatório para o servidor)
- `tema_contexto.json` (opcional)
> **Observação:** se o arquivo `tema_contexto.json` não for encontrado na mesma pasta do cliente, o programa utiliza automaticamente o tema padrão `"blue"` do customtkinter, sem travar a execução.
 
### Execução
 
1. Inicie o **servidor** primeiro e aguarde a mensagem `Servidor Contexto - Alice Iniciado` (o carregamento do modelo e do livro pode levar alguns instantes):
```bash
python servidor_integrador_cosseno.py
```
 
2. Em outro terminal, inicie o **cliente**:
```bash
python cliente_interface_contexto.py
```
 
> **Atenção:** a cada partida nova (botão "Entrar") o servidor recalcula o ranking inteiro, então a tela de jogo pode demorar um pouco para abrir. Para fins de teste, o servidor imprime a palavra secreta no terminal.
 
### Sobre a fonte utilizada
 
A interface usa a fonte **"Alice"** (fonte decorativa do Google Fonts) em títulos e textos. Caso o sistema não tenha essa fonte instalada, o Tkinter substitui automaticamente por uma fonte padrão do sistema operacional e a interface continua funcionando normalmente, apenas com um visual diferente do planejado. Para reproduzir o visual original, recomenda-se instalar a fonte "Alice" no sistema antes de executar o programa.
 
## Funcionalidades implementadas
 
### Interface
 
- **Navegação entre telas**: troca de telas via `mostrar_tela()`, que destrói a tela atual e carrega a nova dentro do `container` principal
- **Menu Principal**: título, decoração temática (naipes de carta e relógio do Coelho Branco) e botões de Entrar, Ajuda, Sobre e Sair
- **Tela de Ajuda**: explica as regras básicas do jogo, com ilustração de Absolem (a lagarta) sobre o cogumelo
- **Tela de Sobre**: nomes da equipe, ilustração com três cartas de baralho e citação das disciplinas e da universidade
### Tela de Jogo
 
- Campo de texto para envio de tentativas (também pela tecla Enter)
- **Posição real** da palavra no ranking, calculada pelo servidor
- **Tabela de tentativas rolável e ordenada por proximidade**: a cada nova tentativa a tabela é reordenada, com a palavra mais próxima da secreta no topo
- **Barra de proximidade colorida** em cada linha, em escala logarítmica:
    - 🟩 verde: muito perto
    - 🟨 amarelo: perto
    - 🟥 vermelho: longe
    - sem barra: muito longe
- Contador de tentativas
- **Validação das palavras**, com pop-ups de aviso:
    - palavra fora do vocabulário do livro ("Palavra inválida")
    - palavra já tentada na partida ("Já tentada")
- Menu de opções (ícone de três pontos) com:
    - **Como jogar** - pop-up com as regras
    - **Dica** - pede ao servidor uma palavra mais próxima da secreta do que a melhor tentativa atual e a adiciona à tabela. A dica só fica disponível depois de uma tentativa que ainda esteja longe da resposta (posição maior que 2), e cada dica precisa de uma nova tentativa antes de poder ser usada de novo
    - **Desistir** - pop-up de confirmação (Sim/Não) e tela de resultado que revela a palavra secreta
    - **Voltar ao menu**
### Telas de resultado
 
- **Vitória**: exibida ao acertar a palavra secreta (posição 1), mostrando o número de tentativas e a palavra
- **Desistência**: exibida ao desistir, mostrando o número de tentativas e a palavra secreta
- Depois de encerrada a partida, não é mais possível enviar tentativas; a única ação disponível é voltar ao menu
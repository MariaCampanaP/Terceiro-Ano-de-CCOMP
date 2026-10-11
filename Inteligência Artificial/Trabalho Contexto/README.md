<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&color=FFDE21&reversal=false"/>

## ☕︎︎ Projeto - Contexto: Alice no País das Maravilhas

Jogo de adivinhação de palavras inspirado no jogo online [Contexto](https://contexto.me/), desenvolvido para as disciplinas de **Inteligência Artificial** e **Redes de Computadores e Sistemas Distribuídos** do curso de Bacharelado em Ciência da Computação da Universidade Estadual do Paraná (UNESPAR).
 
O jogo utiliza como base o livro **Alice no País das Maravilhas**, de Lewis Carroll, tanto para a identidade visual da interface quanto para o vocabulário que será usado no cálculo de similaridade semântica entre as palavras.

---

## ☕︎︎ Breve História do Contexto

O jogo **Contexto** foi inspirado em uma versão norte-americana chamada Semantle, criada pelo programador David Turner.
O Semantle serviu de base para a criação da versão brasileira, focada em semântica e na proximidade de significados das palavras. O jogo utiliza um algoritmo de IA que analisa milhares de textos em português para calcular a proximidade de sentido entre a palavra que você digita e a palavra secreta do dia.
Descobrir a palavra secreta (que recebe a posição número 1) através de tentativas ilimitadas, onde cada palpite recebe uma classificação numérica e de cor (vermelho para longe, amarelo para perto e verde para muito próximo) baseada no contexto em que os termos são usados.

---

## ☕︎︎ Estrutura do Código e Representação

### Organização do `interface.py`

O código é organizado em blocos, na seguinte ordem:

| Bloco | O que faz |
|---|---|
| **Configuração de tema e cores** | Define o modo claro (`set_appearance_mode`), carrega o `tema_contexto.json` e declara as constantes de cor da identidade visual (`FUNDO`, `PAINEL`, `AZUL_ALICE`, `VERMELHO`, `DOURADO`, `MARROM` etc.) |
| **Janela principal e container** | Cria a janela `root` (430x620) e o `container`, área onde cada tela é carregada. A variável `frame_atual` guarda a tela exibida |
| **Funções de navegação e helpers** | `mostrar_tela()`, `sair()` e `criar_botao()` |
| **Telas** | Uma função para cada tela, todas recebendo o `container` e devolvendo um cartão (`frame_externo`) de 340x540 |
| **Inicialização** | Chama `mostrar_tela(tela_menu)` e inicia o loop de eventos com `root.mainloop()` |

### Funções de navegação e helpers
 
| Função | Responsabilidade |
|---|---|
| `mostrar_tela(funcao_tela)` | Destrói a tela atual (se existir), cria a nova pela função recebida e centraliza no container |
| `sair()` | Fecha a aplicação |
| `criar_botao(pai, texto, comando, cor, hover)` | Cria botões com o padrão visual do projeto (tamanho, cantos arredondados, fonte "Alice" e borda dourada) |
 
### Telas
 
| Função | Tela | Conteúdo |
|---|---|---|
| `tela_menu` | Menu Principal | Relógio do Coelho Branco e naipes desenhados no Canvas, título, botões Entrar/Ajuda/Sobre/Sair e frase temática |
| `tela_ajuda` | Ajuda | Ilustração do Absolem sobre o cogumelo e texto com as regras básicas |
| `tela_sobre` | Sobre | Ilustração com três cartas, nomes da equipe, disciplinas e universidade |
| `tela_jogo` | Jogo | Campo de tentativa, contador, tabela de histórico e menu de três pontos |
| `tela_resultado_desistencia` | Resultado da desistência | Número de tentativas, palavra secreta e botão para voltar ao menu |
 
### Funções internas da `tela_jogo`
 
| Função | Responsabilidade |
|---|---|
| `processar_envio()` | Lê a palavra digitada (sem espaços e em minúsculas), registra a tentativa e limpa o campo. Não faz nada se a partida já terminou |
| `adicionar_tentativa_tabela()` | Incrementa o contador e adiciona uma linha com a palavra e a posição no histórico |
| `alternar_menu()` | Abre ou fecha o menu de três pontos |
| `abrir_popup_como_jogar()` | Exibe o pop-up com as regras |
| `pedir_dica()` | Exibe o pop-up informando que a dica será implementada futuramente |
| `confirmar_desistencia()` | Exibe o pop-up de confirmação (Sim/Não); ao confirmar, encerra a partida e abre a tela de resultado |
 
> **Estado da partida:** o contador de tentativas, o menu aberto e o indicador de partida finalizada ficam guardados em listas de um elemento (`contador_tentativas`, `frame_menu_opcoes` e `jogo_finalizado`), para que as funções internas consigam alterar seus valores.

## ☕︎︎ Observações importantes

- O `interface.py` e o `tema_contexto.py` precisam estar na **mesma pasta**. Se o tema não for encontrado, o programa usa automaticamente o tema padrão `"blue"` do customtkinter, sem travar a execução
- A **posição da palavra** no ranking ainda é **simulada** (valor fixo `142`). O cálculo de similaridade semântica com o vocabulário do livro será implementado nas próximas entregas
- A **palavra secreta** ainda não existe: a tela de resultado da desistência mostra apenas um texto provisório.
- A **dica** ainda não foi implementada: o pop-up apenas avisa que ficará para depois
- O jogo ainda **não valida** se a palavra existe no vocabulário nem se ela já foi enviada antes
- Depois de **desistir**, a partida é encerrada e a única ação disponível é voltar ao menu
- Em algumas distribuições Linux, o Tkinter não vem junto com o Python e pode ser necessário instalá-lo.
- A interface usa a fonte **"Alice"** (fonte decorativa do Google Fonts) em títulos e textos. Caso o sistema não tenha essa fonte instalada, o Tkinter substitui automaticamente por uma fonte padrão do sistema operacional. A interface continua funcionando normalmente, apenas com um visual diferente do planejado. Para reproduzir o visual original, recomenda-se instalar a fonte "Alice" no sistema antes de executar o programa.

## ☕︎︎ Tecnologias e Linguagens Utilizadas
 
- **Linguagem**: Python 3
- **Interface gráfica**: [customtkinter](https://github.com/TomSchimansky/CustomTkinter), com tema visual customizado (`tema_contexto.json`)
- **Elementos ilustrados**: Tkinter (Canvas), utilizado em conjunto com o customtkinter para o relógio do Coelho Branco, as cartas de baralho e o Absolem/cogumelo
- **Bibliotecas padrão do Python**: `math` (posição dos ponteiros e marcações do relógio) e `os` (localização do arquivo de tema)
- **Tema**: arquivo JSON com cores, bordas e arredondamentos dos componentes
- **Fonte**: "Alice" (Google Fonts)

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

Este repositório contém todas as disciplinas do 3° ano. Se quiser baixar **somente** a pasta "Trabalho Contexto" (dentro de Inteligência Artificial), use o sparse-checkout do Git:

```bash
git clone --no-checkout https://github.com/MariaCampanaP/Terceiro-Ano-de-CCOMP.git
cd Terceiro-Ano-de-CCOMP
git sparse-checkout init --cone
git sparse-checkout set "Inteligência Artificial/Trabalho Contexto"
git checkout main
```
   
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&color=FFDE21&reversal=false&section=footer"/>

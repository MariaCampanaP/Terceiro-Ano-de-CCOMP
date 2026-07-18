<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&color=FFDE21&reversal=false"/>

## ☕︎︎ Projeto - Algoritmo Genético

O objetivo deste trabalho é compreender e implementar um Algoritmo Genético (AG) para resoolver o Problema do Caixeiro Viajante (TSP - Traveling Salesman Problem). O TSP é um problema clássico de otimização combinatória, onde um vendedor precisa visitar várias cidades exatamente uma vez e retornar à cidade de origem, minimizando a distância total percorrida.

---

## ☕︎︎ Breve História do TSP

O **Problema do Caixeiro Viajante (Traveling Salesman Problem - TSP)** surgiu no século XIX, com aplicações práticas no planejamento de rotas para comerciantes.
Sua primeira descrição formal é atribuída ao matemático **Karl Menger**, em 1832. No entanto, o problema ganhou maior importância a partir do século XX, com o desenvolvimento da matemática aplicada e da computação.
Após a Segunda Guerra Mundial, o TSP se tornou um dos principais desafios da otimização, sendo aplamente estudada por instituições como a **RAND Corporation**.
Hoje, o TSP é conhecido como um problema **NP-difícil (isso significa que não existe, até hoje, um algoritmo conhecido que resolva o problema de forma eficiente para todos os casos)**, servindo como referência para o desenvolvimento e teste de algoritmo em áreas como:
- Lógistica
- Inteligência Artificial
- Pesquisa Operacional

Mesmo após décadas de estudo, ele continua sendo um dos problemas mais importantes e desafiadores da computação.

---

## ☕︎︎ Estrutura do Código e Representação

- **Cromossomo (Caminho)**: É representado pela classe `Caminho`, que contém uma lista ordenada de objetos `Cidade`.
- **Genes**: Cada `Cidade` no vetor é um gene; a ordem delas define a rota
- **Fitness (Aptidão)**: É a distância total do caminho (calculada em `calculaDistancia`). O objetivo é **minimizar** esse valor.

## ☕︎︎ O Ciclo Evolutivo

1. **População Inicial e Elitismo**
   - **População Inicial**: O código gera 1000 indivíduos aletórios para garantir diversidade genética no início.
   -  **Elitismo**: Antes de gerar novos indivíduos, o código ordena a população pela distância e preserva os **25 melhores (Elite)** diretamente para a próxima geração. Isso impede que a melhor solução encontrada seja perdida por mutações ruins.

2. **Método de Seleção (Torneio)**
   - Para escolher quem irá se reproduzir, você usa o **Torneio de tamanho 2**: o código sorteia dois indivíduos e o que tiver a menor distância vence. É um método mais simples de implementar e evita o problema da "superpopulação" de um único indivíduo muito forte que ocorre na roleta.

3. **Operadores e Probabilidade**
O código usa um sorteio (`p = random.randrange(1, 100)`) para decidir a ação:
  - **Crossover (85%)**: Utiliza dois pontos de corte (`c1` e `c2`). O filho herda a parte central de um pai e preenche o restante com os genes do outro pai, garantindo que nenhuma cidade se repita e nenhuma seja esquecida.
  - **Reprodução (10%)**: Apenas copia o vencedor do torneio para a próxima geração.
  - **Mutação (5%)**: Sorteia duas posições e troca as cidades de lugar. O código inclui uma trava de segurança: se a cidade de origem (posição 0) for trocada, ele atualiza automaticamente o destino final (última posição) para garantir que o ciclo feche corretamente na mesma cidade.

## ☕︎︎ Critério de Parada

1. **Parada**: O algoritmo executa por **1000 gerações** fixas.

## ☕︎︎ Como funciona

O algoritmo segue os seguintes passos:
1. **Entrada de dados**
   - O usuário insere cidades no formato:
     `númeroDaCidade x y`
   - Exemplo:
     ```
     1 10 20
     2 30 40
     3 15 25
     ```
2. **População inicial**
   - São gerados 1000 caminhos aleatórios
3. **Evolução**
   - Durante 1000 gerações:
     - Seleção dos melhores indivíduos (elitismo)
     - Aplicação de:
       - Cruzamento (85%)
       - Reprodução (10%)
       - Mutação (5%)
4. **Resultado**
   - Exibe o melhor caminho encontrado
   - Mostra a distância total
   - Plota gráficos de desempenho

## ☕︎︎ Tecnologias e Linguagens Utilizadas

- **Linguagem**: Python;
- **Bibliotecas**: numpy, matplotlib.
- **Visual Studio Code**

## ☕︎︎ Observações importantes

- O programa não lê arquivos .tsp manualmente, é necessário colar os dados manualmente
- Copie apenas as linhas com coordenadas (ignore cabeçalhos como NAME, TYPE, etc.)
- Inserir número com casas decimais faz com que o programa não funcione corretamente por algum motivo.

## ☕︎︎ Instâncias e Resultados

1. Utilizamos três instâncias disponíveis no dataset TSPLIB: https://github.com/mastqe/tsplib
2. Não escolha tamanhos muito similares - Utilize a regra problema pequeno, médio e grande para fazer sua escolha
3. Devido ao avanço dos últimos anos, todos os problemas no dataset TSPLIB foram resolvidos e temos o resultado ótimo de todos eles. Você pode comparar seus resultados nesse link: https://github.com/mastqe/tsplib/blob/master/solutions

## ☕︎︎ Equipe

**Luna**
- GitHub: [Luna-Osti](https://github.com/Luna-Osti)
- LinkedIn: [Luna Osti de França](https://www.linkedin.com/in/luna-osti-de-frança-23961b321/)

**Maria Rita**
- GitHub: [MariaCampanaP](https://github.com/MariaCampanaP)
- LinkedIn: [Maria Rita Campana Peixoto](https://www.linkedin.com/in/maria-rita-campana/)

## ☕︎︎ Como Usar

## Como clonar apenas esta pasta

Este repositório contém todas as disciplinas do 3° ano. Se quiser baixar **somente** a pasta "Trabalho Algoritmo Genético" (dentro de Inteligência Artificial), use o sparse-checkout do Git:

```bash
git clone --no-checkout https://github.com/MariaCampanaP/Terceiro-Ano-de-CCOMP.git
cd Terceiro-Ano-de-CCOMP
git sparse-checkout init --cone
git sparse-checkout set "Inteligência Artificial/Trabalho Algoritmo Genético"
git checkout main
```
   
<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&color=FFDE21&reversal=false&section=footer"/>
